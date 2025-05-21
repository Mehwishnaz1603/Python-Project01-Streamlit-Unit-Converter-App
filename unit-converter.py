import streamlit as st
# --- Title ---
st.title("🌐 Universal Unit Converter")

# --- Theme toggle ---
theme = st.radio("Choose Theme", ["🌞 Light", "🌙 Dark"], horizontal=True)
if theme == "🌙 Dark":
    st.markdown('<style>body, .stApp { background-color: #1e293b; color: #f8fafc !important; }</style>', unsafe_allow_html=True)

# --- Unit Dictionaries ---
length_units = {
    "Meter (m)": 1.0,
    "Kilometer (km)": 0.001,
    "Centimeter (cm)": 100.0,
    "Millimeter (mm)": 1000.0,
    "Mile (mi)": 0.000621371,
    "Yard (yd)": 1.09361,
    "Foot (ft)": 3.28084,
    "Inch (in)": 39.3701
}

weight_units = {
    "Kilogram (kg)": 1.0,
    "Gram (g)": 1000.0,
    "Milligram (mg)": 1e6,
    "Pound (lb)": 2.20462,
    "Ounce (oz)": 35.274
}

speed_units = {
    "Meter/second (m/s)": 1.0,
    "Kilometer/hour (km/h)": 3.6,
    "Miles/hour (mph)": 2.23694,
    "Foot/second (ft/s)": 3.28084,
    "Knot (kn)": 1.94384
}

temperature_units = ["Celsius", "Fahrenheit", "Kelvin"]

# --- Temperature Conversion ---
def convert_temperature(value, from_unit, to_unit):
    if from_unit == to_unit:
        return value
    if from_unit == "Fahrenheit":
        value = (value - 32) * 5/9
    elif from_unit == "Kelvin":
        value = value - 273.15
    if to_unit == "Fahrenheit":
        return (value * 9/5) + 32
    elif to_unit == "Kelvin":
        return value + 273.15
    return value

# --- UI ---
category = st.selectbox("📂 Select Conversion Category", ["Length", "Temperature", "Weight", "Speed"])
value = st.number_input("✏️ Enter Value", value=0.0, format="%.4f")

# --- Conversion Logic ---
if category == "Length":
    from_unit = st.selectbox("📤 From Unit", list(length_units.keys()))
    to_unit = st.selectbox("📥 To Unit", list(length_units.keys()))
    result = value / length_units[from_unit] * length_units[to_unit]
    st.success(f"📏 {value} {from_unit} = {result:.4f} {to_unit}")

elif category == "Weight":
    from_unit = st.selectbox("📤 From Unit", list(weight_units.keys()))
    to_unit = st.selectbox("📥 To Unit", list(weight_units.keys()))
    result = value / weight_units[from_unit] * weight_units[to_unit]
    st.success(f"⚖️ {value} {from_unit} = {result:.4f} {to_unit}")

elif category == "Speed":
    from_unit = st.selectbox("📤 From Unit", list(speed_units.keys()))
    to_unit = st.selectbox("📥 To Unit", list(speed_units.keys()))
    result = value / speed_units[from_unit] * speed_units[to_unit]
    st.success(f"🏎️ {value} {from_unit} = {result:.4f} {to_unit}")

elif category == "Temperature":
    from_unit = st.selectbox("📤 From Unit", temperature_units)
    to_unit = st.selectbox("📥 To Unit", temperature_units)
    result = convert_temperature(value, from_unit, to_unit)
    st.success(f"🌡️ {value} {from_unit} = {result:.2f} {to_unit}")

# --- App Description ---
st.markdown("""
## 📘 About This App
This is a **professional and clean Unit Converter** built with Python & Streamlit. It helps you convert values between various measurement systems.

### 🌟 Features:
- Multi-unit conversion: Length, Weight, Temperature, Speed
- Light/Dark Theme toggle 🌞🌙
- Responsive UI with Tailwind-like styling
- Accurate formulas for real-world use
- FAQ support section

""")

# --- FAQ Section ---
st.subheader("📌 Frequently Asked Questions")
faq = {
    "🔍 What can this app do?": "It can convert Length, Weight, Temperature, and Speed accurately with real-time results.",
    "💡 How do I use it?": "Select the category, enter your value, choose units, and see the converted result instantly.",
    "⚙️ Can I switch themes?": "Yes! Toggle between Light and Dark mode at the top of the page.",
    "📈 Are the results accurate?": "Absolutely. We use tested conversion factors for reliable results.",
    "🚀 Can I add more units?": "Yes, the app is modular and easily expandable to support more types like Volume, Pressure, Energy, etc."
}
for question, answer in faq.items():
    with st.expander(question):
        st.write(answer)
