from playwright.sync_api import sync_playwright

def test_login_success():
    with sync_playwright() as p:
        browser = p.chromium.launch()
        page = browser.new_page()

        page.goto("http://127.0.0.1:5000")

        page.fill('#user-id', 'test')
        page.fill('#user-pw', '1234')
        page.click('text=로그인')

        page.wait_for_selector('text=상품 목록')

        browser.close()