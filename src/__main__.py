from json import load

from .days import Days

if __name__ == "__main__":

    with open("./projects.json", encoding="utf-8") as file:
        projects = load(file)

        days = Days()
        days.add_projects(projects)
        days.print()
