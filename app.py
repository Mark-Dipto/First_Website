
from flask import Flask,render_template

app = Flask(__name__, template_folder='Templates')
JOBS=[
    {
        "id":1,
        "Title":"Data Analysist",
        "Location":"Dhaka",
        "Salary":"1000000tk",
    },
    {
        "id":2,
        "Title":"Data Scientist",
        "Location":"Gazipur",
        "Salary":"1500000tk",
    },
    {
        "id":3,
        "Title":"Software Engineer",
        "Location":"Barisal",
        "Salary":"500000tk",
    },
    {
        "id":4,
        "Title":"Frontend Engineer",
        "Location":"Remote",
        "Salary":"55000tk",
    },
]

@app.route('/')
def hello():
    return render_template("home.html",jobs=JOBS,company_name="Mark First website")

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
