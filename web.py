import streamlit as st
import requests

st.title("Instagram Photo Downloader")
st.info("""This Python application downloads a photo from an Instagram post. 
               \nIt takes the URL of the post as input and saves the photo as a JPG file.""")

user_input = st.text_input(label='', placeholder="Paste the URL", key="user_input")

if st.button("Download Photo"):
    response = requests.get(f"{user_input}media/?size=l", stream=True)

    with open("image.jpg", "wb") as f:
        f.write(response.content)

st.image("image.jpg")


file_content = "Hello, world!"
file_name = "file.txt"

# Display a download button for the file.
st.download_button(label="Download file", data=file_content, file_name=file_name)