############ IMPORT HERE #############
from collections import namedtuple

############## IMPLEMENT FUNCTIONS HERE ############
book_collection = {}
Book = namedtuple('Book', 'title author year_published subject section')
members_dict = {}
Member = namedtuple('Member','student_name house_name')
members_by_house = {"Gryffindor": [], "Hufflepuff": [], "Ravenclaw": [], "Slytherin": []}

def sort_dict(dict_in):
    dict(sorted(dict_in.items(), key=lambda item: item[1]))

#NB title=Hogwarts a History,author=Bathilda 

def hogwarts_library(contents):
    content_by_line = contents.split('\n')
    for command in content_by_line:
        commaand_code = command[:2].upper()
        if command_code == "NB":
            command_nb(command[4:])
        elif command_code == "LI":
            command_li()
        elif command_code == "DB":
            command_db(command[4:])
        elif commaand_code == "FB":
            command_fb(command[4:])
        elif command_code == "AS":
            command_as()
        elif commaand_code == "LM":
            command_lm()
        elif command_code == "PL":
            command_pl()


def command_nb(command="title=Hogwarts a History,author=Bathilda Bagshot,year_published=1947,subject=Historical,section=Non-Restricted"):
    # global book_collection
    # global Book
    args = command.split(',')
    info = {}

    for tokens in args:
        heading, content = tokens.split('=')
        info[heading] = content

    book_obj = Book(info["title"], info["author"], info["year_published"], info["subject"], info["subject"], info["section"])
    book_collection[book_obj.title] = book_obj

def command_li():
    global book_collection
    book_collection = sort_dict(book_collection)
    print("*********************LIBRARY INVENTORY**********************")
    print("Number of books available: ",len(book_collection))
    print("------------------------------------")
    for book in book_collection:
        print("Title: ", book.title)
        print("Author: ", book.author)
        print("Date: ", book.year_published)
        print("Subject: ", book.subject)
        print("Section: ", book.section)
        print("------------------------------------")

def command_db(book_title):
    title = book_title.replace('title=','')
    if title in book_collection:
        del book_collection[title]
    else:
        print("Book Not Found. Cannot be deleted.")

def command_fb(command):
    args = command.split(',')
    searched = {}
    if len(args) == 0:
        command_li()
    else:
        title_fb = 0
        author_fb = 0
        year_published_fb = 0
        subject_fb = 0
        section_fb = 0
        for arg in args:
            if "title=" in arg:
                title_fb = arg.replace("title=",'')
                # Shortlisting based on conditions
                if title_fb in book_collection:
                    searched[title_fb] = book_collection[title_fb]
            elif "author=" in arg:
                author_fb = arg.replace("author=",'')
                if len(searched) != 0:
                    for title in searched:
                        if searched[title].author != author_fb:
                            del searched[title]
                else:
                    for book in book_collection:
                        if book.author == author_fb:
                            searched[book.title] = book
            elif "year_published=" in arg:
                year_published_fb = arg.replace("year_published=",'')
                if len(searched) != 0:
                    for title in searched:
                        if searched[title].year_published != year_published_fb:
                            del searched[title]
                else:
                    for book in book_collection:
                        if book.year_published == year_published_fb:
                            searched[book.title] = book
            elif "subject=" in arg:
                subject_fb = arg.replace("subject=",'')
                if len(searched) != 0:
                    for title in searched:
                        if searched[title].subject != subject_fb:
                            del searched[title]
                else:
                    for book in book_collection:
                        if book.subject == subject_fb:
                            searched[book.title] = book
            elif "section=" in arg:
                section_fb = arg.replace("section=",'')
                if len(searched) != 0:
                    for title in searched:
                        if searched[title].section != section_fb:
                            del searched[title]
                else:
                    for book in book_collection:
                        if book.section == section_fb:
                            searched[book.title] = book
        print("************************BOOK SEARCH*************************")
        print("Number of books found:  ", len(searched))
        print("------------------------------------")
        if len(args == 0):
            for book in book_collection:
                print("Title: ", book.title)
                print("Author: ", book.author)
                print("Date: ", book.year_published)
                print("Subject: ", book.subject)
                print("Section: ", book.section)
                print("------------------------------------")

        elif len(searched) > 0:
            for book in searched:
                print("Title: ", book.title)
                print("Author: ", book.author)
                print("Date: ", book.year_published)
                print("Subject: ", book.subject)
                print("Section: ", book.section)
                print("------------------------------------")
        else:
            print("No books matched the search criteria!")




def command_as(command):
    global book_collection
    global Book
    args = command.split(',')
    for i in range(len(args)):
        if i == 0:
            args[i] = args[i].replace('student_name=','')
        elif i == 1:
            args[i] = args[i].replace('house_name=','')

    member= Member(args[0],args[1])
    if arg[0] in members_dict:
        print("Student Name is already present.")
    members_dict[args[0]] = member
    members_by_house[args[1]].append(member)

def command_lm():
    sort_dict(members_dict)
    # Priting Gryffindors
    
    for house in members_by_house:
        print("------------------------------------")
        print("House ", house," members:")
        print("------------------------------------")
        for member in members_by_house[house]:
            print("Member Name: ", member.student_name)
            print("House Name: ", member.house_name)
            print()

def command_pl(command):
    print(command)

if __name__ == "__main__": 
    command_nb()
