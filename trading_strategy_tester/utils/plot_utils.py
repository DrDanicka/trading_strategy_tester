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


import plotly.graph_objects as go

def plot_light_mode_graph(fig: go.Figure, title: str):
    """
    Apply a light mode theme to a Plotly figure with customized title, hover mode, drag mode, and legend style.

    :param fig: The Plotly figure to update.
    :type fig: go.Figure
    :param title: The title of the plot, which will be centered at the top.
    :type title: str
    """
    fig.update_layout(
        title={
            'text': title,
            'x': 0.5,  # Centers the title
            'xanchor': 'center',
            'yanchor': 'top'
        },
        template='plotly_white',
        hovermode="x unified",
        dragmode="pan",
        legend=dict(
            x=0.02,  # Position from the left (small margin)
            y=0.98,  # Position from the top (small margin)
            traceorder="normal",
            bgcolor="rgba(255, 255, 255, 0.5)",  # Transparent white background for legend
            bordercolor="gray",
            borderwidth=1
        )
    )


def plot_dark_mode_graph(fig: go.Figure, title: str):
    """
    Apply a dark mode theme to a Plotly figure with customized title, hover mode, drag mode, background color, and legend style.

    :param fig: The Plotly figure to update.
    :type fig: go.Figure
    :param title: The title of the plot, which will be centered at the top.
    :type title: str
    """
    fig.update_layout(
        title={
            'text': title,
            'x': 0.5,  # Centers the title
            'xanchor': 'center',
            'yanchor': 'top'
        },
        template='plotly_dark',
        hovermode="x unified",
        dragmode="pan",
        paper_bgcolor="rgba(19, 24, 34, 255)",  # Set background to custom dark color
        plot_bgcolor="rgba(19, 24, 34, 255)",  # Set plot background to custom dark color
        font=dict(color="gray"),
        legend=dict(
            x=0.02,  # Position from the left (small margin)
            y=0.98,  # Position from the top (small margin)
            traceorder="normal",
            bgcolor="rgba(0, 0, 0, 0.5)",  # Transparent black background for legend
            bordercolor="gray",
            borderwidth=1
        )
    )
