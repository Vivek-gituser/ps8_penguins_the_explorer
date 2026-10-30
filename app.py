
import streamlit as st

st.set_page_config(
    page_title="AGENTGATE",
    page_icon="🛡️",
    layout="wide"
)

st.title("🛡️ AGENTGATE")
st.subheader("Independent AI Security Gateway")

st.write(
    "Protecting company information from "
    "unauthorized AI agent actions."
)

st.divider()

st.success("AGENTGATE application started successfully!")

col1, col2, col3 = st.columns(3)

with col1:
    st.metric("Allowed Actions", 0)

with col2:
    st.metric("Blocked Actions", 0)

with col3:
    st.metric("Pending Actions", 0)

st.divider()

st.subheader("Security Gateway Status")

st.info(
    "Security engine is under development. "
    "Protected tools will be connected in the next phase."
)
