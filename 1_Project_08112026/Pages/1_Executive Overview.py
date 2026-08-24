import streamlit as st
import pandas as pd

from utils.data_loader import load_data
from utils.preprocessing import clean_data
from utils.features import create_features
from utils.filters import sidebar_filters
from utils.kpis import calculate_kpis
from utils.style import apply_styles

from utils.charts import (
    donut_chart,
    pie_chart,
    bar_chart,
    horizontal_bar_chart,
    histogram
)


# ==========================================================
# PAGE CONFIG
# ==========================================================

st.set_page_config(
    page_title="Executive Overview",
    page_icon="📊",
    layout="wide"
)

apply_styles()


# ==========================================================
# HEADER
# ==========================================================

st.title("📊 Executive Overview")

st.markdown(
    """
    This page provides management with an overall picture of
    loan applicants, credit exposure, repayment behavior,
    and default risk.
    """
)


# ==========================================================
# DATA PIPELINE
# ==========================================================

try:

    df = load_data("Data/application_train.csv")

    df = clean_data(df)

    df = create_features(df)

    df = sidebar_filters(df)

except Exception as e:

    st.error(f"Error loading data: {e}")
    st.stop()


# ==========================================================
# CHECK FILTERED DATA
# ==========================================================

if df.empty:

    st.warning("No data available for the selected filters.")
    st.stop()


# ==========================================================
# KPIs
# ==========================================================

metrics = calculate_kpis(df)


# =====================================================
# KPI SECTION
# =====================================================

metrics = calculate_kpis(df)

st.subheader("📌 Key Performance Indicators")

col1, col2, col3, col4 = st.columns(4)

col1.metric(
    "Total Applications",
    f"{metrics['total_applications']:,}"
)

col2.metric(
    "Default Customers",
    f"{metrics['default_customers']:,}"
)

col3.metric(
    "Non-Default Customers",
    f"{metrics['non_default_customers']:,}"
)

col4.metric(
    "Default Rate %",
    f"{metrics['default_rate']:.2f}%"
)

col5, col6, col7, col8 = st.columns(4)

col5.metric(
    "Total Credit Amount",
    f"{df['AMT_CREDIT'].sum():,.0f}"
)

col6.metric(
    "Average Credit",
    f"{metrics['avg_credit']:,.0f}"
)

col7.metric(
    "Average Income",
    f"{metrics['avg_income']:,.0f}"
)

col8.metric(
    "Average Age",
    f"{df['AGE'].mean():.0f}"
)

st.divider()


# ==========================================================
# DEFAULT ANALYSIS
# ==========================================================

st.subheader("🎯 Default Analysis")

st.plotly_chart(
    donut_chart(
        df,
        "TARGET",
        "Default vs Non-Default Customers"
    ),
    use_container_width=True
)


st.divider()


# ==========================================================
# APPLICANT BREAKDOWN
# ==========================================================

st.subheader("👥 Applicant Breakdown")

col1, col2 = st.columns(2)

with col1:

    st.plotly_chart(
        pie_chart(
            df,
            "CODE_GENDER",
            "Applications by Gender"
        ),
        use_container_width=True
    )

with col2:

    st.plotly_chart(
        donut_chart(
            df,
            "NAME_CONTRACT_TYPE",
            "Applications by Contract Type"
        ),
        use_container_width=True
    )


col1, col2 = st.columns(2)

with col1:

    st.plotly_chart(
        bar_chart(
            df,
            "NAME_INCOME_TYPE",
            None,
            "Applications by Income Type"
        ),
        use_container_width=True
    )

with col2:

    st.plotly_chart(
        bar_chart(
            df,
            "NAME_EDUCATION_TYPE",
            None,
            "Applications by Education Level"
        ),
        use_container_width=True
    )


st.divider()


# ==========================================================
# CREDIT DISTRIBUTION
# ==========================================================

st.subheader("💳 Credit Amount Distribution")

st.plotly_chart(
    histogram(
        df,
        "AMT_CREDIT",
        "Credit Amount Distribution"
    ),
    use_container_width=True
)


st.divider()


# ==========================================================
# SEGMENT SUMMARY
# ==========================================================

st.subheader("📊 Applicant Summary by Segment")

col1, col2 = st.columns(2)


with col1:

    income_summary = (
        df.groupby("NAME_INCOME_TYPE")
        .agg(
            Applications=("SK_ID_CURR", "count"),
            Default_Rate=("TARGET", "mean"),
            Average_Credit=("AMT_CREDIT", "mean"),
            Average_Income=("AMT_INCOME_TOTAL", "mean")
        )
        .reset_index()
    )

    income_summary["Default_Rate"] *= 100

    st.write("#### Income Type Summary")

    st.dataframe(
        income_summary,
        use_container_width=True,
        hide_index=True
    )


with col2:

    contract_summary = (
        df.groupby("NAME_CONTRACT_TYPE")
        .agg(
            Applications=("SK_ID_CURR", "count"),
            Default_Rate=("TARGET", "mean"),
            Average_Credit=("AMT_CREDIT", "mean"),
            Average_Annuity=("AMT_ANNUITY", "mean")
        )
        .reset_index()
    )

    contract_summary["Default_Rate"] *= 100

    st.write("#### Contract Type Summary")

    st.dataframe(
        contract_summary,
        use_container_width=True,
        hide_index=True
    )


st.divider()


# ==========================================================
# FILTERED DATA
# ==========================================================

with st.expander("🔍 View Filtered Applicant Data"):

    columns = [
        "SK_ID_CURR",
        "TARGET",
        "CODE_GENDER",
        "NAME_CONTRACT_TYPE",
        "NAME_INCOME_TYPE",
        "NAME_EDUCATION_TYPE",
        "AMT_INCOME_TOTAL",
        "AMT_CREDIT",
        "AMT_ANNUITY",
        "AMT_GOODS_PRICE"
    ]

    columns = [
        col for col in columns
        if col in df.columns
    ]

    st.dataframe(
        df[columns].head(100),
        use_container_width=True
    )


# ==========================================================
# KEY INSIGHTS
# ==========================================================

st.subheader("💡 Key Insights")

risk = df.groupby("NAME_INCOME_TYPE")["TARGET"].mean()

insights = [
    f"📈 **Overall Default Rate:** {df['TARGET'].mean() * 100:.2f}%",
    f"💰 **Average Customer Income:** {df['AMT_INCOME_TOTAL'].mean():,.0f}",
    f"💳 **Average Loan Amount:** {df['AMT_CREDIT'].mean():,.0f}",
    f"👥 **Most Common Income Type:** {df['NAME_INCOME_TYPE'].mode()[0]}",
    f"🎓 **Most Common Education Level:** {df['NAME_EDUCATION_TYPE'].mode()[0]}",
    f"⚠️ **Highest Risk Segment:** {risk.idxmax()} ({risk.max() * 100:.2f}%)"
]

col1, col2, col3 = st.columns(3)

for col, insight in zip([col1, col2, col3], insights[:3]):
    col.info(insight)

col1, col2, col3 = st.columns(3)

for col, insight in zip([col1, col2, col3], insights[3:]):
    col.info(insight)

st.divider()

