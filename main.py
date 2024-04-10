import streamlit as st
import pandas as pd

# Load the CSV data into the DataFrame
df = pd.read_csv('car_data.csv')

# Set up the sidebar
st.sidebar.header('Personalize Your Choice')

# Text input for car name
car_name_input = st.sidebar.text_input('Car Name')

# Multiselect for Transmission type
transmission_choice = st.sidebar.multiselect('Transmission Type', ['Manual', 'Automatic'], default=['Manual', 'Automatic'])

# Slider for Selling Price range
selling_price_range = st.sidebar.slider('Selling Price Range', float(df.Selling_Price.min()), float(df.Selling_Price.max()), (0.0, 20.0))

# Slider for Year range
year_range = st.sidebar.slider('Year Range', int(df.Year.min()), int(df.Year.max()), (2000, 2024))

# Submit button to apply filters
if st.sidebar.button('Apply Filters'):
    # Filtering based on the sidebar options
    filtered_df = df
    
    # Filter by car name if input is given
    if car_name_input:
        filtered_df = filtered_df[filtered_df['Car_Name'].str.contains(car_name_input, case=False, na=False)]
    
    # Filter by Transmission
    if transmission_choice:
        filtered_df = filtered_df[df['Transmission'].isin(transmission_choice)]
    
    # Filter by Selling Price range
    filtered_df = filtered_df[(filtered_df['Selling_Price'] >= selling_price_range[0]) & (filtered_df['Selling_Price'] <= selling_price_range[1])]
    
    # Filter by Year range
    filtered_df = filtered_df[(filtered_df['Year'] >= year_range[0]) & (filtered_df['Year'] <= year_range[1])]
    
    st.write(filtered_df)
else:
    # Display original unfiltered data
    st.write(df)
