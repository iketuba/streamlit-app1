# https://docs.streamlit.io/library/get-started/main-concepts

import streamlit as st
import numpy as np
import pandas as pd
import time

st.markdown("# 1ใใผใธ็ฎ ๐")
st.sidebar.markdown("# 1ใใผใธ็ฎ ๐")



st.markdown("## ใใผใฟใใฌใผใ ใ่กจ็คบ")

dataframe = pd.DataFrame(
  np.random.randn(10, 20),
  columns=('ๅ %d' % i for i in range(20))
)

st.dataframe(dataframe.style.highlight_max(color='green',axis=0))

st.table(dataframe)



st.markdown("## ๆใ็ทใฐใฉใ")

chart_data = pd.DataFrame(
     np.random.randn(20, 3),
     columns=['a', 'b', 'c'])

st.line_chart(chart_data)



st.markdown("## ๅฐๅณใๆใ")

map_data = pd.DataFrame(
  np.random.randn(1000, 2) / [50, 50] + [37.76, -122.4],
  columns=['lat', 'lon']
)

st.map(map_data)