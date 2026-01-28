# Web Scraping & API Project

Ky projekt realizon:
- Nxjerrjen e titujve të lajmeve nga faqja News Albania (web scraping)
- Marrjen e të dhënave të motit për Tiranën nga OpenWeatherMap API
- Bashkimin e të dhënave dhe ruajtjen e tyre në një file JSON

## Teknologjitë e përdorura
- Python
- requests
- beautifulsoup4
- OpenWeatherMap API

## Si funksionon projekti
1. Programi lexon faqen https://newsalbania.al/
2. Nxjerr titujt e lajmeve
3. Merr motin aktual për Tiranën nga OpenWeatherMap API
4. Bashkon të dhënat dhe i ruan në file `data.json`

## Si ekzekutohet projekti

1. Instalo libraritë:
pip install -r requirements.txt
2. Ekzekuto skriptin:
python scraper.py
 Rezultati do të ruhet në file:
data.json
Emri: Xhorxhi Molla

