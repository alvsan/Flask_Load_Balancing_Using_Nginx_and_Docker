from flask import Flask
import socket

app = Flask(__name__)

@app.route("/")
def home():
    #return f"Hello, this is an application running on {socket.gethostname()}"
    return f"<p style='text-align: center; color:#{socket.gethostname()[:6]}; background-color:#{socket.gethostname()[6:]}'>Hello, this is an application running on container-id: {socket.gethostname()}.</p>"

if __name__ == "__main__":
    app.run(debug=True)
