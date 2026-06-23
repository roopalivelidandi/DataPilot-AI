import streamlit as st
import pandas as pd

from agents.manager_agent import ManagerAgent

st.set_page_config(
    page_title="DataPilot AI",
    layout="wide"
)

st.title("🚀 DataPilot AI")
st.caption("Autonomous Multi-Agent Data Science Team")

st.markdown("""
Upload a dataset and let a team of AI agents:

-  Analyze your data
-  Detect data quality issues
-  Generate visualizations
-  Recommend machine learning models
-  Create reports
""")

uploaded_file = st.file_uploader(
    "Upload a CSV file",
    type=["csv"]
)

if uploaded_file:

    df = pd.read_csv(uploaded_file)

    manager = ManagerAgent()

    profile, chart, logs = manager.run(df)

    st.subheader(" Dataset Summary")

    col1, col2, col3 = st.columns(3)

    with col1:
        st.metric("Rows", profile["rows"])
        st.metric("Columns", profile["columns"])

    with col2:
        st.metric("Missing Values", profile["missing_values"])
        st.metric("Duplicates", profile["duplicates"])

    with col3:
        st.metric(
            "Data Quality Score",
            f"{profile['quality_score']}%"
        )

    st.subheader(" Agent Activity")

    for log in logs:
        st.success(log)

    st.subheader(" Generated Visualization")

    if chart:
        st.plotly_chart(
            chart,
            use_container_width=True
        )

    st.subheader(" Dataset Preview")

    st.dataframe(df.head())