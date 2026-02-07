def analyze_report(report):
    results = {}

    # ---------------- Hemoglobin ----------------
    hb = report["hemoglobin"]
    if hb < 10:
        status, severity = "Low", "High"
        impact = "Low oxygen carrying capacity may cause fatigue and dizziness."
        action = "Medical consultation recommended."
    elif hb < 12:
        status, severity = "Low", "Moderate"
        impact = "Mild anemia possible, may cause weakness."
        action = "Dietary improvement and monitoring advised."
    else:
        status, severity = "Normal", "Low"
        impact = "Oxygen transport is adequate."
        action = "No action required."

    results["Hemoglobin"] = {
        "value": hb,
        "normal_range": "12 – 16 g/dL",
        "status": status,
        "severity": severity,
        "impact": impact,
        "action": action
    }

    # ---------------- WBC ----------------
    wbc = report["wbc"]
    if wbc > 15000:
        status, severity = "High", "High"
        impact = "Strong indication of infection or inflammation."
        action = "Immediate medical attention recommended."
    elif wbc > 11000:
        status, severity = "High", "Moderate"
        impact = "Possible infection or stress response."
        action = "Consult doctor if symptoms persist."
    else:
        status, severity = "Normal", "Low"
        impact = "Immune response appears normal."
        action = "No action required."

    results["WBC"] = {
        "value": wbc,
        "normal_range": "4,000 – 11,000 cells/µL",
        "status": status,
        "severity": severity,
        "impact": impact,
        "action": action
    }

    # ---------------- Platelets ----------------
    platelets = report["platelets"]
    if platelets < 100000:
        status, severity = "Low", "High"
        impact = "High risk of bleeding."
        action = "Urgent medical evaluation required."
    elif platelets < 150000:
        status, severity = "Low", "Moderate"
        impact = "Mild bleeding risk."
        action = "Regular monitoring advised."
    else:
        status, severity = "Normal", "Low"
        impact = "Normal blood clotting function."
        action = "No action required."

    results["Platelets"] = {
        "value": platelets,
        "normal_range": "150,000 – 450,000 cells/µL",
        "status": status,
        "severity": severity,
        "impact": impact,
        "action": action
    }

    # ---------------- Blood Sugar ----------------
    sugar = report["blood_sugar"]
    if sugar > 200:
        status, severity = "High", "High"
        impact = "High risk of uncontrolled diabetes."
        action = "Immediate medical consultation required."
    elif sugar > 140:
        status, severity = "High", "Moderate"
        impact = "Elevated blood sugar levels."
        action = "Lifestyle changes and medical advice recommended."
    else:
        status, severity = "Normal", "Low"
        impact = "Blood sugar level is within safe range."
        action = "Maintain healthy lifestyle."

    results["Blood Sugar"] = {
        "value": sugar,
        "normal_range": "70 – 140 mg/dL",
        "status": status,
        "severity": severity,
        "impact": impact,
        "action": action
    }

    # ---------------- Cholesterol ----------------
    chol = report["cholesterol"]
    if chol > 240:
        status, severity = "High", "High"
        impact = "High risk of heart disease."
        action = "Medical and lifestyle intervention required."
    elif chol > 200:
        status, severity = "High", "Moderate"
        impact = "Increased cardiovascular risk."
        action = "Dietary changes recommended."
    else:
        status, severity = "Normal", "Low"
        impact = "Heart disease risk is low."
        action = "Maintain healthy diet."

    results["Cholesterol"] = {
        "value": chol,
        "normal_range": "< 200 mg/dL",
        "status": status,
        "severity": severity,
        "impact": impact,
        "action": action
    }

    return results
