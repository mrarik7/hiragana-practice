import streamlit as st 
import random

st.header('Hiragana/ひらがな practice🏋️‍♂️')

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



if st.button('hiragana words levels🈷️'):
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

level = st.radio('whats your level?',['👇','1st row','2nd row','3rd row','4th row','5th row','6th row','7th row'
,'8th row','9th row','10th row'])


if 'aa' not in st.session_state: st.session_state.aa = random.choice(a)
if 'bb' not in st.session_state: st.session_state.bb = random.choice(b)
if 'cc' not in st.session_state: st.session_state.cc = random.choice(c)
if 'dd' not in st.session_state: st.session_state.dd = random.choice(d)
if 'ee' not in st.session_state: st.session_state.ee = random.choice(e)
if 'ff' not in st.session_state: st.session_state.ff = random.choice(f)
if 'gg' not in st.session_state: st.session_state.gg = random.choice(g)
if 'hh' not in st.session_state: st.session_state.hh = random.choice(h)
if 'ii' not in st.session_state: st.session_state.ii = random.choice(i)
if 'jj' not in st.session_state: st.session_state.jj = random.choice(j)


c1,c2,c3,c4,c5 = st.columns(5)
with c3:
    if level == '1st row':
        st.header(st.session_state.aa)
        if c1.button('refresh'):
            st.session_state.aa = random.choice(a)
    if level == '2nd row':
        st.header(st.session_state.bb)
        if c1.button('refresh'):
            st.session_state.bb = random.choice(b)
    if level == '3rd row':
        st.header(st.session_state.cc)
        if c1.button('refresh'):
            st.session_state.cc = random.choice(c)
    if level == '4th row':
        st.header(st.session_state.dd)
        if c1.button('refresh'):
            st.session_state.dd = random.choice(d)
    if level == '5th row':
        st.header(st.session_state.ee)
        if c1.button('refresh'):
            st.session_state.ee = random.choice(e)
    if level == '6th row':
        st.header(st.session_state.ff)
        if c1.button('refresh'):
            st.session_state.ff = random.choice(f)
    if level == '7th row':
        st.header(st.session_state.gg)
        if c1.button('refresh'):
            st.session_state.gg = random.choice(g)
    if level == '8th row':
        st.header(st.session_state.hh)
        if c1.button('refresh'):
            st.session_state.hh = random.choice(h)
    if level == '9th row':
        st.header(st.session_state.ii)
        if c1.button('refresh'):
            st.session_state.ii = random.choice(i)
    if level == '10th row':
        st.header(st.session_state.jj)
        if c1.button('refresh'):
            st.session_state.jj = random.choice(j)

answers = {
    "あ": "a", "い": "i", "う": "u", "え": "e", "お": "o",
    "か": "ka", "き": "ki", "く": "ku", "け": "ke", "こ": "ko",
    "さ": "sa", "し": "shi", "す": "su", "せ": "se", "そ": "so",
    "た": "ta", "ち": "chi", "つ": "tsu", "て": "te", "と": "to",
    "な": "na", "に": "ni", "ぬ": "nu", "ね": "ne", "の": "no",
    "は": "ha", "ひ": "hi", "ふ": "fu", "へ": "he", "ほ": "ho",
    "ま": "ma", "み": "mi", "む": "mu", "め": "me", "も": "mo",
    "や": "ya", "ゆ": "yu", "よ": "yo",
    "ら": "ra", "り": "ri", "る": "ru", "れ": "re", "ろ": "ro",
    "わ": "wa", "を": "wo/o", "ん": "un"
}

ans = st.button('answer✏️')
if ans:
    if level == '1st row':
        st.success(f'Answer: {answers[st.session_state.aa]}')
    if level == '2nd row':
        st.success(f'Answer: {answers[st.session_state.bb]}')
    if level == '3rd row':
        st.success(f'Answer: {answers[st.session_state.cc]}')
    if level == '4th row':
        st.success(f'Answer: {answers[st.session_state.dd]}')
    if level == '5th row':
        st.success(f'Answer: {answers[st.session_state.ee]}')
    if level == '6th row':
        st.success(f'Answer: {answers[st.session_state.ff]}')
    if level == '7th row':
        st.success(f'Answer: {answers[st.session_state.gg]}')
    if level == '8th row':
        st.success(f'Answer: {answers[st.session_state.hh]}')
    if level == '9th row':
        st.success(f'Answer: {answers[st.session_state.ii]}')
    if level == '10th row':
        st.success(f'Answer: {answers[st.session_state.jj]}')

if st.button('info'):
    st.text('katakana coming soon...')
    st.markdown('👤[-arik](https://profilepy-3t8ez4hcjvvmwsczqmxnbz.streamlit.app/)')
    









