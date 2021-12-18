# Fill working hours

Basic script to assist in the logging/tracking of my working hours

## How it works
Create a file called `projects.json` in this directory, detailing project codes with the total hours you're allocating to that project. See [the example file](./projects-example.json) for format.

Then just run the script from this directory. The script sequentially fills days with project times until all hours are spent, and outputs the result.

## Example

```bash
## projects.json
{
    "project-a": 57.0,
    "project-b": 43.2
}

python main.py

## output
╒═══════╤═════════════════╤═══════════════╕
│   Day │ Allocations     │   Total Hours │
╞═══════╪═════════════════╪═══════════════╡
│ 0     │ project-a: 7.40 │           7.4 │
├───────┼─────────────────┼───────────────┤
│ 1     │ project-a: 7.40 │           7.4 │
├───────┼─────────────────┼───────────────┤
│ 2     │ project-a: 7.40 │           7.4 │
├───────┼─────────────────┼───────────────┤
│ 3     │ project-a: 7.40 │           7.4 │
├───────┼─────────────────┼───────────────┤
│ 4     │ project-a: 7.40 │           7.4 │
├───────┼─────────────────┼───────────────┤
│ 5     │ project-a: 7.40 │           7.4 │
├───────┼─────────────────┼───────────────┤
│ 6     │ project-a: 7.40 │           7.4 │
├───────┼─────────────────┼───────────────┤
│ 7     │ project-a: 5.20 │           7.4 │
│       │ project-b: 2.20 │               │
├───────┼─────────────────┼───────────────┤
│ 8     │ project-b: 7.40 │           7.4 │
├───────┼─────────────────┼───────────────┤
│ 9     │ project-b: 7.40 │           7.4 │
├───────┼─────────────────┼───────────────┤
│ 10    │ project-b: 7.40 │           7.4 │
├───────┼─────────────────┼───────────────┤
│ 11    │ project-b: 7.40 │           7.4 │
├───────┼─────────────────┼───────────────┤
│ 12    │ project-b: 7.40 │           7.4 │
├───────┼─────────────────┼───────────────┤
│ 13    │ project-b: 4.00 │           4   │
╘═══════╧═════════════════╧═══════════════╛

```

## Notes
7.4 hour day is hardcoded.

## Requirements
[Poetry](https://python-poetry.org/docs/) is used to manage dependencies and virtual environments.

