from abc import ABC, abstractmethod
import plotly.graph_objects as go

class TradingPlot(ABC):
    """
    An abstract base class that defines the structure for creating trading plots.

    Classes inheriting from TradingPlot must implement the `get_plot` and `shift` methods.
    This class provides a default implementation of the `show_plot` method to display the plot.
    """

    @abstractmethod
    def get_plot(self, dark: bool) -> go.Figure:
        """
        Abstract method to generate a Plotly figure.

        Subclasses must implement this method to return a Plotly figure, which
        will be customized based on the `dark` parameter.

        :param dark: If True, the plot will use a dark theme. If False, it will use a light theme.
        :type dark: bool
        :return: A Plotly figure representing the plot.
        :rtype: go.Figure
        """
        pass


    @abstractmethod
    def shift(self, days_to_shift: int):
        """
        Abstract method to shift the series by a given number of days.

        Subclasses must implement this method to handle the shifting of data in
        the plot, which could be useful for time-based analysis.

        :param days_to_shift: The number of days by which to shift the data.
        :type days_to_shift: int
        """
        pass


    def show_plot(self, dark: bool):
        """
        Display the Plotly plot and remove the mode bar for a cleaner view.

        This method calls the `get_plot` method to generate the figure and then
        displays it using Plotly. The mode bar is disabled, and scroll zoom is enabled.

        :param dark: If True, the plot will use a dark theme. Defaults to True.
        :type dark: bool
        """
        fig = self.get_plot(dark=dark)
        fig.show(config={'displayModeBar': False, 'scrollZoom': True})
