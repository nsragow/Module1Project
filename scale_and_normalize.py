import numpy as np
import sklearn.preprocessing as prprc
import warnings





def min_max_dataframe(dataframe,ignore = []):
    '''
    Min Max scales each column in the dateframe.
    This will make the coefficients easier to compare.
    
    Parameters:
        dataframe - the dataframe to be min max scaled
        ignore - will not min max scale column names in this list
    '''
    from sklearn.exceptions import DataConversionWarning
    warnings.filterwarnings("ignore", category=DataConversionWarning)

    mm_df = dataframe.copy()
    for col in (mm_df.columns[(mm_df.dtypes == "int64") | (mm_df.dtypes == "float64")]):
        if col not in ignore:
            mm_df[col] = min_max_scaled_column(mm_df[col])
    return mm_df




def min_max_scaled_column(col):
    shaped_col = np.array(col).reshape(-1,1)
    scaler = prprc.MinMaxScaler()
    scaler.fit(shaped_col)
    prprc.MinMaxScaler(copy=True, feature_range=(0, 1))

    return scaler.transform(shaped_col)
