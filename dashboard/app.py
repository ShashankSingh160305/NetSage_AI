import streamlit as st
import sys
import os

# Add project root to Python path
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

from checker.diagnose import diagnose


st.set_page_config(
    page_title="NetSage AI",
    page_icon="🌐",
    layout="wide"
)
    
st.title("🌐 NetSage AI")
st.subheader("Network Fault Diagnosis Dashboard")

st.write(
    "Describe your network problem below and NetSage AI will identify "
    "the most likely fault and provide a recommendation."
)

problem = st.text_area(
    "Describe your network problem",
    placeholder="Example: PC0 cannot reach the default gateway",
    height=120
)

if st.button("🔍 Diagnose Network Problem"):

    if problem.strip():

        result = diagnose(problem)

        st.divider()
        st.subheader("📊 Diagnosis Result")

        if result.get("status") == "Match found":

            col1, col2 = st.columns(2)

            with col1:
                st.write("**Case ID:**", result["case_id"])
                st.write("**Symptom:**", result["symptom"])
                st.write("**Fault:**", result["expected_fault"])

            with col2:
                st.write("**OSI Layer:**", result["osi_layer"])
                st.write("**Concept:**", result["concept"])
                st.write("**Severity:**", result["severity"])

            st.info(
                "💡 Recommendation: "
                + result["recommendation"]
            )

        else:
            st.warning(
                "No matching network fault was found in the case database."
            )

    else:
        st.warning("Please enter a network problem.")

st.divider()

st.caption("NetSage AI — Network Fault Diagnosis System")