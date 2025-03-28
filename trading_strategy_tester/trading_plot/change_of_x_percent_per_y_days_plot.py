import pandas as pd
from plotly import graph_objects as go

from trading_strategy_tester.enums.line_colors_enum import LineColor
from trading_strategy_tester.trading_plot.trading_plot import TradingPlot
from trading_strategy_tester.utils.plot_utils import (
    create_plot_series_name,
    add_trace_to_fig,
    set_x_axis_range,
    set_y_axis_range,
    plot_dark_mode_graph,
    plot_light_mode_graph
)


class ChangeOfXPercentPerYDaysPlot(TradingPlot):
    def __init__(self, series: pd.Series, percent: float, number_of_days: int):
        """
        Initialize the ChangeOfXPercentPerYDaysPlot with a series, percentage change, and number of days.

        :param series: The pandas Series containing the data to plot.
        :type series: pd.Series
        :param percent: The percentage change to highlight in the plot.
        :type percent: float
        :param number_of_days: The number of days over which to calculate the change.
        :type number_of_days: int
        """
        self.series = series
        self.percent = percent
        self.number_of_days = number_of_days
        self.days_to_shift = 0

    def get_plot(self, dark: bool = True) -> go.Figure:
        """
        Generate a Plotly figure showing the series with highlighted regions where the percentage change meets the specified criteria.

        :param dark: If True, apply a dark mode theme to the plot. Defaults to True.
        :type dark: bool
        :return: A Plotly Figure object with the plot.
        :rtype: go.Figure
        """
        # Create a Plotly figure
        fig = go.Figure()

        # Add the series to the plot
        series_title, series_name = create_plot_series_name(str(self.series.name))
        add_trace_to_fig(fig, x=self.series.index, y=self.series, name=series_name, color=LineColor.ORANGE)

        # Identify regions where the percentage change meets the criteria
        change_regions = self._identify_change_regions()

        # Add rectangles to highlight the uptrend or downtrend regions
        for region in change_regions:
            fig.add_shape(
                type="rect",
                x0=self.series.index[region[0]],
                x1=self.series.index[region[1]],
                y0=self.series.iloc[region[0]],
                y1=self.series.iloc[region[1]],
                line=dict(color=LineColor.RED.value if self.percent < 0 else LineColor.GREEN.value),
                fillcolor=LineColor.RED.value if self.percent < 0 else LineColor.GREEN.value,
                opacity=0.3
            )

        # Set the range of the x-axis based on the series
        set_x_axis_range(fig, self.series)

        # Set the range of the y-axis based on the series
        set_y_axis_range(fig, self.series, self.series)

        # Set the title of the plot
        title = f'{series_title} Change of {self.percent}% per {self.number_of_days} {'tick' if self.number_of_days == 1 else 'ticks'} Shifted' \
            if self.days_to_shift > 0 else \
            f'{series_title} Change of {self.percent}% per {self.number_of_days} {'tick' if self.number_of_days == 1 else 'ticks'}'

        # Apply dark or light mode theme based on parameter
        if dark:
            plot_dark_mode_graph(fig, title)
        else:
            plot_light_mode_graph(fig, title)

        return fig

    def shift(self, days_to_shift: int):
        """
        Shift the series by a specified number of days.

        :param days_to_shift: The number of days to shift the series by. The shift is applied if the number is within the valid range.
        :type days_to_shift: int
        """
        # Ensure the number of days is within the valid range before shifting
        if 0 <= days_to_shift < len(self.series):
            self.days_to_shift = days_to_shift

        # Shift the series if days_to_shift is positive
        if self.days_to_shift > 0:
            self.series = self.series.shift(self.days_to_shift)

    def _identify_change_regions(self):
        """
        Identify regions where the percentage change in the series meets the specified criteria.

        :return: A list of tuples where each tuple contains the start and end indices of a region with the specified percentage change.
        :rtype: list of tuples
        """
        # Shift the series by the specified number of days
        series_shifted_by_number_of_days = self.series.shift(self.number_of_days)

        # Calculate percentage change
        percent_change = (100 * self.series / series_shifted_by_number_of_days) - 100
        result = pd.Series([False] * len(self.series))

        # Create True intervals where the percentage change meets the criteria
        for i in range(len(self.series)):
            if 0 < self.percent <= percent_change.iloc[i]:
                result[i - self.number_of_days: i + 1] = True
            elif 0 > self.percent >= percent_change.iloc[i]:
                result[i - self.number_of_days: i + 1] = True

        # Initialize an empty list to store the result tuples
        changes = []
        start = None

        # Loop through the series to find the start and end of True segments
        for i, value in enumerate(result):
            if value and start is None:
                # Start of a new True segment
                start = i
            elif not value and start is not None:
                # End of a True segment
                changes.append((start, i - 1))
                start = None

        # If the series ends with a True segment, add the final interval
        if start is not None:
            changes.append((start, len(result) - 1))

        return changes
