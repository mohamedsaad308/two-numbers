## Getting Started

- An API that takes two numbers and returs four airthemetic operations between the two numbers as following:

  1. Addition: number 1 + number 2
  2. Subtraction: number 1 - number 2
  3. Multiplication: nun1 x number 2
  4. Division: number 1 / number 2

## Installing Dependencies

### Python 3.8

Follow instructions to install the latest version of python for your platform in the [python docs](https://docs.python.org/3/using/unix.html#getting-and-installing-the-latest-version-of-python)

### Virtual Enviornment

Create virtula environment:

```bsh
python3 -m venv venv
```

Start the virtual environment

```bsh
source venv/bin/activate
```

### PIP Dependencies

Once you have your virtual environment setup and running, install dependencies by naviging to the `/backend` directory and running:

```bash
pip install -r requirements.txt
```

This will install all of the required packages we selected within the `requirements.txt` file.

#### Key Dependencies

- [Flask](http://flask.pocoo.org/) is a lightweight backend microservices framework. Flask is required to handle requests and responses.

## Running the server

To start the app locally

```bash
flask --app app  --debug run
```

## Error Handling

Errors are returned as a JSON object in the following format:

```json
{
  "error": "405",
  "message": "method not allowed",
  "success": false
}
```

The API returns 2 error types when a request fails:

- 400 : Bad request
- 405 : Method Not Allowed

## Post the two numbers

Example :

```bash
POST /api/two-numbers
```

with json:

```json
{
  "num1": 1000,
  "num2": 12
}
```

Returns

```json
{
  "results": {
    "addition": 1012.0,
    "division": 83.33333333333333,
    "multiplication": 12000.0,
    "substraction": 988.0
  },
  "success": true
}
```

## Testing

To run the tests, run

```
python test_app.py
```
