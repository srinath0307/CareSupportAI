# Caresupport AI

Caresupport AI is a virtual healthcare assistant chatbot designed to provide personalized healthcare support to users. The chatbot takes symptoms as input, asks relevant questions, and predicts possible diseases along with recommended precautions. In addition to the chatbot, the project also includes a website that integrates the chatbot and offers various healthcare-related features.

## Introduction

Caresupport AI aims to bridge the gap between individuals seeking healthcare information and the resources available to them. By utilizing natural language processing and machine learning techniques, the chatbot offers an intuitive way for users to interact and receive accurate predictions and precautions for their symptoms. The website complements the chatbot by providing additional features such as hospital information, appointment booking, health insurance, and multi-language support.

## Scope and Requirements

The main goals of Caresupport AI are as follows:

- Develop a user-friendly chatbot that can accurately predict diseases based on symptoms.
- Provide reliable information about precautions and recommendations for identified diseases.
- Create a website interface that integrates the chatbot and offers additional healthcare-related features.
- Utilize a validated dataset to enhance the accuracy of disease predictions and precautions.
- Enable users to find nearby hospitals based on their location using the Google Maps API.
- Allow users to book appointments with healthcare providers through the website.
- Provide a platform for users to purchase health insurance.
- Support multi-language capabilities using the Google Translate API.

## Technology and Tools

The following technologies and tools are utilized in the Caresupport AI project:

- Frontend: HTML, CSS, JavaScript, Bootstrap
- Backend: Django
- Database: PostgreSQL
- Language: Python
- Cloud Platform: Microsoft Azure
- Machine Learning: Decision Tree Classifier (scikit-learn library)
- APIs: Google Maps API, Google Translate API
- Modules: scikit-learn, pandas, pyttsx3, numpy

## Steps to Run

To run the Care support AI project locally, follow these steps:

1. Clone the repository: `https://github.com/srinath0307/CareSupportAI.git`
2. Install the necessary dependencies: `pip install -r requirements.txt`
3. Configure the database connection in the Django settings file.
4. Set up the required API keys for Google Maps API and Google Translate API in the appropriate configuration files.
5. Launch the Django development server: `python manage.py runserver`



## Design

The Caresupport AI project follows a client-server architecture. The front end is built using HTML, CSS, JavaScript, and Bootstrap to create a user-friendly interface. The backend is implemented in Django, which handles the chatbot logic, database operations, appointment booking, and health insurance functionalities. PostgreSQL is used as the database to store user information and chatbot data.

The chatbot utilizes a decision tree classifier implemented with the scikit-learn library for disease prediction. It is trained on a validated dataset provided by healthcare professionals. The Google Maps API is used to retrieve nearby hospitals based on the user's location, while the Google Translate API enables multi-language support.

## Contributors

The Caresupport AI project is developed and maintained by the following contributors:

* [Srinath M](https://github.com/srinath0307)
* [Sudhir mahaaraja S](https://github.com/Mepsitho)
* [AswinRaj V S](https://github.com/AswinRajVS)
* [Raghul R](https://github.com/raghul20ad039)


