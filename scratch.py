import requests
import shutil

ig_post = input("Enter the url of the post") #  https://www.instagram.com/p/CrLoKlXIT88/
url = f"{ig_post}media/?size=l"

try:
    response = requests.get(url, stream=True)
    with open("image.jpg", "wb") as f:
        shutil.copyfileobj(response.raw, f)

    response.close()

    print("Photo downloaded successfully!")

except ValueError:
    print("Enter a valid URL")
