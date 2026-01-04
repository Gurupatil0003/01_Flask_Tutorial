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


```python

<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8">
<title>AI Personal Diet Coach</title>
<meta name="viewport" content="width=device-width, initial-scale=1.0">

<link href="https://fonts.googleapis.com/css2?family=Poppins:wght@300;400;500;600;700&display=swap" rel="stylesheet">

<style>
* {
    box-sizing: border-box;
    font-family: 'Poppins', sans-serif;
}

body {
    margin: 0;
    min-height: 100vh;
    background: radial-gradient(circle at top left, #1cb5e0, #000046);
    display: flex;
    justify-content: center;
    align-items: flex-start;
    padding: 40px 15px;
    overflow-x: hidden;
}

/* Floating orbs */
.orb {
    position: absolute;
    width: 280px;
    height: 280px;
    background: radial-gradient(circle, rgba(67,206,162,0.6), transparent 70%);
    filter: blur(90px);
    animation: float 10s infinite alternate;
    z-index: -1;
}

.orb.one { top: 10%; left: 10%; }
.orb.two { bottom: 10%; right: 15%; animation-delay: 2s; }

@keyframes float {
    from { transform: translateY(0); }
    to { transform: translateY(-40px); }
}

.container {
    width: 100%;
    max-width: 1100px;
    background: rgba(255,255,255,0.15);
    backdrop-filter: blur(22px);
    border-radius: 26px;
    padding: 40px;
    box-shadow: 0 50px 100px rgba(0,0,0,0.4);
    animation: fadeIn 0.9s ease;
}

@keyframes fadeIn {
    from { opacity: 0; transform: translateY(30px); }
    to { opacity: 1; transform: translateY(0); }
}

h2 {
    text-align: center;
    font-size: 30px;
    font-weight: 700;
    margin-bottom: 30px;
    background: linear-gradient(135deg, #43cea2, #185a9d);
    -webkit-background-clip: text;
    -webkit-text-fill-color: transparent;
}

textarea {
    width: 100%;
    min-height: 110px;
    padding: 18px;
    border-radius: 14px;
    border: none;
    font-size: 15px;
    resize: none;
    outline: none;
}

button {
    width: 100%;
    margin-top: 18px;
    padding: 16px;
    font-size: 17px;
    font-weight: 600;
    border-radius: 14px;
    border: none;
    cursor: pointer;
    background: linear-gradient(135deg, #43cea2, #185a9d);
    color: white;
    transition: all 0.3s ease;
}

button:hover {
    transform: translateY(-2px);
    box-shadow: 0 20px 40px rgba(67,206,162,0.4);
}

/* Cards */
.cards {
    margin-top: 40px;
    display: grid;
    grid-template-columns: repeat(auto-fit, minmax(260px, 1fr));
    gap: 26px;
}

.card {
    background: rgba(255,255,255,0.85);
    border-radius: 22px;
    padding: 26px;
    box-shadow: 0 25px 45px rgba(0,0,0,0.25);
    animation: rise 0.6s ease;
}

@keyframes rise {
    from { opacity: 0; transform: translateY(25px); }
    to { opacity: 1; transform: translateY(0); }
}

.card h3 {
    font-size: 18px;
    margin-bottom: 12px;
    color: #1b5e20;
}

.card p {
    font-size: 14.5px;
    line-height: 1.8;
    color: #333;
    white-space: pre-line;
}

.full {
    grid-column: 1 / -1;
}

.note {
    margin-top: 40px;
    padding: 22px;
    border-radius: 18px;
    background: rgba(67,206,162,0.2);
    color: #0f5132;
    font-size: 14px;
}
</style>
</head>

<body>

<div class="orb one"></div>
<div class="orb two"></div>

<div class="container">
    <h2>🥗 AI Personal Diet Coach</h2>

    <form method="POST">
        <textarea name="message" placeholder="Ask anything diet-related (e.g., how to reduce weight)">{{ user_input }}</textarea>
        <button type="submit">Generate Smart Plan</button>
    </form>

    {% if response %}
        {% set clean = response | replace("**", "") | replace("*", "") %}

        <div class="cards">

            <div class="card full">
                <h3>🎯 Goal Overview</h3>
                <p>{{ clean }}</p>
            </div>

            <div class="card">
                <h3>🧠 Smart Strategy</h3>
                <p>
                Focus on sustainable habits instead of quick fixes.
                Prioritize whole foods, portion control, and consistency.
                </p>
            </div>

            <div class="card">
                <h3>📅 Practical Routine</h3>
                <p>
                Build routines you can follow long-term.
                Track progress weekly and refine slowly.
                </p>
            </div>

            <div class="card">
                <h3>🏃 Lifestyle Upgrade</h3>
                <p>
                Sleep 7–8 hours, stay hydrated,
                manage stress, and stay active daily.
                </p>
            </div>

            <div class="card">
                <h3>✅ Do’s & ❌ Don’ts</h3>
                <p>
                ✔ Eat mindfully  
                ✔ Stay consistent  
                ✘ Avoid crash diets  
                ✘ Avoid processed sugar
                </p>
            </div>

        </div>

        <div class="note">
            💡 This is a general guidance plan. For medical conditions,
            consult a certified nutrition professional.
        </div>
    {% endif %}
</div>

</body>
</html>




```
