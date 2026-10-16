| Command | Description |
|---|---|
| `brew services stop postgresql@17` | Stop the server |
| `brew services restart postgresql@17` | Restart it |
| `psql postgres` | Open a shell on the default database |
| `dropdb demo` | Delete a database |

When working with Python, never `pip install` globally. Instead, use a virtual environment. 