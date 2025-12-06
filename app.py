from flask import Flask, render_template

app = Flask(__name__)

# Student data
students = [
    {"name": "Ayesha", "subject": "Math", "marks": 95, "status": "Topper 🏆"},
    {"name": "Ali", "subject": "Math", "marks": 88, "status": "Passed"},
    {"name": "Sara", "subject": "Math", "marks": 82, "status": "Passed"},
    {"name": "Hamza", "subject": "Math", "marks": 76, "status": "Passed"},
]

@app.route("/")
def index():
    return render_template("index.html", students=students)

if __name__ == "__main__":
    app.run(debug=True)
