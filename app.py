import streamlit as st
from src.build_calculator import Calculator

calculator = Calculator()

OPERATIONS = {
    '+': calculator.add,
    '-': calculator.subtract,
    '*': calculator.multiply,
    '/': calculator.divide
}

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
        
        if st.button('Calculate'):
            if operand in OPERATIONS:
                result = OPERATIONS[operand](num_one, num_two)
                st.write(f'The result is: {result}')
            else:
                st.write("Invalid operand selected.")
    except ZeroDivisionError:
        st.write("Cannot divide by zero.")
    except Exception as e:
        st.write(f"An error occurred: {e}")

if __name__ == "__main__":
    main()