#!/bin/bash
# ============================================
# Script untuk Generate dan Open Allure Report
# ============================================

echo ""
echo "========================================"
echo " Allure Report Generator"
echo "========================================"
echo ""

# Check if allure-results exists
if [ ! -d "allure-results" ]; then
    echo "[ERROR] Folder allure-results tidak ditemukan!"
    echo "[INFO] Jalankan test terlebih dahulu dengan: behave"
    echo ""
    exit 1
fi

# Check if allure-results is empty
if [ -z "$(ls -A allure-results)" ]; then
    echo "[ERROR] Folder allure-results kosong!"
    echo "[INFO] Jalankan test terlebih dahulu dengan: behave"
    echo ""
    exit 1
fi

echo "[1/2] Generating Allure report..."
echo ""

# Generate report
allure generate allure-results --clean -o allure-report

if [ $? -ne 0 ]; then
    echo ""
    echo "[ERROR] Gagal generate report!"
    echo "[INFO] Pastikan Allure sudah terinstall."
    echo "[INFO] Install dengan: brew install allure (macOS) atau apt-get install allure (Linux)"
    echo ""
    exit 1
fi

echo ""
echo "[SUCCESS] Report berhasil di-generate!"
echo ""
echo "[2/2] Opening report in browser..."
echo ""

# Open report
allure open allure-report
