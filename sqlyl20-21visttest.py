import tkinter as tk
from tkinter import ttk, messagebox
import sqlite3
import subprocess
import sys
import os

INSERTER_SCRIPT = "tksqlyl19vist.py"
DB_NAME = "Atammes.db"

# Tables and their columns (WITHOUT id — we use rowid internally)
TABLE_COLUMNS = {
    "rooms": ("room_number", "type", "price", "available"),
    "bookings": ("rooms_id", "users_id", "checkin", "checkout"),
    "payments": ("booking_id", "amount", "payment_date", "method"),
    "users": ("first_name", "last_name", "email", "phone", "image"),
}

TABLES = list(TABLE_COLUMNS.keys())

# 🔹 Open inserter
def add_data():
    subprocess.Popen([sys.executable, INSERTER_SCRIPT], cwd=os.getcwd())

# 🔹 Load data
def load_data_from_db(tree, search_query=""):
    table = selected_table.get()
    columns = ("rowid",) + TABLE_COLUMNS[table]

    # Clear table
    for item in tree.get_children():
        tree.delete(item)

    # Set columns
    tree["columns"] = columns
    for col in columns:
        tree.heading(col, text=col)
        tree.column(col, width=120, anchor="w")

    try:
        conn = sqlite3.connect(DB_NAME)
        cur = conn.cursor()

        query = f"SELECT {', '.join(columns)} FROM {table}"

        if search_query:
            search_conditions = " OR ".join([f"{col} LIKE ?" for col in columns])
            query += f" WHERE {search_conditions}"
            params = ["%" + search_query + "%"] * len(columns)
            cur.execute(query, params)
        else:
            cur.execute(query)

        rows = cur.fetchall()
        conn.close()

    except Exception as e:
        print("DB error:", e)
        rows = []

    for row in rows:
        tree.insert("", "end", values=row, iid=row[0])  # rowid as iid

# 🔹 Search
def on_search():
    load_data_from_db(tree, search_entry.get().strip())

# 🔹 Open update window
def open_update_window(record_id):
    table = selected_table.get()
    columns = ("rowid",) + TABLE_COLUMNS[table]

    update_window = tk.Toplevel(root)
    update_window.title(f"Uuenda ({table})")

    conn = sqlite3.connect(DB_NAME)
    cur = conn.cursor()

    cur.execute(
        f"SELECT {', '.join(columns)} FROM {table} WHERE rowid=?",
        (record_id,)
    )
    record = cur.fetchone()
    conn.close()

    # ✅ FIX: prevent crash
    if record is None:
        messagebox.showerror("Viga", "Kirjet ei leitud!")
        update_window.destroy()
        return

    entries = {}

    for i, col in enumerate(columns):
        tk.Label(update_window, text=col).grid(row=i, column=0, padx=10, pady=5)

        entry = tk.Entry(update_window, width=40)
        entry.grid(row=i, column=1, padx=10, pady=5)

        entry.insert(0, "" if record[i] is None else record[i])
        entries[col] = entry

    def save_update():
        values = [entries[col].get() for col in columns[1:]]  # skip rowid

        conn = sqlite3.connect(DB_NAME)
        cur = conn.cursor()

        set_clause = ", ".join([f"{col}=?" for col in columns[1:]])

        cur.execute(
            f"UPDATE {table} SET {set_clause} WHERE rowid=?",
            values + [record_id]
        )

        conn.commit()
        conn.close()

        load_data_from_db(tree)
        update_window.destroy()

        messagebox.showinfo("Edu", "Andmed uuendatud!")

    tk.Button(update_window, text="Salvesta", command=save_update).grid(
        row=len(columns), column=0, columnspan=2, pady=10
    )

# 🔹 Update button click
def on_update():
    selected = tree.selection()

    if not selected:
        messagebox.showwarning("Valik puudub", "Palun vali rida!")
        return

    record_id = selected[0]
    open_update_window(record_id)

# 🔹 UI
root = tk.Tk()
root.title("Majutus")

# Table selector
selected_table = tk.StringVar(value=TABLES[0])

table_menu = ttk.Combobox(root, textvariable=selected_table, values=TABLES, state="readonly")
table_menu.pack(pady=5)
table_menu.bind("<<ComboboxSelected>>", lambda e: load_data_from_db(tree))

# Search
search_frame = tk.Frame(root)
search_frame.pack(pady=8, fill=tk.X)

tk.Label(search_frame, text="Otsi:").pack(side=tk.LEFT, padx=5)

search_entry = tk.Entry(search_frame)
search_entry.pack(side=tk.LEFT, padx=5, expand=True, fill=tk.X)

tk.Button(search_frame, text="Otsi", command=on_search).pack(side=tk.LEFT, padx=5)

# Table
frame = tk.Frame(root)
frame.pack(pady=10, fill=tk.BOTH, expand=True)

scrollbar = tk.Scrollbar(frame)
scrollbar.pack(side=tk.RIGHT, fill=tk.Y)

tree = ttk.Treeview(frame, yscrollcommand=scrollbar.set, show="headings")
tree.pack(fill=tk.BOTH, expand=True)

scrollbar.config(command=tree.yview)

# Buttons
button_frame = tk.Frame(root)
button_frame.pack(pady=10)

tk.Button(button_frame, text="Lisa andmeid", command=add_data).grid(row=0, column=0, padx=5)
tk.Button(button_frame, text="Uuenda", command=on_update).grid(row=0, column=1, padx=5)

# Initial load
load_data_from_db(tree)

root.mainloop()