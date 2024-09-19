import pandas as pd
import plotly.graph_objects as go

from trading_strategy_tester.enums.line_colors_enum import LineColor
from trading_strategy_tester.enums.source_enum import SourceType
from trading_strategy_tester.trading_plot.trading_plot import TradingPlot
from trading_strategy_tester.utils.plot_utils import set_x_axis_range, set_y_axis_range, plot_dark_mode_graph, \
    plot_light_mode_graph


class PricePlot(TradingPlot):
    def __init__(self, df: pd.DataFrame):
        """
        Initialize the PricePlot class.

        :param df: DataFrame containing the price data with 'Close', 'High', 'Low', and 'Open' columns.
        :type df: pd.DataFrame
        """
        self.df = df

    def get_plot(self, dark: bool = False) -> go.Figure:
        """
        Generate a candlestick plot based on the given price data.

        :param dark: A boolean flag indicating whether the plot should have a dark background or not.
        :type dark: bool
        :return: A plotly Figure object representing the candlestick chart.
        :rtype: go.Figure
        """
        # Create a candlestick chart
        candlestick = go.Candlestick(
            x=self.df.index,  # X-axis: date/time or index
            open=self.df['Open'],  # Opening price
            high=self.df['High'],  # Highest price
            low=self.df['Low'],  # Lowest price
            close=self.df['Close'],  # Closing price
            increasing_line_color=LineColor.GREEN.value,  # Color for increasing candles
            decreasing_line_color=LineColor.RED.value  # Color for decreasing candles
        )

        # Initialize the figure
        fig = go.Figure(data=[candlestick])

        # Set the x-axis range
        set_x_axis_range(fig, self.df[SourceType.CLOSE.value])

        # Set the y-axis range based on the two series
        set_y_axis_range(fig, self.df[SourceType.HIGH.value], self.df[SourceType.LOW.value])

        # Define the plot title
        title = "Price"

        # Apply dark or light theme based on the dark flag
        if dark:
            plot_dark_mode_graph(fig, title)
        else:
            plot_light_mode_graph(fig, title)

        return fig


    def shift(self, days_to_shift: int):
        pass