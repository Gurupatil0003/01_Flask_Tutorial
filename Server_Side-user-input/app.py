from flask import Flask, render_template, request

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def index():
    if request.method == "GET":
        return render_template("index.html")  # Render the form template
    elif request.method == "POST":
        user_input = request.form["user_input"]  # Access user input from form data

        # Server-side processing logic (replace with your specific logic)
        try:
            processed_data = user_input.upper()  # Example processing (replace with actual actions)
        except Exception as e:
            # Handle potential errors during processing (e.g., invalid input)
            processed_data = f"An error occurred: {str(e)}"

        return render_template("result.html", processed_data=processed_data)

if __name__ == "__main__":
    app.run(debug=True)
