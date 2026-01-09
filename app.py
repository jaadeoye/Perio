import streamlit as st

st.write("""
         # Model-based Screening for Periodontitis and Severe Periodontitis
         """
         )
st.markdown('####')
st.write('**:violet[Periodontitis]**')

with st.form(key='periodontitis'):
    age = st.number_input('age',value=0.)
    gender = st.number_input('Gender',value=0.) 
    Q2 = st.number_input('Health of teeth and gums',value=0.)   
    Q4 = st.number_input('Loose teeth without injury',value=0.)   
    st.form_submit_button('Calculate risk')

result = ((1.406 * Q2) + (1.659 * Q4) + (0.105 * age) + (0.834 * gender) - 4.431)
if result < 0.73 :
    st.write('Predicted score is {result}', "**:green[LOW RISK]**")
else:
    st.write('Predicted score is {result}', "**:red[HIGH RISK]**")
         
st.markdown('####')

st.write('**:violet[Severe Periodontitis]**')

with st.form(key='periodontitis'):
    age = st.number_input('age',value=0.)
    smoke = st.number_input('Smoking',value=0.)
    gender = st.number_input('Gender',value=0.)   
    Q1 = st.number_input('Gum disease',value=0.)
    Q2 = st.number_input('Health of teeth and gums',value=0.)   
    Q4 = st.number_input('Loose teeth without injury',value=0.)
    Q6 = st.number_input('Teeth do not look right',value=0.)     
    st.form_submit_button('press to calculate')

result = a + b**2
if result < 0 :
    st.error('negative result')
else:
    st.write(f'result is {result}')



