import streamlit as st
import requests

st.title("Instagram Photo Downloader")
st.info("""This Python application downloads a photo from an Instagram post. 
               \nIt takes the URL of the post as input and saves the photo as a JPG file.""")

user_input = st.text_input(label='Enter a URL',
                           placeholder="Paste the URL in https://www.instagram.com/p/CrL8j9cputW/ format",
                           key="user_input")


if st.button("Download Photo"):
    if len(str(user_input)) == 40:

        response = requests.get(f"{user_input}media/?size=l", stream=True)

        with open("instagram.jpg", "wb") as f:
            f.write(response.content)

        st.image('instagram.jpg')

        with open("instagram.jpg", "rb") as f:
            file_content = f.read()

        file_name = 'download.jpg'

        st.download_button(label="Download file", data=file_content, file_name=file_name, mime='image/jpeg')

    else:
        st.error("Please enter a URL in https://www.instagram.com/p/CrL8j9cputW/ format")
        exit()
