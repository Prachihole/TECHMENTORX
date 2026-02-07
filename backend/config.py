"""
Central medical configuration file
Used across analyzer and trend modules
"""

HEALTH_CONFIG = {
    "Hemoglobin": {
        "normal": (12, 16),
        "weight": 0.25,
        "unit": "g/dL"
    },
    "WBC": {
        "normal": (4000, 11000),
        "weight": 0.20,
        "unit": "cells/µL"
    },
    "Platelets": {
        "normal": (150000, 450000),
        "weight": 0.20,
        "unit": "cells/µL"
    },
    "Blood Sugar": {
        "normal": (70, 140),
        "weight": 0.20,
        "unit": "mg/dL"
    },
    "Cholesterol": {
        "normal": (0, 200),
        "weight": 0.15,
        "unit": "mg/dL"
    }
}
