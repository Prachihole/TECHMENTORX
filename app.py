import streamlit as st
import json

from backend.analyzer import analyze_report
from backend.trends import analyze_trends

# ---------------- Page Config ----------------
st.set_page_config(
    page_title="AI Health Report Simplifier",
    layout="centered"
)

st.title("🩺 AI Health Report Simplifier")
st.write(
    "Simplifying medical reports into clear, actionable, patient-friendly insights."
)

st.divider()

# ---------------- File Upload ----------------
uploaded_file = st.file_uploader(
    "📄 Upload Medical Report (JSON format)",
    type="json"
)

if uploaded_file:
    report = json.load(uploaded_file)
else:
    st.info("Using sample medical report")
    with open("data/sample_report.json") as f:
        report = json.load(f)

# ---------------- Previous Report ----------------
st.subheader("📂 Upload Previous Medical Report (Optional)")
previous_file = st.file_uploader(
    "Upload previous report (JSON)",
    type="json",
    key="previous"
)

previous_report = None
if previous_file:
    previous_report = json.load(previous_file)

# ---------------- Helper ----------------
def severity_badge(severity):
    if severity == "High":
        return "🔴 High Urgency"
    elif severity == "Moderate":
        return "🟡 Moderate Urgency"
    else:
        return "🟢 Low Urgency"

# ---------------- Analysis ----------------
if st.button("🔍 Analyze Report"):
    results = analyze_report(report)

    st.subheader("🧪 Detailed Health Analysis")

    for param, data in results.items():
        st.markdown(
            f"""
### {param}

**Value:** {data['value']}  
**Normal Range:** {data['normal_range']}

**Status:** {data['status']}  
**Urgency Level:** {severity_badge(data['severity'])}

🧠 **Why this matters**  
{data['impact']}

🛠 **Recommended action**  
{data['action']}
"""
        )

        if data["severity"] == "High":
            st.error("⚠️ Immediate medical attention is recommended.")
        elif data["severity"] == "Moderate":
            st.warning("⚠️ Monitoring and lifestyle changes advised.")
        else:
            st.success("✅ No immediate concern.")

        st.divider()

# ---------------- Trend Analysis ----------------
if previous_report:
    st.subheader("📈 Health Trend Analysis")

trend_result = analyze_trends(previous_report, report)

for param, data in trend_result["parameter_trends"].items():
    st.markdown(
        f"""
*{param}*  
Previous Value: {data['previous']}  
Current Value: {data['current']}  
Trend: {data['trend']}  
💬 {data['meaning']}
"""
    )
    st.divider()

st.success(trend_result["overall_trend"])
# ---------------- Disclaimer ----------------
st.caption(
    "⚠️ This tool assists understanding of medical reports. "
    "It does not provide medical diagnosis or replace professional medical advice."
)