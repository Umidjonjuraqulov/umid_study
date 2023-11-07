import streamlit as st


savol=("Kiritilgan son biror sonni kvadrati ekanligiga tekshiruvchi dastur yozing.Agar kiritilgan son biror sonni kvadrati bo'lsa **true** aks holda **false** so'zini chiqarsin.")#savol matnini kiriting

col1,col2 = st.columns((1, 7))
col1.image("images/leetcode_logo.png")
col2.write(f"**Savol**.{savol} ")

st.write("**Yeshim**:")
code = '''
num=int(input("Sonni kiriting: "))
for i in range(1,num):
        if num/i==i:
            s="true"
        elif num/i==num:
            s="false"
        else:
            pass
print(s)
'''
st.code(code, language='python')

st.write("**Natija**:")
st.image("images/14_dars_natija.PNG")