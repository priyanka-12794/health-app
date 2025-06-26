# -*- coding: utf-8 -*-
"""
Created on Thu Jun 26 12:19:03 2025

@author: Asus
"""  


import pickle
import streamlit as st
import joblib

from streamlit_option_menu import option_menu



#loading the saved models
diabetes_model = pickle.load(open('C:/internshipss/diabetes_model (2).sav','rb'))
heart_disease_model = pickle.load(open('C:/internshipss/heart_model (2).sav','rb'))

parkinsons_model = joblib.load('C:/internshipss/parkinsons_model.sav')


#sidebar for navigation
with st.sidebar:
    selected = option_menu('Multiple Disease Prediction System',
                           ['Diabetes Prediction',
                            'Heart Disease Prediction',
                            'Parkinsons Prediction'],
                           icons=['activity','heart','person'],
                           default_index=0)
    
#Diabetes Prediction page
if(selected == 'Diabetes Prediction'):
    
    #page title 
    st.title('Diabetes Prediction using ML')
    
    #getting the input data from the user
    col1, col2, col3 = st.columns(3)
    
    with col1:
        Pregnancies = st.text_input('Number of Pregnancies')
        
    with col2:
        Glucose = st.text_input('Glucose level')
    
    with col3:
        BloodPressure = st.text_input('Blood Pressure value')

    with col1:
        SkinThickness = st.text_input('Skin Thickness value')
        
    with col2:
        Insulin = st.text_input('Insulin in level')
        
    with col3:
        BMI = st.text_input('BMI value')
        
    with col1:
        DiabetesPedigreeFunction = st.text_input('Diabetes Pedigree Function value')
        
    with col2:
        Age = st.text_input('Age of the Person')
        
    #code for Prediction
    diab_diagnosis = ''
    
    #creating a button for Prediction 
    if st.button('Diabetes Test Result'):
        diab_prediction = diabetes_model.predict([[float(Pregnancies), float(Glucose), float(BloodPressure), float(SkinThickness), float(Insulin), float(BMI), float(DiabetesPedigreeFunction), float(Age)]])
        
        if(diab_prediction[0] == 1):
            diab_diagnosis = 'The person is diabetic'
        else:
            diab_diagnosis = 'The person is not diabetic'
        
    st.success(diab_diagnosis)
    
    
    
    
    
#Heart Disease Prediction Page
if(selected == 'Heart Disease Prediction'):
    
    #page title
    st.title('Heart Disease Prediction using ML')
    
    col1, col2, col3 = st.columns(3)
    
    with col1:
        age = st.text_input('Age')
        
    with col2:
        sex=st.text_input('Sex')
        
    with col3:
        cp = st.text_input('Chest Pain types')
    
    with col1:
        trestbps = st.text_input('Resting Blood Pressure')
    
    with col2:
        chol = st.text_input('Serum Cholestoral in mg/dl')
    
    with col3:
        fbs = st.text_input('Fasting Blood Sugar > 120 mg/dl')
    
    with col1:
        restecg = st.text_input('Resting Electrocardiographic results')
    
    with col2:
        thalach = st.text_input('Maximum Heart Rate achieved')
    
    with col3:
        exang = st.text_input('Exercise Induced Angina')
    
    with col1:
        oldpeak = st.text_input('ST depression induced by exercise')
    
    with col2:
        slope = st.text_input('Slope of the peak exercise ST segment')
    
    with col3:
        ca = st.text_input('Major vessels colored by flourosopy')
    
    with col1:
        thal = st.text_input('thal: 0 = normal; 1 = fixed defect; 2=reversable defect')
        
        
    #code for Prediction
    heart_diagnosis = ''
    
    #creating a button for Prediction
    
    if st.button('heart Disease Test Result'):
        heart_prediction = heart_disease_model.predict([[float(age), float(sex), float(cp), float(trestbps),
                float(chol), float(fbs), float(restecg), float(thalach),
                float(exang), float(oldpeak), float(slope), float(ca),
                float(thal)]])

        if(heart_prediction[0] == 1):
            heart_diagnosis = 'The person is having heart disease'
        else:
            heart_diagnosis = 'The person does not have any heart disease'
            
    st.success(heart_diagnosis)
    
    
    
# Parkinson’s Prediction Page
if(selected == 'Parkinsons Prediction'):

    st.title("Parkinson’s Disease Prediction")
    st.write("Parkinsons form loading..")

    col1, col2, col3 = st.columns(3)

    with col1:
        fo = st.text_input("MDVP:Fo(Hz)")
    with col2:
        jitter_abs = st.text_input("MDVP:Jitter(Abs)")
    with col3:
        ppq = st.text_input("MDVP:PPQ")
    with col1:
        shimmer = st.text_input("MDVP:Shimmer")
    with col2:
        apq5 = st.text_input("Shimmer:APQ5")
    with col3:
        dda = st.text_input("Shimmer:DDA")
    with col1:
        dfa = st.text_input("DFA")
    with col2:
        spread2 = st.text_input("Spread2")
    with col3:
        fhi = st.text_input("MDVP:Fhi(Hz)")
    with col1:
        jitter_percent = st.text_input("MDVP:Jitter(%)")
    with col2:
        rap = st.text_input("MDVP:RAP")
    with col3:
        shimmer_db = st.text_input("MDVP:Shimmer(dB)")
    with col1:
        apq = st.text_input("MDVP:APQ")
    with col2:
        nhr = st.text_input("NHR")
    with col3:
        rpde = st.text_input("RPDE")
    with col1:
        d2 = st.text_input("D2")
    with col3:
        flo = st.text_input("MDVP:Flo(Hz)")
    with col1:
        ddp = st.text_input("Jitter:DDP")
    with col2:
        apq3 = st.text_input("Shimmer:APQ3")
    with col3:
        hnr = st.text_input("HNR")
    with col1:
        spread1 = st.text_input("Spread1")
    with col2:
        ppe = st.text_input("PPE")

    diagnosis = ''

    if st.button("Parkinson's Test Result"):
        park_prediction = parkinsons_model.predict([[float(fo), float(jitter_abs), float(ppq), float(shimmer), float(apq5), float(dda),
                                                     float(dfa), float(spread2), float(fhi), float(jitter_percent), float(rap), float(shimmer_db),
                                                     float(apq), float(nhr), float(rpde), float(d2), float(flo), float(ddp), float(apq3), float(hnr),
                                                     float(spread1), float(ppe)]])
        if park_prediction[0] == 1:
            diagnosis = "You have Parkinson's disease"
        else:
            diagnosis = "You do not have Parkinson's disease"

    st.success(diagnosis)


