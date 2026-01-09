import streamlit as st

st.write("""
         # Model-based Screening for Periodontitis and Severe Periodontitis
         """
         )
st.markdown('####')
st.write('**Periodontitis**')

with st.form(key='periodontitis'):
    a = st.number_input('a',value=1.)
    b = st.number_input('b',value=2.)    
    st.form_submit_button('press to calculate')

result = a + b**2
if result < 0 :
    st.error('negative result')
else:
    st.write(f'result is {result}')
         
st.markdown('####')

st.write('**Severe Periodontitis**')

with st.form(key='severe'):
    a = st.number_input('a',value=1.)
    b = st.number_input('b',value=2.)    
    st.form_submit_button('press to calculate')

result = a + b**2
if result < 0 :
    st.error('negative result')
else:
    st.write(f'result is {result}')



