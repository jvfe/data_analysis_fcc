import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import numpy as np

# Import data
df = pd.read_csv("./medical-data-visualizer/medical_examination.csv")

# Add 'overweight' column
df["overweight"] = np.where((df["weight"] / (df["height"] / 100) ** 2) > 25, 1, 0)

# Normalize data by making 0 always good and 1 always bad. If the value of 'cholestorol' or 'gluc' is 1, make the value 0. If the value is more than 1, make the value 1.
df["cholesterol"] = np.where(df["cholesterol"] == 1, 0, 1)
df["gluc"] = np.where(df["gluc"] == 1, 0, 1)

# Draw Categorical Plot
def draw_cat_plot():
    # Create DataFrame for cat plot using `pd.melt` using just the values from 'cholesterol', 'gluc', 'smoke', 'alco', 'active', and 'overweight'.
    df_cat = df.melt(
        id_vars=["id", "cardio"],
        value_vars=["active", "alco", "cholesterol", "gluc", "overweight", "smoke"],
    )

    # Draw the catplot with 'sns.catplot()'
    fig = sns.catplot(
        data=df_cat, x="variable", kind="count", hue="value", col="cardio"
    )
    fig.set(ylabel="total")

    # Do not modify the next two lines
    fig.savefig("./medical-data-visualizer/catplot.png")
    return fig.fig


# Draw Heat Map
def draw_heat_map():
    # Clean the data
    df_heat = df[
        (df["ap_lo"] <= df["ap_hi"])
        & (df["height"] >= df["height"].quantile(0.025))
        & (df["height"] <= df["height"].quantile(0.975))
        & (df["weight"] >= df["weight"].quantile(0.025))
        & (df["weight"] <= df["weight"].quantile(0.975))
    ]

    # Calculate the correlation matrix
    corr = df_heat.corr()

    # Generate a mask for the upper triangle
    mask = np.triu(corr)

    # Set up the matplotlib figure
    fig, _ = plt.subplots(figsize=(12, 12))

    # Draw the heatmap with 'sns.heatmap()'

    ax = sns.heatmap(
        corr,
        mask=mask,
        linewidths=0.1,
        annot=True,
        fmt=".1f",
        center=0,
        vmin=-0.1,
        vmax=0.25,
        square=True,
        cbar_kws={"shrink": 0.45, "format": "%.1f"},
    )

    # Do not modify the next two lines
    fig.savefig("./medical-data-visualizer/heatmap.png")
    return fig
