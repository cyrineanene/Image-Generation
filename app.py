import tkinter as tk
import customtkinter as ctk 

from SDM import SDM

from PIL import ImageTk

import os
from dotenv import load_dotenv

load_dotenv()

auth_token = os.getenv("auth_token")

#User Interface
app = tk.Tk()
app.geometry("532x632")
app.title("Image Generation App")
app.configure(bg='black')
ctk.set_appearance_mode("white") 

root = ctk.CTk()

# Input Box
prompt = ctk.CTkEntry(master=root, height=40, width=512, text_color="white", fg_color="black") 
prompt.place(x=10, y=10)

img_placeholder = ctk.CTkLabel(master=root, height=512, width=512, text="")
img_placeholder.place(x=10, y=110)

SDM = SDM(auth_token)
image = SDM.generate(prompt.get())

#Save image 
output_dir = "generated_images"
os.makedirs(output_dir, exist_ok=True)
name_image= input('Enter the name of your file: ')
image_path = os.path.join(output_dir, f"image_{name_image}.png")
image.save(image_path)

#Display image
img = ImageTk.PhotoImage(image)
img_placeholder.configure(image=img) 

trigger = ctk.CTkButton(height=40, width=120, text_font=("Arial", 15), text_color="black", fg_color="white", command=SDM.generate(prompt)) 
trigger.configure(text="Generate")
trigger.place(x=206, y=60) 

app.mainloop()