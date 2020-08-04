import pandas as pd
import matplotlib.pyplot as plt
from scipy.stats import linregress


def draw_plot():
    # Read data from file
    df = pd.read_csv("sea-level-predictor/epa-sea-level.csv")

    # Create scatter plot
    fig, ax = plt.subplots(figsize=(10, 10))

    ax.scatter(df["Year"], df["CSIRO Adjusted Sea Level"])

    # Create first line of best fit
    slope1, intercept1, _, _, _ = linregress(df["Year"], df["CSIRO Adjusted Sea Level"])

    date_range1 = range(df["Year"].min(), 2050)
    prediction1 = [intercept1 + slope1 * x for x in date_range1]

    ax.plot(date_range1, prediction1, color="red", label="Best fitted line")

    # Create second line of best fit
    df_subset = df.copy()[df["Year"] >= 2000]

    slope2, intercept2, _, _, _ = linregress(
        df_subset["Year"], df_subset["CSIRO Adjusted Sea Level"]
    )

    date_range2 = range(2000, 2050)
    prediction2 = [intercept2 + slope2 * x for x in date_range2]

    ax.plot(date_range2, prediction2, color="green", label="2nd best fitted line")

    # Add labels and title
    ax.set(
        xlabel="Year", ylabel="Sea Level (inches)", title="Rise in Sea Level",
    )
    ax.legend()

    # Save plot and return data for testing (DO NOT MODIFY)
    plt.savefig("sea-level-predictor/sea_level_plot.png")
    return plt.gca()
