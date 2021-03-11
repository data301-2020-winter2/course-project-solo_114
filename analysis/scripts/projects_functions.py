{
 "cells": [],
 "metadata": {},
 "nbformat": 4,
 "nbformat_minor": 5
}
import pandas as pd
import numpy as np
import seaborn as sns

data = pd.read_csv('../data/rawdata/Bike-Sharing-Dataset/day.csv')

df = (pd.DataFrame(data=data)
       .rename(columns={"cnt":"count"})
       .dropna()
       .drop(columns=["dteday","season","yr","mnth","weekday","workingday","holiday","atemp","hum","temp","windspeed"]))
df.head()
def load_and_process(data):
    df1 = (pd.DataFrame(data=data)
       .rename(columns={"cnt":"count"})
       .dropna())
    df2 = (df1
       .drop(columns=["dteday","season","yr","mnth","weekday","workingday","holiday","atemp","hum","temp","windspeed"]))
    return df2

load_and_process(data)

df.describe()
plt1 = df.plot(kind='scatter', x='casual', y='weathersit')
plt2 = df.plot(kind='scatter', x='registered', y='weathersit')
plt3=df['casual'].plot(kind='hist', bins=20, figsize=(12,6), facecolor='pink',edgecolor='black').set_title("Frequency of amount of casual users used the bikesharing system")
plt4=df['registered'].plot(kind='hist', bins=20, figsize=(12,6), facecolor='green',edgecolor='black').set_title("Frequency of amount of registered users used the bikesharing system")