@echo off
setlocal

echo Check if PyTest is installed
python -m pytest --version >nul 2>&1
if %errorlevel% neq 0 (
    echo PyTest is not installed. Installing
    pip install -U pytest
)

python -m pytest --version 

echo Run PyTest
python -m pytest

pause

endlocal