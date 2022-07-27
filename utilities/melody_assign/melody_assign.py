import random
from termcolor import colored

def make_lists(file_name):
    composers_list = list()

    with open(file_name, "r") as f:
        for name in f:
            if not name.isspace():
                composers_list.append(name.strip())

    ideas_list = composers_list.copy()

    return composers_list, ideas_list

def assign_ideas(composers, ideas):
    assign_list = list()
    ideas_backup = ideas.copy()
    x = 0

    while len(ideas) > 0:
        selection = random.choice(ideas)

        if selection == composers[x] and len(ideas) == 1:
            assign_list.clear()
            x = 0
            ideas = ideas_backup
            continue
        elif selection == composers[x]:
            continue
        else:
            assign_list.append((composers[x], selection))
            ideas.remove(selection)
            x += 1

    return assign_list

def main():
    composers, ideas = make_lists("composers.txt")
    selections = assign_ideas(composers, ideas)

    for elements in selections:
        composer, idea = elements
        print(f"{colored(composer, 'magenta')}: {idea}'s idea")

if __name__ == "__main__":
    main()
