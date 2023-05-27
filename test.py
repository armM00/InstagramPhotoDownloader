import streamlit as st
import requests

icon = 'logo.ico'
st.set_page_config(page_title="IGD",
                   page_icon=icon)


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

if user_input:
    if len(user_input) >= 40:
        photo_id = user_input[:41]
    elif len(user_input) == 39:
        photo_id = user_input + "/"
    else:
        st.error("Enter a valid url")

    if st.button("Download Photo"):
        try:
            response = requests.get(f"{user_input}media/?size=l", stream=True)

            with open("insta.jpg", "wb") as f:
                f.write(response.content)

            st.image('insta.jpg')

            with open("insta.jpg", "rb") as f:
                file_content = f.read()

            file_name = 'download.jpg'

            st.download_button(label="Download file", data=file_content, file_name=file_name, mime='image/jpeg')

        except AttributeError:
            st.error("Enter a valid URL")

    if st.button("Reload"):
        st.write("The button doesn't work. Press F5")
with st.expander("Legal Info"):  # Element 5
    st.write("<br><a href='https://linktr.ee/arm_andreasian_' style='color:yellow;'>Armen-Jean Andreasian</a> "
             "<br>Free Apps for All © 2023", unsafe_allow_html=True)
