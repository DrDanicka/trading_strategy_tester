import pandas as pd
import plotly.graph_objects as go

from trading_strategy_tester.enums.line_colors_enum import LineColor
from trading_strategy_tester.enums.source_enum import SourceType
from trading_strategy_tester.trading_plot.trading_plot import TradingPlot
from trading_strategy_tester.utils.plot_utils import set_x_axis_range, set_y_axis_range, plot_dark_mode_graph, \
    plot_light_mode_graph


class PricePlot(TradingPlot):
    def __init__(self, df: pd.DataFrame, trades: list):
        """
        Initialize the PricePlot class.

        :param df: DataFrame containing the price data with 'Close', 'High', 'Low', and 'Open' columns.
        :type df: pd.DataFrame
        """
        self.df = df
        self.trades = trades

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
            open=self.df[SourceType.OPEN.value],
            high=self.df[SourceType.HIGH.value],
            low=self.df[SourceType.LOW.value],
            close=self.df[SourceType.CLOSE.value],
            increasing_line_color=LineColor.GREEN.value,  # Color for increasing candles
            decreasing_line_color=LineColor.RED.value  # Color for decreasing candles
        )

        # Initialize the figure
        fig = go.Figure(data=[candlestick])

        # Calculate average price for offset on BUYs and SELLs
        average_price = self.df[SourceType.CLOSE.value].mean()

        # Get entry dates from the trades
        buy_dates = []
        for trade in self.trades:
            buy_dates.append(trade.entry_date)

        buy_points = self.df[self.df.index.isin(buy_dates)]

        # Add BUY points to the plot
        fig.add_trace(go.Scatter(
            x=buy_points.index,
            y=buy_points[SourceType.LOW.value] - 0.05 * average_price,
            mode='markers',
            marker=dict(symbol='triangle-up', color='blue', size=12),
            name='BUY',
            hovertemplate='<b>%{customdata:.2f}</b>',
            customdata=buy_points[SourceType.OPEN.value]
        ))

        # Get entry dates from the trades
        sell_dates = []
        for trade in self.trades:
            sell_dates.append(trade.exit_date)

        sell_points = self.df[self.df.index.isin(sell_dates)]

        # Add SELL points to the plot
        fig.add_trace(go.Scatter(
            x=sell_points.index,
            y=sell_points[SourceType.HIGH.value] + 0.05 * average_price,
            mode='markers',
            marker=dict(symbol='triangle-down', color='orange', size=12),
            name='SELL',
            hovertemplate='<b>%{customdata:.2f}</b>',
            customdata=sell_points[SourceType.OPEN.value]
        ))

        # Determine volume bar colors based on whether the Close price increased or decreased
        volume_colors = [
            LineColor.GREEN.value if self.df[SourceType.CLOSE.value].iloc[i] >= self.df[SourceType.OPEN.value].iloc[i]
            else LineColor.RED.value for i in range(len(self.df))
        ]

        # Add volume bars as a secondary y-axis
        fig.add_trace(go.Bar(
            x=self.df.index,
            y=self.df['Volume'],
            name='Volume',
            marker=dict(color=volume_colors),  # Use the dynamically set colors
            yaxis='y2',  # Plot on secondary y-axis
            opacity=0.2  # Make the bars slightly transparent
        ))

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

        # Update the layout to add a secondary y-axis for volume
        fig.update_layout(
            yaxis2=dict(
                title="Volume",
                overlaying='y',  # Overlaying the same x-axis
                side='right',  # Volume axis on the right side
                showgrid=False
            ),
            yaxis=dict(title="Price")
        )

        return fig


    def shift(self, days_to_shift: int):
        pass