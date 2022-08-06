import streamlit as st
import Page_1
import Page_2

st.set_page_config(
    page_title="NHTSA Crash Case Analysis",
    page_icon="chart_with_upwards_trend",
    layout="wide",
    initial_sidebar_state="expanded",
   )

PAGES = {
    "Visualization Dashboard": Page_1,
    "Statistic Analysis": Page_2
}


st.sidebar.title("Section")
selection = st.sidebar.selectbox("Choose Pages", list(PAGES.keys())
)


st.title("NHTSA Traffic Accident Analaysis")

page = PAGES[selection]
page.app()