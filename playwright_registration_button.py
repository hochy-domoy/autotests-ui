from playwright.sync_api import sync_playwright, expect

with sync_playwright() as playwright:
    browser = playwright.chromium.launch(headless=False)
    page = browser.new_page()

    page.goto("https://nikita-filonov.github.io/qa-automation-engineer-ui-course/#/auth/registration")

    registration_button = page.get_by_test_id("registration-page-registration-button")
    expect(registration_button).to_be_disabled()

    registration_email = page.get_by_test_id("registration-form-email-input").locator("input")
    registration_email.focus()

    for char in "user.name@gmail.com":
        page.keyboard.type(char, delay=300)

    registration_username = page.get_by_test_id("registration-form-username-input").locator("input")
    registration_username.focus()

    for char in "username":
        page.keyboard.type(char, delay=300)

    registration_password = page.get_by_test_id("registration-form-password-input").locator("input")
    registration_password.focus()

    for char in "password":
        page.keyboard.type(char, delay=300)

    expect(registration_button).to_be_enabled()

    page.wait_for_timeout(5000)