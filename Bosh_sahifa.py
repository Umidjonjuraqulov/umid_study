import streamlit as st

st.set_page_config(page_title='Umid Study', page_icon='⚡️', layout='wide')

col1,col2,col3 = st.columns((1, 2, 7))
col3.title(" Xush kelibsiz ! ")
col1.image("images/python_logo.png")
col2.write("")

st.subheader("Python darslar")
st.write("Assalomu alakum ! **Python dasturlash tili bo'yicha darslar** saytimizda sizni ko'rganimizdan  xursandmiz.Bu sayt orqali python bo'yicha o'z bilim va ko'nikmalaringizni ortirib borishingiz mumkin .Bu saytda  mantiqiy fikrlashni oshiruvchi mashqlar va ularning python dasturlash tilidagi javoblarini topishingiz mumkin.")

col1,col2 = st.columns((1, 9))
col1.image("images/leetcode_logo.png")
col2.subheader("LeetCode")
st.write("Eng ko'p yoqtirilgan LeetCode masalalar va ularning yechimlarini biz bilan o'rganing .")
st.image("images/bosh_sahifa.png")

st.write("**Darslar soni**: ")
col1,col2 = st.columns((2,  11))
col1.write("**Tuzuvchilar**: ")
col2.write("[**Firuz Juraev**](https://firuz-juraevml.github.io/)")
col2.write("[**Umidjon Juraqulov**](https://umidjon.streamlit.app/)")
