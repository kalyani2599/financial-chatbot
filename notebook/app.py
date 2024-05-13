from flask import Flask, render_template, request

app = Flask(__name__)

# Define the function for the chatbot
def simple_chatbot(user_query):
    if user_query == "What is the total revenue?":
        return "The total revenue is [amount]."
    elif user_query == "How has net income changed over the last year?":
        return "The net income has [increased/decreased] by [amount] over the last year."
    # Add more conditions for other predefined queries
    else:
        return "Sorry, I can only provide information on predefined queries."

# Define the route for the homepage
@app.route("/", methods=["GET", "POST"])
def home():
    if request.method == "POST":
        user_input = request.form["user_query"]
        response = simple_chatbot(user_input)
        return render_template("index.html", user_input=user_input, response=response)
    return render_template("index.html")

if __name__ == "__main__":
    app.run(debug=True)