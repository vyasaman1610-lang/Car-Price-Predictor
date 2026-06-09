# 🚗 Car Price Predictor

A Machine Learning web application built with Streamlit that predicts the selling price of a used car based on various features such as year, present price, kilometers driven, fuel type, seller type, transmission type, and ownership history.

## Features

* Predicts used car selling price in lakhs (₹)
* Interactive Streamlit web interface
* Machine Learning model trained using Gradient Boosting Regressor
* Real-time price prediction
* Clean and responsive UI

## Dataset

The dataset contains information about used cars, including:

* Car Name
* Year
* Selling Price
* Present Price
* Kilometers Driven
* Fuel Type
* Seller Type
* Transmission
* Owner

## Technologies Used

* Python
* Streamlit
* NumPy
* Pandas
* Scikit-learn
* Joblib

## Installation

Clone the repository:

```bash
git clone https://github.com/your-username/car-price-predictor.git
cd car-price-predictor
```

Install dependencies:

```bash
pip install -r requirements.txt
```

Run the application:

```bash
streamlit run price_predict.py
```

## Project Structure

```text
car-price-predictor/
│
├── price_predict.py
├── model.pkl
├── requirements.txt
├── README.md
└── Car_Price_Prediction.csv
```

## Input Features

| Feature       | Description                          |
| ------------- | ------------------------------------ |
| Year          | Manufacturing year of the car        |
| Present Price | Current ex-showroom price (in lakhs) |
| Kms Driven    | Total kilometers driven              |
| Owner         | Number of previous owners            |
| Fuel Type     | Petrol, Diesel, or CNG               |
| Seller Type   | Dealer or Individual                 |
| Transmission  | Manual or Automatic                  |

## Sample Prediction

Input:

* Year: 2014
* Present Price: 6.87
* Kms Driven: 42450
* Fuel Type: Diesel
* Seller Type: Dealer
* Transmission: Manual
* Owner: 0

Output:

* Predicted Selling Price: ₹4.60 Lakhs (approx.)

## Deployment

This application can be deployed easily using Streamlit Community Cloud.

1. Push the project to GitHub.
2. Sign in to Streamlit Community Cloud.
3. Create a new app and connect your repository.
4. Select `price_predict.py` as the entry point.
5. Deploy.

## Future Improvements

* Add support for additional car brands and models.
* Implement feature importance visualization.
* Compare multiple machine learning models.
* Add data analytics dashboard.
* Improve prediction accuracy through hyperparameter tuning.

## Author

Developed as a Machine Learning project using Python, Scikit-learn, and Streamlit.
