import pandas as pd
import numpy as np
import streamlit as st
import pickle as pk

model = pk.load(open('Heart_disease_model.pk1','rb'))

data = pd.read_csv('heart_disease.csv')

st.header('HEART DISEASE PREDICTOR')

gender = st.selectbox('Choose Gender', data['Gender'].unique())
if gender == 'Male':
    gen = 1 
else:
    gen=0

age=st.number_input('Enter Age')
currentSmoker=st.number_input('Is Patient CurrentSmoker')
cigsPerDay=st.number_input('Enter cigsPerDay')
BPMeds=st.number_input('Is Patient on BPMeds')
prevalentStroke=st.number_input('Is Patient Had Stroke')
prevalentHyp=st.number_input('Enter PrevalentHyp Status')
diabetes=st.number_input('Enter Diabetes Status')
totChol=st.number_input('Enter totChol')
sysBP=st.number_input('Enter sysBP')
diaBP=st.number_input('Enter diaBP')
BmI=st.number_input('Enter BMI')
heartRate=st.number_input('Enter HeartRate')
glucose=st.number_input('Enter glucose')

# input = np.array([[gender,age,currentSmoker,cigsPerDay,BPMeds,prevalentStroke,prevalentHyp,diabetes,totChol,sysBP,diaBP,BmI,heartRate,glucose]])
if st.button('Predict'):
    input = np.array([[gen,age,currentSmoker,cigsPerDay,BPMeds,prevalentStroke,prevalentHyp,diabetes,totChol,sysBP,diaBP,BmI,heartRate,glucose]])
    output=model.predict(input)
    if output == 0 :
        stn = 'Patient is Healthy,NO heart disease'
    else:
        stn= "Patient may have Heart disease"
    st.markdown(stn)    
    



