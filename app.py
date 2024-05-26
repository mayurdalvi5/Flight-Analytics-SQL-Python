import streamlit as st
import base64
from dbhelper import DB
import plotly.graph_objects as go
import plotly.express as px


# Function to load and encode the image
def get_base64_image(image_file):
    with open(image_file, "rb") as image:
        return base64.b64encode(image.read()).decode()


# Load the image and encode it in Base64
image_file = "flight-statistics-scaled.jpg"
base64_image = get_base64_image(image_file)

# Inject CSS to set the background image
page_bg_img = f'''
<style>
.stApp {{
    background-image: url("data:image/jpeg;base64,{base64_image}");
    background-size: cover;
}}
</style>
'''

st.markdown(page_bg_img, unsafe_allow_html=True)

################


db = DB()

st.sidebar.title("Flights Analytics")

user_option = st.sidebar.selectbox("Menu", ["Select One", "Check Flights", "Analytics"])

if user_option == "Check Flights":
    st.title("Check Flights")

    col1, col2 = st.columns(2)

    with col1:
        city = db.fetch_city_names()
        source = st.selectbox("Source", sorted(city))

    with col2:
        destination = st.selectbox("Destination", sorted(city, reverse=True))

    if st.button("Search"):
        results = db.fetch_all_flights(source, destination)

        if len(results) == 0:
            st.error("No flights available from {} and {}".format(source, destination))
        else:
            st.dataframe(results)
elif user_option == "Analytics":
    airline, frequency = db.fetch_airline_frequency()

    fig = go.Figure(
        go.Pie(
            labels=airline,
            values=frequency,
            hoverinfo="label+percent",
            textinfo="value",
        )
    )
    st.header("Pie Chart")
    st.plotly_chart(fig)

    city, frequency = db.busy_airport()
    fig = px.bar(x=city, y=frequency)
    st.plotly_chart(fig, theme="streamlit", use_container_width=True)

    date, frequency = db.daily_frequency()
    fig = px.line(x=date, y=frequency)
    st.plotly_chart(fig, theme="streamlit", use_container_width=True)

else:
    st.title("About Project")
    st.write(
        """

Develop a Python application that connects seamlessly to MySQL, 
extracting crucial flight details like date, departure time, duration, 
and prices with user-specified source and destination filters. Utilize the 
acquired data for in-depth analytics, identifying the busiest airports and creating 
insightful visualizations using Plotly charts. With its user-friendly interface, 
this project empowers users to effortlessly explore and analyze flight information, 
serving as a robust tool for making well-informed decisions in the dynamic realm of air travel."""
    )
