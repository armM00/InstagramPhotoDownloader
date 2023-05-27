import streamlit as st
import requests
import io

icon = 'logo.ico'
st.set_page_config(page_title="IGD", page_icon=icon)

animation = """
<style>
@keyframes example {
    0%   {background-color: #0D1B2A;}
    25%  {background-color: #2B2D42;}
    50%  {background-color: #1D1D1D;}
    75%  {background-color: #2B2D42;}
    100% {background-color: #0D1B2A;}
}

[data-testid="stAppViewContainer"] > .main {
    animation-name: example;
    animation-duration: 10s;
    animation-timing-function: linear;
    animation-iteration-count: infinite;
}
</style>
"""
st.markdown(animation, unsafe_allow_html=True)

st.title("Instagram Photo Downloader")
st.info("""This app downloads a photo from an Instagram post. 
               \nIt takes the URL of the post as input and saves the photo as a JPG file.""")

user_input = st.text_input(label='Enter a URL',
                           placeholder="https://www.instagram.com/p/BsOGulcndj-/",
                           key="user_input").strip()

if st.button("Download Photo") and len(user_input) >= 40:
    try:
        url = user_input[:40]
        response = requests.get(f"{url}media/?size=l", stream=True)
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
elif len(user_input) < 40:
    st.error("Please enter a valid URL")
