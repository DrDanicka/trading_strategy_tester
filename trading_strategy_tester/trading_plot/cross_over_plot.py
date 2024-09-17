import pandas as pd
import plotly.graph_objects as go

from trading_strategy_tester.trading_plot.trading_plot import TradingPlot
from trading_strategy_tester.utils.plot_utils import create_plot_series_name, add_trace_to_fig, plot_dark_mode_graph, \
    plot_light_mode_graph


class CrossOverPlot(TradingPlot):
    def __init__(self, series1: pd.Series, series2: pd.Series):
        """
        Initialize the CrossOverPlot object with two series.

        :param series1: The first time series (e.g., price, moving average) to be plotted.
        :type series1: pd.Series
        :param series2: The second time series, aligned with series1, for comparison in crossover detection.
        :type series2: pd.Series
        """
        self.series1 = series1
        self.series2 = series2


    def get_plot(self, dark: bool = True) -> go.Figure:
        """
        Generate an interactive Plotly plot showing the crossover points between two time series.
        The plot will contain filled rectangles at crossover points and have the option to be in dark mode.

        :param dark: If True, the plot will use a dark theme. Defaults to False.
        :type dark: bool
        :return: A Plotly Figure object representing the crossover plot with filled rectangles.
        :rtype: go.Figure
        """

        # Create the plotly figure
        fig = go.Figure()

        # Add the first series (series1)
        series1_name = create_plot_series_name(str(self.series1.name))
        add_trace_to_fig(fig, x=self.series1.index, y=self.series1, name=series1_name)

        # Add the second series (series2)
        series2_name = create_plot_series_name(str(self.series2.name))
        add_trace_to_fig(fig, x=self.series2.index, y=self.series2, name=series2_name)

        # Iterate through the series to detect crossovers and draw rectangles
        for i in range(1, len(self.series1)):
            prev_index = self.series1.index[i - 1]
            current_index = self.series1.index[i]

            prev_value1 = self.series1.iloc[i - 1]
            current_value1 = self.series1.iloc[i]
            prev_value2 = self.series2.iloc[i - 1]
            current_value2 = self.series2.iloc[i]

            # Detect a crossover (when series1 crosses above series2 or vice versa)
            if prev_value1 < prev_value2 and current_value1 > current_value2:

                # Calculate the top and bottom of the rectangle (max and min values between the two series)
                top = max(current_value1, current_value2, prev_value1, prev_value2)
                bottom = min(current_value1, current_value2, prev_value1, prev_value2)

                # Add a filled rectangle where crossover occurred
                fig.add_shape(
                    type="rect",
                    x0=prev_index,
                    x1=current_index,
                    y0=bottom,
                    y1=top,
                    line=dict(color="red"),
                    fillcolor="rgba(255, 0, 0, 0.2)",  # Light red color with 20% opacity
                )


        # Set range on x-axis
        x_min = self.series1.index.min()
        x_max = self.series1.index.max()

        fig.update_xaxes(
            range=[x_min, x_max],
            minallowed=x_min,
            maxallowed=x_max
        )

        # Set range on y-axis
        min_value = min(self.series1.min(), self.series2.min())
        max_value = max(self.series1.max(), self.series2.max())

        y_min = min_value - 0.05 * max(abs(max_value), abs(min_value))
        y_max = max_value + 0.05 * max(abs(max_value), abs(min_value))

        fig.update_yaxes(
            range=[y_min, y_max],
            minallowed=y_min,
            maxallowed=y_max,
            fixedrange=True
        )

        title = f"{series1_name} and {series2_name} Crossover Plot"

        if dark:
            plot_dark_mode_graph(fig, title)
        else:
            plot_light_mode_graph(fig, title)

        return fig

    def show_plot(self, dark: bool = True):
        """
        Show the generated Plotly plot while removing the mode bar.

        :param dark: If True, the plot will use a dark theme.
        :type dark: bool
        """
        fig = self.get_plot(dark=dark)
        fig.show(config={'displayModeBar': False, 'scrollZoom': True})