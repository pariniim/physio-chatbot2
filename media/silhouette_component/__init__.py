import os
import streamlit.components.v1 as components

# Declare the component
_component_func = components.declare_component(
    "interactive_silhouette",
    path=os.path.dirname(os.path.abspath(__file__))
)

def st_silhouette(key=None):
    """
    Renders an interactive SVG silhouette.
    Returns a list of selected body parts.
    """
    component_value = _component_func(key=key, default=[])
    return component_value
