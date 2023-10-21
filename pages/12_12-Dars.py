import streamlit as st


savol=("Bir sonni ikkinchi songa bo'lgandagi butun qismni chiqaruvchi dastur tuzing.")#savol matnini kiriting

col1,col2 = st.columns((1, 7))
col1.image("images/leetcode_logo.png")
col2.write(f"**Savol**.{savol} ")

st.write("**Yeshim**:")
code = '''
bulinuvchi=int(input("bo'linuvchini kiriting: "))
buluvchi=int(input("bo'luvchini kiriting: "))
bulinma_butun_qismi=0
while bulinuvchi>abs(buluvchi):
    bulinma_butun_qismi=bulinma_butun_qismi+1
    bulinuvchi=bulinuvchi-buluvchi
print(bulinma_butun_qismi)
'''
st.code(code, language='python')

st.write("**Natija**:")
st.image("images/12_dars_natija.png")
st.write("**Yangi funksiyalar**:")
st.write("**abs(a)** - a sonning absalyut qiymatini chiqaruvchi funksiya. ")