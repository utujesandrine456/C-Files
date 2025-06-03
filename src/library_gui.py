import tkinter as tk
from tkinter import messagebox, ttk
import struct
import os
import logging

# Set up logging
logging.basicConfig(filename='library_gui.log', level=logging.DEBUG, 
                    format='%(asctime)s - %(levelname)s - %(message)s')

# Directory for data files
DATA_DIR = "../data"
BOOK_FILE = os.path.join(DATA_DIR, "books.dat")
AUTHOR_FILE = os.path.join(DATA_DIR, "authors.dat")
PUBLISHER_FILE = os.path.join(DATA_DIR, "publishers.dat")
BORROW_FILE = os.path.join(DATA_DIR, "borrow.dat")
FINE_FILE = os.path.join(DATA_DIR, "fines.dat")
MEMBER_FILE = os.path.join(DATA_DIR, "members.dat")
STAFF_FILE = os.path.join(DATA_DIR, "staffs.dat")

# Ensure data directory exists
if not os.path.exists(DATA_DIR):
    os.makedirs(DATA_DIR)

class LibraryManagement:
    def __init__(self, root):
        self.root = root
        self.root.title("Library Management System")
        self.root.geometry("600x400")

        # Main frame
        self.main_frame = tk.Frame(self.root)
        self.main_frame.pack(pady=20)

        # Title
        tk.Label(self.main_frame, text="Library Management System", font=("Arial", 16, "bold")).pack(pady=10)

        # Buttons for each operation
        buttons = [
            ("Add Book", self.add_book),
            ("View Books", self.view_books),
            ("Add Author", self.add_author),
            ("View Authors", self.view_authors),
            ("Add Borrowing", self.add_borrowing),
            ("View Borrowings", self.view_borrowings),
            ("Add Fine", self.add_fine),
            ("View Fines", self.view_fines),
            ("Add Member", self.add_member),
            ("View Members", self.view_members),
            ("Add Publisher", self.add_publisher),
            ("View Publishers", self.view_publishers),
            ("Add Staff", self.add_staff),
            ("View Staff", self.view_staff),
            ("Exit", self.root.quit)
        ]

        for text, command in buttons:
            tk.Button(self.main_frame, text=text, width=20, command=command).pack(pady=5)

    def add_book(self):
        add_window = tk.Toplevel(self.root)
        add_window.title("Add Book")
        add_window.geometry("300x400")

        fields = ["Book ID", "Title", "Author ID", "Publisher ID", "ISBN", "Genre", "Year Published", "Copies Available", "Shelf Location"]
        entries = {}
        for field in fields:
            tk.Label(add_window, text=f"{field}:").pack()
            entries[field] = tk.Entry(add_window)
            entries[field].pack()

        def save_book():
            try:
                book_id = int(entries["Book ID"].get())
                title = entries["Title"].get().strip()
                author_id = int(entries["Author ID"].get())
                publisher_id = int(entries["Publisher ID"].get())
                isbn = entries["ISBN"].get().strip()
                genre = entries["Genre"].get().strip()
                year_published = int(entries["Year Published"].get())
                copies_available = int(entries["Copies Available"].get())
                shelf_location = entries["Shelf Location"].get().strip()

                if not all([book_id, title, author_id, publisher_id, isbn, genre, year_published, copies_available, shelf_location]):
                    messagebox.showerror("Error", "All fields are required!")
                    return

                title = title[:100].ljust(100, '\0')
                isbn = isbn[:20].ljust(20, '\0')
                genre = genre[:50].ljust(50, '\0')
                shelf_location = shelf_location[:30].ljust(30, '\0')

                with open(BOOK_FILE, "ab") as fp:
                    fp.write(struct.pack('i100sii20s50si30s', book_id, title.encode(), author_id, publisher_id, isbn.encode(), genre.encode(), year_published, copies_available, shelf_location.encode()))
                messagebox.showinfo("Success", "Book added successfully!")
                add_window.destroy()
            except ValueError:
                messagebox.showerror("Error", "Invalid input! Ensure ID, Year, and Copies are integers.")

        tk.Button(add_window, text="Save", command=save_book).pack(pady=10)

    def view_books(self):
        view_window = tk.Toplevel(self.root)
        view_window.title("Book List")
        view_window.geometry("800x400")

        tree = ttk.Treeview(view_window, columns=("ID", "Title", "Author ID", "Publisher ID", "ISBN", "Genre", "Year", "Copies", "Shelf"), show="headings")
        tree.heading("ID", text="Book ID")
        tree.heading("Title", text="Title")
        tree.heading("Author ID", text="Author ID")
        tree.heading("Publisher ID", text="Publisher ID")
        tree.heading("ISBN", text="ISBN")
        tree.heading("Genre", text="Genre")
        tree.heading("Year", text="Year Published")
        tree.heading("Copies", text="Copies Available")
        tree.heading("Shelf", text="Shelf Location")
        tree.pack(fill="both", expand=True)

        try:
            with open(BOOK_FILE, "rb") as fp:
                while True:
                    data = fp.read(struct.calcsize('i100sii20s50si30s'))
                    if not data:
                        break
                    book_id, title, author_id, publisher_id, isbn, genre, year_published, copies_available, shelf_location = struct.unpack('i100sii20s50si30s', data)
                    try:
                        tree.insert("", "end", values=(
                            book_id,
                            title.decode('utf-8', errors='replace').rstrip('\0'),
                            author_id,
                            publisher_id,
                            isbn.decode('utf-8', errors='replace').rstrip('\0'),
                            genre.decode('utf-8', errors='replace').rstrip('\0'),
                            year_published,
                            copies_available,
                            shelf_location.decode('utf-8', errors='replace').rstrip('\0')
                        ))
                    except UnicodeDecodeError as e:
                        logging.error(f"Book ID {book_id}: Decode error - {e}")
                        messagebox.showwarning("Warning", f"Some book data is corrupted (ID: {book_id}). Check library_gui.log.")
        except FileNotFoundError:
            messagebox.showerror("Error", "No books found!")

    def add_author(self):
        add_window = tk.Toplevel(self.root)
        add_window.title("Add Author")
        add_window.geometry("300x200")

        fields = ["Author ID", "Name", "Bio"]
        entries = {}
        for field in fields:
            tk.Label(add_window, text=f"{field}:").pack()
            entries[field] = tk.Entry(add_window)
            entries[field].pack()

        def save_author():
            try:
                author_id = int(entries["Author ID"].get())
                name = entries["Name"].get().strip()
                bio = entries["Bio"].get().strip()

                if not all([author_id, name, bio]):
                    messagebox.showerror("Error", "All fields are required!")
                    return

                name = name[:100].ljust(100, '\0')
                bio = bio[:500].ljust(500, '\0')

                with open(AUTHOR_FILE, "ab") as fp:
                    fp.write(struct.pack('i100s500s', author_id, name.encode(), bio.encode()))
                messagebox.showinfo("Success", "Author added successfully!")
                add_window.destroy()
            except ValueError:
                messagebox.showerror("Error", "Author ID must be an integer!")

        tk.Button(add_window, text="Save", command=save_author).pack(pady=10)

    def view_authors(self):
        view_window = tk.Toplevel(self.root)
        view_window.title("Author List")
        view_window.geometry("600x400")

        tree = ttk.Treeview(view_window, columns=("ID", "Name", "Bio"), show="headings")
        tree.heading("ID", text="Author ID")
        tree.heading("Name", text="Name")
        tree.heading("Bio", text="Bio")
        tree.pack(fill="both", expand=True)

        try:
            with open(AUTHOR_FILE, "rb") as fp:
                while True:
                    data = fp.read(struct.calcsize('i100s500s'))
                    if not data:
                        break
                    author_id, name, bio = struct.unpack('i100s500s', data)
                    try:
                        tree.insert("", "end", values=(
                            author_id,
                            name.decode('utf-8', errors='replace').rstrip('\0'),
                            bio.decode('utf-8', errors='replace').rstrip('\0')
                        ))
                    except UnicodeDecodeError as e:
                        logging.error(f"Author ID {author_id}: Decode error - {e}")
                        messagebox.showwarning("Warning", f"Some author data is corrupted (ID: {author_id}). Check library_gui.log.")
        except FileNotFoundError:
            messagebox.showerror("Error", "No authors found!")

    def add_borrowing(self):
        add_window = tk.Toplevel(self.root)
        add_window.title("Add Borrowing")
        add_window.geometry("300x300")

        fields = ["Borrowing ID", "Book ID", "Member ID", "Borrow Date", "Due Date", "Return Date", "Staff ID"]
        entries = {}
        for field in fields:
            tk.Label(add_window, text=f"{field}:").pack()
            entries[field] = tk.Entry(add_window)
            entries[field].pack()

        def save_borrowing():
            try:
                borrowing_id = int(entries["Borrowing ID"].get())
                book_id = int(entries["Book ID"].get())
                member_id = int(entries["Member ID"].get())
                borrow_date = entries["Borrow Date"].get().strip()
                due_date = entries["Due Date"].get().strip()
                return_date = entries["Return Date"].get().strip()
                staff_id = int(entries["Staff ID"].get())

                if not all([borrowing_id, book_id, member_id, borrow_date, due_date, staff_id]):
                    messagebox.showerror("Error", "All required fields must be filled!")
                    return

                borrow_date = borrow_date[:20].ljust(20, '\0')
                due_date = due_date[:20].ljust(20, '\0')
                return_date = return_date[:20].ljust(20, '\0')

                with open(BORROW_FILE, "ab") as fp:
                    fp.write(struct.pack('iii20s20s20si', borrowing_id, book_id, member_id, borrow_date.encode(), due_date.encode(), return_date.encode(), staff_id))
                messagebox.showinfo("Success", "Borrowing added successfully!")
                add_window.destroy()
            except ValueError:
                messagebox.showerror("Error", "Invalid input! Ensure IDs are integers.")

        tk.Button(add_window, text="Save", command=save_borrowing).pack(pady=10)

    def view_borrowings(self):
        view_window = tk.Toplevel(self.root)
        view_window.title("Borrowing List")
        view_window.geometry("800x400")

        tree = ttk.Treeview(view_window, columns=("ID", "Book ID", "Member ID", "Borrow Date", "Due Date", "Return Date", "Staff ID"), show="headings")
        tree.heading("ID", text="Borrowing ID")
        tree.heading("Book ID", text="Book ID")
        tree.heading("Member ID", text="Member ID")
        tree.heading("Borrow Date", text="Borrow Date")
        tree.heading("Due Date", text="Due Date")
        tree.heading("Return Date", text="Return Date")
        tree.heading("Staff ID", text="Staff ID")
        tree.pack(fill="both", expand=True)

        try:
            with open(BORROW_FILE, "rb") as fp:
                while True:
                    data = fp.read(struct.calcsize('iii20s20s20si'))
                    if not data:
                        break
                    borrowing_id, book_id, member_id, borrow_date, due_date, return_date, staff_id = struct.unpack('iii20s20s20si', data)
                    try:
                        tree.insert("", "end", values=(
                            borrowing_id,
                            book_id,
                            member_id,
                            borrow_date.decode('utf-8', errors='replace').rstrip('\0'),
                            due_date.decode('utf-8', errors='replace').rstrip('\0'),
                            return_date.decode('utf-8', errors='replace').rstrip('\0'),
                            staff_id
                        ))
                    except UnicodeDecodeError as e:
                        logging.error(f"Borrowing ID {borrowing_id}: Decode error - {e}")
                        messagebox.showwarning("Warning", f"Some borrowing data is corrupted (ID: {borrowing_id}). Check library_gui.log.")
        except FileNotFoundError:
            messagebox.showerror("Error", "No borrowings found!")

    def add_fine(self):
        add_window = tk.Toplevel(self.root)
        add_window.title("Add Fine")
        add_window.geometry("300x200")

        fields = ["Fine ID", "Borrowing ID", "Amount", "Paid", "Date Paid"]
        entries = {}
        for field in fields:
            tk.Label(add_window, text=f"{field}:").pack()
            entries[field] = tk.Entry(add_window)
            entries[field].pack()

        def save_fine():
            try:
                fine_id = int(entries["Fine ID"].get())
                borrowing_id = int(entries["Borrowing ID"].get())
                amount = float(entries["Amount"].get())
                paid = entries["Paid"].get().strip().lower() in ['1', 'true', 'yes']
                date_paid = entries["Date Paid"].get().strip()

                if not all([fine_id, borrowing_id, amount]):
                    messagebox.showerror("Error", "Fine ID, Borrowing ID, and Amount are required!")
                    return

                date_paid = date_paid[:20].ljust(20, '\0') if paid else ''.ljust(20, '\0')

                with open(FINE_FILE, "ab") as fp:
                    fp.write(struct.pack('iidi20s', fine_id, borrowing_id, amount, int(paid), date_paid.encode()))
                messagebox.showinfo("Success", "Fine added successfully!")
                add_window.destroy()
            except ValueError:
                messagebox.showerror("Error", "Invalid input! Ensure IDs are integers and Amount is a number.")

        tk.Button(add_window, text="Save", command=save_fine).pack(pady=10)

    def view_fines(self):
        view_window = tk.Toplevel(self.root)
        view_window.title("Fine List")
        view_window.geometry("600x400")

        tree = ttk.Treeview(view_window, columns=("ID", "Borrowing ID", "Amount", "Paid", "Date Paid"), show="headings")
        tree.heading("ID", text="Fine ID")
        tree.heading("Borrowing ID", text="Borrowing ID")
        tree.heading("Amount", text="Amount")
        tree.heading("Paid", text="Paid")
        tree.heading("Date Paid", text="Date Paid")
        tree.pack(fill="both", expand=True)

        try:
            with open(FINE_FILE, "rb") as fp:
                while True:
                    data = fp.read(struct.calcsize('iidi20s'))
                    if not data:
                        break
                    fine_id, borrowing_id, amount, paid, date_paid = struct.unpack('iidi20s', data)
                    try:
                        tree.insert("", "end", values=(
                            fine_id,
                            borrowing_id,
                            f"{amount:.2f}",
                            "Yes" if paid else "No",
                            date_paid.decode('utf-8', errors='replace').rstrip('\0')
                        ))
                    except UnicodeDecodeError as e:
                        logging.error(f"Fine ID {fine_id}: Decode error - {e}")
                        messagebox.showwarning("Warning", f"Some fine data is corrupted (ID: {fine_id}). Check library_gui.log.")
        except FileNotFoundError:
            messagebox.showerror("Error", "No fines found!")

    def add_member(self):
        add_window = tk.Toplevel(self.root)
        add_window.title("Add Member")
        add_window.geometry("300x300")

        fields = ["Member ID", "Name", "Address", "Phone", "Email", "Date Joined", "Membership Status"]
        entries = {}
        for field in fields:
            tk.Label(add_window, text=f"{field}:").pack()
            entries[field] = tk.Entry(add_window)
            entries[field].pack()

        def save_member():
            try:
                member_id = int(entries["Member ID"].get())
                name = entries["Name"].get().strip()
                address = entries["Address"].get().strip()
                phone = entries["Phone"].get().strip()
                email = entries["Email"].get().strip()
                date_joined = entries["Date Joined"].get().strip()
                membership_status = entries["Membership Status"].get().strip()

                if not all([member_id, name, address, phone, email, date_joined, membership_status]):
                    messagebox.showerror("Error", "All fields are required!")
                    return

                name = name[:100].ljust(100, '\0')
                address = address[:200].ljust(200, '\0')
                phone = phone[:20].ljust(20, '\0')
                email = email[:100].ljust(100, '\0')
                date_joined = date_joined[:20].ljust(20, '\0')
                membership_status = membership_status[:20].ljust(20, '\0')

                with open(MEMBER_FILE, "ab") as fp:
                    fp.write(struct.pack('i100s200s20s100s20s20s', member_id, name.encode(), address.encode(), phone.encode(), email.encode(), date_joined.encode(), membership_status.encode()))
                messagebox.showinfo("Success", "Member added successfully!")
                add_window.destroy()
            except ValueError:
                messagebox.showerror("Error", "Member ID must be an integer!")

        tk.Button(add_window, text="Save", command=save_member).pack(pady=10)

    def view_members(self):
        view_window = tk.Toplevel(self.root)
        view_window.title("Member List")
        view_window.geometry("800x400")

        tree = ttk.Treeview(view_window, columns=("ID", "Name", "Address", "Phone", "Email", "Date Joined", "Status"), show="headings")
        tree.heading("ID", text="Member ID")
        tree.heading("Name", text="Name")
        tree.heading("Address", text="Address")
        tree.heading("Phone", text="Phone")
        tree.heading("Email", text="Email")
        tree.heading("Date Joined", text="Date Joined")
        tree.heading("Status", text="Membership Status")
        tree.pack(fill="both", expand=True)

        try:
            with open(MEMBER_FILE, "rb") as fp:
                while True:
                    data = fp.read(struct.calcsize('i100s200s20s100s20s20s'))
                    if not data:
                        break
                    member_id, name, address, phone, email, date_joined, membership_status = struct.unpack('i100s200s20s100s20s20s', data)
                    try:
                        tree.insert("", "end", values=(
                            member_id,
                            name.decode('utf-8', errors='replace').rstrip('\0'),
                            address.decode('utf-8', errors='replace').rstrip('\0'),
                            phone.decode('utf-8', errors='replace').rstrip('\0'),
                            email.decode('utf-8', errors='replace').rstrip('\0'),
                            date_joined.decode('utf-8', errors='replace').rstrip('\0'),
                            membership_status.decode('utf-8', errors='replace').rstrip('\0')
                        ))
                    except UnicodeDecodeError as e:
                        logging.error(f"Member ID {member_id}: Decode error - {e}")
                        messagebox.showwarning("Warning", f"Some member data is corrupted (ID: {member_id}). Check library_gui.log.")
        except FileNotFoundError:
            messagebox.showerror("Error", "No members found!")

    def add_publisher(self):
        add_window = tk.Toplevel(self.root)
        add_window.title("Add Publisher")
        add_window.geometry("300x200")

        fields = ["Publisher ID", "Name", "Address", "Contact Info"]
        entries = {}
        for field in fields:
            tk.Label(add_window, text=f"{field}:").pack()
            entries[field] = tk.Entry(add_window)
            entries[field].pack()

        def save_publisher():
            try:
                publisher_id = int(entries["Publisher ID"].get())
                name = entries["Name"].get().strip()
                address = entries["Address"].get().strip()
                contact_info = entries["Contact Info"].get().strip()

                if not all([publisher_id, name, address, contact_info]):
                    messagebox.showerror("Error", "All fields are required!")
                    return

                name = name[:100].ljust(100, '\0')
                address = address[:200].ljust(200, '\0')
                contact_info = contact_info[:100].ljust(100, '\0')

                with open(PUBLISHER_FILE, "ab") as fp:
                    fp.write(struct.pack('i100s200s100s', publisher_id, name.encode(), address.encode(), contact_info.encode()))
                messagebox.showinfo("Success", "Publisher added successfully!")
                add_window.destroy()
            except ValueError:
                messagebox.showerror("Error", "Publisher ID must be an integer!")

        tk.Button(add_window, text="Save", command=save_publisher).pack(pady=10)

    def view_publishers(self):
        view_window = tk.Toplevel(self.root)
        view_window.title("Publisher List")
        view_window.geometry("600x400")

        tree = ttk.Treeview(view_window, columns=("ID", "Name", "Address", "Contact"), show="headings")
        tree.heading("ID", text="Publisher ID")
        tree.heading("Name", text="Name")
        tree.heading("Address", text="Address")
        tree.heading("Contact", text="Contact Info")
        tree.pack(fill="both", expand=True)

        try:
            with open(PUBLISHER_FILE, "rb") as fp:
                while True:
                    data = fp.read(struct.calcsize('i100s200s100s'))
                    if not data:
                        break
                    publisher_id, name, address, contact_info = struct.unpack('i100s200s100s', data)
                    try:
                        tree.insert("", "end", values=(
                            publisher_id,
                            name.decode('utf-8', errors='replace').rstrip('\0'),
                            address.decode('utf-8', errors='replace').rstrip('\0'),
                            contact_info.decode('utf-8', errors='replace').rstrip('\0')
                        ))
                    except UnicodeDecodeError as e:
                        logging.error(f"Publisher ID {publisher_id}: Decode error - {e}")
                        messagebox.showwarning("Warning", f"Some publisher data is corrupted (ID: {publisher_id}). Check library_gui.log.")
        except FileNotFoundError:
            messagebox.showerror("Error", "No publishers found!")

    def add_staff(self):
        add_window = tk.Toplevel(self.root)
        add_window.title("Add Staff")
        add_window.geometry("300x300")

        fields = ["Staff ID", "Name", "Role", "Email", "Phone"]
        entries = {}
        for field in fields:
            tk.Label(add_window, text=f"{field}:").pack()
            entries[field] = tk.Entry(add_window)
            entries[field].pack()

        def save_staff():
            try:
                staff_id = int(entries["Staff ID"].get())
                name = entries["Name"].get().strip()
                role = entries["Role"].get().strip()
                email = entries["Email"].get().strip()
                phone = entries["Phone"].get().strip()

                if not all([staff_id, name, role, email, phone]):
                    messagebox.showerror("Error", "All fields are required!")
                    return

                name = name[:100].ljust(100, '\0')
                role = role[:50].ljust(50, '\0')
                email = email[:100].ljust(100, '\0')
                phone = phone[:20].ljust(20, '\0')

                with open(STAFF_FILE, "ab") as fp:
                    fp.write(struct.pack('i100s50s100s20s', staff_id, name.encode(), role.encode(), email.encode(), phone.encode()))
                messagebox.showinfo("Success", "Staff added successfully!")
                add_window.destroy()
            except ValueError:
                messagebox.showerror("Error", "Staff ID must be an integer!")

        tk.Button(add_window, text="Save", command=save_staff).pack(pady=10)

    def view_staff(self):
        view_window = tk.Toplevel(self.root)
        view_window.title("Staff List")
        view_window.geometry("600x400")

        tree = ttk.Treeview(view_window, columns=("ID", "Name", "Role", "Email", "Phone"), show="headings")
        tree.heading("ID", text="Staff ID")
        tree.heading("Name", text="Name")
        tree.heading("Role", text="Role")
        tree.heading("Email", text="Email")
        tree.heading("Phone", text="Phone")
        tree.pack(fill="both", expand=True)

        try:
            with open(STAFF_FILE, "rb") as fp:
                while True:
                    data = fp.read(struct.calcsize('i100s50s100s20s'))
                    if not data:
                        break
                    staff_id, name, role, email, phone = struct.unpack('i100s50s100s20s', data)
                    try:
                        tree.insert("", "end", values=(
                            staff_id,
                            name.decode('utf-8', errors='replace').rstrip('\0'),
                            role.decode('utf-8', errors='replace').rstrip('\0'),
                            email.decode('utf-8', errors='replace').rstrip('\0'),
                            phone.decode('utf-8', errors='replace').rstrip('\0')
                        ))
                    except UnicodeDecodeError as e:
                        logging.error(f"Staff ID {staff_id}: Decode error - {e}")
                        messagebox.showwarning("Warning", f"Some staff data is corrupted (ID: {staff_id}). Check library_gui.log.")
        except FileNotFoundError:
            messagebox.showerror("Error", "No staff found!")

if __name__ == "__main__":
    root = tk.Tk()
    app = LibraryManagement(root)
    root.mainloop()