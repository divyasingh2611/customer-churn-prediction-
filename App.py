import pickle
import streamlit as st

st.title('Telecom Customer Churn Prediction :male-office-worker:')

load = open('Final_model.pkl','rb')
model = pickle.load(load)


def predict(Voice_messages, Night_mins, Evening_mins, Day_charge, Customer_calls):
    prediction = model.predict([[Voice_messages, Night_mins, Evening_mins, Day_charge, Customer_calls]])
    return prediction

def main():
    
    st.markdown('Determining wether the customer churns or not')
    #International_plan = st.selectbox('Do you have an int plan?',('Yes','No'))
    Customer_calls = st.number_input('No of calls to Customer Care', min_value= 0 , max_value=100)
    Voice_messages = st.number_input('No of voice messages', min_value= 0 , max_value=100)
    Day_charge = st.number_input('Day Charge')
    Night_mins = st.number_input('Night Mins used')
    Evening_mins = st.number_input('Evening Mins used')

    
    if st.button('Predict'):
        result = predict(Voice_messages, Night_mins, Evening_mins, Day_charge, Customer_calls)
        st.success('Did the customer churn?: {} '.format(result))                          
                          
        
if __name__ == '__main__':
    main()

