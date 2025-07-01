@echo off
REM Habitat Radiomics Environment Setup Script (Windows)
REM This script will help you quickly set up the project environment

echo ====================================
echo   Habitat Radiomics Environment Setup
echo ====================================
echo.

REM Check if Python is installed
python --version >nul 2>&1
if %errorlevel% neq 0 (
    echo Error: Python not found!
    echo Please install Python 3.7 or higher first
    echo Download: https://www.python.org/downloads/
    pause
    exit /b 1
)

echo Python is installed:
python --version
echo.

REM Check if conda is available
conda --version >nul 2>&1
if %errorlevel% eq 0 (
    echo Conda detected, using Conda to create environment...
    echo.
    
    REM Create conda environment
    echo Creating habitat-radiomics environment...
    conda create -n habitat-radiomics python=3.8 -y
    
    REM Activate environment
    echo Activating environment...
    call conda activate habitat-radiomics
    
    REM Install dependencies
    echo Installing project dependencies...
    pip install -r requirements.txt
    
    echo.
    echo ====================================
    echo   Environment Setup Complete!
    echo ====================================
    echo.
    echo Usage:
    echo 1. Activate environment: conda activate habitat-radiomics
    echo 2. Run analysis: python examples/basic_usage.py
    echo 3. Or use: python -m src.main
    echo.
    echo For more information, see README.md
    
) else (
    echo Conda not detected, using pip and virtual environment...
    echo.
    
    REM Create virtual environment
    echo Creating virtual environment...
    python -m venv habitat-radiomics-env
    
    REM Activate virtual environment
    echo Activating virtual environment...
    call habitat-radiomics-env\Scripts\activate.bat
    
    REM Upgrade pip
    echo Upgrading pip...
    python -m pip install --upgrade pip
    
    REM Install dependencies
    echo Installing project dependencies...
    pip install -r requirements.txt
    
    echo.
    echo ====================================
    echo   Environment Setup Complete!
    echo ====================================
    echo.
    echo Usage:
    echo 1. Activate environment: habitat-radiomics-env\Scripts\activate.bat
    echo 2. Run analysis: python examples/basic_usage.py
    echo 3. Or use: python -m src.main
    echo.
    echo For more information, see README.md
)

echo.
pause 