import allure
import pytest
from assertpy import assert_that

from pages.about_page import AboutPage
from pages.login_page import LoginPage
from pages.projects_page import ProjectsPage


@allure.severity(allure.severity_level.BLOCKER)
@allure.epic("Security")
@allure.story("Login Feature's Functionality")
@pytest.mark.security
class TestLogin:
    _error_msg = "These credentials do not match our records."
    _page_title = "My Workspace"

    @allure.description("test invalid login")
    @pytest.mark.parametrize("email,password", [("nirt236@gmail.com", "123456"), ("elias@gmail.com", "12345Tr")])
    @pytest.mark.run(order=3)
    def test_invalid_login(self, create_driver, email, password):
        about_page = AboutPage()
        about_page.click_login_link()
        login_page = LoginPage()
        login_page.login(email, password)
        assert_that(login_page.get_error_message()).is_equal_to(self._error_msg)

    @allure.description("Test valid login")
    @pytest.mark.run(order=1)
    def test_valid_login(self, create_driver, prep_properties):
        config_reader = prep_properties
        username = config_reader.config_section_dict("Base Url")["username"]
        password = config_reader.config_section_dict("Base Url")["password"]
        about_page = AboutPage()
        login_page = LoginPage()
        projects_page = ProjectsPage()
        about_page.click_login_link()
        login_page.login(username, password)
        assert_that(projects_page.get_title()).is_equal_to(self._page_title)

    @allure.description("Log out from app")
    @allure.title("This test has a custom title")
    @pytest.mark.run(order=2)
    def test_logout(self, create_driver, prep_properties):
        config_reader = prep_properties
        username = config_reader.config_section_dict("Base Url")["username"]
        password = config_reader.config_section_dict("Base Url")["password"]
        about_page = AboutPage()
        about_page.click_login_link()
        login_page = LoginPage()
        projects_page = ProjectsPage()
        login_page.login(username, password)
        projects_page.logout()
        assert_that(login_page.get_page_title()).is_true()

    @allure.description("Skip Test example")
    @pytest.mark.skip(reason="no way of currently testing this")
    def test_skip(self):
        pass
