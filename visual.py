import seaborn as sns
def present(model):
    print(f"adjRSquared={model.rsquared_adj}")
    sns.scatterplot(x=model.model.endog,y=model.resid)    
