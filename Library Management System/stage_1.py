from utilities import *
from common import *
from constants import *


# NB title=Curses and Counter-Curses,author=VindictusViridian,year_published=1703,subject=Curses,section=Restricted
def command_nb(command):
    info=token_parser(command)
    print(info)
    book_obj=Book(**info)
    book_collection[book_obj.title]=book_obj


def command_li():
    global book_collection
    book_collection=sort_dict(book_collection)
    print("*********************LIBRARY INVENTORY**********************")
    print("Number of books available: ", len(book_collection))
    if len(book_collection) == 0:
        return
    print("------------------------------------")
    for book in book_collection.values():
        print_book(book)


def command_db(book_title):
    title=book_title.replace('title=', '')
    if title in book_collection:
        del book_collection[title]
    else:
        print("Book Not Found. Cannot be deleted.")


def command_fb(command):
    arguments=token_parser(command)
    for books in book_collection.values():
        is_okay=True
        for k, v in arguments.items():
            if getattr(books, k) != v:
                is_okay=False
                break
        if (is_okay):
            print_book(books)


def command_as(command):
    args=token_parser(command)
    member=Member(**args)
    if getattr(member, 'student_name') in members_dict:
        print("Student Name is already present.")
    members_dict[member.student_name]=member
    members_by_house[member.house].append(member)


def command_lm():
    for house in members_by_house:
        print("------------------------------------")
        print("House ", house, " members:")
        print("------------------------------------")
        for member in members_by_house[house]:
            print("Member Name: ", member.student_name)
            print("House Name: ", member.house)
            print()


def command_pl(command):
    print(command)
