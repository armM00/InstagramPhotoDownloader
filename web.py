import streamlit as st
import requests

icon = 'logo.ico'

st.set_page_config(page_title="IGD",
                   page_icon=icon)


st.title("Instagram Photo Downloader")
st.info("""This Python application downloads a photo from an Instagram post. 
               \nIt takes the URL of the post as input and saves the photo as a JPG file.""")

user_input = st.text_input(label='Enter a URL',
                           placeholder="https://www.instagram.com/p/BsOGulcndj-/",
                           key="user_input").strip()

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
    elif len(str(user_input)) > 40:
        url = user_input[:40]
        response = requests.get(f"{url}media/?size=l", stream=True)

        with open("instagram.jpg", "wb") as f:
            f.write(response.content)

        st.image('instagram.jpg')

        with open("instagram.jpg", "rb") as f:
            file_content = f.read()

        file_name = 'download.jpg'

        st.download_button(label="Download file", data=file_content, file_name=file_name, mime='image/jpeg')
    else:
        st.markdown(
            "<p style='color:gray'>Please enter a URL in 40 "
            "characters-long format<br>Example: <b>https://www.instagram.com/p/BsOGulcndj-/</b> </p>",
            unsafe_allow_html=True)

        if st.button("Reload"):
            st.rerun()
with st.expander("Legal Info"):  # Element 5
    st.write("<br><a href='https://linktr.ee/arm_andreasian_' style='color:yellow;'>Armen-Jean Andreasian</a> "
             "<br>Free Apps for All © 2023", unsafe_allow_html=True)