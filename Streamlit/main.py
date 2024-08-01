import streamlit as st
import pandas as pd
import numpy as np

st.title('Diagram')

slider_val = st.slider('Chọn một giá trị', 0, 100)
st.write(f'Giá trị bạn chọn là: {slider_val}')

chart_data = pd.DataFrame(
    np.random.randn(20, 3),
    columns=['A', 'B', 'C']
)

st.line_chart(chart_data)