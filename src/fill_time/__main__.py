from json import load

from .days import Days


def main():
    with open("./projects.json", encoding="utf-8") as file:
        projects = load(file)

        days = Days()
        days.add_projects(projects)
        days.print()


if __name__ == "__main__":
    main()
