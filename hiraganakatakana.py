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

if "char" not in st.session_state:
    st.session_state.char = ""

level = st.radio('whats your level?',['👇','1st row','2nd row','3rd row','4th row','5th row','6th row','7th row'
,'8th row','9th row','10th row'])

    
c1,c2,c3,c4,c5 = st.columns(5)
with c3:
    if st.button("refresh⭮"):
        if level == '1st row':
            st.session_state.char = random.choice(a)
        elif level == '2nd row':
            st.session_state.char = random.choice(b)
        elif level == '3rd row':
            st.session_state.char = random.choice(c)
        elif level == '4th row':
            st.session_state.char = random.choice(d)
        elif level == '5th row':
            st.session_state.char = random.choice(e)
        elif level == '6th row':
            st.session_state.char = random.choice(f)
        elif level == '7th row':
            st.session_state.char = random.choice(g)
        elif level == '8th row':
            st.session_state.char = random.choice(h)
        elif level == '9th row':
            st.session_state.char = random.choice(i)
        elif level == '10th row':
            st.session_state.char = random.choice(j)
    st.header(st.session_state.char)
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
with c3:
    if st.button("Answer🔍"):
        st.subheader(answers.get(st.session_state.char, "Not found"))



if st.button('info'):
    st.text('katakana coming soon...')
    st.markdown('👤[-arik](https://profilepy-3t8ez4hcjvvmwsczqmxnbz.streamlit.app/)')
    











