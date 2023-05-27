import streamlit as st
import requests
import io
from streamlit_elements import design


icon = 'logo.ico'
st.set_page_config(page_title="IGD", page_icon=icon)

design.animation()

st.title("Instagram Photo Downloader")
st.info("""This app downloads a photo from an Instagram post. 
               \nIt takes the URL of the post as input and saves the photo as a JPG file.""")

user_input = st.text_input(label='Enter a URL',
                           placeholder="https://www.instagram.com/p/BsOGulcndj-/",
                           key="user_input")
length = len(user_input)
if st.button("Download Photo") and length >= 40:
    try:
        url = user_input[:40] + "media/?size=l"
        response = requests.get(url)
        if response.status_code == 200:
            image_bytes = io.BytesIO(response.content)
            st.image(image_bytes, use_column_width=True)

            file_content = response.content
            file_name = 'download.jpg'

            st.download_button(label="Download file", data=file_content, file_name=file_name, mime='image/jpeg')
        else:
            st.error("Failed to download the photo. Please try again later.")
    except (requests.HTTPError, requests.ConnectionError) as e:
        st.error("An error occurred while downloading the photo. Please try again later.")
        st.error(str(e))
elif length < 40 and length != 0:
    st.error("Please enter a valid URL")
