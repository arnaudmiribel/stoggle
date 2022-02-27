import inspect

import streamlit as st
from htbuilder import details, div, p, styles, summary

st.title("▸ Toggle!")

def stoggle(title: str, text: str):
    """
    Displays a toggle widget in Streamlit

    Args:
        title (str): Summary of the toggle (always shown)
        text (str): Content shown after toggling
    """

    st.write(
    str(
        div(
            style=styles(
                    line_height=1.8,
                )
        ) 
                (
                    details(summary(title), p(text)
                    )
    )), 
    unsafe_allow_html=True)

stoggle("Click me!", 
"""Lorem ipsum dolor sit amet, consectetur adipiscing elit. 
Mauris non finibus purus. Morbi et lorem dolor. Vestibulum 
justo diam, bibendum at blandit a, lacinia a leo. Etiam ac 
efficitur libero. Proin vehicula at mauris eget posuere. 
Morbi eu orci et urna posuere vestibulum. Lorem ipsum dolor 
sit amet, consectetur adipiscing elit. Ut feugiat tempus 
velit, vel dictum sapien auctor in. In viverra lobortis sem
eget tincidunt. Donec elit elit, rutrum sed purus facilisis,
ultricies feugiat justo. Ut id tortor leo. Nulla facilisi.
Etiam est arcu, iaculis non est vel, congue mattis nunc. 
Donec in ante nec felis venenatis pulvinar. Quisque eu mauris 
elementum, pellentesque leo eget, consequat dolor.

Integer sodales id tortor non luctus. Aliquam erat volutpat. 
Morbi egestas elit felis, tincidunt maximus felis euismod ut. 
Integer varius interdum lorem in dapibus. Cras ac tortor mollis 
dolor convallis porttitor. Sed non leo a libero semper rhoncus. 
Donec sed mollis lectus.

Quisque quis urna sit amet magna accumsan scelerisque. Cras sit 
amet facilisis nisl. Donec vel nisi id libero mattis facilisis 
ac sit amet augue. In varius mauris sit amet justo scelerisque 
egestas. Duis eget lobortis quam. Duis lacinia pulvinar tortor, 
non bibendum magna venenatis sit amet. In hac habitasse platea 
dictumst. Morbi sed iaculis tortor, id gravida tellus. 
Pellentesque habitant morbi tristique senectus et netus et 
malesuada fames ac turpis egestas. Nulla semper est massa, 
id euismod ante ornare nec. Nulla facilisi.""")

for _ in range(2):
    st.write("")

""" ### Code """

imports = """import streamlit as st
from htbuilder import details, div, p, styles, summary

"""
source_code = inspect.getsource(stoggle)
st.code(imports + source_code)
