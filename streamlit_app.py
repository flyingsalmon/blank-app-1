#import streamlit as st
#import numpy as np
#import pandas as pd
'''
chart_data = pd.DataFrame(
     np.random.randn(20, 3),
     columns=['a', 'b', 'c'])

st.line_chart(chart_data)
'''

import streamlit as st
import numpy as np
import pandas as pd

map_data = pd.DataFrame(
    np.random.randn(100, 2) / [50, 50] + [47.86, -122.2],
    columns=['lat', 'lon'])

st.map(map_data)