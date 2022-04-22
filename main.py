import pydeck as pdk
from pydeck.types import String
import pandas as pd
import streamlit as st
import numpy as np

st.title('World Heritage Plus(DEMO)')

df = pd.read_csv('WH_sample_mapbox_app.csv')

df_random = pd.DataFrame(
   np.random.randn(1000, 2) / [50, 50] + [37.76, -122.4],
   columns=['lat', 'lon'])

#----------------------------------
num_list = ['登録基準(ⅰ)', '登録基準(ⅱ)', '登録基準(ⅲ)', '登録基準(ⅳ)', '登録基準(ⅴ)', 
            '登録基準(ⅵ)', '登録基準(ⅶ)', '登録基準(ⅷ)', '登録基準(ⅸ)', '登録基準(ⅹ)']

numbers = st.multiselect('登録基準を選択してください', num_list, num_list)
#----------------------------------

heritage_df = pd.DataFrame()
for n in numbers:
    n = n.replace('登録基準', '')
    n = df[df[n]==1]
    heritage_df = heritage_df.append(n)

st.pydeck_chart(pdk.Deck(
   map_style='mapbox://styles/mapbox/outdoors-v11',
   initial_view_state=pdk.ViewState(
       latitude=37.76,
       longitude=-122.4,
       zoom=11,
       pitch=50,
   ),
   layers=[
       pdk.Layer(
           'ScatterplotLayer',
           data=heritage_df,
           get_position='[lon, lat]',
           pickable=True,
           opacity=0.8,
           stroked=True,
           filled=True,
           radius_scale=5,
           radius_min_pixels=10,
           radius_max_pixels=5,
           line_width_min_pixels=1,
           get_fill_color=[255, 140, 0],
       )],
       tooltip={"text": "{popup}"}))
