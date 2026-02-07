def next_steps(parameter, status):
    if "Low" in status:
        return "👉 Consider consulting a doctor if symptoms appear."
    elif "High" in status:
        return "👉 Lifestyle changes and medical advice recommended."
    else:
        return "👍 No action needed. Maintain healthy habits."
def next_steps(parameter, status):
    """
    Provides guidance based on health status
    """
    if "Low" in status or "High" in status:
        return "👉 Please consult a doctor if symptoms persist."
    else:
        return "👍 No immediate action needed. Maintain healthy habits."