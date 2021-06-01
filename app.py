from flask import Flask, jsonify, request
from http import HTTPStatus


app = Flask(__name__)


todos = [
    {"id": 1, "name": "Feed the cat.", "done": False},
    {"id": 2, "name": "wash the dishes.", "done": False},
]


@app.route("/todos", methods=["GET"])
def get_todos():
    return jsonify({"data": todos})


@app.route("/todos/<int:todo_id>", methods=["GET"])
def get_todo(todo_id):
    todo = next((todo for todo in todos if todo["id"] == todo_id), None)
    if not todo:
        return jsonify({"to-do": "Not found"}), HTTPStatus.NOT_FOUND
    return jsonify(todo)


@app.route("/todos", methods=["POST"])
def create_todo():
    data = request.get_json()
    name = data.get("name")
    done = data.get("done")

    todo = {"id": len(todos) + 1, "name": name, "done": done}
    todos.append(todo)
    return jsonify(todo)


@app.route("/todos/<int:todo_id>", methods=["PUT"])
def update_todo(todo_id):
    todo = next((todo for todo in todos if todo["id"] == todo_id), None)
    data = request.get_json()
    if not todo:
        return jsonify({"to-do": "Not found"}), HTTPStatus.NOT_FOUND
    todo.update({"name": data.get("name"), "done": data.get("done")})
    return jsonify(todo)


@app.route("/todos/<int:todo_id>", methods=["DELETE"])
def delete_todo(todo_id):
    todo = next((todo for todo in todos if todo["id"] == todo_id), None)
    if not todo:
        return jsonify({"to-do": "Not found"}), HTTPStatus.NOT_FOUND
    todos.remove(todo)
    return jsonify({"data": todos})


if __name__ == "__main__":
    app.run()
