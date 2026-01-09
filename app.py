import streamlit as st
import math

def reset_form_values():
    # Reset Periodontitis keys
    st.session_state['age'] = 0.0
    st.session_state['gender'] = 0.0
    st.session_state['Q2'] = 0.0
    st.session_state['Q4'] = 0.0
    # Reset Severe Periodontitis keys
    st.session_state['age'] = 0.0
    st.session_state['smoke'] = 0.0
    st.session_state['Q1'] = 0.0
    st.session_state['Q2'] = 0.0
    st.session_state['Q4'] = 0.0
    st.session_state['Q6'] = 0.0

st.write("""
         # Model-based Screening for Periodontitis and Severe Periodontitis
         """
         )
st.markdown('####')
st.write('**:violet[Periodontitis]**')

st.button("Reset Values", on_click=reset_form_values)

with st.form(key='periodontitis'):
    age = st.number_input('Age',value=0.)
    gender = st.number_input('Gender',value=0.) 
    Q2 = st.number_input('Health of teeth and gums',value=0.)   
    Q4 = st.number_input('Loose teeth without injury',value=0.)   
    st.form_submit_button('Calculate risk')

resulta = ((1.406 * Q2) + (1.659 * Q4) + (0.105 * age) + (0.834 * gender) - 4.431)
resultb = - resulta
result = 1 / (1 + math.exp(resultb))
if result < 0.73 :
    st.write(f'Predicted score is {result:.3g}')
    st.write("**:green[LOW RISK]**")
else:
    st.write(f'Predicted score is {result:.3g}')
    st.write("**:red[HIGH RISK]**")
         
st.markdown('####')

st.write('**:violet[Severe Periodontitis]**')

with st.form(key='severeperiodontitis'):
    age = st.number_input('Age')
    smoke = st.number_input('Smoking',value=0.)  
    Q1 = st.number_input('Gum disease',value=0.)
    Q2 = st.number_input('Health of teeth and gums',value=0.)   
    Q4 = st.number_input('Loose teeth without injury',value=0.)
    Q6 = st.number_input('Teeth do not look right',value=0.)     
    st.form_submit_button('Calculate risk')

resulta = ((1.055 * Q1) + (1.778 * Q2) + (1.142 * Q4) + (1.380 * Q6) + (0.130 * age) + (2.110 * smoke) - 9.785)
resultb = - resulta
result = 1 / (1 + math.exp(resultb))
if result < 0.42 :
    st.write(f'Predicted score is {result:.3g}')
    st.write("**:green[LOW RISK]**")
else:
    st.write(f'Predicted score is {result:.3g}')
    st.write("**:red[HIGH RISK]**")



