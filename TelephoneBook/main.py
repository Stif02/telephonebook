from pathlib import Path
from TelephoneBook.contact import Contact
from TelephoneBook.user import User


def init():

    user1=User("admin","pawa","vawa,")
    user2 = User("usver", "cawa", "rawa,")
    user3 = User("bad", "sanya", "sanyok,")

    contact1=Contact(user1,7,567891234)
    contact2=Contact(user2,3,444455555)
    contact3=Contact(user3,5,666677777)

    user1.add(contact2,"Друг")
    user2.add(contact3,"Коллега")
    user3.add(contact1,"Жена")

    user1.add_friend(user2)
    user2.add_friend(user3)
    user3.add_friend(user1)

    user1.share(user2,"Друг")
    user1.share(user3,"Друг")


def operation(x,y,operand=lambda x,y:x+y):
    return operand(x,y)
def print_hi(x):
    if type(x)==int:
        return x
    elif type(x)==str:
        return ord(x[0])
    else:
        return ord(x)

if __name__ == '__main__':
    for file in Path("").iterdir():
        print(file)
    init()

