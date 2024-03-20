# Iris Classification Flask App

This repository contains code for a Flask web application that serves a machine learning model for classifying Iris flowers.

## Steps to Run the Application

### 1. Clone the Repository

Clone this repository to your local machine using the following command:

```bash
git clone <repository_url>
```

### 2. Install Dependencies

Make sure you have Python and Docker installed on your system. Then, navigate to the project directory and install the required Python dependencies using pip:

```
pip install -r requirements.txt
```

### 3. Train the Model

Run the train.py script to train the machine learning model using the Iris dataset:

```
python train.py
```

This will train the model and save it as model.pkl.

### 4. Run the Flask Application

Build the Docker image using the provided Dockerfile:

```
docker build -t iris_flask_app .
```

Then, run the Docker container:

```
docker run -p 5000:5000 iris_flask_app
```

The Flask application should now be running locally on port 5000.

### 5. Test the Endpoint

You can test the /predict endpoint using tools like Postman. Send a POST request to http://localhost:5000/predict with the feature data in JSON format.

Example request body:

```
{
    "features": [5.1, 3.5, 1.4, 0.2]
}
```

You should receive a JSON response with the predicted class.

### 6. Push to GitHub

Initialize a Git repository, commit your changes, and push to GitHub:

```
git init
git add .
git commit -m "Initial commit"
git remote add origin <repository_url>
git push -u origin master
```

## File Structure

### app.py:

Flask application file containing the /predict endpoint.

### train.py:

Script to train the machine learning model.

### model.pkl:

Trained machine learning model.

### Dockerfile:

Dockerfile for building the Docker image.

### Makefile:

Makefile for simplifying Docker commands.

### requirements.txt:

List of Python dependencies.

### Iris.csv:

Dataset used for training the model.
