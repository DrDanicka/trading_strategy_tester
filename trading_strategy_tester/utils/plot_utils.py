import pandas as pd
import plotly.graph_objects as go

from trading_strategy_tester.enums.line_colors_enum import LineColor


def create_plot_series_name(name: str) -> (str, str):
    """
    Create a formatted name for the plot series based on its components.

    The name is split by underscores (`_`), where the first part is treated as the ticker,
    the second part is treated as the source, and the remaining parts are considered parameters.

    :param name: The original name string for the plot series.
    :type name: str
    :return: A source as title and formatted string for the plot series name in the format source(param1, param2, ...).
    :rtype: (str, str)
    """
    list_name = name.split('_')

    ticker = list_name[0]
    source = list_name[1]
    rest = list_name[2:]
    title = source

    if title == 'Const':
        title = f'Const. {rest[0]}'

    if ticker != '':
        params = [ticker] + rest
    else:
        params = rest

    return title, f'{source}({", ".join(params)})'


def add_trace_to_fig(fig: go.Figure, x: pd.Series, y: pd.Series, name: str, color: LineColor):
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
    :param color: The color of the trace.
    :type color: str
    """
    if name.startswith('Const'):
        fig.add_trace(go.Scatter(x=x, y=y, mode='lines', name=name, line=dict(color='gray', dash='dash')))
    else:
        fig.add_trace(go.Scatter(x=x, y=y, mode='lines', name=name, line=dict(color=color.value)))


def plot_common_parameters_graph(fig: go.Figure, title: str):
    """
    Apply common parameters to a Plotly figure with customized title, hover mode, drag mode, and legend style.

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
        } if not title.startswith('Price') else None,
        hovermode="x unified",
        dragmode="pan",
        showlegend=True if not title.startswith('Price') else False,
        autosize=True,
        margin=dict(l=0, r=0, t=10, b=0),
        height=None
    )

def plot_light_mode_graph(fig: go.Figure, title: str):
    """
    Apply a light mode theme to a Plotly figure with customized title, hover mode, drag mode, and legend style.

    :param fig: The Plotly figure to update.
    :type fig: go.Figure
    :param title: The title of the plot, which will be centered at the top.
    :type title: str
    """
    plot_common_parameters_graph(fig, title)

    fig.update_layout(
        template='plotly_white',
        legend=dict(
            x=0.02,  # Position from the left (small margin)
            y=0.98,  # Position from the top (small margin)
            traceorder="normal",
            bgcolor="rgba(255, 255, 255, 0.5)",  # Transparent white background for legend
            bordercolor="gray",
            borderwidth=1
        ),
    )


def plot_dark_mode_graph(fig: go.Figure, title: str):
    """
    Apply a dark mode theme to a Plotly figure with customized background color, and legend style.

    :param fig: The Plotly figure to update.
    :type fig: go.Figure
    :param title: The title of the plot, which will be centered at the top.
    :type title: str
    """
    plot_common_parameters_graph(fig, title)

    fig.update_layout(
        template='plotly_dark',
        paper_bgcolor="#121212",  # Set background to custom dark color
        plot_bgcolor="#121212",  # Set plot background to custom dark color
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


def set_x_axis_range(fig: go.Figure, series: pd.Series):
    """
    Set the range of the x-axis for the provided Plotly figure.

    The function calculates the minimum and maximum values of the index (typically time)
    of the provided pandas series and sets these as the limits of the x-axis.

    :param fig: The Plotly figure to update the x-axis range.
    :type fig: go.Figure
    :param series: A pandas series whose index will be used to determine the x-axis range.
    :type series: pd.Series
    """
    x_min = series.index.min()
    x_max = series.index.max()

    fig.update_xaxes(
        range=[x_min, x_max],
        minallowed=x_min,
        maxallowed=x_max
    )


def set_y_axis_range(fig: go.Figure, series1: pd.Series, series2: pd.Series):
    """
    Set the range of the y-axis for the provided Plotly figure based on two pandas series.

    The function calculates the minimum and maximum values across both series and adds
    a 5% margin on both ends to provide some padding. The y-axis range is then updated.

    :param fig: The Plotly figure to update the y-axis range.
    :type fig: go.Figure
    :param series1: The first pandas series used to calculate the y-axis range.
    :type series1: pd.Series
    :param series2: The second pandas series used to calculate the y-axis range.
    :type series2: pd.Series
    """
    min_value = min(series1.min(), series2.min())
    max_value = max(series1.max(), series2.max())

    # Add a 5% margin to the y-axis to prevent lines from touching the plot edges
    y_min = min_value - 0.05 * max(abs(max_value), abs(min_value))
    y_max = max_value + 0.05 * max(abs(max_value), abs(min_value))

    fig.update_yaxes(
        range=[y_min, y_max],
        minallowed=y_min,
        maxallowed=y_max,
        fixedrange=True  # TODO consider whether it should be adjustable in future implementations
    )
