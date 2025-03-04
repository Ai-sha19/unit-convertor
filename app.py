import streamlit as st

# Custom CSS for styling
st.markdown(
    """
    <style>
        .stSelectbox, .stNumberInput {
            border-radius: 5px;
            padding: 8px;
            background-color: #fff;
            color: black;
            border: 1px solid #ccc;
        }
    </style>
    """,
    unsafe_allow_html=True
)

# Conversion Functions
def distance_convertor(from_unit, to_unit, value):
    units = {'Meters': 1, 'Kilometers': 1000, 'Feet': 0.3048, 'Miles': 1609.34}
    return value * units[from_unit] / units[to_unit]

def length_convertor(from_unit, to_unit, value):
    units = {'Millimeters': 0.001, 'Centimeters': 0.01, 'Meters': 1, 'Inches': 0.0254, 'Feet': 0.3048, 'Yards': 0.9144}
    return value * units[from_unit] / units[to_unit]

def temperature_convertor(from_unit, to_unit, value):
    if from_unit == to_unit:
        return value  # Explicitly returning the same value for clarity
    elif from_unit == "Celsius" and to_unit == "Fahrenheit":
        return (value * 9/5) + 32
    elif from_unit == "Fahrenheit" and to_unit == "Celsius":
        return (value - 32) * 5/9

def weight_convertor(from_unit, to_unit, value):
    units = {'Kilograms': 1, 'Grams': 0.001, 'Pounds': 0.453592, 'Ounces': 0.0283495}
    return value * units[from_unit] / units[to_unit]

def pressure_convertor(from_unit, to_unit, value):
    units = {'Pascals': 1, 'Hectopascals': 100, 'Kilopascals': 1000, 'Bar': 100000}
    return value * units[from_unit] / units[to_unit]

# UI
st.title("Unit Converter")

# Select Category
category = st.selectbox("Select Category", ["Distance", "Length", "Temperature", "Weight", "Pressure"])

if category == "Distance":
    from_unit, to_unit = st.selectbox("From", ["Meters", "Kilometers", "Feet", "Miles"]), st.selectbox("To", ["Meters", "Kilometers", "Feet", "Miles"])
    value = st.number_input("Enter Value", min_value=0.0, format="%.2f")

    if st.button("Convert", key="distance"):
        result = distance_convertor(from_unit, to_unit, value)
        st.success(f"{value} {from_unit} = {result:.2f} {to_unit}")

elif category == "Length":
    from_unit, to_unit = st.selectbox("From", ["Millimeters", "Centimeters", "Meters", "Inches", "Feet", "Yards"]), st.selectbox("To", ["Millimeters", "Centimeters", "Meters", "Inches", "Feet", "Yards"])
    value = st.number_input("Enter Value", min_value=0.0, format="%.2f")

    if st.button("Convert", key="length"):
        result = length_convertor(from_unit, to_unit, value)
        st.success(f"{value} {from_unit} = {result:.2f} {to_unit}")

elif category == "Temperature":
    from_unit, to_unit = st.selectbox("From", ["Celsius", "Fahrenheit"]), st.selectbox("To", ["Celsius", "Fahrenheit"])
    value = st.number_input("Enter Value", format="%.2f")

    if st.button("Convert", key="temperature"):
        result = temperature_convertor(from_unit, to_unit, value)
        st.success(f"{value} {from_unit} = {result:.2f} {to_unit}")

elif category == "Weight":
    from_unit, to_unit = st.selectbox("From", ["Kilograms", "Grams", "Pounds", "Ounces"]), st.selectbox("To", ["Kilograms", "Grams", "Pounds", "Ounces"])
    value = st.number_input("Enter Value", min_value=0.0, format="%.2f")

    if st.button("Convert", key="weight"):
        result = weight_convertor(from_unit, to_unit, value)
        st.success(f"{value} {from_unit} = {result:.2f} {to_unit}")

elif category == "Pressure":
    from_unit, to_unit = st.selectbox("From", ["Pascals", "Hectopascals", "Kilopascals", "Bar"]), st.selectbox("To", ["Pascals", "Hectopascals", "Kilopascals", "Bar"])
    value = st.number_input("Enter Value", min_value=0.0, format="%.2f")

    if st.button("Convert", key="pressure"):
        result = pressure_convertor(from_unit, to_unit, value)
        st.success(f"{value} {from_unit} = {result:.2f} {to_unit}")