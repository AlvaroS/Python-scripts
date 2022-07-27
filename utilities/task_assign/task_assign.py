import random
from termcolor import colored

def makelists(file_name):
    people_list = list()
    tasks_list = list()
    line = str()

    with open(file_name, "r") as f:
        line = f.readline().strip()
        while line != "Tasks":
            line = f.readline().strip().replace('- ', '')
            if line == "Tasks":
                break
            people_list.append(line.replace('- ', ''))
        while line:
            line = f.readline().strip().replace('- ', '')
            if line == '':
                break
            tasks_list.append(line)

    return people_list, tasks_list

def assign_tasks(people_list, tasks_list):
    for element in tasks_list:
        selection = random.choice(people_list)

        yield (element, selection)

def main():
    person, task = makelists("list.txt")
    for x, y in assign_tasks(person, task):
        print(f"{colored(x, 'magenta')}: {y}")

if __name__ == "__main__":
    main()