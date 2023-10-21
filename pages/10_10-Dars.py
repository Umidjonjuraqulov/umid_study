import streamlit as st



savol_1=("Berilgan massivni songa o'tkazib songa 1 ni qo'shib yana sonni qayta massivga o'tkazings")
col1,col2 = st.columns((1, 7))
col1.image("images/leetcode_logo.png")
col2.write(f"**Savol**.{savol_1} ")
st.write("**Yeshim**:")
code = '''
massiv_1=[1,5,8,7,9]
son_korinishda=''
L=len(massiv_1)
massiv_natija=[]
for i in range(0,L):
    son_korinishda=str(son_korinishda)+str(massiv_1[i])
son_korinishda=int(son_korinishda)
yigindi=son_korinishda+1
yigindi=str(yigindi)
uzunlik=len(yigindi)
for i in range(0,uzunlik):
    massiv_natija.append(yigindi[i])
print(massiv_natija)
'''
st.code(code, language='python')
st.write("**Natija**:")
st.image("images/10_dars_natija.png")
st.write("**Yangi funksiyalar** :")
