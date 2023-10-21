import streamlit as st


savol_1=("Logarifmni hisoblovchi dastur tuzing,ya`ni a son b sonning nechinchi darajasi.Misol uchun a=8, b=2 bo'lsa javob:3 .")
st.write(f"**Savol**.{savol_1} ")
st.write("**Yeshim.1**:")
code = '''
a=int(input("a="))
b=int(input("b="))
def logorifm(a,b):
    n=1
    if b>1:
        for i in range (1,int(a/b)):
            s=a/b
            a=s
            if s>1:
                n=n+1
            if s == 1: 
                break
    else:
        n=0
        print(n)
    
    return n 

print(logorifm(a, b))
'''
st.code(code, language='python')

st.write("**Yeshim.2**:")
code = '''
a=int(input("a="))
b=int(input("b="))
def logorifm(a,b):
    n=1
    if b>1:
        for i in range (1,int(a/b)):
            s=a/b
            a=s
            if s>1:
                n=n+1
            if s == 1: 
                break
    else:
        n=0
        print(n)
    
    return n 

print(logorifm(a, b))
'''
st.code(code, language='python')

st.write("**Natija.1**:")
st.image("images/6_dars_natija1.png")
st.write("**Natija.2**:")
st.image("images/6_dars_natija2.png")
st.write("**Yangi funksiyalar** :")
st.write("**break** - **if** operatori ichida ishlatiladigan funksiya bo'lib shartga tekshirishni yanlovchi funksiya.")
st.write("**def** - bu python dasturlash tilida funksiya yaratuvchi funksiya. ")
st.write("**return** - bu yaratilgan **def** funksiyani ishga tushiruvchi funksiya. ")

st.write("**izoh:**")
st.write("yechimlardagi **def** dan keyin kelgan **logorifm(a,b)** - bu funksiya nomi, ya'ni biz bu nom orqali funksiyani chaqirib uni ishlatishimiz mumkin.")
