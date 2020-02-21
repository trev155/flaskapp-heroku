from flask import Flask, request, jsonify, render_template

app = Flask(__name__)

@app.route('/getmsg/', methods=['GET'])
def respond():
    name = request.args.get("name", None)
    print(f"got name {name}")
    response = {}

    if not name:
        response["ERROR"] = "no name found, please send a name"
    elif str(name).isdigit():
        response["ERROR"] = "name can't be nuneric"
    else:
        response["MESSAGE"] = f"Welcome {name} to our awesome platform"

    return jsonify(response)

@app.route("/post", methods=["POST"])
def post_something():
    name = request.form.get("name")
    print(name)
    
    if name:
        return jsonify({
            "Message": f"Welcome {name} to our awesome platform",
            "METHOD": "POST"
        })
    else:
        return jsonify({
            "ERROR": "no name found, please send a name"
        })


@app.route("/")
def index():
    return render_template("index.html", message="Hello Flask!");
    
    # return "<h1>Welcome to our server. Hello world</h1><img src='https://trevtestbucket.s3.us-east-2.amazonaws.com/20180908_192759.jpg' width='800' height='600'></img>"

@app.route("/img", methods=["POST"])
def image_endpoint():
    return render_template("image.html", message="/static/testimage.jpg")


if __name__ == "__main__":
    app.run(port=5002)


