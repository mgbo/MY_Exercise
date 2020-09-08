
import csv
import tkinter as tk
from contact import Contact
from form import ContactForm, ContactList

class App(tk.Tk):
	def __init__(self):
		super().__init__()
		self.title("CSV Contact list")
		self.list = ContactList(self, height=12) # Listbox for GUI View
		self.form = ContactForm(self) # contact form for GUI View
		self.contacts = self.load_contacts() # upload data from csv file


		for contact in self.contacts:
			self.list.insert(contact) # upload data to listbox 

		self.list.pack(side=tk.LEFT, padx=10, pady=10)
		self.form.pack(side=tk.LEFT, padx=10, pady=10)
		self.list.bind_doble_click(self.show_contact)

	def load_contacts(self):
		with open("contacts.csv", 'r') as f:
			return [Contact(*r) for r in csv.reader(f)]

	def show_contact(self, index):
		contact = self.contacts[index]
		self.form.load_details(contact)

if __name__ == "__main__":
	app = App()
	app.mainloop()