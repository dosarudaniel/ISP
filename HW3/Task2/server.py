from flask import Flask, request, make_response, render_template
import sys
from bcrypt import hashpw, gensalt

app = Flask(__name__)

@app.route("/", methods=['POST'])
def sendResponse():

    if request.method == "POST":
        print("Here " + request.method, file=sys.stderr)
        print("Here password " + request.json["pass"], file=sys.stderr)
        print("Here user " + request.json["user"], file=sys.stderr)

        return hashpw(request.json["pass"].encode("utf-8"), gensalt())

if __name__ == '__main__':
    app.run()
