"""
Explanation Layer
-----------------
Responsible only for converting analysis results
into patient-friendly language.
No medical decision logic here.
"""

def severity_text(severity):
    """
    Converts severity level into readable explanation
    """
    if severity == "High":
        return "This parameter requires urgent attention."
    elif severity == "Moderate":
        return "This parameter should be monitored closely."
    else:
        return "This parameter is within a safe range."


def status_badge(status):
    """
    Adds friendly icons to status
    """
    badges = {
        "Normal": "🟢 Normal",
        "High": "🔴 High",
        "Low": "🟡 Low"
    }
    return badges.get(status, status)


def trend_text(trend):
    """
    Human-friendly explanation for trend analysis
    """
    if "Improving" in trend:
        return "This parameter is moving in a healthier direction."
    elif "Worsening" in trend:
        return "This parameter is showing signs of deterioration."
    else:
        return "This parameter has remained stable."