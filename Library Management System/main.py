############ IMPORT HERE #############
from collections import namedtuple
import os
from common import *
from constants import *
from utilities import *
from datetime import timedelta


def run_stage_1(command_code, filtered_command):
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


def run_stage_2(command_code, filtered_command):
    if command_code == "CB":
        command_cb(filtered_command)
    elif command_code == "SD":
        command_sd(filtered_command)
    elif command_code == "CR":
        command_cr()


def hogwarts_library(contents):
    content_by_line = [i for i in contents.split(
        '\n') if not i.startswith('**')]

    for command in content_by_line:
        command = command.strip()
        command_code = command[:2].upper()
        filtered_command = command[2:].strip()
        run_stage_1(command_code, filtered_command)
        run_stage_2(command_code, filtered_command)


# ******************* Stage 1 [Start] ********************************
def command_nb(command):
    info = token_parser(command)
    book_obj = Book(**info)
    book_collection[book_obj.title] = book_obj


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

# ******************* Stage 1 [End] ********************************


# ******************* Stage 2 [Start] ********************************
Checkout = namedtuple('Checkout', ['title', 'student_name', 'due_date'])


def command_sd(command):
    global start_date
    start_date = datetime.datetime.strptime(command, '%m/%d/%Y')


def command_cb(command):
    info = token_parser(command)
    for title, book in checkouts.items():
        if book.title == info["title"]:
            command_pl("**Already Checked out")
            return

    if info['title'] not in book_collection:
        command_pl('**Invalid book')
        return

    elif info.get('student_name') not in members_dict:
        command_pl('**Student not found')

    if 'number_of_days' not in info:
        info['due_date'] = start_date + timedelta(days=14)
    else:
        info['due_date'] = start_date + \
            timedelta(days=int(info['number_of_days']))
    if info.get('number_of_days'):
        del info['number_of_days']
    if book_collection[info.get('title')].section == "Restricted":
        if info.get('pass_code'):
            if info['pass_code'] in ("Accio", "Protego"):
                del info['pass_code']

                checkout_obj = Checkout(
                    **info)
                checkouts[checkout_obj.title] = checkout_obj
        else:
            command_pl('**missing pass code')
    else:
        if info.get('pass_code'):
            del info['pass_code']
        checkout_obj = Checkout(
            **info)
        checkouts[checkout_obj.title] = checkout_obj


def command_cr():
    global checkouts
    checkout_by_houses = {house_name: []
                          for house_name in sorted(houses_by_name)}
    checkouts = sort_dict(checkouts)
    for k, v in checkouts.items():
        house_name = members_dict[v.student_name].house
        checkout_by_houses[house_name].append(v)
    for key, house in checkout_by_houses.items():
        house.sort()

    for k, v in checkout_by_houses.items():
        if len(v) == 0:
            continue
        print("Students of: ", k)
        for i in v:
            print(i.student_name)


def command_la(command):


def command_dt(command):
    pass


def command_ad(command):
    pass


def get_file_path(stage_path, name="Stage2_CB_CR_LA.txt"):
    return str(os.path.join(stage_path, name))


def main():
    stage_number = 2
    stage_path = f"Stage{stage_number}"
    with open(get_file_path(stage_path), 'r') as f:
        hogwarts_library(f.read().strip())


if __name__ == "__main__":
    main()
