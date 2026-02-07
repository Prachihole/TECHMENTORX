def analyze_report(report):
    results = {}

    # Hemoglobin
    if report["hemoglobin"] < 12:
        results["Hemoglobin"] = ("⚠️ Low", "Low hemoglobin may cause weakness or fatigue.")
    else:
        results["Hemoglobin"] = ("✅ Normal", "Your hemoglobin level is normal.")

    # WBC
    if report["wbc"] > 11000:
        results["WBC"] = ("⚠️ High", "High WBC may indicate infection.")
    else:
        results["WBC"] = ("✅ Normal", "White blood cell count is normal.")

    # Platelets
    if report["platelets"] < 150000:
        results["Platelets"] = ("⚠️ Low", "Low platelets may increase bleeding risk.")
    else:
        results["Platelets"] = ("✅ Normal", "Platelet count is healthy.")

    # Blood Sugar
    if report["blood_sugar"] > 140:
        results["Blood Sugar"] = ("❌ High", "High blood sugar may indicate diabetes.")
    else:
        results["Blood Sugar"] = ("✅ Normal", "Blood sugar level is normal.")

    # Cholesterol
    if report["cholesterol"] > 200:
        results["Cholesterol"] = ("⚠️ High", "High cholesterol increases heart risk.")
    else:
        results["Cholesterol"] = ("✅ Normal", "Cholesterol level is healthy.")

    return results
