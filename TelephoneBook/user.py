from TelephoneBook.phonebook import PhoneBook
class User:
    def __init__(self, login, first_name, last_name):
        self.login = "@" + login
        self.first_name = first_name
        self.last_name = last_name
        self.friends = []
        self.phone_books = {}

    def add_friend(self, user):
        self.friends.append(user)

    def remove_friend(self, user):
        self.friends.remove(user)

    def add(self, contact, tag):
        if tag not in self.phone_books:
            self.phone_books[tag] = PhoneBook()
        self.phone_books[tag].add_contact(contact)

    def share(self, user, tag):
        if user not in self.friends:
            print("This user is not your friend.")
        elif tag not in self.phone_books:
            print("You don't have a phone book with this tag.")
        else:
            user.phone_books[tag] = self.phone_books[tag]
            print("You shared phone book.")
