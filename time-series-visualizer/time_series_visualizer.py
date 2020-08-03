import matplotlib.pyplot as plt
import matplotlib.dates as mdates
from matplotlib.dates import DateFormatter
import pandas as pd
import seaborn as sns
from pandas.plotting import register_matplotlib_converters

register_matplotlib_converters()

# Import data (Make sure to parse dates. Consider setting index column to 'date'.)
df = pd.read_csv(
    "time-series-visualizer/fcc-forum-pageviews.csv",
    parse_dates=True,
    index_col="date",
)

# Clean data
df = df[
    (df["value"] >= df["value"].quantile(0.025))
    & (df["value"] <= df["value"].quantile(0.975))
]


def draw_line_plot():
    # Draw line plot
    fig, ax = plt.subplots(figsize=(18, 6))

    ax.plot(df.index.values, df["value"], color="red")

    ax.set(
        xlabel="Date",
        ylabel="Page Views",
        title="Daily freeCodeCamp Forum Page Views 5/2016-12/2019",
    )

    date_form = DateFormatter("%Y-%m")
    ax.xaxis.set_major_formatter(date_form)
    ax.xaxis.set_major_locator(mdates.MonthLocator(bymonth=[1, 7]))

    # Save image and return fig (don't change this part)
    fig.savefig("time-series-visualizer/line_plot.png")
    return fig


def draw_bar_plot():
    # Copy and modify data for monthly bar plot
    df_bar = df.copy().reset_index()

    df_bar["year"] = df_bar["date"].dt.year
    df_bar["month"] = df_bar["date"].dt.strftime("%B")

    # Draw bar plot
    month_order = [
        "January",
        "February",
        "March",
        "April",
        "May",
        "June",
        "July",
        "August",
        "September",
        "October",
        "November",
        "December",
    ]

    plot = sns.catplot(
        x="year",
        y="value",
        hue="month",
        hue_order=month_order,
        palette=sns.color_palette(),
        kind="bar",
        ci=None,
        data=df_bar,
        legend=False,
    )

    plot.set(xlabel="Years", ylabel="Average Page Views")
    plt.legend(title="Months", loc="upper left", labels=month_order)
    fig = plot.fig

    # Save image and return fig (don't change this part)
    fig.savefig("time-series-visualizer/bar_plot.png")
    return fig


def draw_box_plot():
    # Prepare data for box plots (this part is done!)
    df_box = df.copy()
    df_box.reset_index(inplace=True)
    df_box["year"] = [d.year for d in df_box.date]
    df_box["month"] = [d.strftime("%b") for d in df_box.date]

    # Draw box plots (using Seaborn)
    df_box["month_num"] = df_box["date"].dt.month
    df_box.sort_values(by=["month_num", "year"], inplace=True)

    fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(16, 8))

    ax1 = sns.boxplot(x="year", y="value", data=df_box, ax=ax1)
    ax2 = sns.boxplot(x="month", y="value", data=df_box, ax=ax2)

    ax1.set_ylabel("Page Views")
    ax2.set_ylabel("Page Views")

    ax1.set_xlabel("Year")
    ax2.set_xlabel("Month")

    ax1.set_title("Year-wise Box Plot (Trend)")
    ax2.set_title("Month-wise Box Plot (Seasonality)")

    # Save image and return fig (don't change this part)
    fig.savefig("time-series-visualizer/box_plot.png")
    return fig
