from flask import Flask

app = Flask(__name__)

@app.route("/")

def home() :
    return "Isaach Shoun Valmoria - The reason why was not able to do the semifinals on time because of a horrible tootache that made my gums swell."

if __name__ == '__main__':
    app.run(debug=True)
