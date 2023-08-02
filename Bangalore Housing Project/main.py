from flask import Flask, render_template, request
import pandas as pd
import pickle
import numpy as np
app=Flask(__name__)
data=pd.read_csv('Cleaned_Data.csv')
pipe=pickle.load(open("RidgeModel.pkl",'rb'))
@app.route('/')
def index():
    locations=sorted(data['location'].unique())
    return render_template('index.html',location=locations)
@app.route('/predict',methods=['POST'])
def predict():
    locations=request.form.get('location')
    bhk=int(request.form.get('bhk'))
    bath=int(request.form.get('Bathrooms'))

    sqft=request.form.get('sqft')
    
    print(locations,bhk,bath,sqft)
    input=pd.DataFrame([[locations,sqft,bath,bhk]],columns=['location','total_sqft','bath','bhk'])
    prediction=pipe.predict(input)[0]*1e5
    return str(np.round(prediction,2))
if __name__=="__main__":
    app.run(debug=True,port=1000)