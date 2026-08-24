import streamlit as st
import pandas as pd


def sidebar_filters(df: pd.DataFrame):

    st.sidebar.header("Filters")

    # ==========================================================
    # AGE
    # ==========================================================
    if "AGE" not in df.columns:
        df["AGE"] = (abs(df["DAYS_BIRTH"]) / 365).round(0)

    age_min = int(df["AGE"].min())
    age_max = int(df["AGE"].max())

    age_range = st.sidebar.slider(
        "Age Range",
        min_value=age_min,
        max_value=age_max,
        value=(age_min, age_max)
    )

    # ==========================================================
    # INCOME
    # ==========================================================
    income_min = float(df["AMT_INCOME_TOTAL"].min())
    income_max = float(df["AMT_INCOME_TOTAL"].max())

    income_range = st.sidebar.slider(
        "Income Range",
        min_value=income_min,
        max_value=income_max,
        value=(income_min, income_max)
    )

    # ==========================================================
    # CREDIT
    # ==========================================================
    credit_min = float(df["AMT_CREDIT"].min())
    credit_max = float(df["AMT_CREDIT"].max())

    credit_range = st.sidebar.slider(
        "Credit Range",
        min_value=credit_min,
        max_value=credit_max,
        value=(credit_min, credit_max)
    )

    # ==========================================================
    # TARGET
    # ==========================================================
    target = st.sidebar.multiselect(
        "Target",
        options=sorted(df["TARGET"].dropna().unique()),
        default=sorted(df["TARGET"].dropna().unique())
    )

    # ==========================================================
    # GENDER
    # ==========================================================
    gender = st.sidebar.multiselect(
        "Gender",
        options=sorted(df["CODE_GENDER"].dropna().unique()),
        default=sorted(df["CODE_GENDER"].dropna().unique())
    )

    # ==========================================================
    # CONTRACT TYPE
    # ==========================================================
    contract = st.sidebar.multiselect(
        "Contract Type",
        options=sorted(df["NAME_CONTRACT_TYPE"].dropna().unique()),
        default=sorted(df["NAME_CONTRACT_TYPE"].dropna().unique())
    )

    # ==========================================================
    # INCOME TYPE
    # ==========================================================
    income_type = st.sidebar.multiselect(
        "Income Type",
        options=sorted(df["NAME_INCOME_TYPE"].dropna().unique()),
        default=sorted(df["NAME_INCOME_TYPE"].dropna().unique())
    )

    # ==========================================================
    # EDUCATION
    # ==========================================================
    education = st.sidebar.multiselect(
        "Education",
        options=sorted(df["NAME_EDUCATION_TYPE"].dropna().unique()),
        default=sorted(df["NAME_EDUCATION_TYPE"].dropna().unique())
    )

    # ==========================================================
    # FAMILY STATUS
    # ==========================================================
    family_status = st.sidebar.multiselect(
        "Family Status",
        options=sorted(df["NAME_FAMILY_STATUS"].dropna().unique()),
        default=sorted(df["NAME_FAMILY_STATUS"].dropna().unique())
    )

    # ==========================================================
    # OCCUPATION
    # ==========================================================
    occupation = st.sidebar.multiselect(
        "Occupation",
        options=sorted(df["OCCUPATION_TYPE"].dropna().unique()),
        default=sorted(df["OCCUPATION_TYPE"].dropna().unique())
    )

    # ==========================================================
    # HOUSING TYPE
    # ==========================================================
    housing = st.sidebar.multiselect(
        "Housing Type",
        options=sorted(df["NAME_HOUSING_TYPE"].dropna().unique()),
        default=sorted(df["NAME_HOUSING_TYPE"].dropna().unique())
    )

    # ==========================================================
    # CAR OWNERSHIP
    # ==========================================================
    car_ownership = st.sidebar.multiselect(
        "Car Ownership",
        options=sorted(df["FLAG_OWN_CAR"].dropna().unique()),
        default=sorted(df["FLAG_OWN_CAR"].dropna().unique())
    )

    # ==========================================================
    # PROPERTY OWNERSHIP
    # ==========================================================
    property_ownership = st.sidebar.multiselect(
        "Property Ownership",
        options=sorted(df["FLAG_OWN_REALTY"].dropna().unique()),
        default=sorted(df["FLAG_OWN_REALTY"].dropna().unique())
    )

    # ==========================================================
    # APPLY ALL FILTERS
    # ==========================================================
    filtered_df = df[
        (df["TARGET"].isin(target)) &
        (df["CODE_GENDER"].isin(gender)) &
        (df["AGE"].between(age_range[0], age_range[1])) &
        (df["AMT_INCOME_TOTAL"].between(income_range[0], income_range[1])) &
        (df["AMT_CREDIT"].between(credit_range[0], credit_range[1])) &
        (df["NAME_CONTRACT_TYPE"].isin(contract)) &
        (df["NAME_INCOME_TYPE"].isin(income_type)) &
        (df["NAME_EDUCATION_TYPE"].isin(education)) &
        (df["NAME_FAMILY_STATUS"].isin(family_status)) &
        (df["OCCUPATION_TYPE"].isin(occupation)) &
        (df["NAME_HOUSING_TYPE"].isin(housing)) &
        (df["FLAG_OWN_CAR"].isin(car_ownership)) &
        (df["FLAG_OWN_REALTY"].isin(property_ownership))
    ]

    return filtered_df


# import streamlit as st

# def sidebar_filters(df):

#     st.sidebar.header("Filters")

#     if "AGE" not in df.columns:
#         df["AGE"] = (abs(df["DAYS_BIRTH"]) / 365).round(0)
#     age_min = int(df["AGE"].min())
#     age_max = int(df["AGE"].max())

#     age_range = st.sidebar.slider(
#         "Age Range",
#         age_min,
#         age_max,
#         (age_min, age_max))    
    
#     target = st.sidebar.multiselect("Target",df["TARGET"].unique(),default=df["TARGET"].unique())
#     gender = st.sidebar.multiselect("Gender",df["CODE_GENDER"].dropna().unique(),default=df["CODE_GENDER"].dropna().unique())
#     education = st.sidebar.multiselect("Education",df["NAME_EDUCATION_TYPE"].dropna().unique(),
#                                        default = df["NAME_EDUCATION_TYPE"].dropna().unique())
#     contract = st.sidebar.multiselect("Contract Type",df["NAME_CONTRACT_TYPE"].dropna().unique(),
#                                       default=df["NAME_CONTRACT_TYPE"].dropna().unique())    
    
#     filtered_df = df[(df["TARGET"].isin(target))&
#                      (df["CODE_GENDER"].isin(gender))&
#                      (df["NAME_EDUCATION_TYPE"].isin(education))&
#                      (df["NAME_CONTRACT_TYPE"].isin(contract))&
#                      (df["AGE"].between(age_range[0],age_range[1]))]
    
#     return filtered_df

## Usage
# from utils.filters import sidebar_filters

# filtered_df = sidebar_filters(df)




# import streamlit as st
# def sidebar_filters(df):
#     st.sidebar.header("Filters")
#     target = st.sidebar.multiselect(
#         "Target",
#         df["TARGET"].unique(),
#         default=df["TARGET"].unique()
#     )
#     gender = st.sidebar.multiselect(
#         "Gender",
#         df["CODE_GENDER"].dropna().unique(),
#         default=df["CODE_GENDER"].dropna().unique()
#     )
#     education = st.sidebar.multiselect(
#         "Education",
#         df["NAME_EDUCATION_TYPE"].dropna().unique(),
#         default=df["NAME_EDUCATION_TYPE"].dropna().unique()
#     )
#     contract = st.sidebar.multiselect(
#         "Contract Type",
#         df["NAME_CONTRACT_TYPE"].dropna().unique(),
#         default=df["NAME_CONTRACT_TYPE"].dropna().unique()
#     )
#     filtered_df = df[
#         (df["TARGET"].isin(target))
#         &
#         (df["CODE_GENDER"].isin(gender))
#         &
#         (df["NAME_EDUCATION_TYPE"].isin(education))
#         &
#         (df["NAME_CONTRACT_TYPE"].isin(contract))
#     ]

#     return filtered_df

# #from utils.filters import sidebar_filters
