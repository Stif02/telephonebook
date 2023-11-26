from TelephoneBook.user import *
from TelephoneBook.contact import *
class PhoneBook:
    def __init__(self):
        self.contacts = []

    def add_contact(self, contact):
        self.contacts.append(contact)

    def remove_contact(self, contact):
        self.contacts.remove(contact)

    def get_contacts_by_country(self, country_code):
        return [contact for contact in self.contacts if contact.country_code == country_code]

    def get_contacts_by_user(self, user):
        return [contact for contact in self.contacts if contact.user== user]