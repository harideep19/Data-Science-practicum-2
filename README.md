


Forecasting Cryptocurrency Prices Using ARIMA and LSTM

| Section | Content |
|---|---|
| 1 | Data Loading & Preprocessing |
| 2 | Exploratory Data Analysis |
| 3 | Feature Engineering |
| 4 | Train / Test Split |
| 5 | Evaluation Utilities |
| 6 | Model 1 — ARIMA |
| 7 | Model 2 — Prophet |
| 8 | Model 3 — LSTM Univariate |
| 9 | Model 4 — LSTM Multivariate |
| 10 | Model 5 — Hybrid ARIMA + LSTM |
| 11 | Walk-Forward Cross-Validation |
| 12 | Multi-Horizon Forecast Analysis |
| 13 | LSTM with 3-Hour Context Window |
| 14 | Multi-Day Forecast Evaluation (2 / 5 / 10 / 15 days) |
| 15 | Cross-Market Analysis — Gold, NASDAQ & DXY |
| 16 | Final Comparison & Conclusions |

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


| Model | MAE ($) | RMSE ($) | MAPE (%) | Directional Accuracy (%) |
|---|---:|---:|---:|---:|
| ARIMA(2,1,2) | 30.18 | 46.46 | 0.0433 | 49.6 |
| Prophet | 8897.93 | 10155.09 | 13.0135 | 50.1 |
| LSTM Univariate | 64.52 | 96.26 | 0.0928 | 48.3 |
| LSTM Multivariate | 68.91 | 103.54 | 0.0990 | 48.8 |
| Hybrid ARIMA + LSTM | 30.21 | 46.48 | 0.0433 | 49.6 |

Additional Analysis

Walk-Forward Cross-Validation

Walk-forward cross-validation was used to test the stability of the ARIMA model.

| Fold | MAE ($) |
|---|---:|
| Fold 1 | 37.28 |
| Fold 2 | 31.24 |
| Fold 3 | 30.75 |
| Fold 4 | 26.80 |
Arima performance is improved from fold 1 to fold 4
### Multi-Horizon Forecasting

ARIMA and LSTM were also tested at multiple forecast horizons.

| Model | 1 Min | 5 Min | 10 Min | 30 Min |
|---|---:|---:|---:|---:|
| ARIMA(2,1,2) | 32.96 | 72.76 | 100.35 | 166.10 |
| LSTM Univariate | 69.36 | 87.18 | 126.28 | 215.81 |



### Cross-Market Analysis

The project also included cross-market analysis using:

- Gold
- NASDAQ
- U.S. Dollar Index

NASDAQ showed a strong positive relationship with bitcoin daily returns
The multi-market LSTM analysis improved the BTC prediction by reducing 6.8% MAE compared with
the BTC-Only LSTM


Conclusion

This project compares five forecasting models for bitcoin price prediction and ARIMA(2,1,2) results lower error values among all other models also Multi-Horizon analysis shows as horizon increases error values are increasing.External market indicators improves bitcoin predictions compared with BTC only LSTM






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
-  Prophet model training
- LSTM univariate model training
- LSTM multivariate model training
- Hybrid model
- Additional analysis(walk-forawd cross validation, Multi Horizon Forecast analysis, LSTM 3-Hour window , Multi-day forecast analysis and multi-market analysis)
- Model evaluation
- Results
