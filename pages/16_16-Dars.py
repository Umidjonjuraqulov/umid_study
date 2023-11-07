import streamlit as st


savol=("* dan romp shaklini yasovchi dartur tuzing.")#savol matnini kiriting

col1,col2 = st.columns((1, 7))
col1.image("images/leetcode_logo.png")
col2.write(f"**Savol**.{savol} ")

st.write("**Yeshim**:")
code = '''
n=10
for i in range(1,n+1):
    s=i*2-1
    print((n-i)*" "+"*"*s)
for i in range(n-1,0,-1):
    s=i*2-1
    print((n-i)*" "+"*"*s)
'''
st.code(code, language='python')

st.write("**Natija**:")
st.image("images/16_dars_natija.PNG
