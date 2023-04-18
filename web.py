import os
import streamlit
import requests
import shutil

streamlit.title("Instagram Photo Downloader")
streamlit.info("""This Python application downloads a photo from an Instagram post. 
               \nIt takes the URL of the post as input and saves the photo as a JPG file.""")

user_input = streamlit.text_input(label='', placeholder="Paste the URL", key="user_input")

if streamlit.button("Download Photo"):

    response = requests.get(f"{user_input}media/?size=l", stream=True)

    desktop_path = os.path.join(os.path.join(os.environ["USERPROFILE"]), "Desktop")

    with open(os.path.join(desktop_path, "image.jpg"), "wb") as f:
        shutil.copyfileobj(response.raw, f)

    response.close()

    streamlit.success("Photo downloaded successfully!")




