from flask import Flask, request, app,render_template
from flask import Response
from Forms import CreateUserForm_regression
import pickle
import numpy as np
import pandas as pd


app = Flask(__name__)


scaler=pickle.load(open("models/standardScalar.pkl", "rb"))
model = pickle.load(open("models/modelForPrediction.pkl", "rb"))

@app.route('/',methods=['GET','POST'])
def predict_datapoint():
    result=""
    form = CreateUserForm_regression(request.form)
    if request.method=='POST':

        Pregnancies=int(request.form.get("Pregnancies"))
        Glucose = float(request.form.get('Glucose'))
        BloodPressure = float(request.form.get('BloodPressure'))
        SkinThickness = float(request.form.get('SkinThickness'))
        Insulin = float(request.form.get('Insulin'))
        BMI = float(request.form.get('BMI'))
        DiabetesPedigreeFunction = float(request.form.get('DiabetesPedigreeFunction'))
        Age = float(request.form.get('Age'))

        new_data=scaler.transform([[Pregnancies,Glucose,BloodPressure,SkinThickness,Insulin,BMI,DiabetesPedigreeFunction,Age]])
        predict=model.predict(new_data)
       
        if predict[0] ==1 :
            result = 'WE ARE SORRY TO INFORM THAT YOU MAY HAVE DIABETES! PLEASE SEEK MEDICAL ADVICE'
            return render_template('single_prediction.html',result=result)
        else:
            result ="CONGRATULATIONS! YOU DO NOT HAVE DIABETES! STAY HEALTHY."


        return render_template('single_prediction.html',result=result)

    else:
        return render_template('regression.html', form=form)

@app.route('/page2',methods=['GET','POST'])
def predict_datapoint_c():
    result=""
    if request.method=='POST':

        Pregnancies=int(request.form.get("Pregnancies"))
        Glucose = float(request.form.get('Glucose'))
        BloodPressure = float(request.form.get('BloodPressure'))
        SkinThickness = float(request.form.get('SkinThickness'))
        Insulin = float(request.form.get('Insulin'))
        BMI = float(request.form.get('BMI'))
        DiabetesPedigreeFunction = float(request.form.get('DiabetesPedigreeFunction'))
        Age = float(request.form.get('Age'))

        new_data=scaler.transform([[Pregnancies,Glucose,BloodPressure,SkinThickness,Insulin,BMI,DiabetesPedigreeFunction,Age]])
        predict=model.predict(new_data)
       
        if predict[0] ==1 :
            result = 'WE ARE SORRY TO INFORM THAT YOU MAY HAVE DIABETES! PLEASE SEEK MEDICAL ADVICE'
            return render_template('single_prediction.html',result=result)
        else:
            result ="CONGRATULATIONS! YOU DO NOT HAVE DIABETES! STAY HEALTHY."


        return render_template('single_prediction.html',result=result)

    else:
        return render_template('classification.html')

if __name__=="__main__":
    app.run(host='0.0.0.0')
