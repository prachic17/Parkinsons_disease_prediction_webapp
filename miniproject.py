# -*- coding: utf-8 -*-

import pandas as pd
from sklearn.model_selection import train_test_split
from xgboost import XGBClassifier
import pickle


df=pd.read_csv(r'parkinsons.data')
X = df.drop(['name','status'], axis=1)
y= df.status
X_train, X_valid, y_train, y_valid = train_test_split(X, y,random_state=7)

pks_model = XGBClassifier()

pks_model.fit(X_train.values, y_train.values)

pickle.dump(pks_model,open('model.pkl','wb'))






