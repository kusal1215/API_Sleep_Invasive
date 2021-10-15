# -*- coding: utf-8 -*-
"""
Created on Fri May  7 23:49:11 2021

@author: kusal
"""

# 1. Library imports
import uvicorn
from fastapi import FastAPI
from DepressionIP import DepressionIP
import numpy as np
import pickle
import pandas as pd
# 2. Create the app object
app = FastAPI()
pickle_in = open("sleep_data_model_pickle","rb")
mp=pickle.load(pickle_in)

# 3. Index route, opens automatically on http://127.0.0.1:8000
@app.get('/')
def index():
    return {'message': 'Hello, World'}

# 4. Route with a single parameter, returns the parameter within a message
#    Located at: http://127.0.0.1:8000/AnyNameHere
@app.get('/{name}')
def get_name(name: str):
    return {'Welcome To Behaviour Analysis': f'{name}'}

# 3. Expose the prediction functionality, make a prediction from the passed
#    JSON data and return the predicted Bank Note with the confidence
@app.post('/predict')
def predict_depression(data:DepressionIP):
    data = data.dict()
    print(data)
    
    Gender=data['Gender']
    Age=data['Age']
    Totaltimef=data['Totaltimef']
    Deepsleepf=data['Deepsleepf']
    REMSf=data['REMSf']
    LightSleepf=data['LightSleepf']
    print(mp.predict([[Gender,Age,Totaltimef,Deepsleepf,REMSf,LightSleepf]]))
    prediction = mp.predict([[Gender,Age,Totaltimef,Deepsleepf,REMSf,LightSleepf]])
    if(prediction[0] == 0):
        prediction="Normal"
    else:
        prediction="Not Optimal"
    return {
        'prediction': prediction
    }

# 5. Run the API with uvicorn
#    Will run on http://127.0.0.1:8000
if __name__ == '__main__':
    uvicorn.run(app, host='127.0.0.1', port=8000)
    
#uvicorn app:app --reload