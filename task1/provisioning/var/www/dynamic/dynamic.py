from flask import Flask
import datetime
from flask import request

 
app = Flask(__name__)
 
@app.route("/")
def hello():
    return "<br>".join([
        "This is a dynamic page served via flask",
        "Current time: " + str(datetime.datetime.now().isoformat()),
        "Browser info: " + str(request.headers.get('User-Agent'))
    ])
 
if __name__ == "__main__":
    app.run()