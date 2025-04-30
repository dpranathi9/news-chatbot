import streamlit as st
import requests

# Get the query parameters from the URL
query_params = st.experimental_get_query_params()

# Extract the name from the URL if present
name = query_params.get("name", ["Friend"])[0]  # default to "Friend"

# Greet the user
st.title(f"Hi 👋 {name}! Hello/Namaskar/Aadab")

# NewsAPI Key
NEWS_API_KEY = "bf6fdce177a740e19ed32670ec9cd89b"  # Replace this with your actual API key

def get_top_headlines(api_key):
    url = f"https://newsapi.org/v2/top-headlines?country=us&apiKey={api_key}"
    response = requests.get(url)
    data = response.json()
    articles = data.get("articles", [])[:5]
    return [(a["title"], a["url"]) for a in articles]
    
if name:
    greeting = f"Welcome to the news chatbot"
    st.subheader(greeting)

    st.write("Here are today's top news headlines:")

    headlines = get_top_headlines(NEWS_API_KEY)
    for title, url in headlines:
        st.markdown(f"- [{title}]({url})")
