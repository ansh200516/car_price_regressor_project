import streamlit as st
import pandas as pd
import pickle
data = pd.DataFrame(pickle.load(open('data.pkl', 'rb')))
st.markdown("""
    <style>
    .title {
        font-size: 36px;
        color: #FF6347;
        text-align: center;
        margin-bottom: 10px;
    }
    .subtitle {
        font-size: 24px;
        color: #4682B4;
        text-align: center;
        margin-bottom: 20px;
    }
    .form-container {
        background-color: #F0F8FF;
        padding: 20px;
        border-radius: 10px;
        margin-top: 0; /* Remove top margin */
    }
    .prediction-container {
        background-color: #FFFACD;
        padding: 20px;
        border-radius: 10px;
        margin-top: 20px;
        text-align: center;
    }
    .price-text {
        color: #32CD32; /* Set the price color to green */
        font-size: 24px;
        font-weight: bold;
    }
    .collected-input-container {
        background-color: #E6E6FA;
        padding: 20px;
        border-radius: 10px;
        margin-top: 20px;
        text-align: center;
    }
    .st-selectbox, .st-number_input {
        margin-top: 0; /* Remove top margin */
        margin-bottom: 10px; /* Adjust bottom margin as needed */
    }
    </style>
""", unsafe_allow_html=True)
st.markdown('<div class="title">Car Price Prediction</div>', unsafe_allow_html=True)
st.markdown('<div class="subtitle">Predict the price of a car based on various features</div>', unsafe_allow_html=True)
with st.form(key='car_prediction_form', clear_on_submit=True):
    st.markdown('<div class="form-container">', unsafe_allow_html=True)
    manufacturer = st.selectbox('Manufacturer', options=data['Manufacturer'].unique())
    filtered_models = data[data['Manufacturer'] == manufacturer]['Model'].unique()
    model = st.selectbox('Model', options=filtered_models)

    filtered_categories = data[(data['Manufacturer'] == manufacturer) & (data['Model'] == model)]['Category'].unique()
    category = st.selectbox('Category', options=filtered_categories)

    leather_interior = st.selectbox('Leather Interior', options=['Yes', 'No'])
    fuel_type = st.selectbox('Fuel Type', options=data['Fuel type'].unique())
    gear_box_type = st.selectbox('Gear Box Type', options=data['Gear box type'].unique())
    drive_wheels = st.selectbox('Drive Wheels', options=data['Drive wheels'].unique())
    wheel = st.selectbox('Wheel', options=['Left', 'Right'])
    color = st.selectbox('Color', options=data['Color'].unique())

    prod_year = st.number_input('Production Year', min_value=1900, max_value=2024, step=1)
    engine_volume = st.number_input('Engine Volume (L)', min_value=0.0, format="%.2f")
    mileage = st.number_input('Mileage (km)', min_value=0, step=1)
    cylinders = st.number_input('Cylinders', min_value=0, step=1)
    airbags = st.number_input('Airbags', min_value=0, step=1)

    is_turbo = st.selectbox('Turbo', options=['Yes', 'No'])
    is_turbo_value = 1 if is_turbo == 'Yes' else 0

    submit_button = st.form_submit_button(label='Get Price')

    st.markdown('</div>', unsafe_allow_html=True)


input_data = pd.DataFrame(
    [[manufacturer, model, category, leather_interior, fuel_type, gear_box_type,
      drive_wheels, wheel, color, prod_year, engine_volume, mileage, cylinders, airbags, is_turbo_value]],
    columns=['Manufacturer', 'Model', 'Category', 'Leather interior', 'Fuel type',
             'Gear box type', 'Drive wheels', 'Wheel', 'Color', 'Prod. year',
             'Engine volume', 'Mileage', 'Cylinders', 'Airbags', 'isTurbo']
)
st.markdown('<div class="collected-input-container">', unsafe_allow_html=True)
st.write('**Collected Input:**')
st.write(input_data)
st.markdown('</div>', unsafe_allow_html=True)

pipe = pickle.load(open('model.pkl', 'rb'))

if submit_button:
    prediction = pipe.predict(input_data)
    st.markdown('<div class="prediction-container">', unsafe_allow_html=True)
    st.markdown(f'**Price in USD (including Tax):** <span class="price-text">${prediction[0]:,.2f}</span>',
                unsafe_allow_html=True)
    st.markdown('</div>', unsafe_allow_html=True)
