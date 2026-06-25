from flask import Flask

app = Flask(__name__)

existing_models = [
    "Nissan",
    "Volkswagen",
    "Range Rover",
    "Lexus"
]


@app.route("/")
def home():
    return "Welcome to the Car Company. Browse our available models."


@app.route("/models/<string:model>")
def get_model(model):
    if model in existing_models:
        return f"{model} is available."

    return f"{model} is not available.", 404


if __name__ == "__main__":
    app.run(debug=True)