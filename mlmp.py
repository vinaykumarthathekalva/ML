# -*- coding: utf-8 -*-
"""MLMP.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1Re1uE5ft2bETcHzruwNyhF-HRMv3lFxG
"""

from sklearn.feature_extraction.text import CountVectorizer
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score,confusion_matrix,classification_report

data=pd.read_csv('/content/drive/My Drive/python-smartknower/Reviews.csv')
data

data.drop(['Id','ProductId','UserId','ProfileName','Time','Text','HelpfulnessNumerator','HelpfulnessDenominator'],axis=1,inplace=True)
data.dropna(axis=0,inplace=True)

data['Sentiment']=data['Score'].apply(lambda Score: 'Positive' if Score>3 else('Negative' if Score<3 else "Neutral"))
index=data[data['Sentiment']==0].index
data.drop(index=index,axis=0,inplace=True)
data

X=data.iloc[:,1]
y=data['Sentiment']

xtrain,xtest,ytrain,ytest=train_test_split(X,y,test_size=0.3,random_state=0)

cv = CountVectorizer()
xtrain_tr = cv.fit_transform(xtrain)
xtest_tr= cv.transform(xtest)

from sklearn.linear_model import LogisticRegression
clf=LogisticRegression()
clf.fit(xtrain_tr,ytrain)


# Commented out IPython magic to ensure Python compatibility.
# %%writefile ML_APP.py
# import streamlit as st
# from PIL import Image
# from sklearn.feature_extraction.text import CountVectorizer
# import pandas as pd
# from sklearn.model_selection import train_test_split
# from sklearn.metrics import accuracy_score,confusion_matrix,classification_report
# data=pd.read_csv('/content/drive/My Drive/python-smartknower/Reviews.csv')
# data.drop(['Id','ProductId','UserId','ProfileName','Time','Text','HelpfulnessNumerator','HelpfulnessDenominator'],axis=1,inplace=True)
# data.dropna(axis=0,inplace=True)
# data['Sentiment']=data['Score'].apply(lambda Score: 'Positive' if Score>3 else('Negative' if Score<3 else "Neutral"))
# index=data[data['Sentiment']==0].index
# data.drop(index=index,axis=0,inplace=True)
# X=data.iloc[:,1]
# y=data['Sentiment']
# xtrain,xtest,ytrain,ytest=train_test_split(X,y,test_size=0.3,random_state=0)
# cv = CountVectorizer()
# xtrain_tr = cv.fit_transform(xtrain)
# xtest_tr= cv.transform(xtest)
# from sklearn.linear_model import LogisticRegression
# clf=LogisticRegression()
# clf.fit(xtrain_tr,ytrain)
# 
# 
# 
# 
# 
# st.title("SENTIMENT ANALYSIS")
# image=Image.open('/content/drive/My Drive/python-smartknower/Reviews_Image.jpeg')
# st.image(image,width=800)
# review=st.text_input('Enter your short review :')
# df= {'review':review}
# df=pd.DataFrame(df,index=[0])
# to_pred=df.iloc[:,0]
# result=clf.predict(cv.transform(to_pred))
# if(st.button('Predict')):
#     st.write(result[0])

from pyngrok import ngrok
ngrok.connect(port='8501')

!streamlit run ML_APP.py
 
