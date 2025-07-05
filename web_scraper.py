import requests
from bs4 import BeautifulSoup

def scrape_website(url):
    """Extrae títulos y enlaces de una página web (solo para uso ético)."""
    try:
        response = requests.get(url)
        soup = BeautifulSoup(response.text, 'html.parser')
        
        data = {
            "title": soup.title.string if soup.title else "Sin título",
            "links": [a['href'] for a in soup.find_all('a', href=True)][:5]  # Solo primeros 5 enlaces
        }
        return data
    except Exception as e:
        return {"error": str(e)}