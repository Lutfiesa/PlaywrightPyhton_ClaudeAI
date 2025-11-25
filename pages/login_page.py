"""
Page Object untuk Login Page SauceDemo
"""

class LoginPage:
    """Class untuk mengelola elemen dan aksi di halaman login"""

    def __init__(self, page):
        self.page = page
        self.url = "https://www.saucedemo.com/"

        # Locators
        self.username_input = "#user-name"
        self.password_input = "#password"
        self.login_button = "#login-button"
        self.error_message = "[data-test='error']"

    def navigate(self):
        """Navigasi ke halaman login"""
        self.page.goto(self.url)
        self.page.wait_for_load_state("networkidle")

    def enter_username(self, username):
        """Memasukkan username"""
        self.page.fill(self.username_input, username)

    def enter_password(self, password):
        """Memasukkan password"""
        self.page.fill(self.password_input, password)

    def click_login_button(self):
        """Klik tombol login"""
        self.page.click(self.login_button)

    def get_error_message(self):
        """Mendapatkan text error message"""
        return self.page.inner_text(self.error_message)

    def is_error_displayed(self):
        """Cek apakah error message ditampilkan"""
        return self.page.is_visible(self.error_message)


class ProductPage:
    """Class untuk mengelola elemen di halaman produk"""

    def __init__(self, page):
        self.page = page

        # Locators
        self.products_title = ".title"
        self.inventory_container = "#inventory_container"

    def is_on_product_page(self):
        """Verifikasi user berada di halaman produk"""
        return self.page.is_visible(self.inventory_container)

    def get_page_title(self):
        """Mendapatkan title halaman produk"""
        return self.page.inner_text(self.products_title)
