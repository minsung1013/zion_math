import streamlit as st

st.title('최상위 수학 6-2')
st.subheader('page')

corrects = ['9', '6', '1', '120000', '가', '30240', '50', '01:35', '36']
problems = ['4-1', '4-2','4-3','5-1: 숫자만','5-2','5-3: 숫자만','6-1: 숫자만','6-2:시간:분','6-3']
answers = []

for i in range(len(problems)):
    form = st.form(problems[i])
    answers.append(form.text_input(problems[i]))

    if answers[i] == corrects[i]:
        form.write('good job')
    else:
        form.write('sorry, try again')

    form.form_submit_button("Submit")

if corrects == answers:
    st.balloons()