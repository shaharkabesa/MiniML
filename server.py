from flask import Flask, render_template, request
from libs.neumpymultilayer import neumpymultilayer;
app = Flask(__name__)



@app.route("/")
def home():
    return render_template("index.html")


@app.route("/research", methods=["POST"])
def research(): 
    if request.method == 'POST':
        data = request.json

        
        print(data["red_color"])
        return "<h1>request heard</h1>"



if __name__ == "__main__":
    app.run(debug=True)