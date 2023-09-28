import numpy as np
import time
import matplotlib.pyplot as plt
from sklearn.preprocessing import MinMaxScaler, StandardScaler
from sklearn.metrics import accuracy_score, confusion_matrix, classification_report
import pickle
import os
import pandas as pd
import seaborn as sns
import random

with open('r_clf_best.sav', 'rb') as f:
    clf = pickle.load(f)
    
scaler = MinMaxScaler()

files = os.listdir('../real_data/csv/')

meta = pd.read_csv('../real_data/metadata.csv')
meta.columns = ["index", "station", "yyyy.yyyy", "type", "description", "unknown", "magnitude"]
meta.set_index("index", inplace=True)

def datavis_func ():
    station = files[random.randrange(1, len(files))][0:4]
    df = pd.read_csv('../real_data/csv/' + 'TBLP.csv')
    df.drop(['site', 'YYMMMDD', '__MJD', 'week', 'd', 'reflon', '_e0(m)', '____n0(m)', 'u0(m)', '_ant(m)', 'sig_e(m)', 'sig_n(m)', 'sig_u(m)', '__corr_en', '__corr_eu', '__corr_nu'], axis=1, inplace=True)
    df.columns = ['date', 'un', 'ue', 'uz']

    rows_to_keep = [x for x in range(df.shape[0]) if x % 3 == 1]
    df = df.iloc[rows_to_keep, :]

    un = df[['date','un']]
    ue = df[['date','ue']]
    uz = df[['date','uz']]
    un_scaled = scaler.fit_transform(df['un'].to_numpy().reshape(-1, 1))
    ue_scaled = scaler.fit_transform(df['ue'].to_numpy().reshape(-1, 1))
    uz_scaled = scaler.fit_transform(df['uz'].to_numpy().reshape(-1, 1))

    df['un'] = un_scaled
    df['ue'] = ue_scaled
    df['uz'] = uz_scaled
    
    generate_visual(station, df)
    
    
def generate_visual (station, df):
    offset_dates = meta[meta.station==station]
    eq_dates = offset_dates[offset_dates.magnitude.isnull()==False]['yyyy.yyyy']
    offset_dates = offset_dates[offset_dates.magnitude.isnull()==True]['yyyy.yyyy']
    
    window_size = 200
    interval_size = 10

    un_pred_dates = [] 
    i = 0 
    while i < df.shape[0] - window_size:    
        pred = clf.predict(np.array(df.iloc[i:i+window_size]['un']).reshape(1,-1))

        if pred == 1:
            un_pred_dates.append(df.iloc[i+int(window_size/2), 0])    

        i += interval_size

    ue_pred_dates = [] 
    i = 0 
    while i < df.shape[0] - window_size:    
        pred = clf.predict(np.array(df.iloc[i:i+window_size]['ue']).reshape(1,-1))

        if pred == 1:
            ue_pred_dates.append(df.iloc[i+int(window_size/2), 0])    

        i += interval_size

    uz_pred_dates = [] 
    i = 0 
    while i < df.shape[0] - window_size:    
        pred = clf.predict(np.array(df.iloc[i:i+window_size]['uz']).reshape(1,-1))

        if pred == 1:
            uz_pred_dates.append(df.iloc[i+int(window_size/2), 0])    

        i += interval_size


    fig, ax = plt.subplots(figsize=(12, 6))

    np.random.seed(42)
    x = np.random.rand(150)

    fig, ax = plt.subplots(figsize=(12, 6))
    plt.plot(df[['date', 'un']].set_index('date'), label='un');
    plt.legend()
    ax.vlines(un_pred_dates, 0, 1, colors='red', alpha=0.3)
    ax.vlines(list(offset_dates), 0, 1, colors='brown', linewidth=4)
    ax.vlines(list(eq_dates), 0, 1, colors='green', linewidth=4)
    plt.savefig('real_data_vis/imgs/'+ station + '_pred_vis_un.jpg')

    plt.figure()
    fig, ax = plt.subplots(figsize=(12, 6))
    plt.plot(df[['date', 'ue']].set_index('date'), label='ue');
    plt.legend()
    ax.vlines(ue_pred_dates, 0, 1, colors='red', alpha=0.3)
    ax.vlines(list(offset_dates), 0, 1, colors='brown', linewidth=4)
    ax.vlines(list(eq_dates), 0, 1, colors='green', linewidth=4)
    plt.savefig('real_data_vis/imgs/'+ station + '_pred_vis_ue.jpg')

    plt.figure()
    fig, ax = plt.subplots(figsize=(12, 6))
    plt.plot(df[['date', 'uz']].set_index('date'), label='uz');
    plt.legend()
    ax.vlines(uz_pred_dates, 0, 1, colors='red', alpha=0.3)
    ax.vlines(list(offset_dates), 0, 1, colors='brown', linewidth=4)
    ax.vlines(list(eq_dates), 0, 1, colors='green', linewidth=4)
    plt.savefig('real_data_vis/imgs/'+ station + '_pred_vis_uz.jpg')

    plt.xticks(rotation=25);
    plt.legend();
    
    
    
def square_num_func(x):
    return x * x