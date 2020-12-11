############ IMPORT HERE #############
from collections import namedtuple
import os
############## IMPLEMENT FUNCTIONS HERE ############
book_collection = {}
# title(str), author(str), year_published(int), subject(str), section(str)
Book = namedtuple('Book', ['title', 'author',
                           'year_published', 'subject', 'section'])
# Book = namedtuple('Book', 'title author year_published subject section')
members_dict = {}
Member = namedtuple('Member', 'student_name house')
members_by_house = {"Gryffindor": [],
                    "Hufflepuff": [], "Ravenclaw": [], "Slytherin": []}


def sort_dict(dict_in):
    return dict(sorted(dict_in.items(), key=lambda item: item[1]))


def hogwarts_library(contents):
    content_by_line = [i for i in contents.split(
        '\n') if not i.startswith('**')]
    
    for command in content_by_line:
        command = command.strip()
        command_code = command[:2].upper()
        filtered_command = command[2:].strip()
        if command_code == "NB":
            command_nb(filtered_command)
        elif command_code == "LI":
            command_li()
        elif command_code == "DB":
            command_db(filtered_command)
        elif command_code == "FB":
            command_fb(filtered_command)
        elif command_code == "AS":
            command_as(filtered_command)
        elif command_code == "LM":
            command_lm()
        elif command_code == "PL":
            command_pl(filtered_command)


def token_parser(command):
    args = command.split(',')
    info = {}

    for tokens in args:
        heading, content = tokens.split('=')
        info[heading] = content
    return info

# NB title=Curses and Counter-Curses,author=VindictusViridian,year_published=1703,subject=Curses,section=Restricted


def command_nb(command):
    info = token_parser(command)
    book_obj = Book(**info)
    book_collection[book_obj.title] = book_obj


def print_book(book):
    print("Title: ", book.title)
    print("Author: ", book.author)
    print("Date: ", book.year_published)
    print("Subject: ", book.subject)
    print("Section: ", book.section)
    print("------------------------------------")


def command_li():
    global book_collection
    book_collection = sort_dict(book_collection)
    print("*********************LIBRARY INVENTORY**********************")
    print("Number of books available: ", len(book_collection))
    if len(book_collection) == 0:
        return
    print("------------------------------------")
    for book in book_collection.values():
        print_book(book)


def command_db(book_title):
    title = book_title.replace('title=', '')
    if title in book_collection:
        del book_collection[title]
    else:
        print("Book Not Found. Cannot be deleted.")


def command_fb(command):
    arguments = token_parser(command)
    for books in book_collection.values():
        is_okay = True
        for k, v in arguments.items():
            if getattr(books, k) != v:
                is_okay = False
                break
        if (is_okay):
            print_book(books)


def command_as(command):
    args = token_parser(command)
    member = Member(**args)
    if getattr(member, 'student_name') in members_dict:
        print("Student Name is already present.")
    members_dict[member.student_name] = member
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
    input()


def get_file_path(stage_path, name="Stage1Commands.txt"):
    return str(os.path.join(stage_path, name))


def main():
    stage_number = 1
    stage_path = f"Stage{stage_number}"
    with open(get_file_path(stage_path), 'r') as f:
        hogwarts_library(f.read().strip())


if __name__ == "__main__":
    main()
