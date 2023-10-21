import streamlit as st


savol=("Bizga massiv belingan bo'lsa uning elementlari orasidan maxsimal, minimal qiymatlari hamda elementlari o'rtacha qiymatini chiqaruvchi dastur tuzing.Misol uchun bizga M=[1, 7, 8, 3, 14, 11, 4] massiv berilgan bo'lsin.")



st.write(f"**Savol**.{savol} ")

st.write("**Yeshim**:")
code = '''
M=[1, 7, 8, 3, 14, 11, 4]
L=len(M)
Max=M[0]
for i in range (1,L):
    if Max<M[i]:
        Max=M[i]
print(f"Maksimal :{Max}")
Min=M[0]
for j in range (1,L):
    if Min>M[j]:
        Min=M[j]
print(f"Minimal :{Min}")
s=0
for i in range(0,L):
    s+=int(M[i])
    p=s/L
print(f"O'rtacha qiymati:{p}")
'''
st.code(code, language='python')
st.write("**Natija**:")
st.image("images/3_dars_natija.png")
st.write("**Yangi funksiyalar** :")
st.write("")
