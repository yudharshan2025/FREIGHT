import pandas as pd
import numpy as np
from datetime import datetime, timedelta

# -----------------------------
# Configuration
# -----------------------------
START_DATE = "2021-01-01"
END_DATE = "2025-12-31"
OUTPUT_FILE = "data.csv"

np.random.seed(42)  # for reproducibility

# -----------------------------
# Generate date range
# -----------------------------
dates = pd.date_range(start=START_DATE, end=END_DATE, freq="D")

data = []

# -----------------------------
# Weather generation logic
# -----------------------------
for date in dates:
    month = date.month

    # Seasonal behavior
    if month in [3, 4, 5, 6]:  # Summer
        temperature = np.random.normal(35, 3)
        humidity = np.random.normal(50, 10)
        rainfall = max(0, np.random.normal(2, 3))
        pressure = np.random.normal(1008, 4)

    elif month in [7, 8, 9]:  # Monsoon
        temperature = np.random.normal(30, 2)
        humidity = np.random.normal(80, 8)
        rainfall = max(0, np.random.normal(15, 10))
        pressure = np.random.normal(1005, 3)

    elif month in [11, 12, 1, 2]:  # Winter
        temperature = np.random.normal(22, 3)
        humidity = np.random.normal(65, 10)
        rainfall = max(0, np.random.normal(1, 2))
        pressure = np.random.normal(1015, 4)

    else:  # Transition months (Oct)
        temperature = np.random.normal(28, 2)
        humidity = np.random.normal(60, 8)
        rainfall = max(0, np.random.normal(5, 4))
        pressure = np.random.normal(1010, 3)

    wind_speed = max(0, np.random.normal(4, 2))

    # Clamp values to realistic limits
    temperature = round(np.clip(temperature, 15, 45), 1)
    humidity = int(np.clip(humidity, 30, 95))
    pressure = int(np.clip(pressure, 990, 1025))
    wind_speed = round(np.clip(wind_speed, 0, 15), 1)
    rainfall = round(np.clip(rainfall, 0, 60), 1)

    data.append([
        date.strftime("%Y-%m-%d"),
        temperature,
        humidity,
        pressure,
        wind_speed,
        rainfall
    ])

# -----------------------------
# Create DataFrame & CSV
# -----------------------------
df = pd.DataFrame(
    data,
    columns=["date", "temperature", "humidity", "pressure", "wind_speed", "rainfall"]
)

df.to_csv(OUTPUT_FILE, index=False)

print(f"✅ Weather dataset generated: {OUTPUT_FILE}")
print(f"📊 Total records: {len(df)}")