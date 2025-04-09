from flask import Flask
app = Flask(__name__)

@app.route('/')
def hello():
    return "Hello, Wild Rydes 100952658 saurabh!"

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=80)
