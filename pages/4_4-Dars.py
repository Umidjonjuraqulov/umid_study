import streamlit as st


savol=("Ixtiyoriy 2 ta massiv berilganda ularni elementlarini tartiblab qo'shish.Misol uchun quyidagi A va B massivlar berilgan bo'lsin  A=[5,6,7,2,1,6], B=[7, 3, 8] .(.sort()funksiyasidan foydalanmasdan bajaring)")

col1,col2 = st.columns((1, 7))
col1.image("images/leetcode_logo.png")
col2.write(f"**Savol**.{savol} ")

st.write("**Yeshim**:")
code = '''
A=[5,6,7,2,1,6]
B=[7, 3, 8]
M=A+B
m=len(M)
for i in range (0,m):
    c=(m-i)-1
    for j in range (0,c):
        if M[j]>M[j+1]:
            a=M[j]
            M[j]=M[j+1]
            M[j+1]=a
print(M)
'''
st.code(code, language='python')
st.write("**Natija**:")
st.image("images/4_dars_natija.PNG")
st.write("**Yangi funksiyalar** :")
st.write("")
