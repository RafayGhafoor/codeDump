def print_book(book):
    print("Title: ", book.title)
    print("Author: ", book.author)
    print("Date: ", book.year_published)
    print("Subject: ", book.subject)
    print("Section: ", book.section)
    print("------------------------------------")


def sort_dict(dict_in):
    return dict(sorted(dict_in.items(), key=lambda item: item[1]))


def token_parser(command):
    args = command.split(',')
    info = {}

    for tokens in args:
        heading, content = tokens.split('=')
        info[heading.strip()] = content.strip()
    return info
