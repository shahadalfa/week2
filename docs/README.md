# Text-to-SQL Demo (Week 2)

A small interactive demo showing natural language questions mapped to SQL
queries, executed against a sample SQLite database. Built in the style of
the Spider text-to-SQL dataset.

## Project Structure

```
week2/
├── data/
│   ├── questions.json   # Sample questions paired with correct SQL
│   └── sample.db         # SQLite database (department & employee tables)
├── scripts/
│   └── run_demo.py       # Interactive demo script
└── docs/
    └── README.md
```

## How to Run

```bash
python3 scripts/run_demo.py
```

You'll see a numbered list of natural language questions. Pick one, and the
script will show the matching SQL query and the results from running it
against the sample database.

## Database Schema

**department**(dept_id, dept_name, budget)
**employee**(emp_id, emp_name, dept_id, salary)

## Workflow

This project follows a standard Git feature-branch workflow:

1. Repository created and organized into `data/`, `scripts/`, `docs/`.
2. Feature developed on `feature/text-to-sql-demo` branch.
3. Pull Request opened to review and merge the feature.
4. Feature merged into `main`.
5. Demo run via `run_demo.py`.
