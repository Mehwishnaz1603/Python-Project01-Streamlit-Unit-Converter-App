import streamlit as st

st.set_page_config(page_title="Unit Converter", layout="centered")
st.title("🌍 Universal Unit Converter")

# --- Dictionaries for conversion rates ---
length_units = {
    "Meter": 1.0,
    "Kilometer": 0.001,
    "Centimeter": 100.0,
    "Millimeter": 1000.0,
    "Mile": 0.000621371,
    "Yard": 1.09361,
    "Foot": 3.28084,
    "Inch": 39.3701
}

weight_units = {
    "Kilogram": 1.0,
    "Gram": 1000.0,
    "Milligram": 1e6,
    "Pound": 2.20462,
    "Ounce": 35.274
}

temperature_units = ["Celsius", "Fahrenheit", "Kelvin"]

# --- Temperature conversion function ---
def convert_temperature(value, from_unit, to_unit):
    if from_unit == to_unit:
        return value

    # Convert from from_unit to Celsius
    if from_unit == "Fahrenheit":
        value = (value - 32) * 5/9
    elif from_unit == "Kelvin":
        value = value - 273.15

    # Convert from Celsius to to_unit
    if to_unit == "Fahrenheit":
        return (value * 9/5) + 32
    elif to_unit == "Kelvin":
        return value + 273.15
    return value

# --- UI Elements ---
category = st.selectbox("Select Conversion Category", ["Length", "Temperature", "Weight"])

value = st.number_input("Enter Value", value=0.0, format="%.4f")

if category == "Length":
    from_unit = st.selectbox("From Unit", list(length_units.keys()))
    to_unit = st.selectbox("To Unit", list(length_units.keys()))
    result = value / length_units[from_unit] * length_units[to_unit]
    st.success(f"{value} {from_unit} = {result:.4f} {to_unit}")

elif category == "Weight":
    from_unit = st.selectbox("From Unit", list(weight_units.keys()))
    to_unit = st.selectbox("To Unit", list(weight_units.keys()))
    result = value / weight_units[from_unit] * weight_units[to_unit]
    st.success(f"{value} {from_unit} = {result:.4f} {to_unit}")

elif category == "Temperature":
    from_unit = st.selectbox("From Unit", temperature_units)
    to_unit = st.selectbox("To Unit", temperature_units)
    result = convert_temperature(value, from_unit, to_unit)
    st.success(f"{value} {from_unit} = {result:.2f} {to_unit}")
