def print_hi():
    print("Hi")
imports = {}
def import_all(global_dict):
    import pandas as pd
    import numpy as np
    import statsmodels.api as sm
    import matplotlib.pyplot as plt
    import seaborn as sns
    import sklearn.preprocessing as prprc
    import feature_engineering as fe
    import dataframe_cleaning, scale_and_normalize
    import ols_models, visual
    global_dict["visual"] = visual
    global_dict["om"] = ols_models
    global_dict["dataframe_cleaning"] = dataframe_cleaning
    global_dict["scale_and_normalize"] = scale_and_normalize
    global_dict["pd"] = pd
    global_dict["np"] = np
    global_dict["sm"] = sm
    global_dict["plt"] = plt
    global_dict["sns"] = sns
    global_dict["prprc"] = prprc
    global_dict["fe"] = fe
    global_dict["df"] = pd.read_csv("kc_house_data.csv")
    
