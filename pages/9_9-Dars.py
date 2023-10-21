import streamlit as st


savol=("Biror ixtiyoriy son kiritilganda bizga berilgan M massivdagi shu songa teng elementni indexsini chiqaruvchi, agar son mavjud bo'lmasa sonni massivda qanday o'rin egallasa shu indexni chiqaruvchi dastur tuzing.M=[1,3,4,6,7,8,9,10,12,13,14,15,20,21,30,40] massivni ixtiyoriy o'zgartirish mumkin  ")#savol matnini kiriting

col1,col2 = st.columns((1, 7))
col1.image("images/leetcode_logo.png")
col2.write(f"**Savol**.{savol} ")

st.write("**Yeshim**:")
code = '''
M=[1,3,4,6,7,8,9,10,12,13,14,15,20,21,30,40]
L=len(M)
a=int(input("a="))
for i in range(0,L):
    if a==M[i]:
        print(i)
    if M[i]<a<M[i+1] :
        print(i+1)
'''
st.code(code, language='python')

st.write("**Natija**:")
st.image("images/9_dars_natija.PNG")
st.write("**Yangi funksiyalar**:")
