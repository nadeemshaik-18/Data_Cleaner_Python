#importing dependencies
import pandas as pd
import numpy as np
import xlrd
import openpyxl
import time
import random
import os


# data_path = "sales.xlsx"
# data_name = "New_Sales"

def data_Cleaner(data_path,data_name):

    print("Thank You for sharing details!")

    sec = random.randint(1,3) 

    # printing delay message
    print(f"Please wait for {sec} seconds! checking the file path !")
    time.sleep(sec)


    #checking if the path exists
    if not os.path.exists(data_path):
        print("Incorrect Path! Please enter correct path!")
        return
    else:
        #checking the dataset type
        if data_path.endswith(".csv"):
            print("Dataset is CSV FILE!")
            data = pd.read_csv(data_path,encoding_errors="ignore")

        elif data_path.endswith(".xlsx"):
            print("Dataset is EXCEL FILE!")
            data = pd.read_excel(data_path)
        else:
            print("Unkown File Type")
            return
      # printing delay message
    sec = random.randint(1,4)
    print(f"Please wait for {sec} seconds! checking total columns and rows !")
    time.sleep(sec)

    # showing number of records in dataset
    print(f"Dataset contains total rows:{data.shape[0]} \ntotal columns:{data.shape[1]}")

    # start cleaning

      # printing delay message
    sec = random.randint(1,3)
    print(f"Please wait for {sec} seconds! checking Duplicates !")
    time.sleep(sec)

    # checking duplicates
    duplicates = data.duplicated()
    total_duplicates = data.duplicated().sum()
    print(f"Dataset has: {total_duplicates} duplicate records")

    # saving duplicates
    if total_duplicates>0:
        duplicate_records = data[duplicates]
        duplicate_records.to_csv(f"{data_name}_duplicates.csv",index=None)

    # deleting duplicates
    df = data.drop_duplicates()

    # finding missing values 
    total_missing_value = df.isnull().sum().sum()
    missing_value_by_colums = df.isnull().sum()

    print(f"Dataset has Total missing value: {total_missing_value}")
    print(f"Dataset contain missing value by columns \n{missing_value_by_colums}")

    # dealing with missing values

      # printing delay message
    sec = random.randint(1,6)
    print(f"Please wait for {sec} seconds! Cleaning the dataset !")
    time.sleep(sec)

    columns = df.columns

    for col in columns:
        # filling mean for numeric columns all rows
        if df[col].dtype in(float,int):
            df[col]=df[col].fillna(df[col].mean())

        else:
        # dropping all rows with missing records for non number col
            df.dropna(subset=col,inplace=True)


    # data is cleaned
    print(f"Congrats! Dataset is cleaned! \nNumber of Rows: {df.shape[0]} Number of Columns: {df.shape[1]}")

    # printing delay message
    sec = random.randint(1,5)
    print(f"Please wait for {sec} seconds! Saving and Exporting datasets !")
    time.sleep(sec)

    # saving the cleaned dataset
    df.to_csv(f"{data_name}_Clean_data.csv",index=None)
    print("Dataset is saved and Exported :)")

if __name__ == "__main__":
    print("Welcome to Data Cleaner!")
    data_path = input("Please enter dataset path :")
    data_name = input("Please enter dataset name :")

    data_Cleaner(data_path,data_name)