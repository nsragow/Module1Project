import pandas as pd
def clean(housing_df):
    '''
    Compound cleaning function. Runs each other cleaning function in this file in the order originally intended.
    
    housing_df (parameter) 
    |
    v clean_null_columns
    |
    v fix_misleading_columns
    |
    v convert_date_to_ordinal
    |
    v
    cleaned_df (return)
    '''
    return convert_date_to_ordinal(fix_misleading_columns(
        clean_null_columns(housing_df)))

def convert_date_to_ordinal(housing_df):
    df_cleaned = housing_df.copy()
    df_cleaned.date = df_cleaned.date.apply(lambda date : date.toordinal())
    return df_cleaned

def fix_misleading_columns(housing_df):

    df_cleaned = housing_df.copy()
    #get the median of sqft to be inserted into all '?' columns
    bsmt_median = df_cleaned[df_cleaned.sqft_basement != "?"].sqft_basement.astype("float64").median()
    #set '?'s to the median, then convert to 'float64'
    df_cleaned.sqft_basement = df_cleaned.sqft_basement.apply(
        lambda entry : bsmt_median if entry == "?" else entry).astype("float64")
    #convert date col to datetime type
    df_cleaned.date = pd.to_datetime(df_cleaned.date)
    
    return df_cleaned

def clean_null_columns(housing_df):
    '''
    Cleans and mutates the dataframe columns containing nulls to prepare it for modeling.
    
    Changed Columns:
        Waterfront:
            Changes to dummy variables `yes`, `no` and `missing` (implied).
            This will give the models a chance to discover if there is a correlation between missing and the dependent variable. If there is no correlation it can be dropped.
        Yr_renovated:
            Removed due to miniscule r_squared
        View:
            Replaced Nan's with the mean. This has miniscule negative affects on the correlation.
    '''
    #First move waterfront to dummy variables
    df_cleaned = housing_df.copy()
    df_cleaned["waterfront"] = df_cleaned.waterfront.apply(lambda val : "True" if val == 1 else "False" if val == 0 else "Missing")
    df_cleaned = df_cleaned.join(
        pd.get_dummies(df_cleaned["waterfront"],prefix="waterfront")
    )
    df_cleaned = df_cleaned.drop("waterfront_Missing",axis=1)
    df_cleaned = df_cleaned.drop("waterfront",axis=1)
    #next remove yr_renovated as it does not seem to explain much of the varience
    df_cleaned = df_cleaned.drop("yr_renovated",axis=1)
    #replacing missing values in view with the mean
    df_cleaned.view = df_cleaned.view.fillna(df_cleaned.view.mean())
    
    return df_cleaned
    