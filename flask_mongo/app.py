from flask import Flask, render_template, request
from pymongo import MongoClient

app = Flask(__name__)

# MongoDB local connection
client = MongoClient("mongodb://localhost:27017/")
db = client["studentDB"]
collection = db["students"]

@app.route("/", methods=["GET", "POST"])
def form():
    error = None

    if request.method == "POST":
        try:
            name = request.form["name"]
            email = request.form["email"]

            # Force error if fields are empty
            if not name or not email:
                raise Exception("All fields are required")

            collection.insert_one({
                "name": name,
                "email": email
            })

            return render_template("success.html")

        except Exception as e:
            error = str(e)

    return render_template("form.html", error=error)

if __name__ == "__main__":
    app.run(debug=True)
