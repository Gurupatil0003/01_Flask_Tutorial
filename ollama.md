```python
from agno.agent import Agent
from agno.models.ollama import Ollama

model = Ollama("llama3.2:1b")

agent = Agent(
    name="PythonInterviewAgent",
    model=model,
     instructions="""
You are a Personal diet coach.

Rules:
1. help me to make diet plan
2.whenever u see diet then  only response otherwise say:
plese say:it's not a diet plan.
"""
)

print("🐍 Python Interview Agent")
print("Type 'exit' to quit")
print("=" * 50)

while True:
    user_input = input("\nYou: ").strip()

    if user_input.lower() == "exit":
        print("Goodbye 👋")
        break

    response = agent.run(user_input)

    print("\n🤖 Agent:")
    print(response.content)
    print("=" * 50)
```

```python


from flask import Flask, render_template, request
from agno.agent import Agent
from agno.models.ollama import Ollama

app = Flask(__name__)

# Load model
model = Ollama("llama3.2:1b")

# Create agent
agent = Agent(
    name="DietCoachAgent",
    model=model,
    instructions="""
You are a Personal diet coach.

Rules:
1. Help me to make diet plans only.
2. Whenever you see diet-related questions, respond properly.
3. Otherwise say exactly:
it's not a diet plan.
"""
)

@app.route("/", methods=["GET", "POST"])
def index():
    response = ""
    user_input = ""

    if request.method == "POST":
        user_input = request.form.get("message")
        result = agent.run(user_input)
        response = result.content

    return render_template("index.html", user_input=user_input, response=response)

if __name__ == "__main__":
    app.run(debug=True)



```

```python

<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>Personal Diet Coach</title>
    <style>
        body {
            font-family: Arial, sans-serif;
            background: #f4f6f8;
            padding: 40px;
        }
        .container {
            max-width: 750px;
            background: white;
            padding: 25px;
            border-radius: 10px;
            margin: auto;
        }
        textarea {
            width: 100%;
            padding: 10px;
            font-size: 15px;
        }
        button {
            margin-top: 15px;
            padding: 10px 20px;
            font-size: 16px;
            cursor: pointer;
        }
        .section {
            margin-top: 25px;
        }
        .section h3 {
            color: #2e7d32;
            border-bottom: 2px solid #e0e0e0;
            padding-bottom: 5px;
        }
        .item {
            margin-left: 15px;
            margin-top: 5px;
        }
        .note {
            margin-top: 20px;
            background: #f1f8e9;
            padding: 15px;
            border-radius: 5px;
        }
    </style>
</head>
<body>

<div class="container">
    <h2>🥗 Personal Diet Coach</h2>

    <form method="POST">
        <textarea name="message" rows="4" placeholder="Ask for a diet plan...">{{ user_input }}</textarea>
        <button type="submit">Generate Diet Plan</button>
    </form>

    {% if response %}
        <div class="section">
            <h3>📋 Diet Plan</h3>

            {% set text = response %}

            {% if "Breakfast" in text %}
                <div class="section">
                    <h3>🍳 Breakfast</h3>
                    <p>{{ text.split("Breakfast")[1].split("Lunch")[0] }}</p>
                </div>
            {% endif %}

            {% if "Lunch" in text %}
                <div class="section">
                    <h3>🥗 Lunch</h3>
                    <p>{{ text.split("Lunch")[1].split("Dinner")[0] }}</p>
                </div>
            {% endif %}

            {% if "Dinner" in text %}
                <div class="section">
                    <h3>🍽️ Dinner</h3>
                    <p>{{ text.split("Dinner")[1].split("Snack")[0] }}</p>
                </div>
            {% endif %}

            {% if "Snack" in text %}
                <div class="section">
                    <h3>🍎 Snacks</h3>
                    <p>{{ text.split("Snack")[1] }}</p>
                </div>
            {% endif %}

            <div class="note">
                💡 You can swap ingredients or proteins based on your preference.
            </div>
        </div>
    {% endif %}
</div>

</body>
</html>


```
