"""
Step definitions for Login feature
"""
from behave import given, when, then, use_step_matcher
from pages.login_page import LoginPage, ProductPage

# Use re matcher for better regex support
use_step_matcher("re")


@given('User opens the SauceDemo login page')
@when('User opens the SauceDemo login page')
def step_open_login_page(context):
    """Open SauceDemo login page"""
    context.login_page = LoginPage(context.page)
    context.login_page.navigate()


@when(r'User enters username "(?P<username>.*)"')
def step_enter_username(context, username):
    """Enter username - handles empty strings properly"""
    context.login_page.enter_username(username)


@when(r'User enters password "(?P<password>.*)"')
def step_enter_password(context, password):
    """Enter password - handles empty strings properly"""
    context.login_page.enter_password(password)


@when('User clicks the Login button')
def step_click_login(context):
    """Click login button"""
    context.login_page.click_login_button()


@then('User successfully logged into the product page')
def step_verify_product_page(context):
    """Verify user successfully logged into the product page"""
    context.product_page = ProductPage(context.page)
    assert context.product_page.is_on_product_page(), "User is not on the product page"

@then('User sees the title "(?P<expected_title>.*)"')
def step_verify_title(context, expected_title):
    """Verify page title"""
    actual_title = context.product_page.get_page_title()
    assert actual_title == expected_title, f"Expected title: {expected_title}, but got: {actual_title}"


@then('User sees the error message "(?P<expected_error>.*)"')
def step_verify_error_message(context, expected_error):
    """Verify error message"""
    assert context.login_page.is_error_displayed(), "Error message is not displayed"
    actual_error = context.login_page.get_error_message()
    assert expected_error in actual_error, f"Expected error: {expected_error}, but got: {actual_error}"
