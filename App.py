import streamlit as st
import math

# Title
st.title("Advanced Calculator App")

# Input numbers
num1 = st.number_input("Enter the first number", value=0.0)
num2 = st.number_input("Enter the second number", value=0.0)

# Operations
basic_ops = ["Addition", "Subtraction", "Multiplication", "Division"]
advanced_ops = ["Exponentiation", "Square Root (of first number)", "Logarithm (base 10 of first number)"]

operation = st.selectbox(
    "Choose an operation",
    basic_ops + advanced_ops
)

# Initialize session state for history
if "history" not in st.session_state:
    st.session_state.history = []

# Perform calculation
result = None
try:
    if operation == "Addition":
        result = num1 + num2
    elif operation == "Subtraction":
        result = num1 - num2
    elif operation == "Multiplication":
        result = num1 * num2
    elif operation == "Division":
        result = num1 / num2 if num2 != 0 else "Error: Division by zero"
    elif operation == "Exponentiation":
        result = num1 ** num2
    elif operation == "Square Root (of first number)":
        result = math.sqrt(num1) if num1 >= 0 else "Error: Negative number"
    elif operation == "Logarithm (base 10 of first number)":
        result = math.log10(num1) if num1 > 0 else "Error: Non-positive number"

    # Save history
    st.session_state.history.append(f"{operation}: {result}")

except Exception as e:
    result = f"Error: {str(e)}"

# Display result
if result is not None:
    st.success(f"Result: {result}")

# Display calculation history
if st.session_state.history:
    st.subheader("Calculation History")
    for i, entry in enumerate(st.session_state.history, 1):
        st.write(f"{i}. {entry}")
