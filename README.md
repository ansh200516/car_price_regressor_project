# Car Price Predictor
This project allows users to predict the price of a car based on various features. The prediction model leverages a machine learning model to estimate the price of a car given its characteristics.
## Features
* **Manufacturer Selection**: Choose the manufacturer of the car.
* **Model Selection**: Filter available models based on the selected manufacturer.
* **Category Selection**: Filter available categories based on the selected model.
* **Leather Interior**: Choose whether the car has a leather interior.
* **Fuel Type**: Select the type of fuel used by the car.
* **Gear Box Type**: Choose the type of gear box.
* **Drive Wheels**: Select the drive wheels configuration.
* **Wheel Position**: Choose whether the steering wheel is on the left or right.
* **Color**: Select the color of the car.
* **Production Year**: Input the production year of the car.
* **Engine Volume**: Specify the engine volume in liters.
* **Mileage**: Input the mileage of the car in kilometers.
* **Cylinders**: Specify the number of cylinders.
* **Airbags**: Input the number of airbags.
* **Turbo**: Choose whether the car has a turbo.
## How It Works
1. **User Input**: The user fills in the car features in the form provided.
2. **Data Collection**: The app collects and displays the entered data.
3. **Prediction**: Upon submission, the app uses a pre-trained model (model.pkl) to predict the price based on the input features.
4. **Result Display**: The predicted price is displayed in USD, including tax.
## Live Demo
You can try the Car Price Predictor app live [Click here to try the demo](https://carpriceregreapprproject-8pee53qfopzt2f7xze7yez.streamlit.app/)
## File Structure
* app.py: Main Streamlit application script.
* data.pkl: Serialized data file used for filtering options.
* model.pkl: Serialized machine learning model used for predictions.
* requirements.txt: List of dependencies.

