pyproject.toml

```python

[project]
name = "simple-mcp"
version = "0.1.0"
requires-python = ">=3.11"
dependencies = [
    "fastapi>=0.165.0",
    "fastmcp[apps]>=4.2.6",
    "google-genai>=3.6.1",
    "mcp[cli]",
]


```


```python

from fastmcp import FastMCP
from google import genai

mcp = FastMCP("Gemini Calculator")

client = genai.Client(api_key="AIzaSyA3koXS7uL32NHX5evLxfxKNPRVluxhRUs")

@mcp.tool()
def calculate(a: float, b: float, operation: str):
    if operation == "add":
        return a + b
    elif operation == "subtract":
        return a - b
    elif operation == "multiply":
        return a * b
    elif operation == "divide":
        return a / b

@mcp.tool()
def ask_gemini(question: str):
    response = client.models.generate_content(
        model="gemini-2.5-flash",
        contents=question
    )
    return response.text

mcp.run()

```
```python
uv run fastmcp dev inspector server.py

```


```python
uv add "fastmcp[apps]"
```

```python

from fastmcp import FastMCP
from prefab_ui.app import PrefabApp
from prefab_ui.components import Column, Heading, Text

mcp = FastMCP("Student App")

@mcp.tool(app=True)
def student_app():
    with Column(gap=3) as view:
        Heading("My Student Dashboard")
        Text("Welcome to Python and AI!")
        Heading("Total Students: 65")
        Text("Course: Generative AI")

    return PrefabApp(view=view)

if __name__ == "__main__":
    mcp.run()


```

## mcp app
```python

from fastmcp import FastMCP
from prefab_ui.app import PrefabApp
from prefab_ui.components import Column, Heading, Text

mcp = FastMCP("Student App")

@mcp.tool(app=True)
def student_app():
    with Column(gap=3) as view:
        Heading("My Student Dashboard")
        Text("Welcome to Python and AI!")
        Heading("Total Students: 65")
        Text("Course: Generative AI")

    return PrefabApp(view=view)

if __name__ == "__main__":
    mcp.run()

```

```python
uv run fastmcp dev apps server.py
          or 
uv run fastmcp dev apps server.py --dev-port 8081

```


```
