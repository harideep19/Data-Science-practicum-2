


Forecasting Cryptocurrency Prices Using ARIMA and LSTM

Overview

This project focuses on forecasting Bitcoin prices using two different approach's ARIMA and LSTM. The main goal of the project is to compare their performances and evaluate their performances using metrics to understand which model is capturing both Trend and sudden changes 

Dataset

Source        - Binance API
Data type     - 1 miniute interval
Duration      - 60 days
Features used - Open, High , Low , close

Data preprocessing

Data was converted to appropriated formats and made data readable by converting UNIX timestamps to datetime formate
Removed unnecessary columns and checked for missing values

Exploratory Data Analysis

Analyzed Trends by price trends and rolling mean and standard deviation and visualized fluctuations 
Observed the Non-stationary Data
Time series decomposition (trend, seasonality, residuals)



Models Used

 ARIMA Model
Applied first order differencing to make the data suitable for model
Parameter selection using ACF and PACF analysis
Hyperparameter Tuning selected Best final model ARIMA(0,1,0)
Captured flat line which is predicting same observed value
Limitation: Cannot capture sudden price changes


LSTM Model
Sequence-based deep learning model
Input as 60 time steps
Architecture:
used 2 LSTM layers with 50 units each and dropout of 0.2 and a Dense output layer
Model trained on Adam optimizer with MSE loss function 

Model Evaluation

Model	
ARIMA	
MAE	RMSE	MAPE - 466.92	577.49	0.70%
LSTM	
MAE	RMSE	MAPE - 64.41	94.64	0.09%


Conclusion

LSTM outperforms ARIMA for cryptocurrency forecasting due to its ability to capture complex patterns and volatility. ARIMA works well as a baseline but is limited for real-time dynamic data.
