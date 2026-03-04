# CirLat Konverter 🔄  
### Serbian Version 2.0 – Local • Lightweight • Enterprise Utility

<p align="center">
![Python](https://img.shields.io/badge/Python-3.x-blue)
![UI](https://img.shields.io/badge/UI-PyQt5-green)
![License](https://img.shields.io/badge/License-GPLv3-brightgreen)
![Responsive](https://img.shields.io/badge/Responsive-Yes-yellow)
![Version](https://img.shields.io/badge/Version-2.0-orange)
</p>

---

## 🛡 O projektu

**CirLat Konverter** je desktop aplikacija za jednostavnu i brzu konverziju teksta između ćirilice i latinice na srpskom jeziku.  

- 100% lokalna aplikacija, bez slanja podataka na internet  
- Responzivan GUI dizajn sa **PyQt5**  
- Pamti istoriju konverzija  
- Brzo kopiranje i brisanje teksta  

---

## 🎯 Namenjeno za

- 👤 Privatne korisnike koji žele brzu konverziju teksta  
- 💻 Pisce, novinare i developere koji rade sa dokumentima na srpskom  
- 📝 Situacije kada je potrebno brzo prebacivanje između ćirilice i latinice  

---

## 🚀 Funkcionalnosti

| Funkcija | Opis |
|----------|------|
| **Ćirilica → Latinica** | Jedan klik za transliteraciju u latinicu |
| **Latinica → Ćirilica** | Jedan klik za transliteraciju u ćirilicu |
| **Istorija konverzija** | Klikom na stavku vraća konvertovani tekst u glavno polje |
| **Kopiranje** | Kopira trenutni tekst u clipboard |
| **Brisanje teksta** | Briše sadržaj glavnog polja |
| **Brisanje istorije** | Briše sve prethodne konverzije |
| **Izlaz** | Zatvara aplikaciju |
| **Responzivan dizajn** | Automatski prilagođava veličinu elemenata ekranu |

---

## ⚙️ Tehnologije i zavisnosti

- Python 3.10+  
- [PyQt5](https://pypi.org/project/PyQt5/) – GUI
- PyQt5
- cyrtranslit

---

📷 Screenshot

---

🛠 Struktura projekta
cirlat-konverter/
│
├─ app.py            # Glavni PyQt5 kod
├─ ap.py             # Početna verzija aplikacije PyQt5 kod
├─ ico.ico           # Ikonica prozora (opciono)
├─ requirements.txt  # Zavisnosti
└─ README.md         # Ovaj fajl

---

🔄 Life-Cycle Aplikacije

Pokretanje aplikacije → prazno tekst polje

Unos teksta → izbor konverzije

Tekst se prikazuje u glavnom polju

Istorija beleži prethodne konverzije

Mogućnost kopiranja, brisanja teksta i istorije

Zatvaranje aplikacije klikom na Izlaz

---

🧩 Česti problemi & rešenja
Problem	Rešenje
Klik na istoriju ne radi	Proveri da li je tekst prethodno konvertovan i dodan u istoriju
Tekst se ne kopira	Klikni "Kopiraj" dok je tekst u polju selektovan
Aplikacija ne startuje	Proveri da li su instalirani PyQt5 i cyrtranslit

---

🏆 Unikatne vrednosti

Lakoća i brzina – samo lokalna aplikacija

Pamti istoriju prethodnih konverzija

Responzivan i modern GUI

Minimalne zavisnosti, spremno za distribuciju

---

📜 Licenca

Ovaj projekat je objavljen pod GPLv3 licencom.
Ako koristite ili modifikujete kod, dužni ste da zadržite autorstvo i objavite izmene pod istom licencom.

---

🔄 CirLat Konverter – Brzo, lokalno i responzivno rješenje za konverziju ćirilice i latinice.
- [cyrtranslit](https://pypi.org/project/cyrtranslit/) – transliteracija ćirilice/latinice
