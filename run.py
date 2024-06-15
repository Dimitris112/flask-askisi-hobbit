import os
from flask import Flask

app = Flask(__name__)

@app.route("/")
def index():
    return "Hello, World"


if __name__ == "__main__":
    app.run(
        host=os.environ.get("IP", "0.0.0.0"),
        port=int(os.environ.get("PORT", "5000")),
        debug=True
    )
# debug=True mono gia to development kommati
# debug=False otan einai etoimo to project na paradwthei klp - security issue alliws