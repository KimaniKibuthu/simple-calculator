"""
Manages the Streamlit deployment of the calculator application.
"""

import streamlit as st
from calculator.basic_calculator import BasicCalculator

calculator = BasicCalculator()

OPERATIONS = {
    "+": calculator.add,
    "-": calculator.subtract,
    "*": calculator.multiply,
    "/": calculator.divide,
}


def perform_calculation(num_one, operand, num_two):
    """
    Perform the calculation based on user input.
    """
    if operand in OPERATIONS:
        return OPERATIONS[operand](num_one, num_two)
    else:
        raise ValueError("Invalid operand selected.")


def main():
    """
    Main function to run the Streamlit calculator application.
    """
    st.set_page_config(page_title="Calculator", page_icon="🧊")
    st.title("Calculator")

    try:
        num_one = st.number_input("Insert the first digit")
        operand = st.selectbox("Select an operand", ("+", "-", "/", "*"))
        num_two = st.number_input("Insert the second digit")

        if st.button("Calculate"):
            try:
                result = perform_calculation(num_one, operand, num_two)
                st.write(f"The result is: {result}")
            except ZeroDivisionError:
                st.write("Cannot divide by zero.")
            except Exception as e:
                st.write(f"An error occurred: {e}")
    except Exception as e:
        st.write(f"An unexpected error occurred: {e}")


if __name__ == "__main__":
    main()
