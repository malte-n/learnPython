import csv
from datetime import datetime
import matplotlib.pyplot as plt


filename = "/Users/malte.niepel/Desktop/mniepel/ehmatthes-pcc_2e-078318e/chapter_16/the_csv_file_format/data/sitka_weather_2018_simple.csv"
with open(filename) as f:
    reader = csv.reader(f)
    header_row = next(reader)
    print(header_row)
    # Getting dates and high temperatures from this file.
    dates, highs, lows = [], [], []
    for row in reader:

        current_date = datetime.strptime(row[2], "%Y-%m-%d")
        high = int(row[5])
        low = int(row[6])
        dates.append(current_date)
        highs.append(high)
        lows.append(low)


# Plot the high teamperatures
plt.style.use("seaborn")
fig, ax = plt.subplots()
ax.plot(dates, highs, c="red", alpha=0.5)
ax.plot(dates, lows, c="blue", alpha=0.5)
ax.fill_between(dates, highs, lows, facecolor="black", alpha=0.2)

# Format plot
plt.title("Daily and low temperatures - 2018", fontsize=24)
plt.xlabel("", fontsize=16)
fig.autofmt_xdate()  # make the dates display in diagonal
plt.ylabel("Temperatures (F)", fontsize=16)
plt.tick_params(axis="both", which="major", labelsize=16)

plt.show()
