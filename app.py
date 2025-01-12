#Application code by Jagpreet Singh Sandhu
from flask import Flask
app = Flask(__name__)

@app.route("/info")
def lw():
    return "welcome to LW ......"
