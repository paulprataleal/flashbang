## 1. Description of the Problem

This notebook focuses on short-term forecasting of hourly electricity consumption using historical energy data from a household setting.

### 1.1. Description of the Dataset

**Context**: Measurements of electric power consumption in one household with a one-minute sampling rate over a period of almost 4 years. Different electrical quantities and some sub-metering values are available.

#### Data Set Information:

This archive contains 2,075,259 measurements gathered between December 2006 and November 2010 (47 months).

#### Notes:
1. $global\_active\_power \times \frac{1000}{60} - sub\_metering_1 - sub\_metering_2 - sub\_metering_3$ represents the active energy consumed every minute (in watt-hour) in the household by electrical equipment not measured in sub-meterings 1, 2 and 3.

2. The dataset contains some missing values in the measurements (nearly 1,25% of the rows). All calendar timestamps are present in the dataset but for some timestamps, the measurement values are missing. For instance, the dataset shows missing values on April 28, 2007.

#### Attributes Information:
1. `date`: date in format *dd/mm/yyyy*
2. `time`: time in format *hh:mm:ss*
3. `global_active_power`: household global minute-averaged active power (in kilowatt)
4. `global_reactive_power`: household global minute-averaged reactive power (in kilowatt)
5. `voltage`: minute-averaged voltage (in volt)
6. `global_intensity`: household global minute-averaged current intensity (in ampere)
7. `sub_metering_1`: energy sub-metering No. 1 (in watt-hour of active energy). It corresponds to the kitchen, containing mainly a dishwasher, an oven and a microwave (hot plates are not electric but gas powered).
8. `sub_metering_2`: energy sub-metering No. 2 (in watt-hour of active energy). It corresponds to the laundry room, containing a washing-machine, a tumble-drier, a refrigerator and a light.
9. `sub_metering_3`: energy sub-metering No. 3 (in watt-hour of active energy). It corresponds to an electric water-heater and an air-conditioner.

Raw power values (kW) are converted into energy consumption (kWh) to ensure consistency with standard energy metrics. Missing values are handled through interpolation, and temporal features are extracted from the datetime index

#### Data Online Repository
* *https://www.kaggle.com/datasets/uciml/electric-power-consumption-data-set/data*

---
### 1.2. Our Work 

#### Objective

The main objective is to forecast electricity consumption one hour ahead, using only information that would realistically be available at prediction time. The analysis emphasizes avoiding data leakage and ensuring proper temporal validation.

#### Models and Baselines

To assess model performance, several approaches are compared:

* **Random Walk (Persistence) baseline**: assumes next-hour consumption equals the previous hour.
* **Seasonal Naive Baseline**: uses consumption from the same hour in the previous year.
* **SARIMA (Seasonal ARIMA)**: A classical statistical time series model that explicitly models autocorrelation, trends, and seasonal patterns. SARIMA serves as a strong linear baseline and a reference for traditional forecasting approaches.
* **XGBoost Regressor**: a tree-based gradient boosting model using lagged consumption values and calendar-based features.
* **LSTM (Long Short-Term Memory)**: A recurrent neural network designed to model sequential dependencies and non-linear temporal dynamics. LSTM is used to capture complex patterns in consumption behavior over time.

Baselines provide a reference point to evaluate whether more complex models truly capture predictive signal beyond simple heuristics.

#### Evaluation

Model performance is evaluated on a held-out test set using standard regression metrics:
* Mean Absolute Error (MAE)
* Root Mean Squared Error (RMSE)
* Mean Absolute Percentage Error (MAPE)

Visual comparisons are also used to assess how well each model captures daily consumption patterns and short-term dynamics.
