"""
Trend Analysis Module
--------------------
Compares previous and current medical reports
and provides meaningful health trend insights.
"""

from backend.config import HEALTH_CONFIG


def calculate_trend(previous, current, low, high):
    """
    Determines direction and magnitude of change
    """
    threshold = 0.05 * (high - low)

    if abs(current - previous) <= threshold:
        return "➖ Stable"

    if current < previous:
        return "⬆ Improving"
    else:
        return "⬇ Worsening"


def interpret_trend(trend):
    """
    Converts trend into clinical meaning
    """
    if "Improving" in trend:
        return "Shows positive response and health improvement."
    elif "Worsening" in trend:
        return "Indicates potential health deterioration."
    else:
        return "No significant change observed."


def analyze_trends(previous_report, current_report):
    trends = {}
    improving = 0
    worsening = 0

    for param in current_report:
        if param not in previous_report:
            continue

        prev_val = previous_report[param]
        curr_val = current_report[param]

        low, high = HEALTH_CONFIG[param]["normal"]

        trend = calculate_trend(prev_val, curr_val, low, high)
        interpretation = interpret_trend(trend)

        if "Improving" in trend:
            improving += 1
        elif "Worsening" in trend:
            worsening += 1

        trends[param] = {
            "previous": prev_val,
            "current": curr_val,
            "trend": trend,
            "meaning": interpretation
        }

    # ---------------- Overall Trend Summary ----------------
    if improving > worsening:
        overall = "🟢 Overall health trend is improving."
    elif worsening > improving:
        overall = "🔴 Overall health trend is deteriorating."
    else:
        overall = "🟡 Overall health trend is stable."

    return {
        "parameter_trends": trends,
        "overall_trend": overall
    }