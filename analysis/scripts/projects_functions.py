{
 "cells": [],
 "metadata": {},
 "nbformat": 4,
 "nbformat_minor": 5
}
import pandas as pd
import numpy as np
import seaborn as sns
data = pd.read_csv('data/rawdata/Bike-Sharing-Dataset/day.csv')
def load_and_process(data):
    df1 = (pd.DataFrame(data=data)
       .rename(columns={"cnt":"count"})
       .dropna())
    df2 = (df1
       .drop(columns=["dteday","season","yr","mnth","weekday","workingday","holiday","atemp","hum","temp","windspeed"]))
    return df2

load_and_process(data)
def EAD(df):
    df.describe()
    ##The minimum number of casual users was 2 and the maximum was 3410.
    ##The minimum number of registered users was 22 and the maximum was 6946.
    ##The average number of casual users is around 848 users per day.
    ##The mean for registered user is over 4 times higher that casual users, at around 3656 users a day.
    plt1 = df.plot(kind='scatter', x='casual', y='weathersit')
    plt2 = df.plot(kind='scatter', x='registered', y='weathersit')
    ##In both situations (casual and registered users,plt1 and plt2), you can see that there are generally lower counts of users on days where the weather situation is 3 (light snow or rain, thunderstorms,etc.)
    ##There are higher counts when the wheather situation is 1 (clear to partly cloudy).
    ##There is a greater range of registered users using the bikeshare system in wheather situation 3 than for casual users.
    plt3=df['casual'].plot(kind='hist', bins=20, figsize=(12,6), facecolor='pink',edgecolor='black').set_title("Frequency of amount of casual users used the bikesharing system")
    ##This graph shows that there is a high frequency of days where there are few casual users.
    ##It also shows that there are less commonly days where over 2000 people are using the bikes.
    plt4=df['registered'].plot(kind='hist', bins=20, figsize=(12,6), facecolor='green',edgecolor='black').set_title("Frequency of amount of registered users used the bikesharing system")
    ##This graph shows that there are many days where around 4000 users are using the bikesharing system.
    ##It also shows that there are few days when few or many people using bikes.