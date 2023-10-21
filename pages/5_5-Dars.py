import streamlit as st


savol=("Paskal uchburchagini tuzing.")

col1,col2 = st.columns((1, 7))
col1.image("images/leetcode_logo.png")
col2.write(f"**Savol**.{savol} ")
col2.image("images/paskal_uchburchagi.jpg")

st.write("**Yeshim**:")
code = '''
q=input("")
M1=[1,1]
M2=[]
for i in range(1,int(q)):
    print(f"Aylanish: {i}")
    L=len(M1)
    a=0
    b=M1[0]
    for j in range(0,L+1):
        M2.append(a+b)
        a=b
        if (j+1)<L:
            b=M1[j+1]
        else :
            b=0
    M1 = M2 
    print(M2)
    M2 = []
'''
st.code(code, language='python')
st.write("**Natija**:")
st.image("images/5_dars_natija.PNG")
st.write("**Yangis funksiyalar** :")
st.write("**append()** - massiv ichiga element qo'shuvchi funksiya")
