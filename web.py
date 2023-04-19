import streamlit as st
import requests

st.title("Instagram Photo Downloader")
st.info("""This Python application downloads a photo from an Instagram post. 
               \nIt takes the URL of the post as input and saves the photo as a JPG file.""")

user_input = st.text_input(label='', placeholder="Paste the URL", key="user_input")
url = st.session_state["user_input"][0:40]


if st.button("Download Photo"):
    response = requests.get(f"{url}media/?size=l", stream=True)
    try:

        with open("instagram.jpg", "wb") as f:
            f.write(response.content)

        st.image('instagram.jpg')

        with open("instagram.jpg", "rb") as f:
            file_content = f.read()

        file_name = 'download.jpg'

        st.download_button(label="Download file", data=file_content, file_name=file_name, mime='image/jpeg')

