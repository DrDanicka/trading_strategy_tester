from abc import ABC, abstractmethod
import plotly.graph_objects as go

class TradingPlot(ABC):
    @abstractmethod
    def get_plot(self) -> go.Figure:
        pass