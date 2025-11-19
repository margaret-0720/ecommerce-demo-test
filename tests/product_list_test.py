from playwright.sync_api import sync_playwright

def test_product_list_visible():
    with sync_playwright() as p:
        browser = p.chromium.launch()
        page = browser.new_page()

        page.goto("http://127.0.0.1:5000")
        page.fill('#user-id', 'test')
        page.fill('#user-pw', '1234')
        page.click('text=로그인')

        page.wait_for_selector('text=화이트 티셔츠')
        page.wait_for_selector('text=블랙 조거팬츠')

        browser.close()