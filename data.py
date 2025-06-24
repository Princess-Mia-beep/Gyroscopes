# Experiment Data as pandas data frame
import pandas as pd


# Pt 1
# Raw Measurement Data for Part 1
data_10g = {
        "time_trial1_s": [19.38,16.05,12.21],
    "time_trial2_s":[19.50,14.88,12.25],
    "time_trial3_s":[19.15,15.31,12.83],
    "height_m": [0.9,0.6,0.4]
}
data_70g = {
    "time_trial1_s": [8.5,7.28,5.76],
    "time_trial2_s":[7.90,6.71,5.50],
    "time_trial3_s":[7.55,6.36,5.43],
    "height_m": [0.9,0.7,0.5]
}
data_100g = {
    "time_trial1_s": [5.90,4.18,3.51],
    "time_trial2_s":[5.38,4.08,3.18],
    "time_trial3_s":[5.15,4.14,3.20],
    "height_m": [0.9,0.6,0.4]
}

# Converting to panads dataframe 
df = pd.DataFrame(data_10g)
df["t_avg_s"] = df[["time_trial1_s","time_trial2_s","time_trial3_s"]].mean(axis=1)
df["t_avg_s_sqr"]=df["t_avg_s"]**2
pd_data_100g = df[['height_m', 't_avg_s_sqr']]

df = pd.DataFrame(data_70g)
df["t_avg_s"] = df[["time_trial1_s","time_trial2_s","time_trial3_s"]].mean(axis=1)
df["t_avg_s_sqr"]=df["t_avg_s"]**2
pd_data_70g = summary_df = df[['height_m', 't_avg_s_sqr']]

df = pd.DataFrame(data_100g)
df["t_avg_s"] = df[["time_trial1_s","time_trial2_s","time_trial3_s"]].mean(axis=1)
df["t_avg_s_sqr"]=df["t_avg_s"]**2
pd_data_100g = df[['height_m', 't_avg_s_sqr']]

