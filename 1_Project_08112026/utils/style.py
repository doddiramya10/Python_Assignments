import streamlit as st


def apply_styles():

    st.markdown("""
    <style>

    /* KPI Cards */
    [data-testid="stMetric"] {
        background: linear-gradient(
            135deg,
            #EEF2FF,
            #E0F2FE
        );

        padding: 18px;
        border-radius: 15px;

        border: 1px solid #D8DDF5;

        box-shadow: 0px 3px 10px rgba(99, 102, 241, 0.08);
    }

    /* KPI Label */
    [data-testid="stMetricLabel"] {
        color: #475569 !important;
        font-weight: 600;
    }

    /* KPI Value */
    [data-testid="stMetricValue"] {
        color: #312E81 !important;
        font-weight: 700;
    }

    </style>
    """, unsafe_allow_html=True)