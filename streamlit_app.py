import streamlit as st
import requests
import os

from news_video import VideoGenerator
from news_api import NewsAPI

news_api_key = os.getenv('NEWS_API_KEY')
news_client = NewsAPI(news_api_key)
video_api_key = os.getenv('BEARER TOKEN')
video_generator=VideoGenerator(video_api_key)

st.set_page_config(
    layout="wide",
    page_title="AI News Anchor"
)

st.title=('AI News Anchor')
st.markdown('<style>h1{color:orange; text-align:center  }</style>', unsafe_allow_html=True)

input_url=st.text_input("Enter The image URL","")
query=st.text_input("Enter query keywords","")

num_news=st.slider("Number of News",min_value=1,max_value=9,value=5)

if st.button("Generate"):
    if input_url.strip()and query.strip and num_news is not None and num_news>0:
       

            video_url = video_generator.generate_video(final_text, image_url)

            st.warning("AI News Anchor Video")
           
            st.video(video_url)
    
    else:
        st.write("Failed to fetch news data. Please check your query and API key.")

        
        
 
