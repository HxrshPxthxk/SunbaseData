import streamlit as st
import pandas as pd
import numpy as np

import joblib
def main():
    model = joblib.load("model.sav")
    st.title('Customer Churn Prediction App')
    st.markdown("""
     :dart:  This Streamlit app is made to predict customer churn. 
    """)
    
    st.info("Input data below")
    
    
    st.subheader('Enter Age')
    age = st.number_input('Age of the customer', min_value=0, max_value=120, value=18)
    
    st.subheader("Gender based data")
    gender = st.selectbox('Your Gender:', ('Male', 'Female'))
    
    st.subheader("Location based data")
    location = st.selectbox('Your Location:', ('Houstan', 'Los Angeles','New York','Miami'))
    
    st.subheader('Enter Subscription Length in Months')
    sub = st.number_input('Enter Subscription Length in Months', min_value=0, max_value=200, value=1)
    
    st.subheader('Enter Monthly Bill')
    mon_bill = st.number_input(label='Monthly Bill',step=1.,format="%.2f")
    
    st.subheader('Enter Total GB Used')
    tgbu = st.number_input('Enter Total GB Used', min_value=0, max_value=1000, value=1)
    
    if gender == 'Male':
        gen = 1
    else:
        gen = 0
        
    
    if location == 'Miami':
        loc_m = 1
        loc_h = 0
        loc_a = 0
        loc_n = 0
    elif location == 'Los Angeles':
        loc_m = 0
        loc_h = 0
        loc_a = 1
        loc_n = 0 
    elif location == 'New York':
        loc_m = 0
        loc_h = 0
        loc_a = 0
        loc_n = 1 
    else:
        loc_m = 0
        loc_h = 1
        loc_a = 0
        loc_n = 0 
    
    data = {
        'Age' : age, 'Gender': gen, 'Location': location,'Subscription_Length_Months': sub, 'Monthly_Bill': mon_bill, 'Total_Usage_GB': tgbu
    }
    features_df = pd.DataFrame.from_dict([data])
    st.dataframe(features_df)
    true_df = pd.DataFrame.from_dict([data])
    true_df.drop(['Subscription_Length_Months','Monthly_Bill'],axis=1,inplace = True)
    true_df['Location_Houston'] = loc_h
    true_df['Location_Los_Angeles'] = loc_a
    true_df['Location_Miami'] = loc_m
    true_df['Location_New_York'] = loc_n
    new_feature_df = true_df[['Age','Gender','Total_Usage_GB','Location_Houston','Location_Los_Angeles','Location_Miami','Location_New_York']]
    prediction = model.predict(new_feature_df)
    
    if st.button('Predict'):
            if prediction == 1:
                st.warning('Yes, the customer will terminate the service.')
            else:
                st.success('No, the customer is happy with Services.')
if __name__ == '__main__':
        main()
