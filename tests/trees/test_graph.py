import pytest

from src.trees.graph import Graph 

def test_add_vertex():
    g = Graph()

    g.add_vertex(1)

    assert g.get_vertex(1).data == 1
    assert g.get_vertex(1).connected_to == {}

def test_add_edge():
    g = Graph()
    g.add_vertex(1)
    g.add_vertex(2)

    g.add_edge(1, 2)

    v1_connections = g.get_vertex(1).get_connections()
    assert v1_connections[0].data == 2

    v2_connections = g.get_vertex(2).get_connections()
    assert v2_connections[0].data == 1



