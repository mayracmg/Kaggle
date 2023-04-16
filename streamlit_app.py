import streamlit as st
import sklearn
import pickle

model = pickle.load(open("model.pkl", "rb"))

st.title("Week 2: The Airbnb dataset of Amsterdam")
st.markdown(
    "The dataset contains modifications with regards to the original for illustrative & learning purposes"
)

amenities = st.slider('How many amenities does the listing have?', 0, 50, 20)
accommodates = st.slider('How many people does the listing accommodate?', 1, 16, 2)
instant_bookable = st.radio(
    "Is the listing instantly bookable?",
    ("True", "False"))
instant_bookable = 1 if instant_bookable == "True" else 0

user_input = [[amenities, accommodates, instant_bookable]]

if st.button('Predict?'):
    st.write("The model predicts that the average tip for this listing is:", model.predict(user_input).round(2))
