Helpdesk App

Prosty system zgłoszeń IT (Help Desk) umożliwiający użytkownikom zgłaszanie problemów oraz administratorowi zarządzanie zgłoszeniami poprzez panel webowy.

Demo
https://helpdesk-app-upvz.onrender.com

Funkcjonalności

- Dodawanie zgłoszeń przez użytkownika  
- Panel administratora (admin)  
- Zmiana statusu zgłoszeń (OPEN / CLOSED)  
- Zapisywanie danych w bazie SQLite 

Technologie

- Python (Flask)
- SQLite
- HTML / CSS
- Gunicorn (deployment)
- Render (hosting)
  
Instalacja lokalna

```bash
git clone https://github.com/johns3132/helpdesk-app.git
cd helpdesk-app

python3 -m venv venv
source venv/bin/activate   # Windows: venv\Scripts\activate

pip install -r requirements.txt
python app.py
