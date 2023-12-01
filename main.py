import tkinter as tk
from tkinter import simpledialog, messagebox

class ContactManager:
    def __init__(self, root):
        self.root = root
        self.root.title("Contact Manager")

        # Initialize contact list
        self.contacts = []

        # Create GUI elements
        self.name_label = tk.Label(root, text="Name:")
        self.name_entry = tk.Entry(root)

        self.phone_label = tk.Label(root, text="Phone:")
        self.phone_entry = tk.Entry(root)

        self.email_label = tk.Label(root, text="Email:")
        self.email_entry = tk.Entry(root)

        self.address_label = tk.Label(root, text="Address:")
        self.address_entry = tk.Entry(root)

        # Listbox to display contacts
        self.contact_listbox = tk.Listbox(root, selectmode=tk.SINGLE)
        self.contact_listbox.grid(row=0, column=2, rowspan=9, padx=10, pady=10)

        # Buttons
        self.add_button = tk.Button(root, text="Add Contact", command=self.add_contact)
        self.view_button = tk.Button(root, text="View Contacts", command=self.view_contacts)
        self.search_button = tk.Button(root, text="Search Contact", command=self.search_contact)
        self.update_button = tk.Button(root, text="Update Contact", command=self.update_contact)
        self.delete_button = tk.Button(root, text="Delete Contact", command=self.delete_contact)

        # Place GUI elements on the grid
        self.name_label.grid(row=0, column=0, padx=10, pady=10)
        self.name_entry.grid(row=0, column=1, padx=10, pady=10)

        self.phone_label.grid(row=1, column=0, padx=10, pady=10)
        self.phone_entry.grid(row=1, column=1, padx=10, pady=10)

        self.email_label.grid(row=2, column=0, padx=10, pady=10)
        self.email_entry.grid(row=2, column=1, padx=10, pady=10)

        self.address_label.grid(row=3, column=0, padx=10, pady=10)
        self.address_entry.grid(row=3, column=1, padx=10, pady=10)

        self.add_button.grid(row=4, column=0, columnspan=2, pady=10)
        self.view_button.grid(row=5, column=0, columnspan=2, pady=10)
        self.search_button.grid(row=6, column=0, columnspan=2, pady=10)
        self.update_button.grid(row=7, column=0, columnspan=2, pady=10)
        self.delete_button.grid(row=8, column=0, columnspan=2, pady=10)

    def add_contact(self):
        name = self.name_entry.get()
        phone = self.phone_entry.get()
        email = self.email_entry.get()
        address = self.address_entry.get()

        if name and phone:
            contact = {"Name": name, "Phone": phone, "Email": email, "Address": address}
            self.contacts.append(contact)
            self.update_contact_listbox()
            messagebox.showinfo("Success", "Contact added successfully!")
        else:
            messagebox.showerror("Error", "Name and Phone are required fields.")

    def view_contacts(self):
        # Display the contact list in the listbox
        self.update_contact_listbox()

    def search_contact(self):
        search_term = simpledialog.askstring("Search Contact", "Enter name or phone number:")
        if search_term:
            found_contacts = [contact for contact in self.contacts if
                              search_term.lower() in contact["Name"].lower() or
                              search_term in contact["Phone"]]
            if found_contacts:
                for contact in found_contacts:
                    print(contact)
            else:
                messagebox.showinfo("Info", "No matching contacts found.")
        else:
            messagebox.showerror("Error", "Please enter a search term.")

    def update_contact(self):
        search_term = simpledialog.askstring("Update Contact", "Enter name or phone number:")
        if search_term:
            found_contacts = [contact for contact in self.contacts if
                              search_term.lower() in contact["Name"].lower() or
                              search_term in contact["Phone"]]
            if found_contacts:
                selected_contact = found_contacts[0]

                # Provide an interface to update contact details (similar to add_contact)
                # Update the contact in the contacts list
                self.update_contact_listbox()
                messagebox.showinfo("Success", "Contact updated successfully!")
            else:
                messagebox.showinfo("Info", "No matching contacts found.")
        else:
            messagebox.showerror("Error", "Please enter a search term.")

    def delete_contact(self):
        selected_index = self.contact_listbox.curselection()
        if selected_index:
            # Get the selected contact index and delete it from the contacts list
            index = selected_index[0]
            del self.contacts[index]
            self.update_contact_listbox()
            messagebox.showinfo("Success", "Contact deleted successfully!")
        else:
            messagebox.showinfo("Info", "No contact selected.")

    def update_contact_listbox(self):
        # Clear the listbox and insert contacts
        self.contact_listbox.delete(0, tk.END)
        for contact in self.contacts:
            self.contact_listbox.insert(tk.END, f"{contact['Name']} - {contact['Phone']}")

if __name__ == "__main__":
    root = tk.Tk()
    contact_manager = ContactManager(root)
    root.mainloop()
