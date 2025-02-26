import streamlit as st

# Define unit categories, their units, and icons
categories = {
    '📏 Length': ['Kilometer', 'Meter', 'Centimeter', 'Millimeter', 'Mile', 'Yard', 'Foot', 'Inch'],
    '🏞️ Area': ['Square Kilometer', 'Square Meter', 'Square Mile', 'Square Yard', 'Square Foot', 'Square Inch', 'Hectare', 'Acre'],
    '📶 Data Transfer Rate': ['Bit per second', 'Kilobit per second', 'Megabit per second', 'Gigabit per second', 
                             'Byte per second', 'Kilobyte per second', 'Megabyte per second', 'Gigabyte per second'],
    '💾 Digital Storage': ['Bit', 'Byte', 'Kilobyte', 'Megabyte', 'Gigabyte', 'Terabyte', 'Petabyte'],
    '⚡ Energy': ['Joule', 'Kilojoule', 'Calorie', 'Kilocalorie', 'Watt-hour', 'Kilowatt-hour', 'Electron volt'],
    '📡 Frequency': ['Hertz', 'Kilohertz', 'Megahertz', 'Gigahertz'],
    '⛽ Fuel Economy': ['Miles per gallon', 'Kilometers per liter', 'Liters per 100 kilometers', 'Miles per liter'],
    '⚖️ Mass': ['Tonne', 'Kilogram', 'Gram', 'Milligram', 'Pound', 'Ounce'],
    '📐 Plane Angle': ['Degree', 'Radian', 'Gradian', 'Milliradian'],
    '🌡️ Pressure': ['Pascal', 'Kilopascal', 'Bar', 'PSI', 'Atmosphere', 'Millimeter of mercury'],
    '🚀 Speed': ['Meter per second', 'Kilometer per hour', 'Mile per hour', 'Knot', 'Foot per second'],
    '🌡️ Temperature': ['Celsius', 'Fahrenheit', 'Kelvin'],
    '⏰ Time': ['Second', 'Minute', 'Hour', 'Day', 'Week', 'Month', 'Year'],
    '🧪 Volume': ['Cubic meter', 'Liter', 'Milliliter', 'Gallon', 'Quart', 'Pint', 'Cup', 'Fluid ounce', 'Cubic foot', 'Cubic inch']
}

# Conversion functions for each category
def convert_length(value, from_unit, to_unit):
    conversions = {
        'Kilometer': 1000,
        'Meter': 1,
        'Centimeter': 0.01,
        'Millimeter': 0.001,
        'Mile': 1609.34,
        'Yard': 0.9144,
        'Foot': 0.3048,
        'Inch': 0.0254
    }
    return value * conversions[from_unit] / conversions[to_unit]

def convert_area(value, from_unit, to_unit):
    conversions = {
        'Square Kilometer': 1e6,
        'Square Meter': 1,
        'Square Mile': 2.59e6,
        'Square Yard': 0.836127,
        'Square Foot': 0.092903,
        'Square Inch': 0.00064516,
        'Hectare': 10000,
        'Acre': 4046.86
    }
    return value * conversions[from_unit] / conversions[to_unit]

def convert_data_transfer_rate(value, from_unit, to_unit):
    conversions = {
        'Bit per second': 1,
        'Kilobit per second': 1e3,
        'Megabit per second': 1e6,
        'Gigabit per second': 1e9,
        'Byte per second': 8,
        'Kilobyte per second': 8e3,
        'Megabyte per second': 8e6,
        'Gigabyte per second': 8e9
    }
    return value * conversions[from_unit] / conversions[to_unit]

def convert_digital_storage(value, from_unit, to_unit):
    conversions = {
        'Bit': 1,
        'Byte': 8,
        'Kilobyte': 8e3,
        'Megabyte': 8e6,
        'Gigabyte': 8e9,
        'Terabyte': 8e12,
        'Petabyte': 8e15
    }
    return value * conversions[from_unit] / conversions[to_unit]

def convert_energy(value, from_unit, to_unit):
    conversions = {
        'Joule': 1,
        'Kilojoule': 1e3,
        'Calorie': 4.184,
        'Kilocalorie': 4184,
        'Watt-hour': 3600,
        'Kilowatt-hour': 3.6e6,
        'Electron volt': 1.60218e-19
    }
    return value * conversions[from_unit] / conversions[to_unit]

def convert_frequency(value, from_unit, to_unit):
    conversions = {
        'Hertz': 1,
        'Kilohertz': 1e3,
        'Megahertz': 1e6,
        'Gigahertz': 1e9
    }
    return value * conversions[from_unit] / conversions[to_unit]

def convert_fuel_economy(value, from_unit, to_unit):
    conversions = {
        'Miles per gallon': 1,
        'Kilometers per liter': 2.35215,
        'Liters per 100 kilometers': 235.215,
        'Miles per liter': 0.425144
    }
    return value * conversions[from_unit] / conversions[to_unit]

def convert_mass(value, from_unit, to_unit):
    conversions = {
        'Tonne': 1000,
        'Kilogram': 1,
        'Gram': 0.001,
        'Milligram': 1e-6,
        'Pound': 0.453592,
        'Ounce': 0.0283495
    }
    return value * conversions[from_unit] / conversions[to_unit]

def convert_plane_angle(value, from_unit, to_unit):
    conversions = {
        'Degree': 1,
        'Radian': 57.2958,
        'Gradian': 0.9,
        'Milliradian': 0.0572958
    }
    return value * conversions[from_unit] / conversions[to_unit]

def convert_pressure(value, from_unit, to_unit):
    conversions = {
        'Pascal': 1,
        'Kilopascal': 1e3,
        'Bar': 1e5,
        'PSI': 6894.76,
        'Atmosphere': 101325,
        'Millimeter of mercury': 133.322
    }
    return value * conversions[from_unit] / conversions[to_unit]

def convert_speed(value, from_unit, to_unit):
    conversions = {
        'Meter per second': 1,
        'Kilometer per hour': 0.277778,
        'Mile per hour': 0.44704,
        'Knot': 0.514444,
        'Foot per second': 0.3048
    }
    return value * conversions[from_unit] / conversions[to_unit]

def convert_temperature(value, from_unit, to_unit):
    if from_unit == to_unit:
        return value
    if from_unit == 'Celsius':
        if to_unit == 'Fahrenheit':
            return (value * 9/5) + 32
        elif to_unit == 'Kelvin':
            return value + 273.15
    elif from_unit == 'Fahrenheit':
        if to_unit == 'Celsius':
            return (value - 32) * 5/9
        elif to_unit == 'Kelvin':
            return (value - 32) * 5/9 + 273.15
    elif from_unit == 'Kelvin':
        if to_unit == 'Celsius':
            return value - 273.15
        elif to_unit == 'Fahrenheit':
            return (value - 273.15) * 9/5 + 32
    return value

def convert_time(value, from_unit, to_unit):
    conversions = {
        'Second': 1,
        'Minute': 60,
        'Hour': 3600,
        'Day': 86400,
        'Week': 604800,
        'Month': 2.628e6,
        'Year': 3.154e7
    }
    return value * conversions[from_unit] / conversions[to_unit]

def convert_volume(value, from_unit, to_unit):
    conversions = {
        'Cubic meter': 1,
        'Liter': 0.001,
        'Milliliter': 1e-6,
        'Gallon': 0.00378541,
        'Quart': 0.000946353,
        'Pint': 0.000473176,
        'Cup': 0.000236588,
        'Fluid ounce': 2.95735e-5,
        'Cubic foot': 0.0283168,
        'Cubic inch': 1.63871e-5
    }
    return value * conversions[from_unit] / conversions[to_unit]

# Main conversion function
def convert_units(value, from_unit, to_unit, category):
    if 'Length' in category:
        return convert_length(value, from_unit, to_unit)
    elif 'Area' in category:
        return convert_area(value, from_unit, to_unit)
    elif 'Data Transfer Rate' in category:
        return convert_data_transfer_rate(value, from_unit, to_unit)
    elif 'Digital Storage' in category:
        return convert_digital_storage(value, from_unit, to_unit)
    elif 'Energy' in category:
        return convert_energy(value, from_unit, to_unit)
    elif 'Frequency' in category:
        return convert_frequency(value, from_unit, to_unit)
    elif 'Fuel Economy' in category:
        return convert_fuel_economy(value, from_unit, to_unit)
    elif 'Mass' in category:
        return convert_mass(value, from_unit, to_unit)
    elif 'Plane Angle' in category:
        return convert_plane_angle(value, from_unit, to_unit)
    elif 'Pressure' in category:
        return convert_pressure(value, from_unit, to_unit)
    elif 'Speed' in category:
        return convert_speed(value, from_unit, to_unit)
    elif 'Temperature' in category:
        return convert_temperature(value, from_unit, to_unit)
    elif 'Time' in category:
        return convert_time(value, from_unit, to_unit)
    elif 'Volume' in category:
        return convert_volume(value, from_unit, to_unit)
    else:
        return value

# Sidebar for developer information
st.sidebar.title("Developer Information")
image_path = "D:/Learning/python/q3/unit-conversion/pics.jpg"

st.sidebar.markdown("""
Name: Muhammad Adnan  
Email: dononlineboss@gmail.com  
Mobile: 0321-2121147
LinkedIn: https://www.linkedin.com/in/muhammad~adnan/)  
""")

st.sidebar.markdown("---")
st.sidebar.markdown("### About the App")
st.sidebar.markdown("This app allows you to convert units across various categories such as Length, Area, Temperature, and more.")


# Main app

col1, col2 = st.columns([1, 5])  # Adjust width ratio as needed

with col1:
    st.image("converter-icon.png", width=100)
with col2:
    st.title("Unit Conversion App")

# st.image("converter-icon.png", width=50)
# st.title("Unit Conversion App")
st.markdown("Welcome to the Unit Conversion App! Select a category and units to convert.")

# Dropdown to select category
category = st.selectbox("Select a Category", list(categories.keys()))

# Dropdowns to select from and to units
col1, col2 = st.columns(2)
with col1:
    from_unit = st.selectbox("From", categories[category])
with col2:
    to_unit = st.selectbox("To", categories[category])

# Input for value to convert
value = st.number_input("Enter Value", min_value=0.0, format="%f")

# Convert button
if st.button("Convert"):
    result = convert_units(value, from_unit, to_unit, category)
    st.success(f"**Result:** {value} {from_unit} = {result:.6f} {to_unit}")

# Add some styling and icons
st.markdown("---")
st.markdown("### Categories and Icons")
for cat, units in categories.items():
    st.markdown(f"**{cat}**")
    st.write(", ".join(units))

# Footer
st.markdown("---")
st.markdown("Built with ❤️ using [Streamlit](https://streamlit.io/)")