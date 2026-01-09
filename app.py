import streamlit as st

st.write("""
         # Model-based Screening for Periodontitis and Severe Periodontitis
         """
         )
st.markdown('####')
st.write('**:violet[Periodontitis]**')

with st.form(key='periodontitis'):
    Age = st.number_input('age',value=0.)
    Smoking = st.number_input('smoke',value=0.)
    Gender = st.number_input('gender',value=0.)   
    Gum disease = st.number_input('Q1',value=0.)
    Health of teeth and gums = st.number_input('Q2',value=0.)   
    Loose teeth without injury = st.number_input('Q4',value=0.)
    Teeth do not look right = st.number_input('Q6',value=0.)     
    st.form_submit_button('press to calculate')

result = a + b**2
if result < 0 :
    st.error('negative result')
else:
    st.write(f'result is {result}')
         
st.markdown('####')

st.write('**:violet[Severe Periodontitis]**')

with st.form(key='severe'):
    a = st.number_input('a',value=1.)
    b = st.number_input('b',value=2.)    
    st.form_submit_button('press to calculate')

result = a + b**2
if result < 0 :
    st.error('negative result')
else:
    st.write(f'result is {result}')



