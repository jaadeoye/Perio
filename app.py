import streamlit as st
import math

def reset_form_values():
    # Periodontitis keys
    st.session_state['p_age'] = 0.0
    st.session_state['p_gender'] = 0.0
    st.session_state['p_Q2'] = 0.0
    st.session_state['p_Q4'] = 0.0

    # Severe Periodontitis keys
    st.session_state['s_age'] = 0.0
    st.session_state['s_smoke'] = 0.0
    st.session_state['s_Q1'] = 0.0
    st.session_state['s_Q2'] = 0.0
    st.session_state['s_Q4'] = 0.0
    st.session_state['s_Q6'] = 0.0

st.write("""
         # Model-based Screening for Periodontitis and Severe Periodontitis
         """
         )
op_gender = {"Female": 0, "Male": 1}

st.button("Reset Values", on_click=reset_form_values)
st.markdown('####')
st.write('**:violet[Periodontitis]**')

with st.form(key='periodontitis'):
    age = st.number_input('Age', key='p_age', min_value=0, max_value=120,  step=1, format="%d")
    gender= st.radio('Gender', op_gender.keys(), key='p_gender') 
    gender= op_gender[gender]
    #gender = st.number_input('Gender', key='p_gender', min_value=0, max_value=5,  step=1, format="%d") 
    Q2 = st.number_input('Health of teeth and gums', key='p_Q2', min_value=0, max_value=120,  step=1, format="%d")   
    Q4 = st.number_input('Loose teeth without injury', key='p_Q4', min_value=0, max_value=120,  step=1, format="%d")   
    st.form_submit_button('Calculate risk')

resulta = ((1.406 * Q2) + (1.659 * Q4) + (0.105 * age) + (0.834 * gender) - 4.431)
result = 1 / (1 + math.exp(-resulta))
if result < 0.73 :
    st.write(f'Predicted score is {result:.3g}')
    st.write("**:green[LOW RISK]**")
else:
    st.write(f'Predicted score is {result:.3g}')
    st.write("**:red[HIGH RISK]**")
         
st.markdown('####')

st.write('**:violet[Severe Periodontitis]**')

with st.form(key='severeperiodontitis'):
    age = st.number_input('Age', key='s_age', min_value=0, max_value=120,  step=1, format="%d")
    smoke = st.number_input('Smoking', key='s_smoke', min_value=0, max_value=5,  step=1, format="%d")  
    Q1 = st.number_input('Gum disease', key='s_Q1', min_value=0, max_value=5,  step=1, format="%d")
    Q2 = st.number_input('Health of teeth and gums', key='s_Q2', min_value=0, max_value=120,  step=1, format="%d")   
    Q4 = st.number_input('Loose teeth without injury', key='s_Q4', min_value=0, max_value=120,  step=1, format="%d")
    Q6 = st.number_input('Teeth do not look right', key='s_Q6', min_value=0, max_value=120,  step=1, format="%d")     
    st.form_submit_button('Calculate risk')

resulta = ((1.055 * Q1) + (1.778 * Q2) + (1.142 * Q4) + (1.380 * Q6) + (0.130 * age) + (2.110 * smoke) - 9.785)
result = 1 / (1 + math.exp(-resulta))
if result < 0.42 :
    st.write(f'Predicted score is {result:.3g}')
    st.write("**:green[LOW RISK]**")
else:
    st.write(f'Predicted score is {result:.3g}')
    st.write("**:red[HIGH RISK]**")



