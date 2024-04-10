# Flask TodoList API

This is a simple Flask application that implements a TodoList API.

## Prerequisites

* Python 3.9 or higher
* Flask 3.0.0 or higher

## Installation

1. Clone the repository:

``` 
git clone https://github.com/your-username/flask-todolist-api.git
```

2. Install the dependencies:

```
pip install -r requirements.txt
```
3. Run the application
```
flask run
```
## Usage

The API provides the following endpoints:

* `/`: Returns a welcome message.
* `/about`: Returns information about the API.
* `/todos`: Returns a list of all todos.
* `/todos/<id>`: Returns a single todo with the specified ID.
* `/todos/create`: Creates a new todo.
* `/todos/<id>/update`: Updates a todo with the specified ID.
* `/todos/<id>/delete`: Deletes a todo with the specified ID.

## Example

To create a new todo, send a POST request to the `/todos/create` endpoint with the following JSON data:

json { "title": "My new todo", "description": "This is a description of my new todo." }

To retrieve a single todo, send a GET request to the `/todos/<id>` endpoint, where `<id>` is the ID of the todo you want to retrieve.

```
curl http://localhost:5000/todos/1
```
