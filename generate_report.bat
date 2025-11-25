@echo off
REM ============================================
REM Script untuk Generate dan Open Allure Report
REM ============================================

echo.
echo ========================================
echo  Allure Report Generator
echo ========================================
echo.

REM Check if allure-results exists
if not exist "allure-results" (
    echo [ERROR] Folder allure-results tidak ditemukan!
    echo [INFO] Jalankan test terlebih dahulu dengan: behave
    echo.
    pause
    exit /b 1
)

REM Check if allure-results is empty
dir /b "allure-results" | findstr "^" >nul
if errorlevel 1 (
    echo [ERROR] Folder allure-results kosong!
    echo [INFO] Jalankan test terlebih dahulu dengan: behave
    echo.
    pause
    exit /b 1
)

echo [1/2] Generating Allure report...
echo.

REM Generate report
allure generate allure-results --clean -o allure-report

if errorlevel 1 (
    echo.
    echo [ERROR] Gagal generate report!
    echo [INFO] Pastikan Allure sudah terinstall.
    echo [INFO] Install dengan: scoop install allure
    echo.
    pause
    exit /b 1
)

echo.
echo [SUCCESS] Report berhasil di-generate!
echo.
echo [2/2] Opening report in browser...
echo.

REM Open report
allure open allure-report

pause
