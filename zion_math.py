import streamlit as st

st.title('최상위 수학 6-2')

mon = '월요일 PAGE 66-68'
corrects = ['나가다마라', '다가나', '4', '다라', '나다라']
problems = ['1-1: 순서대로 예:가나다라마','2-1: 예: 가나다','2-2','3-1: 예 가나','3-2: 예 가나다']

tue = '화요일_PAGE 69-71'
corrects_tue = ['10','16','125','12']
problems_tue = ['5-1','5-2','6-1','6-2']

wed = '수요일_PAGE 72-74'
corrects_wed = ['2','5','34','168','다','2']
problems_wed = ['7-1','7-2','8-1','8-2','심화9 답만 예: 가', '9-1']

thu = "목요일_PAGE 75-77"
corrects_thu = ['3','2','43','6','ㄷㄹㅁ', '1,4', '2']
problems_thu = ['3','4','5','6','7 예: ㄱㄴㄷ','8예: 1,2','9']

fri = "금요일_PAGE 78-80"
corrects_fri = ['18','6','54','8','7','72','10','다라','3']
problems_fri = ['10','11','12','13','14','16','1','2: 예 가나','3']


with st.expander(mon):
    answers = []
    if len(corrects) != len(problems):
        st.write('프로그램에 에러가 있습니다. 관리자에게 문의하세요')

    for i in range(len(problems)):
        form = st.form(problems[i] + 'mon')
        answers.append(form.text_input(problems[i]))

        if answers[i] == corrects[i]:
            form.subheader('good job')
        else:
            form.write('sorry, try again')

        form.form_submit_button("Submit")

    if corrects == answers:
        st.balloons()


with st.expander(tue):
    answers_tue = []
    if len(corrects_tue) != len(problems_tue):
        st.write('프로그램에 에러가 있습니다. 관리자에게 문의하세요')

    for i in range(len(problems_tue)):
        form = st.form(problems_tue[i] + 'tue')
        answers_tue.append(form.text_input(problems_tue[i]))

        if answers_tue[i] == corrects_tue[i]:
            form.subheader('good job')
        else:
            form.write('sorry, try again')

        form.form_submit_button("Submit")

    if corrects_tue == answers_tue:
        st.balloons()


with st.expander(wed):
    answers_wed = []
    if len(corrects_wed) != len(problems_wed):
        st.write('프로그램에 에러가 있습니다. 관리자에게 문의하세요')

    for i in range(len(problems_wed)):
        form = st.form(problems_wed[i] + 'wed')
        answers_wed.append(form.text_input(problems_wed[i]))

        if answers_wed[i] == corrects_wed[i]:
            form.subheader('good job')
        else:
            form.write('sorry, try again')

        form.form_submit_button("Submit")

    if corrects_wed == answers_wed:
        st.balloons()


with st.expander(thu):
    answers_thu = []
    if len(corrects_thu) != len(problems_thu):
        st.write('프로그램에 에러가 있습니다. 관리자에게 문의하세요')

    for i in range(len(problems_thu)):
        form = st.form(problems_thu[i] + 'thu')
        answers_thu.append(form.text_input(problems_thu[i]))

        if answers_thu[i] == corrects_thu[i]:
            form.subheader('good job')
        else:
            form.write('sorry, try again')

        form.form_submit_button("Submit")

    if corrects_thu == answers_thu:
        st.balloons()

with st.expander(fri):
    answers_fri = []
    if len(corrects_fri) != len(problems_fri):
        st.write('프로그램에 에러가 있습니다. 관리자에게 문의하세요')

    for i in range(len(problems_fri)):
        form = st.form(problems_fri[i] + 'fri')
        answers_fri.append(form.text_input(problems_fri[i]))

        if answers_fri[i] == corrects_fri[i]:
            form.subheader('good job')
        else:
            form.write('sorry, try again')

        form.form_submit_button("Submit")

    if corrects_fri == answers_fri:
        st.balloons()