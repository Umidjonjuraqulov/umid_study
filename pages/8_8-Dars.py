import streamlit as st


savol=("ixtiyoriy son kiritilganda M massivdagi kiritilgan songa teng sonni o'chirib tashlovchi dastur tuzing.Misol uchun quyidagi M massiv berilgan bo'lsin  M=[1,5,4,3,1,7,5,1,6,8,4,9,12].Bunda biz M massivni ixtiyoriy o'zgartirishimiz mumkin.")

col1,col2 = st.columns((1, 7))
col1.image("images/leetcode_logo.png")
col2.write(f"**Savol**.{savol} ")

st.write("**Yeshim**:")
code = '''
M=[1,5,4,3,1,7,5,1,6,8,4,9,12]
a=int(input("a="))
L=len(M)
for i in range(L-1,0-1,-1):
    if M[i]==a:
        del M[i]
print(M)
'''
st.code(code, language='python')
st.write("**Natija**:")
st.image("images/8_dars_natija.png")
st.write("**Yangi funksiyalar** :")
st.write("")