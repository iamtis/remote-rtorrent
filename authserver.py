from flask import Flask, render_template, request

app = Flask(__name__)

auth_code = None

@app.route("/callback")
def main():
    try:
        auth_code = request.args.get('code')
    except:
        return render_template("failure.html")
    
    f = open("api_key", "w")
    f.write(auth_code)

    return render_template("success.html", code=auth_code)
    