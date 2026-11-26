from flask import Flask
app = Flask(__name__)
@app.route("/")
def home():
    return "Hello World! I'm using Flask."
    
@app.route("/members")
def hello_name():
    return f"C0C25034" "C0C25067" "C0C25004" "C0C26047"

@app.route("/membername")
def hello_name():
    return f"櫻井惣元""星野智紀"
