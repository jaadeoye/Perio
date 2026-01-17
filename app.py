import streamlit as st
import math

def reset_form_values():
    # Periodontitis keys
    st.session_state['p_age'] = 0
    st.session_state['p_gender'] = 'Female'
    st.session_state['p_smoke'] = 'No'
    st.session_state['p_Q1'] = 'No'    
    st.session_state['p_Q2'] = 'Excellent'
    st.session_state['p_Q4'] = 'No'
    st.session_state['p_Q6'] = 'No'


st.write("""
         # Model-based Screening for Periodontitis and Severe Periodontitis
         """
         )
op_gender = {"Female": 0, "Male": 1}
op_smoke = {"No":0, "Yes":1}
op_q1 = {"No":0, "Yes":1}
op_q2 = {"Excellent":0, "Very Good":0, "Good":0, "Fair":1, "Poor":1}
op_q4 = {"No":0, "Yes":1}
op_q6 = {"No":0, "Yes":1}

st.button("Reset Values", on_click=reset_form_values)
st.markdown('####')
st.write('**:violet[Input form]**')

with st.form(key='periodontitis'):
    age = st.number_input('Age', key='p_age', min_value=0, max_value=120,  step=1, format="%d")
    gender= st.radio('Gender', op_gender.keys(), key='p_gender') 
    gender= op_gender[gender]
    smoke=st.radio('Smoking', op_smoke.keys(), key='p_smoke')
    smoke=op_smoke[smoke]
    Q1=st.radio('Do you think you may have gum disease?', op_q1.keys(), key='p_Q1')
    Q1=op_q1[Q1]
    Q2=st.radio('Overall, how would you rate the health of your teeth and gums?', op_q2.keys(), key='p_Q2')
    Q2=op_q2[Q2]
    Q4=st.radio('Have you ever had any teeth become loose on their own, without injury?', op_q4.keys(), key='p_Q4')
    Q4=op_q4[Q4]
    Q6=st.radio('During the past 3 months, have you noticed a tooth that doesn’t look right?', op_q6.keys(), key='p_Q6')
    Q6=op_q6[Q6]  
    submit=st.form_submit_button('Calculate risk')

if submit:
    resulta = ((1.406 * Q2) + (1.659 * Q4) + (0.105 * age) + (0.834 * gender) - 4.431)
    result = 1 / (1 + math.exp(-resulta))
    if result < 0.73 :
        st.write(f'Periodontitis calculated risk is **:green[LOW]** with predicted score {result:.3g}')
    
    else:
        st.write(f'Periodontitis calculated risk is **:red[HIGH RISK]** with predicted score {result:.3g}')

    resultb = ((1.055 * Q1) + (1.778 * Q2) + (1.142 * Q4) + (1.380 * Q6) + (0.130 * age) + (2.110 * smoke) - 9.785)
    result_sev = 1 / (1 + math.exp(-resultb))
    if result_sev < 0.42 :
        st.write(f'Severe periodontitis calculated risk is **:green[LOW]** with predicted score {result_sev:.3g}')
    else:
        st.write(f'Severe periodontitis calculated risk is **:red[HIGH RISK]** with predicted score {result_sev:.3g}')


st.markdown('####')



