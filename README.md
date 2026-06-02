


Forecasting Cryptocurrency Prices Using ARIMA and LSTM

Overview

This project focuses on forecasting Bitcoin prices using two different approach's ARIMA and LSTM. The main goal of the project is to compare their performances and evaluate their performances using metrics to understand which model is capturing both Trend and sudden changes 

Dataset

- source  Binance API  
- Data type  1-minute interval Bitcoin data  
- Duration: ~60 days
- Features used  open ,high , low and valume

Data preprocessing

Data was converted to appropriated formats and made data readable by converting UNIX timestamps to datetime formate
Removed unnecessary columns and checked for missing values


Models Used

## 1. ARIMA Model


Autoregressive Integrated Moving Average(ARIMA) is a statistical model which is used for time series forecasting were model used past values and past errors for prediction.

In this project:

- First-order differencing was applied to make data stationary.
- AIC was used for model selection.
- ARIMA(2,1,2) as selected as best model based on lower AIC
- Rolling one-step-ahead forecasting was used for evaluation.

## 2. LSTM Univariate Model

LSTM is a deep learning model which designed to capture the non-linear patterns 

- Only Bitcoin close price is used as input.
- A 60-step lookback window was used.
- Since the data is one-minute interval data, 60 step window represent one hour of previous price data.
- The model used two LSTM layers.
- Adam optimizer was used.
- Mean Squared Error was used as the loss function.

## 3. LSTM Multivariate Model

The  mulitvariate LSTM model will use the multiple features by XGBoost instead of only the close price.
The input features included:

- Technical indicators
- Lag features
- Rolling mean
- Rolling standard deviation
- Return features
- Time-based features

## 4. Prophet Model

Prophet is a time series forecasting model designed to capture trend and seasonality.

In this project, Prophet did not perform well because Bitcoin one-minute data does not have clear seasonal patterns. The model produced very high error compared with ARIMA and LSTM.

##5. Hybrid ARIMA + LSTM Model

The Hybrid model combines ARIMA and LSTM.

The idea behind this model was:

- ARIMA captures the linear pattern.
- LSTM model will captures the non-linear patterns from ARIMA resuduals
- Final prediction is created by combining ARIMA prediction and LSTM residual prediction.

Model Evaluation


- Model	              MAE	      RMSE	    MAPE (%)	    Dir. Acc (%)
- ARIMA      	        30.18	    46.46	    0.0433	      49.6
- Hybrid ARIMA+LSTM	  30.21	    46.48	    0.0433	      49.6
- LSTM Univariate	    64.52	    96.26	    0.0928	      48.3
- LSTM Multivariate	  68.91	    103.54	  0.0990	      48.8
- Prophet	            8897.93	  10155.09	13.0135	      50.1

Additional Analysis

Walk-Forward Cross-Validation

Walk-forward cross-validation was used to test the stability of the ARIMA model.

| Fold | MAE ($) |
|---|---:|
| Fold 1 | 37.28 |
| Fold 2 | 31.24 |
| Fold 3 | 30.75 |
| Fold 4 | 26.80 |



Conclusion

LSTM outperforms ARIMA for cryptocurrency forecasting due to its ability to capture complex patterns and volatility. ARIMA works well as a baseline but is limited for real-time dynamic data.



How to Run

- clone repository
- git clone https://github.com/harideep19/Data-Science-practicum-2.git
- Select Notebook file
- Install Required Libraries

Run the project
Run all cells step by step to perform:
- Data preprocessing
- Exploratory Data Analysis (EDA)
- ARIMA model training
- LSTM model training
- Model evaluation
- Results
