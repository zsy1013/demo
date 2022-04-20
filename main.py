import pydeck as pdk
from pydeck.types import String
import pandas as pd
import streamlit as st
import numpy as np
import json

st.title('World Heritage Plus(DEMO)')

#json_open = open('/Users/otsukashigeki/Desktop/output (1).json', 'r')
#json_load = json.load(json_open)

#DATA = pd.read_csv('/Users/otsukashigeki/Desktop/sample.csv')
DATA_2 = pd.read_csv('https://github.com/zsy1013/demo/blob/main/WH_sample2.csv')

df = pd.DataFrame(
   np.random.randn(1000, 2) / [50, 50] + [37.76, -122.4],
   columns=['lat', 'lon'])

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
           data=DATA_2,
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
           #tooltip={"html": '<b>popup:</b>'}
           #tooltip={'text':'{popup}'}
           #radius=200,
           #elevation_scale=4,
           #elevation_range=[0, 1000],
           #pickable=True,
           #extruded=True,
       )],
       tooltip={"text": "{popup}"}))
       #pdk.Layer(
       #    'HeatmapLayer',
       #    data=DATA,
       #    get_position='[lon, lat]',
       #    get_color='[200, 30, 0, 160]',
       #    get_radius=200,
       #),
