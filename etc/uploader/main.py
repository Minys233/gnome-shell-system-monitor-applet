import os
import sys

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.options import Options


def get_driver():
    options = Options()
    options.add_experimental_option("detach", True)
    return webdriver.Chrome(options=options)


def main(username, password):
    login_url = 'https://extensions.gnome.org/accounts/login/?next=/upload/'

    driver = get_driver()
    driver.get(login_url)

    ipt_username = WebDriverWait(driver, 10) \
        .until(EC.element_to_be_clickable(
            (By.CSS_SELECTOR, 'form.auth_form input#id_username')))
    ipt_password = WebDriverWait(driver, 10) \
        .until(EC.element_to_be_clickable(
            (By.CSS_SELECTOR, 'form.auth_form input#id_password')))
    btn_submit = WebDriverWait(driver, 10) \
        .until(EC.element_to_be_clickable(
            (By.CSS_SELECTOR, 'form.auth_form button[type=submit]')))
    ipt_username.send_keys(username)
    ipt_password.send_keys(password)
    print("Submitting login form")
    btn_submit.click()


if __name__ == "__main__":
    username, password = os.getenv('USERNAME'), os.getenv('PASSWORD')
    if not all([username, password]):
        print(("Please set the following environment variables: "
               "USERNAME, PASSWORD"))
        sys.exit(1)
    main(username, password)
