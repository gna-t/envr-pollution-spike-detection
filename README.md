Pollution Spike Detection
- This project analyzes air quality data to identify days where pollution levels are unusually high. It focuses on detecting spikes in PM2.5 over time.

What I did
- Loaded and cleaned an air quality dataset
- Converted dates and organized the data
- Calculated a threshold using the top 5 percent of PM2.5 values
- Marked days above this threshold as pollution spikes
- Visualized spikes on a time series graph

Tools
- Python
- pandas
- matplotlib

Files
- spike_detector.py, main script
- air_quality.csv, original dataset
- spikes_detected.csv, dataset with spike labels
- spike_plot.png, visualization of spikes

What I found
- Most PM2.5 values stayed within a lower range, but there were clusters of extreme spikes rather than evenly distributed events. A large concentration of spikes appears near Q3 of 2020, with one very high peak standing out compared to the rest.
