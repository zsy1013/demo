import pydeck as pdk
from pydeck.types import String
import pandas as pd
import streamlit as st
import numpy as np

st.title('World Heritage Plus(DEMO)')

df = pd.read_csv('WH_sample_mapbox_app.csv')
df_rain = pd.read_csv('rain2.csv')
df_tmp = pd.read_csv('tmp.csv')

tmp = st.sidebar.checkbox('気温データ【月平均(℃)】※準備中')
rain = st.sidebar.checkbox('降水量データ【月平均(mm)】※準備中')
tmp_n = st.sidebar.slider('気温の変化(月別)', 1, 12, 1, 1)
rain_n = st.sidebar.slider('降水量の変化(月別)', 1, 12, 1, 1)

t_n = ['Nan', 'J', 1]
if tmp == 1:
    tmp_n = t_n[tmp_n]
else:
    df_tmp = 0

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
heritage_df = heritage_df.drop_duplicates()

try:
    num = len(heritage_df['種類'])
    st.write(f'表示された世界遺産：**{num}** 件')
except:
    st.write('登録基準は1つ以上選んでください')

st.pydeck_chart(pdk.Deck(
   map_style='mapbox://styles/mapbox/outdoors-v11',
   initial_view_state=pdk.ViewState(
       latitude=35.69109990914361,
       longitude=139.75687919760415,
       zoom=8,
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
           get_fill_color=[255, 140, 0]
       ),
       pdk.Layer(
           'ColumnLayer',
           data=df_tmp,
           get_position='[lon, lat]',
           get_elevation=tmp_n,
           elevation_scale=10000,
           radius=5000,
           #auto_highlight=True,
           #pickable=True,
           get_fill_color=[255, 0, 0, 150]
       ),
       pdk.Layer(
           'ColumnLayer',
           data=df_rain,
           get_position='[lon, lat]',
           get_elevation='J',
           elevation_scale=5000,
           radius=5000,  
           get_fill_color=[0, 0, 255, 'J' * 255]
       )],
       tooltip={"text": "{popup}"}))
