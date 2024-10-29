def fever_diagnosis(symptoms):
    if 'fever' in symptoms and 'cough' in symptoms:
        return "Possibility of Flu"
    elif 'fever' in symptoms and 'rash' in symptoms:
        return "Possibility of Measles"
    return "Unknown"

print(fever_diagnosis(['fever', 'cough']))
