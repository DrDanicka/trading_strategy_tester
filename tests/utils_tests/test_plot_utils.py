import unittest
import plotly.graph_objs as go

from trading_strategy_tester.utils.plot_utils import *

class TestPlotUtils(unittest.TestCase):

    def setUp(self):
        # Create a time-indexed pandas Series
        self.dates = pd.date_range(start="2022-01-01", periods=5, freq='D')
        self.series = pd.Series([100, 101, 102, 103, 104], index=self.dates)
        self.series1 = pd.Series([10, 20, 30, 40])
        self.series2 = pd.Series([5, 15, 25, 35])
        self.fig = go.Figure()
        self.title = "Title"
        self.x = pd.Series(pd.date_range(start="2022-01-01", periods=5, freq='D'))
        self.y = pd.Series([1, 2, 3, 4, 5])

    def test_create_plot_series_name_normal_name(self):
        # Arrange
        name = "AAPL_Close_100"
        expected_title = "Close"
        expected_series_name = "Close(AAPL, 100)"

        # Act
        title, series_name = create_plot_series_name(name)

        # Assert
        self.assertEqual(title, expected_title)
        self.assertEqual(series_name, expected_series_name)


    def test_create_plot_series_name_const_name(self):
        # Arrange
        name = "_Const_100"
        expected_title = "Const. 100"
        expected_series_name = "Const(100)"

        # Act
        title, series_name = create_plot_series_name(name)

        # Assert
        self.assertEqual(title, expected_title)
        self.assertEqual(series_name, expected_series_name)

    def test_create_plot_series_name_more_params(self):
        # Arrange
        name = "AAPL_RSI_100_200_400"
        expected_title = "RSI"
        expected_series_name = "RSI(AAPL, 100, 200, 400)"

        # Act
        title, series_name = create_plot_series_name(name)

        # Assert
        self.assertEqual(title, expected_title)
        self.assertEqual(series_name, expected_series_name)


    def test_set_x_axis_range(self):
        # Arrange
        fig = go.Figure()

        # Act
        set_x_axis_range(fig, self.series)
        xaxis = fig.layout.xaxis

        # Assert
        self.assertEqual(xaxis.range[0], self.dates.min())
        self.assertEqual(xaxis.range[1], self.dates.max())
        self.assertEqual(xaxis.minallowed, self.dates.min())
        self.assertEqual(xaxis.maxallowed, self.dates.max())


    def test_common_parameters_with_title(self):
        # Arrange
        title = "My Strategy Plot"

        # Act
        plot_common_parameters_graph(self.fig, title)
        layout = self.fig.layout

        # Assert
        self.assertIsNotNone(layout.title)
        self.assertEqual(layout.title.text, title)
        self.assertEqual(layout.title.x, 0.5)
        self.assertEqual(layout.title.xanchor, 'center')
        self.assertEqual(layout.title.yanchor, 'top')

        self.assertEqual(layout.hovermode, "x unified")
        self.assertEqual(layout.dragmode, "pan")
        self.assertTrue(layout.showlegend)
        self.assertTrue(layout.autosize)
        self.assertEqual(layout.margin.l, 0)
        self.assertEqual(layout.margin.r, 0)
        self.assertEqual(layout.margin.t, 10)
        self.assertEqual(layout.margin.b, 0)
        self.assertIsNone(layout.height)


    def test_common_parameters_price_title(self):
        # Arrange
        title = "Price Chart"

        # Act
        plot_common_parameters_graph(self.fig, title)
        layout = self.fig.layout

        # Assert
        self.assertIsNone(layout.title.text)
        self.assertFalse(layout.showlegend)

        self.assertEqual(layout.hovermode, "x unified")
        self.assertEqual(layout.dragmode, "pan")
        self.assertTrue(layout.autosize)
        self.assertEqual(layout.margin.l, 0)
        self.assertEqual(layout.margin.r, 0)
        self.assertEqual(layout.margin.t, 10)
        self.assertEqual(layout.margin.b, 0)
        self.assertIsNone(layout.height)


    def test_light_mode_styling(self):
        # Act
        plot_light_mode_graph(self.fig, self.title)
        layout = self.fig.layout

        # Assert
        self.assertAlmostEqual(layout.legend.x, 0.02)
        self.assertAlmostEqual(layout.legend.y, 0.98)
        self.assertEqual(layout.legend.traceorder, "normal")
        self.assertEqual(layout.legend.bgcolor, "rgba(255, 255, 255, 0.5)")
        self.assertEqual(layout.legend.bordercolor, "gray")
        self.assertEqual(layout.legend.borderwidth, 1)


    def test_dark_mode_styling(self):
        # Act
        plot_dark_mode_graph(self.fig, self.title)
        layout = self.fig.layout

        # Assert
        self.assertEqual(layout.paper_bgcolor, "#121212")
        self.assertEqual(layout.plot_bgcolor, "#121212")
        self.assertIn("color", layout.font)
        self.assertEqual(layout.font.color, "gray")
        self.assertAlmostEqual(layout.legend.x, 0.02)
        self.assertAlmostEqual(layout.legend.y, 0.98)
        self.assertEqual(layout.legend.traceorder, "normal")
        self.assertEqual(layout.legend.bgcolor, "rgba(0, 0, 0, 0.5)")
        self.assertEqual(layout.legend.bordercolor, "gray")
        self.assertEqual(layout.legend.borderwidth, 1)

    def test_y_axis_range_with_margin(self):
        # Arrange
        expected_min = min(self.series1.min(), self.series2.min())
        expected_max = max(self.series1.max(), self.series2.max())
        margin_base = max(abs(expected_min), abs(expected_max))
        margin = 0.05 * margin_base

        y_min_expected = expected_min - margin
        y_max_expected = expected_max + margin

        # Act
        set_y_axis_range(self.fig, self.series1, self.series2)
        layout = self.fig.layout

        # Assert
        self.assertAlmostEqual(layout.yaxis.range[0], y_min_expected, places=6)
        self.assertAlmostEqual(layout.yaxis.range[1], y_max_expected, places=6)
        self.assertAlmostEqual(layout.yaxis.minallowed, y_min_expected, places=6)
        self.assertAlmostEqual(layout.yaxis.maxallowed, y_max_expected, places=6)
        self.assertTrue(layout.yaxis.fixedrange)

    def test_negative_and_positive_values(self):
        # Arrange
        s1 = pd.Series([-100, -50, 0])
        s2 = pd.Series([50, 100, 150])

        expected_min = min(s1.min(), s2.min())
        expected_max = max(s1.max(), s2.max())
        margin_base = max(abs(expected_min), abs(expected_max))
        margin = 0.05 * margin_base

        y_min_expected = expected_min - margin
        y_max_expected = expected_max + margin

        # Act
        set_y_axis_range(self.fig, s1, s2)
        layout = self.fig.layout

        # Assert
        self.assertAlmostEqual(layout.yaxis.range[0], y_min_expected, places=6)
        self.assertAlmostEqual(layout.yaxis.range[1], y_max_expected, places=6)

    def test_regular_trace(self):
        add_trace_to_fig(self.fig, self.x, self.y, name="Strategy Equity", color=LineColor.RED)
        self.assertEqual(len(self.fig.data), 1)

        trace = self.fig.data[0]
        self.assertEqual(trace.name, "Strategy Equity")
        self.assertEqual(trace.mode, "lines")
        self.assertEqual(trace.line.color, LineColor.RED.value)
        self.assertIsNone(trace.line.dash)

    def test_const_trace(self):
        add_trace_to_fig(self.fig, self.x, self.y, name="Const Level", color=LineColor.RED)
        self.assertEqual(len(self.fig.data), 1)

        trace = self.fig.data[0]
        self.assertEqual(trace.name, "Const Level")
        self.assertEqual(trace.mode, "lines")
        self.assertEqual(trace.line.color, "gray")
        self.assertEqual(trace.line.dash, "dash")

    def test_multiple_traces(self):
        add_trace_to_fig(self.fig, self.x, self.y, name="Const 1", color=LineColor.RED)
        add_trace_to_fig(self.fig, self.x, self.y, name="Equity", color=LineColor.GREEN)

        self.assertEqual(len(self.fig.data), 2)

        const_trace = self.fig.data[0]
        regular_trace = self.fig.data[1]

        self.assertEqual(const_trace.line.color, "gray")
        self.assertEqual(const_trace.line.dash, "dash")
        self.assertEqual(regular_trace.line.color, LineColor.GREEN.value)
        self.assertIsNone(regular_trace.line.dash)


