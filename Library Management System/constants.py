from collections import namedtuple
# student_name(str), house(str), checked_out_books(list=[])
Member = namedtuple('Member', ['student_name', 'house'])
members_dict = {}
houses_by_name = ["Gryffindor", "Hufflepuff", "Ravenclaw", "Slytherin"]
members_by_house = {"Gryffindor": [],
                    "Hufflepuff": [], "Ravenclaw": [], "Slytherin": []}
