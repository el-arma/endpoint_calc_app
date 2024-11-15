[![Pylint](https://github.com/el-arma/endpoint_calc_app/actions/workflows/pylint.yml/badge.svg)](https://github.com/el-arma/endpoint_calc_app/actions/workflows/pylint.yml)

***This document is partially generated by LLM

# Flask Calculator API

This project is a simple Flask API that performs basic arithmetic operations: addition, subtraction, multiplication, and division. The API provides an HTTP GET endpoint to calculate the result based on the operation type and two numeric arguments provided as URL query parameters.

## Features

- Perform basic arithmetic operations: addition (`sum`), subtraction (`sub`), multiplication (`mul`), and division (`div`).
- Provide error handling for division by zero and invalid operations.

## Installation

1. Clone the repository:
    ```bash
    git clone https://github.com/el-arma/endpoint_calc_app
    ```

   ```bash
    cd endpoint_calc_app
    ```

2. Install dependencies:
    ```bash
    pip install -r requirements.txt
    ```

3. Run the application:
    ```bash
    python app.py
    ```

The application will start running on `http://127.0.0.1:5000` (that means locally - only on your computer, on port 5000).

## Usage

To use the `/calculate` endpoint, make an HTTP GET request with the following query parameters:

- `op`: The operation to perform (`sum`, `sub`, `mul`, or `div`).
- `arg1`: The first integer argument.
- `arg2`: The second integer argument.

### Example Requests

**Addition**

```
http://127.0.0.1:5000/calculate?op=sum&arg1=10&arg2=5
```

**Subtraction**

```
http://127.0.0.1:5000/calculate?op=sub&arg1=10&arg2=5
```

**Multiplication**

```
http://127.0.0.1:5000/calculate?op=mul&arg1=10&arg2=5
```

**Division**

```
http://127.0.0.1:5000/calculate?op=div&arg1=10&arg2=5
```

### Example Response

For a request like `http://127.0.0.1:5000/calculate?op=sum&arg1=10&arg2=5`, the response will be:

```json
    "10 + 5 = 15"
```

## License

This project is provided for educational purposes.

