# api_integration - Mall för API-integration, DEL A och DEL B

import requests

#------------DEL A------------

# === 1. KONFIGURATION (https://newsapi.org/docs) ===
EXTERNAL_API_URL = 'https://newsapi.org/v2/top-headlines'
EXTERNAL_API_KEY = 'e335478f585e4ec4abe680e94a96cf51' 

# === 2. FUNKTION FÖR ATT HÄMTA DATA FRÅN EXTERNAL API ===
def fetch_data():
    params = {
        "country": "us",      
        "apiKey": EXTERNAL_API_KEY
    }
    try:
        response = requests.get(EXTERNAL_API_URL, params=params)
        response.raise_for_status()  # Kasta fel om något gick fel
        return response.json()       # Returnera hämtad data som JSON
    except requests.RequestException as e:
        print("Fel vid hämtning av data:", e)
        return None

# === 3. TRANSFORMERA DATA TILL RÄTT FORMAT ===
def transform_data(data):
    #[1 VG poäng] om ni skickar in "description" och "content", och returnera dessa i transformed_data.
    articles = data.get("articles", [])
    if not articles:
        print("Inga artiklar hittades i datan.")
        return None

    first_article = articles[0]
    return_data = {
        "title": first_article.get("title"),
        "description": first_article.get("description"),
        "content": first_article.get("content")
    }
    return return_data

#------------DEL B------------

# === 4. FUNKTION FÖR ATT SKICKA DATA TILL INTERNT API ===
# KONFIGURATION (https://lindstorm.nu/register)
INTERNAL_API_URL = 'https://lindstorm.nu/api/uppgift/' 
INTERNAL_API_KEY = '1da57915c8d113d2c4a6c6dab24d34ceae6ed4abe947acad2e41698a08ccc287'

def send_data_to_api(transformed_data):
    headers = {
        "Content-Type": "application/json",
        "X-API-KEY": INTERNAL_API_KEY 
    }
    try:
        response = requests.post(INTERNAL_API_URL, json=transformed_data, headers=headers)
        return response
    except requests.RequestException as e:
        print("Fel vid sändning av data till internt API:", e)
        return None

# === 5. KÖR INTEGRATIONEN ===

# Här behöver ni inte ändra något om ni inte vill [VG]
def run():
    # === Hämta data från en extern källa ===
    nyhetsdata = fetch_data()
    if not nyhetsdata:  # Om ingen data hämtas, avbryt funktionen
        print('Fel vid hämtning av data!')
        return
    
    # === Transformera den hämtade datan ===
    transformed_data = transform_data(nyhetsdata)
    if not transformed_data:  # Om transformationen misslyckas, avbryt funktionen
        print('Fel vid transformation av data!')
        return

    # === Skicka den transformerade datan till API:t ===
    sparad_data = send_data_to_api(transformed_data)

    # === Kontrollera om API-svaret är korrekt (statuskod 201 Created) ===
    if not sparad_data or sparad_data.status_code != 201:
        status = sparad_data.status_code if sparad_data else "Okänd"
        print(f'Fel vid API-anrop! Förväntade 201 men fick {status}')
        return  # Avslutar funktionen om API-anropet misslyckas

    # === Om allt lyckades, bekräfta att processen är klar ===
    print('Data hämtad, transformerad och skickad vidare!')
    print('API Response:', sparad_data.text)  # Skriver ut API-responsens text för debugging

# === 6. EXEKVERA SCRIPTET ===
if __name__ == '__main__':
    run()