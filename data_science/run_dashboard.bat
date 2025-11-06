@echo off
echo ======================================
echo CityAssist Data Science Dashboard
echo ======================================
echo.
echo Starting dashboard application...
echo Dashboard will open in your browser at http://localhost:8501
echo.
echo Press Ctrl+C to stop the server
echo.

cd /d %~dp0
streamlit run app/dashboard.py
pause
