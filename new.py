import flask
from flask import Flask
from flask import render_template, request

app = Flask(__name__)
@app.route('/')
def get():
  return render_template("index.html")
@app.route("/video",methods=["POST"])
def ret():
	url = request.form["url"]
	url = str(url).split("v=")[1]
	retUrl = "https://www.youtube-nocookie.com/embed/{}".format(url)
	return render_template("video.html", data=retUrl)
if __name__=="__main__":
	app.run("0.0.0.0",port=5000)
