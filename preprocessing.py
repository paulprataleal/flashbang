import numpy as np
import pandas as pd

# ----------------------------------------------------------------------------
# -------------------------- 1. Feature Engineering --------------------------
# ----------------------------------------------------------------------------

# Read the data
df = pd.read_csv("household_power_consumption.csv", sep=";", low_memory=False)

# Convert the date column into a date object
df["Date"] = pd.to_datetime(df["Date"], dayfirst=True).dt.date

# Convert the time column into a date object
df["Time"] = pd.to_datetime(df["Time"], format="%H:%M:%S").dt.time

# Convert the numeric columns into floats
for column in df.columns:
    if column not in ["Date", "Time"]:
        df[column] = pd.to_numeric(df[column], errors="coerce")

# Create a datetime column
df["Datetime"] = pd.to_datetime(df["Date"].astype(str) + " " + df["Time"].astype(str))

# Create a column for each component of the date
df["Year"] = df["Datetime"].dt.year
df["Month"] = df["Datetime"].dt.month
df["Day"] = df["Datetime"].dt.day
df["Hour"] = df["Datetime"].dt.hour
df["Minute"] = df["Datetime"].dt.minute
df["Second"] = df["Datetime"].dt.second

# Reorganise columns
order = [
    "Datetime",
    "Year",
    "Month",
    "Day",
    "Hour",
    "Minute",
    "Second",
    "Date",
    "Time",
    "Global_active_power",
    "Global_reactive_power",
    "Voltage",
    "Global_intensity",
    "Sub_metering_1",
    "Sub_metering_2",
    "Sub_metering_3",
]

df = df[order]

# Columns in lowercase
df.columns = [col.lower() for col in df.columns]

print(df.head())
