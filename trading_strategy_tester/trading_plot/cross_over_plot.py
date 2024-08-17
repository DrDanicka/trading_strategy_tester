import pandas as pd
import plotly.graph_objects as go
from trading_strategy_tester.trading_plot.trading_plot import TradingPlot


class CrossOverPlot(TradingPlot):
    def __init__(self, series1 : pd.Series, series2 : pd.Series):
        self.series1 = series1
        self.series2 = series2

    def get_plot(self) -> go.Figure:
        """
        Generate an interactive plot showing the crossover points between two time series.

        The function creates an interactive plot with zooming and panning capabilities, marking the crossover points
        between the two series with cross markers.

        Parameters:
        -----------
        series1 : pd.Series
            The first time series to be plotted. This could be a price series, moving average, etc.
        series2 : pd.Series
            The second time series to be plotted. This should be of the same length and aligned with series1.

        Returns:
        --------
        go.Figure
            A Plotly Figure object representing the crossover plot.
        """

        # Find crossover points
        crossover_points = (self.series1 > self.series2) & (self.series1.shift(1) < self.series2.shift(1))

        # Create the plotly figure
        fig = go.Figure()

        # Add series1 to the plot
        fig.add_trace(go.Scatter(x=self.series1.index, y=self.series1, mode='lines', name=self.series1.name,
                                 line=dict(color='blue')))

        # Add series2 to the plot
        fig.add_trace(go.Scatter(x=self.series2.index, y=self.series2, mode='lines', name=self.series2.name,
                                 line=dict(color='orange')))

        # Add crossover points
        fig.add_trace(go.Scatter(x=self.series1[crossover_points].index,
                                 y=self.series1[crossover_points],
                                 mode='markers',
                                 name='Crossover',
                                 marker=dict(color='red', size=10, symbol='x')))

        # Update layout for better readability and interactivity
        fig.update_layout(
            title=f"{self.series1.name} and {self.series2.name} Crossover Plot",
            xaxis_title="Date",
            yaxis_title="Value",
            legend_title="Legend",
            hovermode="x unified",
            template="plotly_dark"
        )

        return fig