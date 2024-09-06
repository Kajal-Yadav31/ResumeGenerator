from django.shortcuts import render
import joblib
from django.http import HttpResponse

# Load the model
model = joblib.load('Employee_salary_model.pkl')
print(type(model))


def prediction(request):
    if request.method == "POST":
        # Extracting form data
        age = request.POST.get('age')
        gender = request.POST.get('gender')
        degree = request.POST.get('degree')
        job_title = request.POST.get('job_title')
        experience = request.POST.get('experience')

        # Convert inputs to appropriate types
        try:
            age = float(age) if age else 0.0
            gender = int(gender) if gender else 0
            degree = int(degree) if degree else 0
            job_title = int(job_title) if job_title else 0
            experience = float(experience) if experience else 0.0
        except ValueError as e:
            return HttpResponse(f"Invalid input: {e}")

        # Debugging step: check input values
        print(
            f"Inputs - Age: {age}, Gender: {gender}, Degree: {degree}, Job Title: {job_title}, Experience: {experience}")

        # Predict the salary using the model
        try:
            prediction_result = round(model.predict(
                [[age, gender, degree, job_title, experience]])[0])
        except Exception as e:
            return HttpResponse(f"Error during prediction: {e}")

        # Render the result to the template
        return render(request, 'SalaryPrediction/salary_predict.html', {"output": prediction_result})

    return render(request, 'SalaryPrediction/salary_predict.html')
