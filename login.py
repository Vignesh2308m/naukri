import re
from playwright.sync_api import Playwright, sync_playwright, expect


def run(playwright: Playwright) -> None:
    browser = playwright.firefox.launch(headless=False)
    context = browser.new_context()
    page = context.new_page()
    page.goto("https://www.naukri.com/")
    page.get_by_role("link", name="Login", exact=True).click()
    page.get_by_placeholder("Enter your active Email ID /").click()
    page.get_by_placeholder("Enter your active Email ID /").fill("vicky.manoharan2018@gmail.com")
    page.get_by_placeholder("Enter your password").click()
    page.get_by_placeholder("Enter your password").fill("Nila#0912")
    page.get_by_role("button", name="Login", exact=True).click()
    page.get_by_role("link", name="View profile").click()
    # ---------------------
    context.close()
    browser.close()


with sync_playwright() as playwright:
    run(playwright)
