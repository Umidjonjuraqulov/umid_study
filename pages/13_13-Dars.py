import streamlit as st


savol=("Kiritilgan raqamlar orasida 1 raqami necha marta takrorlanganini chiqaruvchi dastur tuzing.")#savol matnini kiriting

col1,col2 = st.columns((1, 7))
col1.image("images/leetcode_logo.png")
col2.write(f"**Savol**.{savol} ")

st.write("**Yeshim**:")
code = '''
a=input("Sonni kiriting: ")
l=len(a)
n=0
for i in range(0,l):
    if int(a[i])==1:
        n=n+1
print(f"Kiritgan raqamlaringiz orasida 1 raqami {n} marta takrorlangan")
'''
st.code(code, language='python')

st.write("**Natija**:")
st.image("images/13_dars_natija.png")
