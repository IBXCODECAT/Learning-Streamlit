import os
import streamlit as st
import streamlit.components.v1 as components

# Declare the custom component
_component_func = components.declare_component(
    "my_component",
    path=os.path.join(os.path.dirname(__file__), "frontend")
)

def my_component(name="World", key=None):
    # Call the frontend component and return the value
    return _component_func(name=name, default=f"Hello, {name}!", key=key)
