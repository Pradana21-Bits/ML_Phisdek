#import Flask 
from flask import Flask
from flask import render_template,request
import pickle
import numpy as np
#create an instance of Flask
app = Flask(__name__)

model_file = open("models/Model.pkl", "rb")

model = pickle.load(model_file)

@app.route("/")
def Home():
	return render_template("Layout.html")
@app.route("/Layout")
def Layout():
	return render_template("Layout.html")	
@app.route("/index")
def form():
  return render_template("index.html")

@app.route("/predict", methods=['GET','POST'])
def predict():
  data = request.form[('Domain')]
  result = model.predict([data])
  result1 =(int(result))
  if result1 == 1 :
  	return render_template("Trust.html")
  else:
  	return render_template("Fake.html")
@app.route("/Trust")
def Trust():
	return render_template("Trust.html")
@app.route("/Fake")
def Fake():
	return render_template("Fake.html")

if __name__ == '__main__':
    app.run(debug=True)