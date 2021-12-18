from collections import deque
from io import StringIO

from tabulate import tabulate


class Day:
    max_hours: float
    allocations: dict[str, float]

    def __init__(self) -> None:
        self.max_hours = 7.4
        self.allocations = {}

    def hours_allocated(self) -> float:
        return sum(self.allocations.values())

    def hours_available(self) -> float:
        return self.max_hours - self.hours_allocated()

    def add_hours(self, project: str, hours: float) -> float:
        if project in self.allocations:
            raise ValueError(
                "Project already exists in this day, cannote allocate again"
            )

        hours_available = self.hours_available()

        excess = hours_available - hours
        if excess >= 0.0:
            # We can fit 'excess' more hours in this day
            # There are no more hours left in the project you gave
            self.allocations[project] = hours
        else:
            # We can't fit any more hours!
            # There are abs(excess) hours left in the project you gave
            self.allocations[project] = hours_available

        if self.hours_available() < 0.0:
            raise ValueError("Day has more hours allocated than the max allowed")

        project_hours_remaining = -excess

        if project_hours_remaining >= 0.0:
            return project_hours_remaining
        return 0.0

    def is_full(self) -> bool:
        return self.hours_available() == 0

    def to_str(self) -> str:
        buffer = StringIO()
        for project, hours in self.allocations.items():
            buffer.write(f"{project}: {hours:.2f}\n")
        return buffer.getvalue()


class Days:
    days: deque[Day] = deque()

    def is_full(self) -> bool:
        return (len(self.days) == 0) or self.days[-1].is_full()

    def add_projects(self, projects: dict[str, float]):
        for project, hours in projects.items():
            self.add_project(project, hours)

    def add_project(self, project: str, hours: float):
        project_hours_remaining = hours
        while project_hours_remaining > 0.0:
            if self.is_full():
                self.days.append(Day())
            project_hours_remaining = self.days[-1].add_hours(
                project, project_hours_remaining
            )

    def print(self) -> None:
        table = []
        for day in self.days:
            element = [day.to_str(), day.hours_allocated()]
            table.append(element)
        if len(table) > 0:
            alignments = ["centre", "left", "decimal"]
            headers = ["Day", "Allocations", "Total Hours"]
            print(
                tabulate(
                    table,
                    tablefmt="fancy_grid",
                    colalign=alignments,
                    headers=headers,
                    showindex=True,
                )
            )
            return
        print("Nothing to print")
