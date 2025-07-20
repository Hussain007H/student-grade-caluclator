import tkinter as tk
from tkinter import messagebox

# Main Window
root = tk.Tk()
root.title("Student Grade Calculator")
root.geometry("400x400")
root.configure(bg="#e0f7fa")

# Function to calculate grade
def calculate():
    try:
        marks = float(entry_marks.get())
        if marks > 100 or marks < 0:
            messagebox.showerror("Invalid", "Enter marks between 0 and 100")
            return
        if marks >= 90:
            grade = "A+"
        elif marks >= 80:
            grade = "A"
        elif marks >= 70:
            grade = "B"
        elif marks >= 60:
            grade = "C"
        elif marks >= 50:
            grade = "D"
        else:
            grade = "F (Fail)"
        label_result.config(text=f"Grade: {grade}", fg="blue")
    except ValueError:
        messagebox.showerror("Invalid", "Please enter a number")

# Heading
label_heading = tk.Label(root, text="Student Grade Calculator", font=("Arial", 16), bg="#e0f7fa")
label_heading.pack(pady=20)

# Entry Label
label_marks = tk.Label(root, text="Enter Marks (%):", font=("Arial", 12), bg="#e0f7fa")
label_marks.pack()

# Entry Field
entry_marks = tk.Entry(root, font=("Arial", 12))
entry_marks.pack(pady=10)

# Button
btn_calc = tk.Button(root, text="Calculate Grade", command=calculate, font=("Arial", 12), bg="#00796b", fg="white")
btn_calc.pack(pady=10)

# Result Label
label_result = tk.Label(root, text="", font=("Arial", 14), bg="#e0f7fa")
label_result.pack(pady=20)

# Start GUI
root.mainloop()
