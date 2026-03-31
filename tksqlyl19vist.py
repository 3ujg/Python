import tkinter as tk
from tkinter import ttk, messagebox
import sqlite3
from datetime import datetime

DB_PATH = "Atammes.db"

# Table schemas (field_name, label, type) - types used for basic validation
TABLE_FIELDS = {
    "bookings": [
        ("rooms_id", "Room ID", "int"),
        ("users_id", "User ID", "int"),
        ("checkin", "Check-in (YYYY-MM-DD)", "date"),
        ("checkout", "Check-out (YYYY-MM-DD)", "date"),
    ],
    "payments": [
        ("booking_id", "Booking ID", "int"),
        ("amount", "Amount (e.g. 123.45)", "decimal"),
        ("payment_date", "Payment Date (YYYY-MM-DD)", "date"),
        ("method", "Method", "text"),
    ],
    "rooms": [
        ("id", "ID", "int"),
        ("room_number", "Room Number", "int"),
        ("type", "Type", "text"),
        ("price", "Price (e.g. 99.99)", "decimal"),
        ("available", "Available (e.g. yes/no)", "text"),
    ],
    "users": [
        ("first_name", "First Name", "text"),
        ("last_name", "Last Name", "text"),
        ("email", "Email", "text"),
        ("phone", "Phone", "text"),
        ("image", "Image (path/URL)", "text"),
    ],
}

class App(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("DB Inserter")
        self.geometry("520x420")
        self.resizable(False, False)

        self.selected_table = tk.StringVar(value="bookings")
        self.entries = {}

        # Table selector
        tk.Label(self, text="Select table:").grid(row=0, column=0, padx=10, pady=8, sticky="w")
        table_cb = ttk.Combobox(self, values=list(TABLE_FIELDS.keys()), textvariable=self.selected_table, state="readonly")
        table_cb.grid(row=0, column=1, padx=10, pady=8, sticky="w")
        table_cb.bind("<<ComboboxSelected>>", lambda e: self.build_form())

        # Frame for dynamic form
        self.form_frame = tk.Frame(self)
        self.form_frame.grid(row=1, column=0, columnspan=2, padx=10, pady=4, sticky="nsew")

        # Buttons
        btn_frame = tk.Frame(self)
        btn_frame.grid(row=99, column=0, columnspan=2, pady=12)
        tk.Button(btn_frame, text="Insert", command=self.insert_data, width=12).grid(row=0, column=0, padx=8)
        tk.Button(btn_frame, text="Clear", command=self.clear_entries, width=12).grid(row=0, column=1, padx=8)
        tk.Button(btn_frame, text="Quit", command=self.destroy, width=12).grid(row=0, column=2, padx=8)

        self.build_form()

    def clear_entries(self):
        for ent in self.entries.values():
            ent.delete(0, tk.END)

    def build_form(self):
        # destroy previous widgets
        for w in self.form_frame.winfo_children():
            w.destroy()
        self.entries.clear()

        fields = TABLE_FIELDS[self.selected_table.get()]
        for i, (fname, label_text, _) in enumerate(fields):
            tk.Label(self.form_frame, text=label_text).grid(row=i, column=0, sticky="w", padx=6, pady=6)
            ent = tk.Entry(self.form_frame, width=40)
            ent.grid(row=i, column=1, padx=6, pady=6)
            self.entries[fname] = ent

    def validate_field(self, value: str, ftype: str):
        if ftype == "int":
            return value.isdigit()
        if ftype == "decimal":
            try:
                float(value)
                return True
            except ValueError:
                return False
        if ftype == "date":
            try:
                datetime.strptime(value, "%Y-%m-%d")
                return True
            except ValueError:
                return False
        # text
        return True

    def validate_data(self):
        fields = TABLE_FIELDS[self.selected_table.get()]
        for fname, label_text, ftype in fields:
            val = self.entries[fname].get().strip()
            # Required checks: for users table first_name/last_name/email/phone are required per schema
            if self.selected_table.get() == "users" and fname in ("first_name", "last_name", "email", "phone") and not val:
                messagebox.showerror("Validation error", f"{label_text} is required.")
                return False
            if val:
                if not self.validate_field(val, ftype):
                    messagebox.showerror("Validation error", f"{label_text} must be of type {ftype}.")
                    return False
        return True

    def insert_data(self):
        if not self.validate_data():
            return

        table = self.selected_table.get()
        fields = TABLE_FIELDS[table]
        cols = [f[0] for f in fields]
        vals = [self.entries[c].get().strip() or None for c in cols]  # empty -> NULL

        placeholders = ", ".join(["?"] * len(cols))
        collist = ", ".join(cols)

        sql = f"INSERT INTO {table} ({collist}) VALUES ({placeholders})"

        try:
            conn = sqlite3.connect(DB_PATH)
            cur = conn.cursor()
            cur.execute(sql, vals)
            conn.commit()
            conn.close()
            messagebox.showinfo("Success", f"Inserted into {table}.")
            self.clear_entries()
        except sqlite3.IntegrityError as e:
            messagebox.showerror("DB error", f"Integrity error: {e}")
        except Exception as e:
            messagebox.showerror("DB error", str(e))

if __name__ == "__main__":
    App().mainloop()
w