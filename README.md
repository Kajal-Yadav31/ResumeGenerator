# Django Resume Generator

## Overview

Django Resume Generator is a web application built using the Django framework that allows users to create, view, edit, and download their resumes. The application includes authentication functionality, form layouts for CV information, a profile view with editing options, and PDF download capability.

## Output 


## Features

1. **Authentication:**
   - Implemented Django custom models for user authentication.
   - Added email verification functionality for account activation.
   - Implemented forgot password functionality for account recovery.

2. **CV Form Layout:**
   - Users can fill in their CV details and upload there pic through a user-friendly form.
   - Display a page listing all user names and email addresses for easy access to CV details.

3. **Profile View:**
   - Users can view only their own profiles.
   - Options for editing, deleting, and navigating back to the main page.
   - Restriction on viewing other users' CVs for enhanced privacy.

4. **Download CV:**
   - Users can download their CV in PDF format.
   - Added functionality to check for typos before downloading.

## Getting Started

### Prerequisites
- Python 3.11.2
- Django 4.2.1
- Additional dependencies are mention in the requirement.txt file

### Installation
1. Clone the repository: `git clone https://github.com/Kajal-Yadav31/ResumeGenerator.git`
2. Navigate to the project directory: `cd ResumeGenerator`
3. Install dependencies: `pip install -r requirements.txt`
4. Apply migrations: `python manage.py migrate`
5. Run the development server: `python manage.py runserver`

### Usage
- Access the application at `http://localhost:8000/` in your web browser.
- Register an account, verify your email, and start creating your resume.
- Explore the features such as profile viewing, editing, and PDF download.

## License
This project is licensed under the [MIT License]


## Contact
For inquiries or issues, contact [kajalyadav3107@gmail.com].
