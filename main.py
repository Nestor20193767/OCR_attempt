import streamlit as st
import requests
from bs4 import BeautifulSoup

def extract_content(url):
    try:
        response = requests.get(url)
        response.raise_for_status()  # Check for request errors
        soup = BeautifulSoup(response.text, 'html.parser')
        
        # Extract titles and paragraphs
        titles = soup.find_all(['h1', 'h2', 'h3'])
        paragraphs = soup.find_all('p')
        
        title_texts = [title.get_text(strip=True) for title in titles]
        paragraph_texts = [p.get_text(strip=True) for p in paragraphs]
        
        return title_texts, paragraph_texts
    except Exception as e:
        return None, f"Error: {e}"

# Streamlit UI
st.title("Web Scraping Tool")
st.write("Este programa permite extraer títulos y párrafos de una página web.")

url = st.text_input("Introduce la URL de la página web:", placeholder="https://ejemplo.com")

if st.button("Realizar Web Scraping"):
    if url:
        with st.spinner("Extrayendo datos..."):
            titles, paragraphs = extract_content(url)
            if titles is not None:
                st.subheader("Títulos encontrados:")
                for title in titles:
                    st.write(f"- {title}")

                st.subheader("Párrafos encontrados:")
                for para in paragraphs:
                    st.write(f"- {para}")
            else:
                st.error(paragraphs)  # Display error message
    else:
        st.warning("Por favor, introduce una URL válida.")


    










