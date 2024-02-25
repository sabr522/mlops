from flask import Flask, request, app,render_template
from flask import Response
from Forms import CreateUserForm_regression
from AImodel import Prediction_sharina
import pickle
import numpy as np
import pandas as pd


app = Flask(__name__)


regression_model =pickle.load(open("models/regression.pkl", "rb"))

@app.route('/',methods=['GET','POST'])
def predict_datapoint():
    result=""
    form = CreateUserForm_regression(request.form)
    if request.method=='POST' and form.validate():

        accommodates = int(request.form.get('accommodates'))
        availability_30 = int(request.form.get('availability_30'))
        bathrooms = int(request.form.get('bathrooms'))
        bedrooms = int(request.form.get('bedrooms'))
        beds = int(request.form.get('beds'))
        calculated_host_listings_count = int(request.form.get('calculated_host_listings_count'))
        host_listings_count = int(request.form.get('host_listings_count'))
        cancellation_policy = request.form.get('cancellation_policy')
        guests_included = int(request.form.get('guests_included'))
        latitude = float(request.form.get('latitude'))
        longitude = float(request.form.get('longitude'))
        maximum_nights = int(request.form.get('maximum_nights'))
        number_of_reviews = int(request.form.get('number_of_reviews'))
        review_scores_communication = int(request.form.get('review_scores_communication'))
        review_scores_rating = int(request.form.get('review_scores_rating'))
        room_type = request.form.get('room_type')
        amenities = request.form.getlist('amenities')

        print(amenities)
        data_arr_sharina = [[accommodates, availability_30, bathrooms, bedrooms, beds, calculated_host_listings_count,
                            cancellation_policy, cancellation_policy,guests_included, host_listings_count,latitude, longitude,
                            maximum_nights, number_of_reviews, review_scores_communication,review_scores_rating, room_type,
                            0,0,0,0,0,0,0,0,0,0,0,0]]
        prediction_s = Prediction_sharina(data_arr_sharina, amenities)
        result = 'Predicted Rent: ${:.2f}'.format(prediction_s)
        print(result)
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
