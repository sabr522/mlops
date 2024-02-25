import pandas as pd
import numpy as np
import pickle
from pycaret.regression import *

def Prediction_sharina(data, amenities):
    model = load_model('models/regression')
    print(model)
    columns = ['accommodates', 'availability_30', 'bathrooms', 'bedrooms', 'beds',
       'calculated_host_listings_count', 'cancellation_policy_flexible',
       'cancellation_policy_strict', 'guests_included', 'host_listings_count',
       'latitude(North)', 'longitude(East)', 'maximum_nights',
       'number_of_reviews', 'review_scores_communication',
       'review_scores_rating', 'room_type_Entire home/apt', 'Cable TV',
       'Carbon Monoxide Detector', 'Doorman', 'Essentials',
       'Fire Extinguisher', 'First Aid Kit', 'Free Parking on Premises',
       'Indoor Fireplace', 'Pool', 'Shampoo', 'Smoke Detector',
       'Suitable for Events']

    
    df = pd.DataFrame(data, columns=columns)
    for i in df.index:
        if df['cancellation_policy_flexible'][i] == "Flexible":
            df['cancellation_policy_flexible'][i] = 1
            df['cancellation_policy_strict'][i] = 0
        elif df['cancellation_policy_flexible'][i] == "Strict":
            df['cancellation_policy_flexible'][i] = 0
            df['cancellation_policy_strict'][i] = 1
        else:
            df['cancellation_policy_flexible'][i] = 0
            df['cancellation_policy_strict'][i] = 0
        if df['room_type_Entire home/apt'][i] == "Entire":
            df['room_type_Entire home/apt'][i] = 1
        else:
            df['room_type_Entire home/apt'][i] = 0
        if 'Cable' in amenities:
            df['Cable TV'][i] = 1
        if 'Carbon' in amenities:
            df['Carbon Monoxide Detector'][i] = 1
        if 'Doorman' in amenities:
            df['Doorman'][i] = 1
        if 'Essentials' in amenities:
            df['Essentials'][i] = 1
        if 'Extinguisher' in amenities:
            df['Fire Extinguisher'][i] = 1
        if 'Firstaid' in amenities:
            df['First Aid Kit'][i] = 1
        if 'Parking' in amenities:
            df['Free Parking on Premises'][i] = 1
        if 'Fireplace' in amenities:
            df['Indoor Fireplace'][i] = 1
        if 'Pool' in amenities:
            df['Pool'][i] = 1
        if 'Shampoo' in amenities:
            df['Shampoo'][i] = 1
        if 'Smoke' in amenities:
            df['Smoke Detector'][i] = 1
        if 'Events' in amenities:
            df['Suitable for Events'][i] = 1
    print(df)
    prediction = predict_model(model, data=df)
    print(prediction['prediction_label'].iloc[0])

    return prediction['prediction_label'].iloc[0]


def Prediction_kaijie(data):
    model = load_model('models/mushroomclass')
    print(model)
    columns = ['cap-shape_flat','bruises','odor_none','gill-size']

    
    df = pd.DataFrame(data, columns=columns)
    for i in df.index:
        if df['cap-shape_flat'][i] == "Yes":
            df['cap-shape_flat'][i] = 1
        else:
            df['cap-shape_flat'][i] = 0
        if df['bruises'][i] == "Yes":
            df['bruises'][i] = 0
        else:
            df['bruises'][i] = 1
        if df['odor_none'][i] == "No":
            df['odor_none'][i] = 1
        else:
            df['odor_none'][i] = 0
        if df['gill-size'][i] == "Narrow":
            df['gill-size'][i] = 1
        else:
            df['gill-size'][i] = 0


    print(df)
    prediction = predict_model(model, data=df)
    print(prediction)

    return prediction[0]
