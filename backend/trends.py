"""
Trend Analysis Module
Compares previous and current medical reports
"""

from backend.analyzer import HEALTH_CONFIG


def calculate_trend(previous, current, low, high):
    """
    Determines health trend for a parameter
    """
    # small change threshold
    threshold = 0.05 * (high - low)

    if abs(current - previous) <= threshold:
        return "➖ Stable"

    # For parameters where lower is better when high
    if current < previous:
        return "⬆ Improving"
    else:
        return "⬇ Worsening"


def analyze_trends(previous_report, current_report):
    trends = {}

    for param in current_report:
        if param not in previous_report:
            continue

        prev_val = previous_report[param]
        curr_val = current_report[param]

        low, high = HEALTH_CONFIG[param]["normal"]

        trend = calculate_trend(prev_val, curr_val, low, high)

        trends[param] = {
            "previous": prev_val,
            "current": curr_val,
            "trend": trend
        }

    return trends