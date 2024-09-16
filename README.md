# Django Resume Generator

## Overview

Django Resume Generator is a secure, scalable web application built using the Django framework that allows users to create, view, edit, and download their resumes. The application features advanced user authentication, profile management, real-time editing, and PDF download capabilities. Additionally, it integrates a machine learning-powered salary prediction model, making it a versatile tool for professionals.

## Demo
https://github.com/Kajal-Yadav31/ResumeGenerator/assets/129850619/dfcd86fd-e8c6-44e9-b93c-8753c4e8ae84

## Features

1. **Authentication:**
   - Implemented Django custom models for user authentication.
   - Added email verification functionality for account activation.
   - Implemented forgot password functionality for account recovery.

2. **Engineered Secure Resume Creation:**
   - Engineered a secure Django-based application for resume creation and management, featuring user authentication with custom user models, email verification, and password reset for enhanced security.

3. **Dynamic PDF Resume Generation**
   - Enabled users to dynamically generate and download resumes in PDF format, with options for real-time editing and template updates, showcasing full-stack development skills in Python and Django.

4. **Machine Learning-Powered Salary Prediction**
   - Implemented a machine learning-powered salary prediction model using Python, utilizing regression algorithms and predictive analytics to estimate salaries based on user inputs.
   - This feature demonstrates proficiency in machine learning and data-driven application development.


## Getting Started

### Prerequisites
- Python 3.11.2
- Django 4.2.1
- Additional dependencies are mention in the requirement.txt file

### Clone the Repository
1. Clone the repository: `git clone https://github.com/Kajal-Yadav31/ResumeGenerator.git`
2. Navigate to the project directory: `cd ResumeGenerator`
3. Install dependencies: `pip install -r requirements.txt`

## Docker Setup

### Prerequisites
- Docker installed on your machine. You can download and install Docker from [here](https://www.docker.com/get-started).

### Running the project

1) To Build and Start the Docker Container :
    `docker-compose up -d`

2) Apply Migrations :
   ` docker-compose exec web python manage.py migrate`

3) Create a Superuser :to access admin panel
    `docker-compose exec web python manage.py createsuperuser`

### Usage
- Access the application at `http://localhost:8000/` in your web browser.
- Register an account, verify your email, and start creating your resume.
- Explore the features such as profile viewing, editing, seleting resume template and PDF download.

## License
This project is licensed under the [MIT License]


## Contact
For inquiries or issues, contact [kajalyadav3107@gmail.com].


