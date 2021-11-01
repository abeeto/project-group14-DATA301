import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

def load_and_process(file):
    df_clean =(
        pd.read_csv(file)
        .drop(["Distance_to_coast", "Distance_to_LA", "Distance_to_SanDiego", "Distance_to_SanJose", "Distance_to_SanFrancisco", "Longitude", "Latitude", "Median_Age"], axis = 1)
        .rename(columns = {"Median_House_Value": "Median House Value", "Median_Income": "Median Income (in thousands)", "Median_Age": "Median Age","Households" : "Number of Households"})
    )       
    df_refine =(
        df_clean
        .apply(lambda x: x * 10 if x.name == "Median Income (in thousands)" else x)
        .assign(Rooms_Per_Household = lambda x: (x["Tot_Rooms"]/x["Number of Households"]))
        .assign(Bedrooms_Per_Household = lambda x: (x["Tot_Bedrooms"]/x["Number of Households"]))
        .assign(People_Per_Household = lambda x: (x["Population"]/x["Number of Households"]))
        .assign(People_Per_Room = lambda x: (x["Rooms_Per_Household"]/x["People_Per_Household"]))
        .drop(columns = ["Tot_Rooms","Tot_Bedrooms"])
        .rename(columns = {"Rooms_Per_Household": "Rooms per Household", "Bedrooms_Per_Household" : "Bedrooms per Household", "People_Per_Household": "People Per Household"})
    )
    return df_refine



