"""
run_demo.py

Interactive Text-to-SQL demo.

Loads a small set of Spider-style natural language questions (each paired
with its correct SQL query), lets the user pick one, runs the query
against a sample SQLite database, and displays the results.
"""

import json
import os
import sqlite3
import sys

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
QUESTIONS_PATH = os.path.join(BASE_DIR, "data", "questions.json")
DB_PATH = os.path.join(BASE_DIR, "data", "sample.db")


def load_questions(path):
    with open(path, "r", encoding="utf-8") as f:
        return json.load(f)


def print_menu(questions):
    print("\n=== Text-to-SQL Interactive Demo ===\n")
    for q in questions:
        print(f"  [{q['id']}] {q['question']}")
    print()


def get_user_choice(questions):
    valid_ids = {q["id"] for q in questions}
    while True:
        raw = input("Select a question number (or 'q' to quit): ").strip()
        if raw.lower() == "q":
            sys.exit(0)
        if raw.isdigit() and int(raw) in valid_ids:
            return int(raw)
        print("Invalid choice, please try again.")


def run_query(sql):
    conn = sqlite3.connect(DB_PATH)
    cur = conn.cursor()
    cur.execute(sql)
    columns = [desc[0] for desc in cur.description]
    rows = cur.fetchall()
    conn.close()
    return columns, rows


def print_results(columns, rows):
    print("\nColumns:", " | ".join(columns))
    print("-" * 40)
    if not rows:
        print("(no rows returned)")
    for row in rows:
        print(" | ".join(str(v) for v in row))
    print()


def main():
    questions = load_questions(QUESTIONS_PATH)
    print_menu(questions)
    choice_id = get_user_choice(questions)
    chosen = next(q for q in questions if q["id"] == choice_id)

    print(f"\nQuestion: {chosen['question']}")
    print(f"SQL:      {chosen['sql']}")

    columns, rows = run_query(chosen["sql"])
    print_results(columns, rows)


if __name__ == "__main__":
    main()
