import functions,dataframe_cleaning
import scale_and_normalize
def run(global_dict):
    functions.import_all(global_dict)
    functions.import_all(globals())
    df = dataframe_cleaning.clean(globals()["df"])
    df = scale_and_normalize.min_max_dataframe(df,ignore=["price"])
    global_dict["df"] = df