import pandas as pd
import numpy as np
import math
def load_and_process(path):
    house = pd.read_csv(path)
    # Method Chain 1 (Load and clean data)   
    house = (   
    pd.read_csv("../data/raw/California_Houses.csv")
    .rename(columns={"Tot_Rooms":"Rooms", "Tot_Bedrooms":"Bedrooms", "Median_Income":"Income", 
                              "Median_House_Value":"House_Value", "Median_Age":"Age"})
      )
    df2 = (
        house
        .apply(lambda x: 10000*x if x.name=='Income' else x)
        .assign(Rooms_Per_House=lambda x: (x['Rooms'] / x['Households']))
        .drop(columns=["Rooms"])
        .assign(Bedrooms_Per_House=lambda x: (x['Bedrooms'] / x['Households']))
        .drop(columns=["Bedrooms"])
        .assign(Population_Per_House=lambda x: (x['Population'] / x['Households']))
        .drop(columns=["Population"])
        .reindex(columns=['House_Value', 'Income', 'Age', 'Rooms_Per_House', 'Bedrooms_Per_House', 'Population_Per_House', 'Households', 'Latitude', 'Longitude', 'Distance_to_coast', 'Distance_to_LA', 'Distance_to_SanDiego', 'Distance_to_SanJose', 'Distance_to_SanFrancisco'])
    )
    return df2