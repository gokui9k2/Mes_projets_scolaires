
import pandas as pd 
from request import get_token, api_request
from elastic_ingestion import main
import time 
from elasticsearch import Elasticsearch
import time
from dotenv import load_dotenv
import os 

load_dotenv()

def data_SIG_STR(df): 
    df_blue = df[["b_age", "b_avg_sig_str_landed", "gender"]].rename(columns={"r_age": "Age", "b_avg_sig_str_landed": "avg_SIG_STR_landed"})
    df_red = df[["r_age", "r_avg_sig_str_landed", "gender"]].rename(columns={"r_age": "Age", "r_avg_sig_str_landed": "avg_SIG_STR_landed"})
    df =pd.concat([df_blue, df_red], ignore_index=True)
    df = df.groupby(["Age", "gender"])["avg_SIG_STR_landed"].mean().unstack()
    df = df.reset_index()
    
    return df


def data_weight_class(df): 
    df_blue = df[['b_avg_sig_str_pct', "weight_class", "gender"]].rename(columns={'b_avg_sig_str_pct': 'avg_SIG_STR_pct'})
    df_red = df[['r_avg_sig_str_pct', "weight_class", "gender"]].rename(columns={'r_avg_sig_str_pct': 'avg_SIG_STR_pct'})
    df_combined = pd.concat([df_blue, df_red], ignore_index=True)
    df_male = df_combined[df_combined["gender"] == "MALE"].groupby("weight_class")["avg_SIG_STR_pct"].mean().reset_index()
    df_female = df_combined[df_combined["gender"] == "FEMALE"].groupby("weight_class")["avg_SIG_STR_pct"].mean().reset_index()

    return df_male, df_female

def winner_ratio(df) : 
    value_counts = df['winner'].value_counts()
    percentage = (value_counts / len(df)) * 100
    return percentage 

def finish_ratio(df) : 
    value_counts = df['finish'].value_counts()
    percentage = (value_counts / len(df)) * 100
    return percentage 

def date(df):
    df['date'] = pd.to_datetime(df['date'], errors='coerce', dayfirst=False)
    df['date'] = df['date'].fillna(pd.to_datetime(df['date'], format='%m/%d/%Y', errors='coerce'))
    df['year'] = df['date'].dt.year
    events_per_year_dict = df['year'].value_counts().sort_index().to_dict()
    
    return events_per_year_dict


def carte(df):
    location_counts = df.groupby(['latitude', 'longitude', 'location']).size()
    location_dict = [
        {
            "latitude": lat,
            "longitude": lon,
            "location": location,
            "count": count
        }
        for (lat, lon, location), count in location_counts.items()
    ]
    return location_dict


def gender_tot(df):
    df_blue = df[['r_fighter', "gender"]].rename(columns={'r_fighter': 'fighter'})
    df_red = df[['b_fighter', "gender"]].rename(columns={'b_fighter': 'fighter'})
    df_combined = pd.concat([df_blue, df_red], ignore_index=True)

    df_unique_fighters = df_combined.drop_duplicates(subset=['fighter'])
    gender_counts = df_unique_fighters["gender"].value_counts()
    gender_dict = gender_counts.to_dict()
    return gender_dict





def wait_for_elasticsearch(host="elasticsearch", port=9200, timeout=60, scheme="http"):
    """Attendre qu'Elasticsearch soit disponible"""
    es = Elasticsearch([{'host': host, 'port': port, 'scheme': scheme}])
    start_time = time.time()
    while True:
        if es.ping():
            print("Elasticsearch est prêt!")
            return True
        if time.time() - start_time > timeout:
            raise ConnectionError("Elasticsearch n'est pas prêt après 60 secondes")
        print("En attente d'Elasticsearch...")
        time.sleep(5)



def process(user):

    login_url = "http://api:8000/login"
    data_url = "http://api:8000/data"
    token = get_token(user.email, user.password, login_url)
    data = api_request(data_url, token)
    df = pd.DataFrame(data['data'])
    df_str = data_SIG_STR(df)
    df_male , df_female = data_weight_class(df)
    red_blue = winner_ratio(df)
    finish_rat = finish_ratio(df)
    ufc_love = date(df)
    influnce_carte = carte(df)
    gender_disparity = gender_tot(df)

    wait_for_elasticsearch()
    main(df)
    return df_str , df_male ,df_female , red_blue ,finish_rat , ufc_love , influnce_carte, gender_disparity

