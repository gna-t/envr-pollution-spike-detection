import pandas as pd
import matplotlib.pyplot as plt


df = pd.read_csv("air_quality.csv")

if "Date" in df.columns and "PM2.5" in df.columns:
    date_column = "Date"
    pm25_column = "PM2.5"
elif "date_local" in df.columns and "arithmetic_mean_a" in df.columns:
    date_column = "date_local"
    pm25_column = "arithmetic_mean_a"
else:
    raise ValueError("CSV must contain either 'Date' and 'PM2.5' or 'date_local' and 'arithmetic_mean_a'.")

df = df[[date_column, pm25_column]].copy()
df.columns = ["Date", "PM2.5"]

df["Date"] = pd.to_datetime(df["Date"])
df = df.dropna(subset=["PM2.5"])
df = df.sort_values("Date")

threshold = df["PM2.5"].quantile(0.95)
df["Spike"] = df["PM2.5"] > threshold

spike_count = df["Spike"].sum()

print(f"PM2.5 spike threshold (95th percentile): {threshold:.2f}")
print(f"Number of spike days: {spike_count}")

df.to_csv("spikes_detected.csv", index=False)

plt.figure(figsize=(12, 6))
plt.plot(df["Date"], df["PM2.5"], color="steelblue", linewidth=1.2, label="PM2.5")
plt.scatter(
    df.loc[df["Spike"], "Date"],
    df.loc[df["Spike"], "PM2.5"],
    color="crimson",
    s=25,
    label="Spike",
)
plt.title("PM2.5 Pollution Spikes Over Time")
plt.xlabel("Date")
plt.ylabel("PM2.5")
plt.legend()
plt.tight_layout()
plt.savefig("spike_plot.png", dpi=300)
plt.show()
