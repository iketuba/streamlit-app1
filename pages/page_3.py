import streamlit as st
import pandas as pd
import numpy as np
import time

st.markdown("# 3ページ目 🎉")
st.sidebar.markdown("# 3ページ目 🎉")



st.markdown("レイアウト")

add_selectbox = st.sidebar.selectbox(
    'よく使う連絡手段は?',
    ('Email', '固定電話', 'スマホ')
)

add_slider = st.sidebar.slider(
    '範囲を選んでください',
    0.0, 100.0, (25.0, 75.0)
)


left_column, right_column = st.columns(2)

left_column.button('押してください!')

with right_column:
    chosen = st.radio(
        '好きな野菜は？',
        ("キャベツ", "レタス", "トマト", "ニンジン"))
    st.write(f"好きな野菜は{chosen}です。")



st.markdown("進行状況")

'はじめ'

latest_iteration = st.empty()
bar = st.progress(0)

for i in range(100):
  latest_iteration.text(f'Iteration {i+1}')
  bar.progress(i + 1)
  time.sleep(0.1)

'おわり'