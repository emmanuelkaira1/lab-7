import tkinter as tk
from tkinter import ttk
from PIL import Image, ImageTk
import requests
from io import BytesIO

def get_random_fox():
    try:
        response = requests.get("https://randomfox.ca/floof/")
        response.raise_for_status()
        return response.json()['image']
    except Exception as e:
        print(f"Error fetching fox image: {e}")
        return None


def update_picture():
    global photo
    image_url = get_random_fox()
    if image_url:
        try:

            img_response = requests.get(image_url)
            img_response.raise_for_status()
            img_data = Image.open(BytesIO(img_response.content))
            img_data = img_data.resize((400, 400),)
            photo = ImageTk.PhotoImage(img_data)
            picture_label.config(image=photo)
            picture_label.image = photo
        except Exception as e:
            print(f"Error displaying the image: {e}")
    else:
        picture_label.config(text="Could not load image.")


root = tk.Tk()
root.title("Random Picture Generator")
root.geometry("450x500")


picture_label = ttk.Label(root, text="Loading...", anchor="center")
picture_label.pack(pady=10)

next_button = ttk.Button(root, text="Next Picture", command=update_picture)
next_button.pack(pady=10)

update_picture()

root.mainloop()