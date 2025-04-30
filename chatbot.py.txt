import streamlit as st
import requests

# NewsAPI Key
NEWS_API_KEY = "bf6fdce177a740e19ed32670ec9cd89b"  # Replace this with your actual API key

def get_top_headlines(api_key):
    url = f"https://newsapi.org/v2/top-headlines?country=us&apiKey={api_key}"
    response = requests.get(url)
    data = response.json()
    articles = data.get("articles", [])[:5]
    return [(a["title"], a["url"]) for a in articles]

st.title("Daily News Chatbot")

name = st.text_input("Enter your name (or type 'friends')")

if name:
    greeting = f"Hi {name}!" if name.lower() != "friends" else "Hi friends!"
    st.subheader(greeting)

    st.write("Here are today's top news headlines:")

    headlines = get_top_headlines(NEWS_API_KEY)
    for title, url in headlines:
        st.markdown(f"- [{title}]({url})")
