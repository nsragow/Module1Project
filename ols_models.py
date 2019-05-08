import initx
initx.run(globals())

def get_models():
    return {"base":base_model,
            "logged":logged_model,
            "logged_inverse":logged_model_inverse,
            "engineered":engineered_model,
            "logged_engineered":engineered_logged_model,
            "s_base":s_base_model,
            "s_logged":s_logged_model,
            "s_logged_inverse":s_logged_model_inverse,
            "s_engineered":s_engineered_model,
            "s_logged_engineered":s_engineered_logged_model,
            "final":final_model
           }

engineered_df = df.copy()
engineered_df.grade = engineered_df.grade.apply(lambda val : 54**val)
engineered_df.sqft_above = engineered_df.sqft_above.apply(lambda val : 12**val)

engineered_df.bathrooms = engineered_df.bathrooms.apply(lambda val : val**2)
engineered_df.sqft_living = engineered_df.sqft_living.apply(lambda val : val**2)
engineered_df.sqft_basement = engineered_df.sqft_basement.apply(lambda val : val**2)
engineered_df.sqft_living15 = engineered_df.sqft_living15.apply(lambda val : val**2)
engineered_df.yr_built = engineered_df.yr_built.apply(lambda val : val**6)
engineered_df.sqft_living = engineered_df.sqft_living.apply(lambda val : val**2)

base_model = sm.OLS(df.price,sm.add_constant(df.drop("price",axis=1))).fit()

logged_model = sm.OLS(np.log(df.price),sm.add_constant(df.drop("price",axis=1))).fit()

logged_model_inverse = sm.OLS(df.price,np.e**sm.add_constant(df.drop("price",axis=1))).fit()

engineered_model = sm.OLS((engineered_df.price),sm.add_constant(engineered_df.drop("price",axis=1))).fit()
engineered_logged_model = sm.OLS(np.log(engineered_df.price),sm.add_constant(engineered_df.drop("price",axis=1))).fit()

logged_model_cols = sm.OLS(np.log(df.price),sm.add_constant(df.drop("price",axis=1))).fit()


subsection = df[df.price > 6.450000e+05]


engineered_df = subsection.copy()
engineered_df.grade = engineered_df.grade.apply(lambda val : 54**val)
engineered_df.sqft_above = engineered_df.sqft_above.apply(lambda val : 12**val)

engineered_df.bathrooms = engineered_df.bathrooms.apply(lambda val : val**2)
engineered_df.sqft_living = engineered_df.sqft_living.apply(lambda val : val**2)
engineered_df.sqft_basement = engineered_df.sqft_basement.apply(lambda val : val**2)
engineered_df.sqft_living15 = engineered_df.sqft_living15.apply(lambda val : val**2)
engineered_df.yr_built = engineered_df.yr_built.apply(lambda val : val**6)
engineered_df.sqft_living = engineered_df.sqft_living.apply(lambda val : val**2)

s_base_model = sm.OLS(subsection.price,sm.add_constant(subsection.drop("price",axis=1))).fit()

s_logged_model = sm.OLS(np.log(subsection.price),sm.add_constant(subsection.drop("price",axis=1))).fit()

s_logged_model_inverse = sm.OLS(subsection.price,np.e**sm.add_constant(subsection.drop("price",axis=1))).fit()

s_engineered_model = sm.OLS((engineered_df.price),sm.add_constant(engineered_df.drop("price",axis=1))).fit()
s_engineered_logged_model = sm.OLS(np.log(engineered_df.price),sm.add_constant(engineered_df.drop("price",axis=1))).fit()

final_model = sm.OLS(np.log(df.price),sm.add_constant(df.drop(["price","waterfront_False","sqft_basement","sqft_above","id"],axis=1))).fit()