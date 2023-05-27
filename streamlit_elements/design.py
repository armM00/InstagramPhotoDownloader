import streamlit as st


def animation():

    cover = """       
    <style>
    @keyframes example {
        0%   {background-color: #0D1B2A;}
        25%  {background-color: #2B2D42;}
        50%  {background-color: #1D1D1D;}
        75%  {background-color: #2B2D42;}
        100% {background-color: #0D1B2A;}
    }
    
    [data-testid="stAppViewContainer"] > .main {
        animation-name: example;
        animation-duration: 10s;
        animation-timing-function: linear;
        animation-iteration-count: infinite;
    }
    </style>
    """

    st.markdown(animation, unsafe_allow_html=True)
    return cover
