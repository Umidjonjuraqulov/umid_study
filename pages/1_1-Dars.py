import streamlit as st



savol_1=("Foydalanuvchi sonni rim raqamida kiritganda sonni arab raqamlaridan foydalanib son ko'rinishida chiqaruvchi dasturni tuzing.Rim raqamlari qiymatlari: I = 1, V = 5, X = 10, L = 50, C = 100, D = 500, M = 1000")
col1,col2 = st.columns((1, 7))
col1.image("images/leetcode_logo.png")
col2.write(f"**Savol**.{savol_1} ")
st.write("**Yeshim**:")
code = '''
raqam=0
rim_raqam=input("Sonni kiriting: ")
rim_lugat={'I':1,'V':5,'X':10,'L':50,'C':100,'D':500,'M':1000}
uzunligi=len(rim_raqam)
for i in range (uzunligi-1,-1,-1):
    if i != uzunligi-1: 
        if rim_lugat[rim_raqam[i]]<rim_lugat[rim_raqam[i+1]]:
            continue
        
    if rim_lugat[rim_raqam[i]]<=rim_lugat[rim_raqam[i-1]]:
        raqam=raqam+rim_lugat[rim_raqam[i]] 
    elif i==0: 
        raqam=raqam+rim_lugat[rim_raqam[i]]
    else :
        raqam=raqam+rim_lugat[rim_raqam[i]] - rim_lugat[rim_raqam[i-1]]

print(f"Javob: {raqam}")
'''
st.code(code, language='python')
st.write("**Natija**:")
st.image("images/1_dars_natija.png")
st.write("**Yangi funksiyalar** :")
st.write("**Input()** - kiritish funkisiyasi.Foydalanuvchidan ma`lumot olish kerak bo'lganda **input()** funksiyasidan foydalanamiz.")
st.write("**len()** - massiv uzunligini topuvchi funksiya.(Massivdagi elementlar soni)")
st.write("**continue** - bu funksiya **if** operatori ichidagi funsiya bo'lib, **if** operatori qabul qilingan shartga tushmaydigan holni tashlab ketuvchi funksiya ")
st.write("**print()** - berilgan ma`lumotlarni chiqaruvchi,natijani  hisoblab chiqaruvchi operator")