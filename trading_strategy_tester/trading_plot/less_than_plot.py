import pandas as pd
import plotly.graph_objects as go
import itertools as it

from trading_strategy_tester.enums.line_colors_enum import LineColor
from trading_strategy_tester.trading_plot.trading_plot import TradingPlot
from trading_strategy_tester.utils.plot_utils import (create_plot_series_name, add_trace_to_fig, set_x_axis_range,
                                                      set_y_axis_range, plot_light_mode_graph, plot_dark_mode_graph)


class LessThanPlot(TradingPlot):
    def __init__(self, series1: pd.Series, series2: pd.Series):
        """
        Initialize the LessThanPlot object with two series.

        :param series1: The first time series to be plotted.
        :type series1: pd.Series
        :param series2: The second time series for comparison in less-than detection.
        :type series2: pd.Series
        """
        self.series1: pd.Series = series1
        self.series2: pd.Series = series2
        self.number_of_days = 0


    def get_plot(self, dark: bool = True) -> go.Figure:
        """
        Generate a Plotly plot comparing two series and highlighting portions where series1 is less than series2.
        This plot will also allow the option of dark mode styling.

        :param dark: If True, the plot will use a dark theme. Defaults to True.
        :type dark: bool
        :return: A Plotly Figure object representing the LessThan plot.
        :rtype: go.Figure
        """
        # Create the Plotly figure
        fig = go.Figure()

        # Add the first series (series1)
        series1_name = create_plot_series_name(str(self.series1.name))
        add_trace_to_fig(fig, x=self.series1.index, y=self.series1, name=series1_name, color=LineColor.YELLOW)

        # Add the second series (series2)
        series2_name = create_plot_series_name(str(self.series2.name))
        add_trace_to_fig(fig, x=self.series2.index, y=self.series2, name=series2_name, color=LineColor.LIGHT_BLUE)

        # Highlight parts where series1 is less than series2
        bool_colors: pd.Series = self.series1 < self.series2
        colors = bool_colors.replace({True: LineColor.RED.value, False: LineColor.TRANSPARENT.value})

        # Create sequences of x and y values for the line segments
        x_pairs = it.pairwise(self.series1.index)
        y_pairs = it.pairwise(self.series1)

        # Add line segments with custom colors based on comparison result
        for x, y, color in zip(x_pairs, y_pairs, colors):
            fig.add_trace(go.Scatter(
                x=x,
                y=y,
                mode='lines',
                line=dict(color=color),
                showlegend=False,
                hoverinfo='none'
            ))

        # Set the x-axis range
        set_x_axis_range(fig, self.series1)

        # Set the y-axis range based on the two series
        set_y_axis_range(fig, self.series1, self.series2)

        # Define the plot title
        title = f"{series1_name} and {series2_name} LessThan Plot Shifted" if self.number_of_days > 0 else f"{series1_name} and {series2_name} LessThan Plot"

        # Apply dark or light theme based on the dark flag
        if dark:
            plot_dark_mode_graph(fig, title)
        else:
            plot_light_mode_graph(fig, title)

        return fig


    def shift(self, number_of_days: int):
        """
        Shifts both series (series1 and series2) by a specified number of days.

        :param number_of_days: The number of days to shift the series by. If the number is within
                               the valid range (0 to len(series1)), the series will be shifted.
        :type number_of_days: int
        """
        # Ensure the number_of_days is within the valid range before shifting
        if 0 <= number_of_days < len(self.series1):
            self.number_of_days = number_of_days

        # Shift both series1 and series2 by the specified number of days if number_of_days is positive
        if self.number_of_days > 0:
            self.series1 = self.series1.shift(self.number_of_days)
            self.series2 = self.series2.shift(self.number_of_days)
