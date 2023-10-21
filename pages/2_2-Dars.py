import streamlit as st


savol=("Kiritilgan sonni polindiryonlikka tekshiruvchi dastur tuzing.Polindiryon songa misollar: 12321, 121, 22, 1")#savol matnini kiriting

col1,col2 = st.columns((1, 7))
col1.image("images/leetcode_logo.png")
col2.write(f"**Savol**.{savol} ")

st.write("**Yeshim**:")
code = '''
son=input("Sonni kiriting: ")
L=len(son)
s=0
p=0
if L==1 :
    N=N+int(son)
    print(f"Bu son polindiryon {son}")
else :
    if L%2==0:
            for i in range (0,(L//2)):
                s+=int(son[i]) 
            for j in range (((L//2)),L):
                p+=int(son[j]) 
            if s==p:
                print(f"Bu son polindiryon {son}")
            else:
                print(f"Bu son polindiryon emas {son}")
    else :
        for i in range (0,(L//2)):
            s+=int(son[i]) 
        for j in range (((L//2)+1),L):
            p+=int(son[j]) 
        if s==p:
            print(f"Bu son polindiryon {son}")
        else:
            print(f"Bu son polindiryon emas {son}")
'''
st.code(code, language='python')

st.write("**Natija**:")
st.image("images/2_dars_natija.PNG")
st.write("**Yangi funksiyalar**:")
