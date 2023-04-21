"""
NOTE:
In order to run this program, download customTkinter and Pillow.

to download customtkinter, 
    - go to your terminal or Command Prompt, then type...
        pip3 install customtkinter
    - then hit enter.

To download Pillow,
    - go to your terminal or Command Prompt, then type...
        pip intall Pillow
    - then hit enter. 
"""

import tkinter as tk
import customtkinter as ctk 
from PIL import Image, ImageTk


# to start the pop-up window
ctk.set_appearance_mode("dark") 
window = ctk.CTk()
window.geometry("800x500")
window.title("Nutrinometer")

# header frame
header_frame = ctk.CTkFrame(master=window,width=450, height=100, corner_radius=20,  fg_color = '#4472C4')

header_frame.grid(row=1, column=5, columnspan=3, padx=10, pady=20, sticky=tk.N)

# header title
header_title = ctk.CTkLabel(master=header_frame, text='Nutrinometer', font=('Times', 50, 'bold'))
header_title.place(relx=0.2, rely=0.25, anchor=tk.NW)

# menu frame
menu_frame = ctk.CTkFrame(master=window, width=300, height=480, fg_color='#404040')
menu_frame.grid(row=1, rowspan=5, column=1, columnspan=2, padx=10, pady=10, sticky=tk.S)


# menu choices
# home icon
icon_home = ctk.CTkImage(Image.open("icons8-home-page-30.png").resize((30,30)))
icon_record = ctk.CTkImage(Image.open("icons8-opened-folder-30.png").resize((30,30)))
icon_analysis = ctk.CTkImage(Image.open("icons8-analytics-30.png").resize((30,30)))

# home menu button
home_button = ctk.CTkButton(master=window, text='Home', image=icon_home, width=140, fg_color='#4472C4')
home_button.grid(row=1, column=1, padx=30, pady=40, sticky=tk.NW)

#record menu button
record_button = ctk.CTkButton(master=window, text='Record',image=icon_record, width=140, fg_color='#4472C4')
record_button.grid(row=1, column=1, padx=30, pady=85, sticky=tk.NW)

# view analysis menu button
analysis_button = ctk.CTkButton(master=window, text='Analysis',image=icon_analysis, width=140, fg_color='#4472C4')
analysis_button.grid(row=1, column=1, padx=30, pady=130, sticky=tk.NW)

# Add Record Button
add_button = ctk.CTkButton(master=window, text='+', width=50, height=50, corner_radius=50, fg_color='#4472C4', font=('Calibri', 40))
add_button.grid(row=5, column=7,padx=25, sticky=tk.NE)


# run
window.mainloop()
