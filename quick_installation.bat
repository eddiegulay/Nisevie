@REM create virtual environment
python -m venv .env

@REM activate virtual environment
".env\Scripts\activate"

@REM Install requirements
echo off
pip install -r requirements.txt

@REM open browser
powershell Start-Process chrome localhost:8000

@REM launch development server when browser is loading
python manage.py runserver
