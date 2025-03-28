import pandas as pd
import plotly.graph_objects as go

from trading_strategy_tester.enums.line_colors_enum import LineColor
from trading_strategy_tester.trading_plot.trading_plot import TradingPlot
from trading_strategy_tester.utils.plot_utils import (create_plot_series_name, add_trace_to_fig, set_x_axis_range,
                                                      set_y_axis_range, plot_light_mode_graph, plot_dark_mode_graph)

class DowntrendPlot(TradingPlot):
    def __init__(self, series: pd.Series, number_of_days: int):
        """
        Initializes the DowntrendPlot with the given series and number of days.

        :param series: The data series to be plotted.
        :type series: pd.Series
        :param number_of_days: The minimum number of consecutive days to consider as an downtrend.
        :type number_of_days: int
        """
        self.series = series
        self.number_of_days = number_of_days
        self.days_to_shift = 0

    def get_plot(self, dark: bool) -> go.Figure:
        """
        Creates a plotly figure that includes the series plot and highlights downtrend areas
        where the trend is downward for at least 'number_of_days'.

        :param dark: Boolean indicating whether to use dark mode for the plot.
        :type dark: bool
        :return: The plotly figure.
        :rtype: go.Figure
        """
        # Create plotly figure
        fig = go.Figure()

        # Add the series
        series_title, series_name = create_plot_series_name(str(self.series.name))
        add_trace_to_fig(fig, x=self.series.index, y=self.series, name=series_name, color=LineColor.LIGHT_BLUE)

        # Identify downtrend regions where the trend is downward for at least 'number_of_days'
        downtrend_regions = self._identify_downtrend_regions()

        # Add red rectangles to highlight downtrend regions
        for region in downtrend_regions:
            fig.add_shape(
                type="rect",
                x0=self.series.index[region[0]],  # Start of the downtrend
                x1=self.series.index[region[1]],  # End of the downtrend
                y0=self.series.min(),  # Lower boundary of the rectangle (e.g., min value of series)
                y1=self.series.max(),  # Upper boundary of the rectangle (e.g., max value of series)
                fillcolor=LineColor.RED.value,
                opacity=0.3,
                line_width=0
            )

        # Set range of x-axis
        set_x_axis_range(fig, self.series)

        # Set range of y-axis
        set_y_axis_range(fig, self.series, self.series)

        title = f'{series_title} Downtrend Plot Shifted' if self.days_to_shift > 0 else f'{series_title} Downtrend Plot'

        if dark:
            plot_dark_mode_graph(fig, title)
        else:
            plot_light_mode_graph(fig, title)

        return fig


    def shift(self, days_to_shift: int):
        """
        Shifts both series by a specified number of days.

        :param days_to_shift: The number of days to shift the series by. If the number is within
                               the valid range (0 to len(series)), the series will be shifted.
        :type days_to_shift: int
        """
        # Ensure the number_of_days is within the valid range before shifting
        if 0 <= days_to_shift < len(self.series):
            self.days_to_shift = days_to_shift

        # Shift series by the specified number of days if number_of_days is positive
        if self.days_to_shift > 0:
            self.series = self.series.shift(self.days_to_shift)


    def _identify_downtrend_regions(self):
        """
        Identifies regions where the series is in a downtrend for at least 'number_of_days'.

        :return: A list of tuples, where each tuple contains the start and end indices of a downtrend region.
        :rtype: list[tuple[int, int]]
        """
        downtrend_regions = []
        start = None

        # Iterate over the series and check for downtrends
        for i in range(1, len(self.series)):
            if self.series.iloc[i] <= self.series.iloc[i - 1]:
                if start is None:
                    start = i - 1  # Start of a downtrend
            else:
                if start is not None and (i - start) >= self.number_of_days:
                    downtrend_regions.append((start, i - 1))
                start = None  # Reset start after a downtrend ends

        # Check if the series ended in a downtrend
        if start is not None and (len(self.series) - start) >= self.number_of_days:
            downtrend_regions.append((start, len(self.series) - 1))

        return downtrend_regions
