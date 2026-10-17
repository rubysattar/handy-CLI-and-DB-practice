# Demo: Database Setup and Queries

A small Python project that creates a `customers`/`orders` database, loads sample data, and runs an aggregation query.

## Requirements

- Python 3.12+ (managed by [uv](https://docs.astral.sh/uv/))
- For the PostgreSQL version only: a local PostgreSQL server

## Setup

```bash
git clone https://github.com/rubysattar/handy-CLI-and-DB-practice.git
cd <repo-folder>
uv sync
```

## Run the SQLite version

No database server needed. This creates `demo.db` in the project folder.

```bash
uv run setup_sqlite.py
```

## Run the PostgreSQL version

```bash
createdb demo
uv run setup_sqlite.py
```

Verify the data:

```bash
psql demo -c "SELECT * FROM customers;"
```

## What the scripts do

1. Drop and recreate the `customers` and `orders` tables
2. Insert sample rows
3. Print total spend per customer (a JOIN with GROUP BY)

Both scripts are safe to rerun; they reset the tables each time.

## Project layout

| File | Purpose |
|------|---------|
| `setup_sqlite.py` | SQLite setup and query |
| `main.py` | PostgreSQL setup and query |
| `pyproject.toml`, `uv.lock` | Dependencies |

# Additional Notes for someone new to (or refreshing their memory on) PostgreSQL
| Command | Description |
|---|---|
| `brew services stop postgresql@17` | Stop the server |
| `brew services restart postgresql@17` | Restart it |
| `psql postgres` | Open a shell on the default database |
| `dropdb demo` | Delete a database |

When working with Python, _never_ `pip install` globally. Instead, use a virtual environment. 

`uv` is a package and project manager for Python. It is a wrapper around `pip` and `virtualenv`. It allows you to create isolated environments for your projects and manage dependencies easily.

| Command | Description |
|---|---|
| `uv init` at project root | Initializes project |
| `uv add pandas` | Add a dependency |
| `uv run setup_sqlite.py` | Run script in the project's virtual environment |
| `uv sync` | Install everything listed in the project 

`python3 setup_sqlite.py` works fine here too. You only need `uv` when you’re installing third-party packages like `psycopg`