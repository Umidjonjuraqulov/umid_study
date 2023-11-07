import streamlit as st


savol=("Kiritilgan son biror sonni 2 ning darajasi ko'rinishida yozish mumkinligiga  tekshiruvchi dastur yozing.Agar kiritilgan  sonni 2 ning darajasi ko'rinishida yozib bo'lsa **true** aks holda **false** so'zini chiqarsin.")#savol matnini kiriting

col1,col2 = st.columns((1, 7))
col1.image("images/leetcode_logo.png")
col2.write(f"**Savol**.{savol} ")

st.write("**Yeshim**:")
code = '''
n=int(input("Sonni kiriting: "))
if n==1:
    print("true")
while n>1:
    n=n/2 
if n==1:
    print("true")
else :
    print("false")
'''
st.code(code, language='python')

st.write("**Natija**:")
st.image("images/15_dars_natija.PNG")