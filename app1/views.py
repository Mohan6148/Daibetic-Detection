from django.shortcuts import render
from django.http import HttpRequest, HttpResponse
from joblib import load
import pandas as pd

# Load the trained diabetes detection model
clf = load('./savedModels/clf.joblib')

def home(request):
    """Render the Home page."""
    return render(request, 'home.html')

def contact(request):
    """Render the Contact page."""
    return render(request, 'contact.html')

def feedback(request):
    """Render the Feedback page."""
    if request.method == 'POST':
        # Handle feedback form submission here (e.g., save feedback)
        return render(request, 'feedback.html', {'message': 'Thank you for your feedback!'})
    return render(request, 'feedback.html')

def predicator(request):
    """Render the Detection page."""
    return render(request, 'detection.html')  # Render the main form for detection

def formInfo(request):
    """Handle form submission from the detection page and perform prediction."""
    if request.method == 'POST':  # Check if the request method is POST
        try:
            # Retrieve input values from the form
            pregnancies = float(request.POST.get('pregnancies'))
            glucose = float(request.POST.get('glucose'))
            blood_pressure = float(request.POST.get('blood_pressure'))
            skin_thickness = float(request.POST.get('skin_thickness'))
            insulin = float(request.POST.get('insulin'))
            bmi = float(request.POST.get('bmi'))
            diabetes_pedigree_function = float(request.POST.get('diabetes_pedigree_function'))
            age = float(request.POST.get('age'))
        except ValueError:
            return render(request, 'result.html', {'error': "Please provide valid numeric inputs."})
        
        # Define the feature names
        feature_names = ['Pregnancies', 'Glucose', 'BloodPressure', 'SkinThickness', 'Insulin', 'BMI', 'DiabetesPedigreeFunction', 'Age']

        # Create a DataFrame with the input values
        input_data = pd.DataFrame([[pregnancies, glucose, blood_pressure, skin_thickness, insulin, bmi, diabetes_pedigree_function, age]],
                                  columns=feature_names)

        # Use the model to predict
        prediction = clf.predict(input_data)

        # Interpret the prediction result
        result = "Diabetic" if prediction[0] == 1 else "Not Diabetic"

        return render(request, 'result.html', {'output': result})

    # If the request is not POST, render the form template
    return render(request, 'detection.html')  # Adjust to your actual form template name
