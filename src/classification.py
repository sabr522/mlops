import seaborn as sns
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import pycaret
import hydra
from omegaconf import DictConfig
from pycaret.classification import *
import os

@hydra.main(config_path="../config/model",config_name="model1")
def modelling(cfg: DictConfig) -> None:


    # Get the current working directory
    current_directory = os.getcwd()
    
    # Print the current working directory
    print("Current working directory:", current_directory)
    df = pd.read_csv(cfg.dataset.path)
    s = setup(data = df, 
          target='class',
          feature_selection=cfg.setup.feature_selection,
          n_features_to_select=cfg.setup.n_features_to_select,
          remove_multicollinearity=cfg.setup.remove_multicollinearity,
          multicollinearity_threshold=cfg.setup.multicollinearity_threshold,
          ordinal_features=cfg.setup.ordinal_features,
          low_variance_threshold=cfg.setup.low_variance_threshold,
          categorical_imputation=cfg.setup.categorical_imputation,
          session_id = 123
          
          )
    df2 = s.get_config('dataset_transformed')
    df2 = df2.reset_index(drop=True)

    s = setup(df2, session_id=123)
    best = compare_models()
    final_best = finalize_model(best)
    save_model(final_best, cfg.model.path)



if __name__ == "__main__":
    modelling()