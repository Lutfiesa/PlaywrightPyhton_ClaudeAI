# 📦 Instalasi Allure Report

Allure adalah framework reporting yang powerful untuk test automation. Berikut cara install Allure di berbagai platform.

---

## 🪟 Windows

### Opsi 1: Menggunakan Scoop (Recommended)

Scoop adalah package manager untuk Windows yang mudah digunakan.

#### 1. Install Scoop (jika belum ada)

Buka PowerShell dan jalankan:

```powershell
Set-ExecutionPolicy RemoteSigned -Scope CurrentUser
irm get.scoop.sh | iex
```

#### 2. Install Allure

```powershell
scoop install allure
```

#### 3. Verifikasi Instalasi

```powershell
allure --version
```

Seharusnya menampilkan versi Allure (contoh: `2.24.0`).

---

### Opsi 2: Manual Download

#### 1. Download Allure

- Kunjungi: https://github.com/allure-framework/allure2/releases
- Download file `allure-x.x.x.zip` (versi terbaru)

#### 2. Extract File

Extract file zip ke folder, contoh: `C:\allure`

#### 3. Tambahkan ke PATH

1. Buka **System Properties** → **Environment Variables**
2. Di **System Variables**, cari `Path` → klik **Edit**
3. Klik **New** dan tambahkan: `C:\allure\bin`
4. Klik **OK** untuk save

#### 4. Restart Terminal

Tutup dan buka ulang terminal/PowerShell.

#### 5. Verifikasi Instalasi

```powershell
allure --version
```

---

### Opsi 3: Menggunakan Chocolatey

Jika sudah punya Chocolatey:

```powershell
choco install allure
```

---

## 🍎 macOS

### Opsi 1: Menggunakan Homebrew (Recommended)

```bash
brew install allure
```

### Opsi 2: Manual Download

1. Download dari: https://github.com/allure-framework/allure2/releases
2. Extract dan tambahkan `bin` folder ke PATH

### Verifikasi Instalasi

```bash
allure --version
```

---

## 🐧 Linux (Ubuntu/Debian)

### Menggunakan Package Manager

```bash
# Add repository
sudo apt-add-repository ppa:qameta/allure
sudo apt-get update

# Install Allure
sudo apt-get install allure
```

### Manual Installation

```bash
# Download
wget https://github.com/allure-framework/allure2/releases/download/2.24.0/allure-2.24.0.tgz

# Extract
tar -zxvf allure-2.24.0.tgz -C /opt/

# Add to PATH
sudo ln -s /opt/allure-2.24.0/bin/allure /usr/bin/allure
```

### Verifikasi Instalasi

```bash
allure --version
```

---

## ✅ Verifikasi Instalasi

Setelah install, jalankan command ini untuk memastikan Allure sudah terinstall:

```bash
allure --version
```

**Output yang diharapkan:**
```
2.24.0
```

---

## 🚀 Cara Menggunakan Allure di Project Ini

### 1. Jalankan Test

```bash
behave
```

Test akan otomatis generate file hasil di folder `allure-results/`.

### 2. Generate Report

**Windows:**
```bash
generate_report.bat
```

**Linux/Mac:**
```bash
chmod +x generate_report.sh
./generate_report.sh
```

Atau secara manual:
```bash
allure generate allure-results --clean -o allure-report
allure open allure-report
```

### 3. Lihat Report

Browser akan otomatis terbuka dengan report Allure yang interaktif! 🎉

---

## 🔧 Troubleshooting

### "allure: command not found"

**Solusi**: Allure belum terinstall atau belum ditambahkan ke PATH. Ikuti langkah instalasi di atas.

### Permission Denied (Linux/Mac)

```bash
chmod +x generate_report.sh
```

### Port Already in Use

Jika Allure server sudah running:
```bash
# Kill proses yang menggunakan port
# Windows
taskkill /F /IM java.exe

# Linux/Mac
pkill -f allure
```

---

## 📚 Resources

- **Allure Documentation**: https://docs.qameta.io/allure/
- **Allure GitHub**: https://github.com/allure-framework/allure2
- **Allure Examples**: https://demo.qameta.io/allure/

---

## 💡 Tips

1. **Jangan commit folder allure-results dan allure-report** ke Git (sudah ada di .gitignore)
2. **History**: Allure bisa track history test jika folder `allure-report/history` di-copy ke `allure-results/history` sebelum generate report baru
3. **CI/CD**: Allure support integration dengan Jenkins, GitLab CI, GitHub Actions, dll

---

Selamat! Allure Report sudah siap digunakan! 🎊
