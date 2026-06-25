# Math HTTP Server

A Python HTTP server that performs basic math operations via query-string endpoints. Uses only the Python standard library (no Flask).

## Run

```bash
python3 app.py
```

Server runs at `http://localhost:5000`.

## Endpoints

| Endpoint   | Example URL                          |
|------------|--------------------------------------|
| Addition   | `http://localhost:5000/add?a=5&b=3`  |
| Subtraction| `http://localhost:5000/sub?a=5&b=3`  |
| Multiplication | `http://localhost:5000/multiply?a=5&b=3` |
| Division   | `http://localhost:5000/divide?a=10&b=2` |

## Example response

```json
{
  "a": 5,
  "b": 3,
  "operation": "addition",
  "result": 8
}
```
