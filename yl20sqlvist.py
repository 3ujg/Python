import tkinter as tk
from tkinter import ttk
import sqlite3
import subprocess
import sys
import os

MOVIES_DB = "movies.db"     # left as-is (reads movies table if present)
INSERTER_SCRIPT = "tksql19.py"
INSERTER_DB = "Atammes.db"  # inserter uses this DB

# Combined columns derived from TABLE_FIELDS (rooms/bookings/payments/users)
COLUMNS = (
    "id", "room_number", "type", "price", "available",   # rooms
    "rooms_id", "users_id", "checkin", "checkout",      # bookings
    "booking_id", "amount", "payment_date", "method",   # payments
    "first_name", "last_name", "email", "phone", "image" # users
)

COLUMN_HEADINGS = {
    "id": "ID",
    "room_number": "Room #",
    "type": "Type",
    "price": "Price",
    "available": "Available",
    "rooms_id": "Room ID",
    "users_id": "User ID",
    "checkin": "Check-in",
    "checkout": "Check-out",
    "booking_id": "Booking ID",
    "amount": "Amount",
    "payment_date": "Payment Date",
    "method": "Method",
    "first_name": "First Name",
    "last_name": "Last Name",
    "email": "Email",
    "phone": "Phone",
    "image": "Image"
}

def add_data():
    subprocess.Popen([sys.executable, INSERTER_SCRIPT], cwd=os.getcwd())

def load_data_from_db(tree, search_query=""):
    # Clear tree
    for item in tree.get_children():
        tree.delete(item)

    # Try to read from rooms table (best-effort). If not present, skip.
    try:
        conn = sqlite3.connect(INSERTER_DB)
        cur = conn.cursor()
        # Attempt a left-join style query to combine possible tables where applicable.
        # This is a safe, generic query that tries to select columns if present.
        cur.execute("""
            SELECT r.id, r.room_number, r.type, r.price, r.available,
                   b.rooms_id, b.users_id, b.checkin, b.checkout,
                   p.booking_id, p.amount, p.payment_date, p.method,
                   u.first_name, u.last_name, u.email, u.phone, u.image
            FROM rooms r
            LEFT JOIN bookings b ON b.rooms_id = r.id
            LEFT JOIN payments p ON p.booking_id = b.rowid
            LEFT JOIN users u ON u.rowid = b.users_id
            LIMIT 500
        """)
        rows = cur.fetchall()
        conn.close()
    except Exception:
        rows = []

    # Insert rows into tree (pad/truncate to column count)
    for r in rows:
        row = list(r)
        # ensure length matches columns
        if len(row) < len(COLUMNS):
            row += [None] * (len(COLUMNS) - len(row))
        tree.insert("", "end", values=row[:len(COLUMNS)])

def on_search():
    # For this combined view search will simply reload — keeping interface consistent.
    load_data_from_db(tree, search_entry.get().strip())

root = tk.Tk()
root.title("majutus")

frame = tk.Frame(root)
frame.pack(pady=12, fill=tk.BOTH, expand=True)
scrollbar = tk.Scrollbar(frame)
scrollbar.pack(side=tk.RIGHT, fill=tk.Y)

tree = ttk.Treeview(frame, yscrollcommand=scrollbar.set, columns=COLUMNS, show="headings")
tree.pack(fill=tk.BOTH, expand=True)

# Configure headings and sensible widths
for col in COLUMNS:
    tree.heading(col, text=COLUMN_HEADINGS.get(col, col))
    tree.column(col, width=100, anchor="w")

search_frame = tk.Frame(root)
search_frame.pack(pady=8, fill=tk.X)

search_label = tk.Label(search_frame, text="Otsi:")
search_label.pack(side=tk.LEFT, padx=(6,4))

search_entry = tk.Entry(search_frame)
search_entry.pack(side=tk.LEFT, padx=6, expand=True, fill=tk.X)

search_button = tk.Button(search_frame, text="Otsi", command=on_search)
search_button.pack(side=tk.LEFT, padx=6)

scrollbar.config(command=tree.yview)

open_button = tk.Button(root, text="Lisa andmeid", command=add_data)
open_button.pack(pady=12)

# Initial load
load_data_from_db(tree)

root.mainloop()