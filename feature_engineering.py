import initx
initx.run(globals())



def find_best_benefit_base(target,feature,function,bases,df=None):
    best_base = None
    best_benefit = None
    
    for base in bases:
        if df is not None:
            df_copy = df.copy()
            df_copy[feature] = df_copy[feature].apply(lambda ent : function(ent,base))
            r_2_changed = sm.OLS(target,sm.add_constant(df_copy)).fit().rsquared
            r_2 = sm.OLS(target,sm.add_constant(df)).fit().rsquared
        else:
            r_2_changed = sm.OLS(target,sm.add_constant(function(np.array(feature),base))).fit().rsquared
            r_2 = sm.OLS(target,sm.add_constant(np.array(feature))).fit().rsquared
                     
                     
        benefit = (r_2_changed - r_2)
        
        
        if best_benefit == None:
            best_benefit = benefit
            best_base = base
        elif benefit > best_benefit:
            
            best_benefit = benefit
            best_base = base
    return best_benefit,best_base

