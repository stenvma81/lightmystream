import streamlit as st
import pandas as pd
import plotly.express as px


@st.cache_data
def get_data_from_excel():
    dataframe = pd.read_excel("testsheet.xlsx")

    return dataframe


test_data = get_data_from_excel()


st.title("Testing streamlit charts")
st.write("Test data: ")
st.write(test_data)


fig = px.line(test_data, x="Date", y="Value", title="Test Line Chart")
st.plotly_chart(fig)