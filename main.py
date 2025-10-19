import tkinter as tk

# Create main window
root = tk.Tk()
root.title("Dynamic Step Counter")
root.geometry("350x250")
root.config(bg="#f5f5f5")

count = tk.IntVar(value=0)
step = tk.IntVar(value=1)

# Functions
def increment():
    count.set(count.get() + step.get())

def decrement():
    count.set(count.get() - step.get())

def reset():
    count.set(0)

# Display label
label = tk.Label(root, textvariable=count, font=("Arial", 50, "bold"), bg="#f5f5f5", fg="#333")
label.pack(pady=15)

# Step selection
step_frame = tk.Frame(root, bg="#f5f5f5")
step_frame.pack(pady=5)
tk.Label(step_frame, text="Step:", font=("Arial", 12), bg="#f5f5f5").pack(side="left", padx=5)
tk.Spinbox(step_frame, from_=1, to=10, textvariable=step, width=5, font=("Arial", 12)).pack(side="left")

# Buttons
btn_frame = tk.Frame(root, bg="#f5f5f5")
btn_frame.pack(pady=15)

tk.Button(btn_frame, text="Increment", command=increment, width=12, bg="#4CAF50", fg="white").grid(row=0, column=0, padx=5)
tk.Button(btn_frame, text="Decrement", command=decrement, width=12, bg="#f44336", fg="white").grid(row=0, column=1, padx=5)
tk.Button(root, text="Reset", command=reset, width=28, bg="#2196F3", fg="white").pack(pady=5)

root.mainloop()