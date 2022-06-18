import streamlit as st
import pandas as pd
import numpy as np

st.markdown("# 2ページ目 ❄️")
st.sidebar.markdown("# 2ページ目 ❄️")



st.markdown("## ウィジェット")

x = st.slider('x')
st.write(x, ' 2乗すると ', x * x)

st.text_input("名前", key="name")
'あなたの名前は ' + st.session_state.name



st.markdown("## チェックボックス")

if st.checkbox('データフレームを見る'):
    chart_data = pd.DataFrame(
       np.random.randn(20, 3),
       columns=['a', 'b', 'c'])

    chart_data



st.markdown("## セレクトボックス")

option = st.selectbox(
    'どの数字が最も好きですか?',
     list(range(10)))

'選んだ数字: ', option