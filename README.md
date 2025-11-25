# Test Automation Playwright - SauceDemo

Project automation testing menggunakan Behave (BDD Framework) dan Playwright untuk testing aplikasi web [SauceDemo](https://www.saucedemo.com/).

## Deskripsi Project

Project ini mengimplementasikan automation testing dengan pendekatan **Behavior-Driven Development (BDD)** menggunakan Behave dan Playwright. Test cases ditulis dalam bahasa Gherkin (bahasa natural) dan menggunakan **Page Object Model (POM)** pattern untuk struktur yang lebih maintainable.

### Aplikasi yang Ditest
- **Website**: [SauceDemo](https://www.saucedemo.com/)
- **Jenis**: E-commerce Demo Application
- **Test Coverage**: Login functionality (positive & negative scenarios)

## Teknologi yang Digunakan

| Teknologi | Versi | Fungsi |
|-----------|-------|--------|
| **Python** | 3.11+ | Bahasa pemrograman utama |
| **Behave** | 1.2.6 | BDD framework untuk Gherkin test scenarios |
| **Playwright** | 1.40.0 | Browser automation library (Chromium, Firefox, WebKit) |
| **Pytest** | 7.4.3 | Python testing framework |
| **Pytest-Playwright** | 0.4.3 | Integrasi Pytest dengan Playwright |
| **Allure-Behave** | 2.13.2 | Test reporting dengan Allure |

## Struktur Project

```
TesetAutomationPlaywright/
├── features/                    # Feature files dan test scenarios
│   ├── __init__.py
│   ├── environment.py          # Behave hooks (setup & teardown) + Allure integration
│   ├── login.feature           # Gherkin feature file untuk login
│   └── steps/                  # Step definitions
│       ├── __init__.py
│       └── login_steps.py      # Implementasi steps login
├── pages/                       # Page Object Model classes
│   ├── __init__.py
│   └── login_page.py           # LoginPage & ProductPage classes
├── utils/                       # Utility functions (jika diperlukan)
│   └── __init__.py
├── screenshots/                 # Auto-generated screenshots saat test gagal
├── allure-results/              # Allure raw results (auto-generated)
├── allure-report/               # Allure HTML report (auto-generated)
├── behave.ini                   # Konfigurasi Behave + Allure formatter
├── requirements.txt             # Python dependencies
├── generate_report.bat          # Script untuk generate Allure report (Windows)
├── generate_report.sh           # Script untuk generate Allure report (Linux/Mac)
├── INSTALL_ALLURE.md            # Panduan instalasi Allure
├── .gitignore                   # Git ignore file
└── README.md                    # Dokumentasi project (file ini)
```

## Fitur Test

### Test Coverage
Project ini mencakup testing untuk fitur login dengan scenarios:

#### Positive Test Scenarios
- ✅ Login dengan kredensial valid (standard user)
- ✅ Login dengan berbagai tipe user (scenario outline)
  - Standard user
  - Problem user
  - Performance glitch user

#### Negative Test Scenarios
- ❌ Login dengan username kosong
- ❌ Login dengan password kosong
- ❌ Login dengan kredensial invalid
- ❌ Login dengan akun yang terkunci (locked_out_user)

### Fitur Framework
- 🌐 Multi-browser support (Chromium, Firefox, WebKit)
- 📸 Automatic screenshot capture saat test gagal
- 🎥 Optional video recording
- 🔍 Optional tracing untuk debugging
- 🎯 Page Object Model pattern
- 🔄 Isolated test execution (setiap scenario dapat browser context baru)
- 📊 **Allure Report integration** untuk web-based reporting

## Prerequisites

### Software Requirements
- **Python** 3.11 atau lebih tinggi
- **pip** (Python package manager)
- **Git** (optional, untuk version control)

### Instalasi Python
Jika belum menginstall Python:
1. Download dari [python.org](https://www.python.org/downloads/)
2. Install dengan mencentang "Add Python to PATH"
3. Verifikasi instalasi:
   ```bash
   python --version
   pip --version
   ```

## Setup & Instalasi

### 1. Clone atau Download Project
```bash
cd C:\Users\lutfi\Documents\Claude Automation\TesetAutomationPlaywright
```

### 2. Install Dependencies
```bash
pip install -r requirements.txt
```

### 3. Install Playwright Browsers
```bash
playwright install
```

Perintah ini akan mendownload browser yang diperlukan (Chromium, Firefox, WebKit).

## Cara Menjalankan Test

### Run All Tests
```bash
behave
```

### Run Tests dengan Tag Tertentu
```bash
# Run positive tests only
behave --tags=@positive

# Run negative tests only
behave --tags=@negative

# Run smoke tests only
behave --tags=@smoke
```

### Run Specific Feature File
```bash
behave features/login.feature
```

### Run dengan Browser Tertentu
```bash
# Chromium (default)
behave

# Firefox
set BROWSER=firefox
behave

# WebKit
set BROWSER=webkit
behave
```

### Run dengan Video Recording
```bash
set RECORD_VIDEO=true
behave
```

### Run dengan Tracing (untuk debugging)
```bash
set TRACE=true
behave
```

## Environment Variables

| Variable | Value | Deskripsi |
|----------|-------|-----------|
| `BROWSER` | chromium/firefox/webkit | Pilih browser untuk testing (default: chromium) |
| `RECORD_VIDEO` | true/false | Aktifkan video recording (default: false) |
| `TRACE` | true/false | Aktifkan tracing untuk debugging (default: false) |

## Page Object Model

Project ini menggunakan Page Object Model pattern untuk memisahkan UI locators dari test logic.

### LoginPage (`pages/login_page.py`)
```python
# Properties
- username_input
- password_input
- login_button
- error_message

# Methods
- navigate()
- enter_username(username)
- enter_password(password)
- click_login_button()
- get_error_message()
- is_error_displayed()
```

### ProductPage (`pages/login_page.py`)
```python
# Properties
- products_title
- inventory_container

# Methods
- is_on_product_page()
- get_page_title()
```

## Test Credentials

Kredensial yang tersedia untuk testing (dari SauceDemo):

| Username | Password | Status |
|----------|----------|--------|
| standard_user | secret_sauce | ✅ Valid |
| locked_out_user | secret_sauce | 🔒 Locked |
| problem_user | secret_sauce | ⚠️ Valid (with issues) |
| performance_glitch_user | secret_sauce | 🐌 Valid (slow) |

## Test Reports

### 🎯 Allure Report (Web Report - Recommended)

Project ini sudah terintegrasi dengan **Allure Report**, sebuah web-based test report yang powerful dan interaktif.

#### Fitur Allure Report:
- 📊 **Dashboard interaktif** dengan grafik dan statistik
- 📸 **Screenshot otomatis** saat test gagal (terintegrasi langsung)
- 🎥 **Video recording** (jika diaktifkan)
- 📈 **Test history & trends** untuk tracking progress
- 🔍 **Detail step-by-step** execution dengan timeline
- 🏷️ **Tags & categories** untuk filtering
- ⚡ **Realtime report** yang mudah di-share

#### Instalasi Allure

**PENTING**: Sebelum generate report, install Allure terlebih dahulu.

Lihat panduan lengkap di: **[INSTALL_ALLURE.md](INSTALL_ALLURE.md)**

**Quick Install (Windows):**
```bash
# Menggunakan Scoop (recommended)
scoop install allure

# Verify
allure --version
```

**Quick Install (macOS):**
```bash
# Menggunakan Homebrew
brew install allure

# Verify
allure --version
```

#### Cara Generate Allure Report

**1. Jalankan Test:**
```bash
behave
```
Hasil test akan tersimpan di folder `allure-results/`.

**2. Generate dan Buka Report:**

**Windows:**
```bash
generate_report.bat
```

**Linux/Mac:**
```bash
chmod +x generate_report.sh
./generate_report.sh
```

**Manual (semua platform):**
```bash
# Generate report
allure generate allure-results --clean -o allure-report

# Open report di browser
allure open allure-report
```

**3. Lihat Report di Browser:**

Browser akan otomatis terbuka dengan URL: `http://localhost:PORT`

#### Screenshot Allure Report

Allure Report menampilkan:
- ✅ Total tests passed/failed/skipped
- 📊 Grafik pie chart dan trend line
- 🔍 Detail setiap test case dengan steps
- 📸 Screenshot langsung di report (tidak perlu buka folder)
- ⏱️ Execution time untuk setiap test
- 🏷️ Tags untuk filtering (@positive, @negative, @smoke)

---

### 📸 Screenshots (Fallback)
- Otomatis tersimpan di folder `screenshots/` saat test gagal
- Format nama: `{scenario_name}_{timestamp}.png`
- Full page screenshot untuk konteks lengkap
- **Juga otomatis ter-attach ke Allure Report**

### 🎥 Video Recording
- Tersimpan di folder `videos/` (jika RECORD_VIDEO=true)
- Format: webm
- Rekaman seluruh test execution

### 🔍 Trace Files
- Tersimpan di folder `traces/` (jika TRACE=true)
- Dapat dibuka dengan: `playwright show-trace trace.zip`
- Berisi screenshots, snapshots, dan network logs
- **Juga otomatis ter-attach ke Allure Report**

## Contoh Output Test

```
Feature: Fitur Login SauceDemo # features/login.feature:3

  @positive @smoke
  Scenario: Login berhasil dengan kredensial valid
    Given pengguna membuka halaman login SauceDemo    # features/steps/login_steps.py:4
    When pengguna memasukkan username "standard_user" # features/steps/login_steps.py:8
    And pengguna memasukkan password "secret_sauce"   # features/steps/login_steps.py:12
    And pengguna mengklik tombol login                # features/steps/login_steps.py:16
    Then pengguna berhasil masuk ke halaman products  # features/steps/login_steps.py:20

1 feature passed, 0 failed, 0 skipped
1 scenario passed, 0 failed, 0 skipped
5 steps passed, 0 failed, 0 skipped, 0 undefined
```

## Troubleshooting

### Error: "Python not found"
**Solusi**: Install Python dan pastikan sudah ditambahkan ke PATH

### Error: "playwright not found"
**Solusi**: Jalankan `playwright install`

### Error: "ModuleNotFoundError"
**Solusi**: Jalankan `pip install -r requirements.txt`

### Test Gagal Terus
1. Cek koneksi internet (website SauceDemo harus bisa diakses)
2. Cek apakah browser sudah terinstall: `playwright install`
3. Lihat screenshot di folder `screenshots/` untuk debugging
4. Aktifkan tracing: `set TRACE=true` dan `behave`

### Browser Tidak Terbuka
**Solusi**: Playwright menggunakan headless mode by default. Untuk melihat browser:
- Edit `features/environment.py`
- Ubah `headless=True` menjadi `headless=False`

## Best Practices

1. **Selalu gunakan Page Object Model** untuk UI interactions
2. **Tulis test scenarios dalam Gherkin** yang mudah dipahami
3. **Gunakan tags** (`@positive`, `@negative`, `@smoke`) untuk organisasi test
4. **Screenshot otomatis** sudah dihandle untuk test yang gagal
5. **Isolasi test**: Setiap scenario mendapat browser context baru
6. **Jangan hardcode data**: Gunakan scenario outline untuk data-driven testing

## Pengembangan Lebih Lanjut

### Menambah Feature Baru
1. Buat file `.feature` baru di folder `features/`
2. Tulis scenarios dalam format Gherkin
3. Buat step definitions di `features/steps/`
4. Buat Page Object di `pages/` (jika diperlukan)

### Menambah Step Definition
```python
@when('pengguna melakukan aksi baru')
def step_impl(context):
    # Implementasi menggunakan Page Object
    context.page_object.perform_action()
```

### Menambah Page Object
```python
class NewPage:
    def __init__(self, page):
        self.page = page
        self.locator = page.locator("#element")

    def perform_action(self):
        self.locator.click()
```

## Kontribusi

Untuk berkontribusi pada project ini:
1. Fork repository (jika menggunakan Git)
2. Buat branch baru untuk feature/bugfix
3. Commit changes dengan message yang jelas
4. Test perubahan dengan menjalankan semua tests
5. Submit pull request

## Kontak & Support

Jika ada pertanyaan atau issue:
- Check dokumentasi di file ini
- Lihat Playwright docs: https://playwright.dev/python/
- Lihat Behave docs: https://behave.readthedocs.io/

## License

Project ini dibuat untuk keperluan pembelajaran dan testing automation.

---

**Dibuat dengan**: Python + Behave + Playwright
**Terakhir diupdate**: November 2024
