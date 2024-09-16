import pandas as pd
import plotly.graph_objects as go

def create_plot_series_name(name: str) -> str:
    """
    Create a formatted name for the plot series based on its components.

    The name is split by underscores (`_`), where the first part is treated as the ticker,
    the second part is treated as the source, and the remaining parts are considered parameters.

    :param name: The original name string for the plot series.
    :type name: str
    :return: A formatted string for the plot series name in the format source(param1, param2, ...).
    :rtype: str
    """
    list_name = name.split('_')

    ticker = list_name[0]
    source = list_name[1]
    rest = list_name[2:]

    if ticker != '':
        params = [ticker] + rest
    else:
        params = rest

    return f'{source}({", ".join(params)})'


def add_trace_to_fig(fig: go.Figure, x: pd.Series, y: pd.Series, name: str):
    """
    Add a trace (line plot) to the Plotly figure. If the series name starts with 'Const',
    it adds a dashed gray line. Otherwise, it adds a regular line plot.

    :param fig: The Plotly figure to which the trace will be added.
    :type fig: go.Figure
    :param x: The x-axis data (usually a time series or date index).
    :type x: pd.Series
    :param y: The y-axis data for the corresponding x-values.
    :type y: pd.Series
    :param name: The name of the series to display in the plot legend.
    :type name: str
    :return: None
    """
    if name.startswith('Const'):
        fig.add_trace(go.Scatter(x=x, y=y, mode='lines', name=name, line=dict(color='gray', dash='dash')))
    else:
        fig.add_trace(go.Scatter(x=x, y=y, mode='lines', name=name))
