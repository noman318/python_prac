# python_prac

A collection of small Python practice scripts.

## Scripts

| File | Description |
|------|-------------|
| `app.py` | Command-line calculator: `add`, `sub`, `mul`, `div`, `mod`, `power` |
| `folder.py` | Prompts for folder names and lists their contents, handling missing folders and permission errors |
| `test_env.py` | Checks whether the `MY_API_KEY` environment variable is set |

## Usage

Requires Python 3.

```bash
# Calculator: python app.py <operation> <num1> <num2>
python app.py add 10 5

# List folder contents
python folder.py

# Check an environment variable
MY_API_KEY=secret python test_env.py
```

Environment variables can be kept in a local `.env` file (git-ignored).
