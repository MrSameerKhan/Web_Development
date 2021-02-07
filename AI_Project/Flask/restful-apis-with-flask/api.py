from flask import Flask, render_template, request, redirect, url_for, jsonify


app = Flask(__name__)


@app.route("/")
@app.route("/basic/<string:tech>")
def technology(tech):
    if tech == "web":
        fullStack = {"Appication Server": "Gunicorn",
                    "Web Server": "Ngnix",
                    "Web Framework":{
                            "lighWeight": "Flask",
                            "HeavyWeight": "Django"
                    }
                    }
        return jsonify(fullStack)
    else:
        AI = {"Computer Vision": "Detection",
        "Natural Language Process": "NER"}

        return jsonify(AI)
    


if __name__ == '__main__':
    app.debug = True
    app.run(host='0.0.0.0', port=3322)
