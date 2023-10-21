import streamlit as st


savol_1=("Massiv ichidagi ikkita bir xil elementni o'chiring.Misol uchun quyidagi massiv berilgan bo'lsin  \nM=[1,5,4,3,1,7,5,1,6,8,4,9,12] .")
st.write(f"**Savol**.{savol_1} ")

st.write("**Yeshim**:")
code = '''
M=[1,5,4,3,1,7,5,1,6,8,4,9,12]
def tartiblash(M):
    m=len(M)
    for i in range (0,m):
        c=(m-i)-1
        for j in range (0,c):
            if M[j]>M[j+1]:
                a=M[j]
                M[j]=M[j+1]
                M[j+1]=a
    return M
N=tartiblash(M)
print(f"tartiblangan:{N}")
X=[]
def chiqaruvchi(N):
    m=len(N)
    for i in range(m-1, 0, -1):
        if N[i]==N[i-1]:
            del N[i]
    return N
A=chiqaruvchi(N)
print(f"Tozalangan to'plam:{A}")
'''
st.code(code, language='python')
st.write("**Natija**:")
st.image("images/7_dars_natija.png")
st.write("**Yangis funksiyalar** :")
st.write("**del ()** - massiv ichidagi ko'rsatilgan elementni o'chiruvchi funksiya.")