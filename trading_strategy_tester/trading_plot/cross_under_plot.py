import pandas as pd
import plotly.graph_objects as go

from trading_strategy_tester.enums.line_colors_enum import LineColor
from trading_strategy_tester.trading_plot.trading_plot import TradingPlot
from trading_strategy_tester.utils.plot_utils import create_plot_series_name, add_trace_to_fig, plot_dark_mode_graph, \
    plot_light_mode_graph, set_x_axis_range, set_y_axis_range


class CrossUnderPlot(TradingPlot):
    def __init__(self, series1: pd.Series, series2: pd.Series):
        """
        Initialize the CrossUnderPlot object with two series.

        :param series1: The first time series (e.g., price, moving average) to be plotted.
        :type series1: pd.Series
        :param series2: The second time series, aligned with series1, for comparison in cross-under detection.
        :type series2: pd.Series
        """
        self.series1 = series1
        self.series2 = series2
        self.days_to_shift = 0


    def get_plot(self, dark: bool) -> go.Figure:
        """
        Generate an interactive Plotly plot showing the cross-under points between two time series.
        The plot will contain filled rectangles at cross-under points and have the option to be in dark mode.

        :param dark: If True, the plot will use a dark theme. Defaults to False.
        :type dark: bool
        :return: A Plotly Figure object representing the cross-under plot with filled rectangles.
        :rtype: go.Figure
        """

        # Create the plotly figure
        fig = go.Figure()

        # Add the first series (series1)
        series1_title, series1_name = create_plot_series_name(str(self.series1.name))
        add_trace_to_fig(fig, x=self.series1.index, y=self.series1, name=series1_name, color=LineColor.YELLOW)

        # Add the second series (series2)
        series2_title, series2_name = create_plot_series_name(str(self.series2.name))
        add_trace_to_fig(fig, x=self.series2.index, y=self.series2, name=series2_name, color=LineColor.PURPLE)

        # Iterate through the series to detect cross-unders and draw rectangles
        for i in range(1, len(self.series1)):
            prev_index = self.series1.index[i - 1]
            current_index = self.series1.index[i]

            prev_value1 = self.series1.iloc[i - 1]
            current_value1 = self.series1.iloc[i]
            prev_value2 = self.series2.iloc[i - 1]
            current_value2 = self.series2.iloc[i]

            # Detect a cross-under (when series1 crosses below series2)
            if prev_value1 > prev_value2 and current_value1 < current_value2:

                # Calculate the top and bottom of the rectangle (max and min values between the two series)
                top = max(current_value1, current_value2, prev_value1, prev_value2)
                bottom = min(current_value1, current_value2, prev_value1, prev_value2)

                # Create a filled rectangle for the cross-under area
                fig.add_shape(
                    type="rect",
                    x0=prev_index,
                    x1=current_index,
                    y0=bottom,
                    y1=top,
                    line=dict(color='red'),
                    fillcolor="rgba(255, 0, 0, 0.2)"
                )

        # Set range for x-axis
        set_x_axis_range(fig, self.series1)

        # Set range for y-axis
        set_y_axis_range(fig, self.series1, self.series2)

        title = f"{series1_title} and {series2_title} Cross-under Plot Shifted"\
            if self.days_to_shift > 0 else f"{series1_title} and {series2_title} Cross-under Plot"

        if dark:
            plot_dark_mode_graph(fig, title)
        else:
            plot_light_mode_graph(fig, title)

        return fig

    def shift(self, days_to_shift: int):
        """
        Shifts both series (series1 and series2) by a specified number of days.

        :param days_to_shift: The number of days to shift the series by. If the number is within
                               the valid range (0 to len(series1)), the series will be shifted.
        :type days_to_shift: int
        """
        # Ensure the number_of_days is within the valid range before shifting
        if 0 <= days_to_shift < len(self.series1):
            self.days_to_shift = days_to_shift

        # Shift both series1 and series2 by the specified number of days if number_of_days is positive
        if self.days_to_shift > 0:
            self.series1 = self.series1.shift(self.days_to_shift)
            self.series2 = self.series2.shift(self.days_to_shift)