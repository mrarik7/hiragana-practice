
import streamlit as st 
import random

st.header('Hiragana practice')

a =('あいうえお')
b =('あいうえおかきくけこ')
c =('あいうえおかきくけこさしすせそ')
d =('あいうえおかきくけこさしすせそたちつてと')
e =('あいうえおかきくけこさしすせそたちつてとなにぬねの')
f =('あいうえおかきくけこさしすせそたちつてとなにぬねのはひふへほ')
g = ('あいうえおかきくけこさしすせそたちつてとなにぬねのはひふへほまみむめも')
h = ('あいうえおかきくけこさしすせそたちつてとなにぬねのはひふへほまみむめもやゆよ')
i = ('あいうえおかきくけこさしすせそたちつてとなにぬねのはひふへほまみむめもやゆよらりるれろ')
j =('あいうえおかきくけこさしすせそたちつてとなにぬねのはひふへほまみむめもやゆよらりるれろわをん')




if st.button('hiragana words'):
    st.text('f1st row→  あ, い, う, え, お')
    st.text('2nd row→  か, き, く, け, こ')
    st.text('3rd row→  さ, し, す, せ, そ')
    st.text('4th row→  た, ち, つ, て, と')
    st.text('5th row→  な, に, ぬ, ね, の')
    st.text('6th row→  は, ひ, ふ, へ, ほ')
    st.text('7th row→  ま, み, む, め, も')
    st.text('8th row→  や, ゆ, よ')
    st.text('9th row→  ら, り, る, れ, ろ')
    st.text('10th row→  わ, を,ん')

    
level = st.selectbox('whats your level?',['👇','1st row','2nd row','3rd row','4th row','5th row','6th row','7th row'
,'8th row','9th row','10th row'])

if 'level1_char' not in st.session_state:
    st.session_state.level1_char = random.choice(a)

aa=random.choice(a)
bb=random.choice(b)
cc=random.choice(c)
dd=random.choice(d)
ee=random.choice(e)
ff=random.choice(f)
hh=random.choice(g)
ii=random.choice(h)
jj=random.choice(i)
kk=random.choice(j)


c1,c2,c3,c4,c5 = st.columns(5)
with c3:
    if level == '1st row':
        u = st.header(aa)
        c1.button('refresh')
    if level == '2nd row':
        u = st.header(bb)
        c1.button('refresh')
    if level == '3rd row':
        st.header(cc)
        c1.button('refresh')
    if level == '4th row':
        st.header(dd)
        c1.button('refresh')
    if level == '5th row':
        st.header(ee)
        c1.button('refresh')
    if level == '6th row':
        st.header(ff)
        c1.button('refresh')
    if level == '7th row':
        st.header(gg)
        c1.button('refresh')
    if level == '8th row':
        st.header(hh)
        c1.button('refresh')

    if level == '9th row':
        st.header(ii)
        c1.button('refresh')
    if level == '10th row':
        st.header(jj)
        c1.button('refresh')

ans = st.button('answer')
if ans:
    if arik == 'あ':
        st.success('ok')


    

