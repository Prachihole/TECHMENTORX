import streamlit as st
import json
from backend.analyzer import analyze_report
from backend.explanations import next_steps

st.set_page_config(page_title="AI Health Report Simplifier", layout="centered")

st.title("🩺 AI Health Report Simplifier")
st.write("Simplifying medical reports into easy, patient-friendly language.")

st.divider()

uploaded_file = st.file_uploader("Upload medical report (JSON format)", type="json")

if uploaded_file:
    report = json.load(uploaded_file)
else:
    st.info("Using sample medical report")
    with open("data/sample_report.json") as f:
        report = json.load(f)

if st.button("Analyze Report"):
    results = analyze_report(report)

    st.subheader("📊 Health Summary")
    for param, (status, explanation) in results.items():
        st.markdown(f"### {param}: {status}")
        st.write(f"💡 {explanation}")
        st.write(next_steps(param, status))
        st.divider()

st.caption("⚠️ This tool assists understanding. It does not replace medical professionals.")
