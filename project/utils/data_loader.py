import streamlit as st
import pandas as pd


def load_data(path=r"C:\Users\RAMYA\Downloads\11_Dashboard_08122026\application_train.csv")->pd.DataFrame:
    df= pd.read_csv(path)
    return df



# df = load_data("Data/application_train.csv")

# print(df.columns)





#from utils.data_loader import load_data