import sys
import os

# Fix import path
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from app import app


def test_header_present():
    layout = app.layout
    header = layout.children[0]
    assert "Soul Foods Sales Dashboard" in header.children


def test_radio_present():
    layout = app.layout

    radio_div = layout.children[2]
    radio = radio_div.children[0]   # ✅ FIX HERE

    assert radio.id == "region-filter"


def test_graph_present():
    layout = app.layout
    graph = layout.children[3]
    assert graph.id == "sales-chart"