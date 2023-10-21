import streamlit as st


savol=("Kiritilgan matndagi eng oxirgi so'zni chiqaruvchi dastur tuzing.")#savol matnini kiriting

col1,col2 = st.columns((1, 7))
col1.image("images/leetcode_logo.png")
col2.write(f"**Savol**.{savol} ")

st.write("**Yeshim**:")
code = '''
matn=input("Matn kiriting: ")
matn_massive = matn.split(' ')
uzunlik=len(matn_massive)
print(matn_massive[uzunlik-1])
'''
st.code(code, language='python')

st.write("**Natija**:")
st.image("images/11_dars_natija.PNG")
st.write("**Yangi funksiyalar**:")
st.write("**.split(' ')** - bu funksiya **(' ')** ichiga kiritgan belgi bo'yicha massiv elemntlariga ajratib beradi . ")
