def analyze_symptoms(symptoms):
    if "fever" in symptoms.lower():
        return "Possible flu or infection. Consider consulting a doctor."
    return "Symptoms are not specific. Monitor and follow up if they worsen."