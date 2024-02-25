import seaborn as sns
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import pycaret
import hydra
from omegaconf import DictConfig
from pycaret.regression import *
from sklearn.preprocessing import MultiLabelBinarizer
import os

def clean_amenities(amenities_str):
    amenities_list = amenities_str.strip('{}').split(',')
    amenities_list = [amenity.strip().strip('"') for amenity in amenities_list]
    return amenities_list

@hydra.main(config_path="../config/model",config_name="model2")
def modelling(cfg: DictConfig) -> None:


    # Get the current working directory
    current_directory = os.getcwd()
    
    # Print the current working directory
    print("Current working directory:", current_directory)
    df = pd.read_csv(cfg.dataset.path)

    df.drop(columns=['Unnamed: 25'], inplace=True)
    df['price'] = df['price'].replace('[\$,]', '', regex=True).astype(float)
    df['amenities_cleaned'] = df['amenities'].apply(clean_amenities)
    mlb = MultiLabelBinarizer()
    amenities_binary = pd.DataFrame(mlb.fit_transform(df['amenities_cleaned']), columns=mlb.classes_, index=df.index)
    df_final = pd.concat([df, amenities_binary], axis=1)
    df = df_final.drop(columns=['amenities', 'amenities_cleaned', ''])

    s = setup(data = df, 
          target='price',
          feature_selection=cfg.setup.feature_selection,
          n_features_to_select=cfg.setup.n_features_to_select,
          remove_multicollinearity=cfg.setup.remove_multicollinearity,
          multicollinearity_threshold=cfg.setup.multicollinearity_threshold,
          session_id = 123
          
          )
    df2 = s.get_config('dataset_transformed')
    df2 = df2.reset_index(drop=True)

    s = setup(df2, session_id=123,transform_target = True, log_experiment = True, experiment_name = '213002D')
    best = compare_models()
    final_best = finalize_model(best)
    save_model(final_best, cfg.model.path)



if __name__ == "__main__":
    modelling()