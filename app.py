import google.generativeai as genai
import streamlit as st

# Configure API Key (Replace with your Gemini API Key)
genai.configure(api_key="AIzaSyAYRgsgELxGrv97Of_5hbG9lEJFPN5ZR6Y")  # Replace with your actual API key

# Function to get AI response from Gemini
def get_ai_response(prompt):
    try:
        model = genai.GenerativeModel("gemini-1.5-pro-latest")
        response = model.generate_content(prompt)
        return response.text
    except Exception as e:
        return f"Error:{str(e)}"

# Streamlit UI
st.title("🌍 AI Travel Planner")
st.write("Plan your trips easily with AI-powered suggestions!")

# User input for destination
destination = st.text_input("Enter your travel destination:", "")

# Get AI response when button is clicked
if st.button("Generate Travel Plan"):
    if destination:
        prompt = f"Create a 5-day travel itinerary for {destination}, including places to visit, food recommendations, and best travel tips."
        itinerary = get_ai_response(prompt)
        st.subheader(f"Your AI-Generated Travel Plan for {destination}:")
        st.write(itinerary)
    else:
        st.warning("Please enter a destination.")
