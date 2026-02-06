import streamlit as st
import math
import time

if 'start_time' not in st.session_state:
    st.session_state.start_time = None
    
@st.dialog("PerioDetect")
def show_intro():
    st.write("Welcome to PerioDetect, a rapid self-service screening tool developed and validated using real cases by dentists and researchers at HKU Dentistry to help you assess your risk of gum disease (periodontitis), a common oral disease. Please follow the steps below to complete the screening.")
    st.markdown('####')
    st.write("**Terms of Service**")
    st.write("Before using PerioDetect, please note:")
    st.write("•	This tool does not provide a diagnosis and is for informational purposes only. It does not replace a professional dental evaluation.")
    st.write("•	Your personal data is protected with strict privacy measures.")
    st.markdown('####')
    st.write("**How to Use PerioDetect**")
    st.write("1.	Enter Your Basic Information")
    st.write("2.	Answer Health-Related Questions")
    st.write("3.	Submit Your Answers")
    st.write("4.	View Your Result")
    if st.button("I understand and agree to proceed"):
        st.session_state.intro_shown = True
        st.session_state.start_time = time.time()
        st.rerun() 

if "intro_shown" not in st.session_state:
    st.session_state.intro_shown = False

if not st.session_state.intro_shown:
    show_intro()
    
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
         # PerioDetect
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
    age = st.number_input('Age', key='p_age', min_value=15, max_value=120,  step=1, format="%d")
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
    result_percent= result * 100
    end_time = time.time()
    start=st.session_state.start_time
    if start is None:
        duration=0.0
    else:
        duration = end_time - start
    
    if result < 0.73 :
        st.write("**Periodontitis Risk:**")
        st.write(f'🔵 Low Risk (Predicted score: **:green[{result_percent:.1f}%]**)')
        st.write("Your responses indicate a low likelihood of having periodontitis.")
    
    else:
        st.write("**Periodontitis Risk:**")
        st.write(f'🔴 High Risk (Predicted score: **:red[{result_percent:.1f}%]**)')
        st.write("Your responses indicate a high likelihood of having periodontitis.")

    resultb = ((1.055 * Q1) + (1.778 * Q2) + (1.142 * Q4) + (1.380 * Q6) + (0.130 * age) + (2.110 * smoke) - 9.785)
    result_sev = 1 / (1 + math.exp(-resultb))
    result_sevpercent= result_sev * 100
    if result_sev < 0.42 :
        st.write("**Severe Periodontitis Risk:**")
        st.write(f'🔵 Low Risk (Predicted score: **:green[{result_sevpercent:.1f}%]**)')
        st.write("Your responses indicate a low likelihood of having severe periodontitis.")
    else:
        st.write("**Severe Periodontitis Risk:**")
        st.write(f'🔴 High Risk (Predicted score: **:red[{result_sevpercent:.1f}%]**)')
        st.write("Your responses indicate a high likelihood of having severe periodontitis.")
    if result < 0.73 and result_sev < 0.42:
        st.write("**Recommendation:** Continue maintaining good oral hygiene and schedule regular dental check-ups to stay healthy.")
    elif result >= 0.73 and result_sev < 0.42:
        st.write("**Recommendation:** We advise you to see a dentist promptly for a comprehensive examination and appropriate treatment to manage early-stage periodontitis and prevent progression to severe periodontitis.")
    elif result >= 0.73 and result_sev >= 0.42:
        st.write("**Recommendation:** We strongly recommend scheduling an appointment with your dentist as soon as possible for a comprehensive evaluation and treatment.")
    else:
        None

    st.success(f"Took {duration:.2f} seconds to complete.")
    st.session_state.start_time = time.time()
    
        


st.markdown('####')



