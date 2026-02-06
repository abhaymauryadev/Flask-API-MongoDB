# Flask API and MongoDB Integration Project

This project demonstrates the use of Flask to create a REST API and a web application that interacts with MongoDB Atlas.  
It includes reading data from a backend file, returning JSON responses, and inserting form data into a cloud database.

---

## 1. Flask API – Read Data from Backend File

### Description
A Flask application is created with an `/api` route.  
When this route is accessed, it reads data from a backend JSON file and returns it as a JSON response.

### Features
- Flask REST API
- Reads data from a backend file
- Returns JSON list as response

### Files Used
- `app.py`
- `data.json`

### How It Works
- The `/api` route opens the backend file
- Data is read using Python file handling
- JSON data is returned using Flask `jsonify`

---

## 2. Flask Form with MongoDB Atlas

### Description
A frontend form is created using HTML.  
When the form is submitted:
- Data is inserted into MongoDB Atlas
- On successful insertion, the user is redirected to a success page
- If an error occurs, the error message is displayed on the same page

### Features
- HTML form handling
- MongoDB Atlas integration
- Error handling without redirection
- Success message display

### Files Used
- `app.py`
- `templates/form.html`
- `templates/success.html`

---

## Technologies Used
- Python
- Flask
- MongoDB Atlas
- PyMongo
- HTML

---

## Project Structure
```
Flask-API-MongoDB/
│
├── flask_api/
│ ├── app.py
│ └── data.json
│
├── flask_mongo/
│ ├── app.py
│ └── templates/
│ ├── form.html
│ └── success.html
│
├── requirements.txt
└── README.md
```
---

## Installation and Execution

### Install Dependencies
```bash
pip install -r requirements.txt

```

### Run  Flask Application
```
python app.py
```

### Access API
```
http://127.0.0.1:5000/api
```

### MongoDB Atlas

MongoDB Atlas is used as a cloud NoSQL database

PyMongo is used to connect Flask with MongoDB

Data submitted through the form is stored in the database


Author
Abhay Maurya