from pages.home_page import HomePage
import time


class TestHomePage:

    def test_open_google(self, setup):
        driver = setup

        home_page = HomePage(driver)
        home_page.open_website("https://www.google.com")

        expected_title = "Google"
        actual_title = home_page.get_page_title()
        time.sleep(2)

        assert expected_title == actual_title
