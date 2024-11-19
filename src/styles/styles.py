import tkinter as tk
from tkinter import messagebox
import main_tkinter

# Función de estilo de los botones
def style_button(btn):
    btn.configure(
        bg="#4CAF50", fg="white", font=("Arial", 12, "bold"), relief="flat", 
        activebackground="#3E8E41", activeforeground="white", cursor="hand2"
    )

def style_button_close(btn):
    btn.configure(
        bg="red", fg="black", font=("Arial", 12, "bold"), relief="flat", 
        activebackground="#3E8E41", activeforeground="white", cursor="hand2"
    )

def style_button_copy_text(btn):
    btn.configure(
        bg="skyblue", fg="black", font=("Arial", 12, "bold"), relief="flat", 
        activebackground="#3E8E41", activeforeground="white", cursor="hand2"
    )

def font_style():
    font_style = ("Arial", 12)
