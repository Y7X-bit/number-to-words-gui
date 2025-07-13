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
app.title("💬 Countella")
app.geometry("600x410")
app.configure(fg_color="#000000")
app.resizable(False, False)

# Title
title = ctk.CTkLabel(app, text="💬 Countella", font=("Segoe UI", 28, "bold"),
                     text_color="#FF0000", bg_color="#000000")
title.pack(pady=(30, 10))

# Entry
entry = ctk.CTkEntry(app, placeholder_text="Enter a number", font=("Segoe UI", 18),
                     width=400, height=45, fg_color="#000000", text_color="white",
                     border_color="#FF0000", border_width=2, corner_radius=10,
                     bg_color="#000000")
entry.pack(pady=(10, 20))

# Output Text Box
output_label = ctk.CTkTextbox(app, width=480, height=100, font=("Segoe UI", 16),
                              wrap="word", fg_color="#000000", text_color="white",
                              border_color="#FF0000", border_width=2, corner_radius=10,
                              bg_color="#000000")
output_label.pack(pady=(0, 20))
output_label.configure(state="disabled")

# Buttons Frame
btn_frame = ctk.CTkFrame(app, fg_color="#000000", bg_color="#000000")
btn_frame.pack(pady=10)

# Convert Button
convert_btn = ctk.CTkButton(btn_frame, text="🔁 Convert", command=convert_number,
                             width=180, height=40, fg_color="#000000", text_color="white",
                             hover_color="#1a1a1a", border_color="#FF0000", border_width=2,
                             corner_radius=12, font=("Segoe UI", 16, "bold"),
                             bg_color="#000000")
convert_btn.grid(row=0, column=0, padx=15)

# Clear Button
clear_btn = ctk.CTkButton(btn_frame, text="❌ Clear", command=clear_all,
                           width=180, height=40, fg_color="#000000", text_color="white",
                           hover_color="#1a1a1a", border_color="#FF0000", border_width=2,
                           corner_radius=12, font=("Segoe UI", 16), bg_color="#000000")
clear_btn.grid(row=0, column=1, padx=15)

# Footer
footer = ctk.CTkLabel(app, text="🔎 Powered by Y7X 💗", text_color="#FF0000",
                      font=("Segoe UI", 13), bg_color="#000000")
footer.pack(pady=(20, 10))

app.mainloop()