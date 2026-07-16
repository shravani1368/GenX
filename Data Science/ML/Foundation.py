''' 
    Author : Vaishnvai Sukum
    Date_Started :26-05-2026
    Moto :
    Motivation :
    user guid : www.xyz.com/project_name/user_guid

'''

import pandas as pd
from sklearn.model_selection import train_test_split
import numpy as np
from scipy.stats import zscore


def Data_loading(location : str , 
                 type :str , 
                 tb_name=None):
    ''' 
    Data_loading
    ____________
    This function formats csv, json, sql files into dataframe
    give inputs as location of file , type of file  and
    if file is `sql` type then enter table name
    '''
    
    if type == "csv":
        df = pd.read_csv(location)
    elif type == "json":
        df = pd.read_json(location)
    elif type == "sql":
        df = pd.read_sql(f"SELECT * FROM {tb_name}",location)
    else:
        return "file cha type check kar "
    
    return df

def Analysis(df):
    line = "-"*64
    print(line)
    print(df.head())
    print(line)

    print(line)
    print("Data set info")
    print(line)
    print(df.description())
    print(line)

    print(line)
    print("Data set statistics ")
    print(line)
    print(df.info())
    print(line)

    return df.head() , df.decsription() , df.info()

def Clean_data(df):
    '''
    This function removes duplicate data and fills in missing entries 
    if int type of entry then mean and if char then mode
    '''
    f_num = df.select_dtypes(include="number").columns
    f_cat = df.select_dtypes(include="object").columns
    
    for col in f_num:
        df[col] = df[col].fillna(df[col].mean())
        
    for col in f_cat:
        df[col] = df[col].fillna(df[col].mode()[0])

    df = df.drop_duplicates()
    
    return df
  # search for data cleaning so no unclean data can pass


def preprocessing(df,
                  prediction_column):
    
  # X and Y splitting
    x= df.drop(df[["PassengerId","Name"]],axis=1)
    new_df = pd.get_dummies(df,dtype=int)#encoding converts srtring to int

    x= new_df.drop(new_df[[prediction_column]],axis=1)
    y = new_df[prediction_column]
    
    x, y = clean_outliers(x,y)

    x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=0.2, random_state=42)
    return x_train, x_test, y_train, y_test,new_df


def is_skewed(df, 
              threshold=0.5):
    skew_vals = df.select_dtypes(include=np.number).skew().abs()
    return skew_vals.mean() > threshold


def iqr_mask(df):
    mask = pd.Series(True, index=df.index)

    for col in df.columns:
        Q1 = df[col].quantile(0.25)
        Q3 = df[col].quantile(0.75)
        IQR = Q3 - Q1

        lower = Q1 - 1.5 * IQR
        upper = Q3 + 1.5 * IQR

        mask &= df[col].between(lower, upper)

    return mask


def zscore_mask(df,
                 threshold=3):
    z_scores = np.abs(zscore(df))
    return (z_scores < threshold).all(axis=1)


def clean_outliers(x,
                   y,
                   skew_threshold=0.5,
                   z_threshold=3):

    numeric_X = x.select_dtypes(include=np.number)

    if is_skewed(numeric_X, skew_threshold):
        mask = iqr_mask(numeric_X)
    else:
        mask = zscore_mask(numeric_X, z_threshold)

    X_clean = x[mask].reset_index(drop=True)
    y_clean = y[mask].reset_index(drop=True)

    return X_clean, y_clean

#$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$
# Machine_Learning Algorithms
#$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$

'''
These algorithums are directly being used by inerting from sklearn 
In simple words this is wrapper over the sklearn library 

'''
# 1.Regression algorithm

from sklearn import linear_model 
def regression(x_train ,
               y_tarin ,
               Algo = "Linear_regression ",
               boost = False):
    '''
    
    '''
    if Algo == "Linear_regression":
        model = linear_model.LinearRegression()
# sklearn web search for regression algo and put in elif
    #elif 
    model.fit (x_train , y_tarin)
    return model 

# 2.Classification
from sklearn.neighbors import KNeighborsClassifier
def classification(x_train ,
                   y_train,
                   Algo ="KNN",
                   boost = False):
    '''

    '''
    if Algo == "KNN" :
        model = KNeighborsClassifier()
    model.fit(x_train , y_train)
    return model 

    #  


