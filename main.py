import json

from src.days import Days

if __name__ == "__main__":

    with open("./projects.json", encoding="utf-8") as file:
        projects = json.load(file)

        days = Days()
        days.add_projects(projects)
        days.print()
