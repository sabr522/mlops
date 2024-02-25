from flask import Flask, request, app,render_template
from flask import Response
from Forms import CreateUserForm_regression, mushroom_form
from AImodel import Prediction_sharina, Prediction_kaijie
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
def predict_kj():
    result=""
    form = mushroom_form(request.form)
    if request.method=='POST':
        flat_cap = request.form.get('flat_cap')
        bruises= request.form.get('bruises')
        odor= request.form.get('odor')
        gillsize= request.form.get('gillsize')

        data_arr = [[flat_cap,bruises,odor,gillsize]]
        p = Prediction_kaijie(data_arr)
        if p == 1:
            result = 'The mushroom is poisonous'
        elif p == 0:
            result = 'The mushroom is edible'
        else:
            result = 'No Prediction'

        return render_template('single_prediction.html',result=result)

    else:
        return render_template('classification.html',form=form)

if __name__=="__main__":
    app.run(host='0.0.0.0')
