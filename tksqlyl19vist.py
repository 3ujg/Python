import tkinter as tk
import sqlite3
from tkinter import messagebox, ttk

DB_NAME = "Atammes.db"

TABLE_FIELDS = {
    "rooms": ["room_number", "type", "price", "available"],
    "bookings": ["rooms_id", "users_id", "checkin", "checkout"],
    "payments": ["booking_id", "amount", "payment_date", "method"],
    "users": ["first_name", "last_name", "email", "phone", "image"]
}

entries = {}

# 🔹 Clear inputs
def clear_entries():
    for entry in entries.values():
        entry.delete(0, tk.END)

# 🔹 Load fields dynamically
def load_fields():
    for widget in form_frame.winfo_children():
        widget.destroy()

    entries.clear()

    table = selected_table.get()
    fields = TABLE_FIELDS[table]

    for i, field in enumerate(fields):
        tk.Label(form_frame, text=field).grid(row=i, column=0, padx=10, pady=5)
        entry = tk.Entry(form_frame, width=40)
        entry.grid(row=i, column=1, padx=10, pady=5)
        entries[field] = entry

# 🔹 Insert data
def insert_data():
    table = selected_table.get()
    fields = TABLE_FIELDS[table]

    values = [entries[field].get() for field in fields]

    try:
        conn = sqlite3.connect(DB_NAME)
        cur = conn.cursor()

        placeholders = ", ".join(["?"] * len(fields))
        query = f"INSERT INTO {table} ({', '.join(fields)}) VALUES ({placeholders})"

        cur.execute(query, values)
        conn.commit()
        conn.close()

        messagebox.showinfo("Edu", "Andmed lisatud!")
        clear_entries()

    except Exception as e:
        messagebox.showerror("Viga", str(e))

# 🔹 UI
root = tk.Tk()
root.title("Lisa andmeid")

selected_table = tk.StringVar(value="rooms")

table_menu = ttk.Combobox(root, textvariable=selected_table, values=list(TABLE_FIELDS.keys()), state="readonly")
table_menu.pack(pady=10)
table_menu.bind("<<ComboboxSelected>>", lambda e: load_fields())

form_frame = tk.Frame(root)
form_frame.pack()

submit_button = tk.Button(root, text="Sisesta", command=insert_data)
submit_button.pack(pady=10)

# Initial load
load_fields()

root.mainloop()