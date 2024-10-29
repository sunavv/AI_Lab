def disease_prediction(symptoms):
    if 'fever' in symptoms and 'cough' in symptoms:
        return "Possible flu"
    elif 'stomach pain' in symptoms and 'nausea' in symptoms:
        return "Possible food poisoning"
    else:
        return "Diagnosis unclear"

print(disease_prediction(['fever', 'cough']))
