import numpy as np
import seaborn as sns
import matplotlib
import matplotlib.pyplot as plt
from pandas import *

def load_and_process(path):
    
#     get rid of unused columns, rename existing ones into more convenient names
    
    df_clean = (
        read_csv(path)
        .drop(['Median_Age','Tot_Rooms','Tot_Bedrooms','Households','Population','Distance_to_SanDiego','Distance_to_SanJose'],axis='columns')
        .rename(columns = {
        'Median_House_Value' : 'med_price',
        'Median_Income' : 'med_income',
        'Distance_to_coast' : 'coast_dist',
        'Distance_to_LA' : 'la_dist',
        'Distance_to_SanFrancisco' : 'sf_dist'
        })
    )

#     convert distances from meters to km, convert income from 10,000's to dollars
    df_units_converted = (
        df_clean.apply(lambda x: x*10000 if x.name == "med_income" else x)
        .apply(lambda x: x/1000 if x.name == "la_dist" or x.name == "sf_dist" or x.name == "coast_dist" else x)
    )
    
    return df_units_converted

load_and_process('../data/raw/California_Houses.csv')