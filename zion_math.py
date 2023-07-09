import streamlit as st

st.title('최상위 수학 6-2')

mon = '월요일 PAGE 46-48'
corrects = ['9.6', '4.5', '5', '0.5', '3', '5', '6', '400', '1', '1', '399', '399', '798', '798', '106']
problems = ['7-1', '7-2', '7-3 (봉지)', '7-3(kg)', '8-1', '8-2', '8-3', '심화9_1', '심화9_2', '심화9_3', '심화9_4', '심화9_5',
            '심화9_6', '심화9_7', '9-1']

tue = '화요일_PAGE 49-51 Level up test'
corrects_tue = ['1.84', '6', '100', '10:15', '2.98', '06:12', '6.5', '28', '1020']
problems_tue = ['1', '2', '3', '4: 예) 12시40분 = 12:40', '5', '6: 예 3분 25초 = 03:25', '7', '8', '9']

wed = '수요일_PAGE 52-54 Level up test-High Level'
corrects_wed = ['90','15','2.5','21.47','0.88','0.5','90576','6','6']
problems_wed = ['10','11','12','13','14','15','1 high level','2 high level','3 high level']

thu = "목요일_PAGE 55-56 High Level"
corrects_thu = ['1.49','1.08','2.7','18.75','25','18']
problems_thu = ['4','5','6','7','8','9']

fri = "금요일_PAGE 60-65 공간과 입체"
corrects_fri = ['라','가','다','다','8','라','가,다','다','8','10','나,다','4' ]
problems_fri = ['1-1-(1)','1-1-(2)','1-2','1-3','1-4','1-5','2-1: 예) 가,나','2-2','2-5','2-6','3-3: 예) 가,나','3-4']


with st.expander(mon):
    answers = []
    if len(corrects) != len(problems):
        st.write('프로그램에 에러가 있습니다. 관리자에게 문의하세요')

    for i in range(len(problems)):
        form = st.form(problems[i] + 'mon')
        answers.append(form.text_input(problems[i]))

        if answers[i] == corrects[i]:
            form.write('good job')
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
            form.write('good job')
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
            form.write('good job')
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
            form.write('good job')
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
            form.write('good job')
        else:
            form.write('sorry, try again')

        form.form_submit_button("Submit")

    if corrects_fri == answers_fri:
        st.balloons()