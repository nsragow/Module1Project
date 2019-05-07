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
    global_dict["pd"] = pd
    global_dict["np"] = np
    global_dict["sm"] = sm
    global_dict["plt"] = plt
    global_dict["sns"] = sns
    global_dict["prprc"] = prprc
    global_dict["df"] = pd.read_csv("kc_house_data.csv")
    
