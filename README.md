# Calculator Documentation

## Project Overview

This project is a simple calculator that performs basic arithmetic operations, including addition, subtraction, multiplication, and division. It provides a streamlined interface for users to perform calculations without any hassle.

## Project Structure

```
ProjectCalculator/
├── src/
│   ├── __init__.py
|   ├── test_calculator.py
│   ├── build_calculator.py
|
├── Dockerfile
├── app.py
├── README.md
└── requirements.txt
```

- **`test_calculator.py`**: Contains unit tests for the calculator functions.
- **`build_calculator.py`**: Implements the Calculator class with arithmetic operations.
- **`Dockerfile`**: Contains instructions to build the Docker image for the calculator application.
- **`app.py`**: Manages the Streamlit deployment of the calculator application.
- **`README.md`**: Provides detailed information about the project, its structure, and setup instructions.
- **`requirements.txt`**: Lists the necessary libraries and dependencies used in the project.


## Setup Instructions


### Docker Setup

1. Build the Docker image:

   ```bash
   docker build -t calculator .
   ```

2. Run the Docker container:

   ```bash
   docker run -d -p 8080:8080 calculator
   ```

3. Verify the Application:
   Open your browser and navigate to http://localhost:8080. 

4. Calculator Usage:

   - Enter the first number.

   - Select the desired arithmetic operation (addition, subtraction, multiplication, or division).

   - Enter the second number.

   - Click the "Calculate" button to see the result displayed.


This simple calculator app provides a convenient way for users to perform basic calculations within a user-friendly interface. 


