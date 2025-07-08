import customtkinter as ctk
from tkinter import messagebox

def number_to_words(n):
    units = ["", "One", "Two", "Three", "Four", "Five", "Six", "Seven", "Eight", "Nine"]
    teens = ["Ten", "Eleven", "Twelve", "Thirteen", "Fourteen", "Fifteen",
             "Sixteen", "Seventeen", "Eighteen", "Nineteen"]
    tens = ["", "", "Twenty", "Thirty", "Forty", "Fifty", "Sixty", "Seventy", "Eighty", "Ninety"]
    thousands = ["", "Thousand", "Million", "Billion"]

    def three_digits_to_words(num):
        word = ""
        if num >= 100:
            word += units[num // 100] + " Hundred "
            num %= 100
        if 10 <= num <= 19:
            word += teens[num - 10] + " "
        else:
            word += tens[num // 10] + " "
            word += units[num % 10] + " "
        return word.strip()

    if n == 0:
        return "Zero"

    word = ""
    chunk_count = 0

    while n > 0:
        chunk = n % 1000
        if chunk != 0:
            word = three_digits_to_words(chunk) + " " + thousands[chunk_count] + " " + word
        n //= 1000
        chunk_count += 1

    return word.strip()

def convert_number():
    try:
        num = int(entry.get())
        words = number_to_words(num)
        output_label.configure(state="normal")
        output_label.delete("1.0", "end")
        output_label.insert("1.0", words)
        output_label.configure(state="disabled")
    except ValueError:
        messagebox.showerror("Error", "Please enter a valid number.")

def clear_all():
    entry.delete(0, "end")
    output_label.configure(state="normal")
    output_label.delete("1.0", "end")
    output_label.configure(state="disabled")

ctk.set_appearance_mode("dark")
ctk.set_default_color_theme("dark-blue")

app = ctk.CTk()
app.title("🔢 Number to Words Converter")
app.geometry("460x300")
app.resizable(False, False)

title = ctk.CTkLabel(app, text="Number to Words", font=("Segoe UI", 24, "bold"), text_color="white")
title.pack(pady=(20, 10))

entry = ctk.CTkEntry(app, placeholder_text="Enter a number", font=("Segoe UI", 16), width=300)
entry.pack(pady=(10, 5))

output_label = ctk.CTkTextbox(app, width=360, height=80, font=("Segoe UI", 15), wrap="word")
output_label.pack(pady=(10, 10))
output_label.configure(state="disabled")

btn_frame = ctk.CTkFrame(app, fg_color="transparent")
btn_frame.pack(pady=5)

convert_btn = ctk.CTkButton(btn_frame, text="🔁 Convert", command=convert_number, fg_color="#FF0033", hover_color="#FF3366", corner_radius=10)
convert_btn.pack(side="left", padx=10)

clear_btn = ctk.CTkButton(btn_frame, text="❌ Clear", command=clear_all, fg_color="#333333", hover_color="#555555", corner_radius=10)
clear_btn.pack(side="left", padx=10)

footer = ctk.CTkLabel(app, text="🔎 Powered by Y7X 💗", text_color="#888", font=("Segoe UI", 12))
footer.pack(pady=(10, 0))

app.mainloop()
