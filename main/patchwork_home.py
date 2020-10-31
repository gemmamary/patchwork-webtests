from selenium.webdriver.common.keys import Keys
from main.patchwork_home_locators import PatchworkHomeLocators


class PatchworkHome:
    def __init__(self, browser):
        self.browser = browser

    def load(self, base_url):
        self.browser.get(base_url)

    def show_filters(self):
        show_patch_filters = self.browser.find_element(
            *PatchworkHomeLocators.SHOW_PATCH_FILTERS
        )
        show_patch_filters.click()

    def hide_filters(self):
        show_patch_filters = self.browser.find_element(
            *PatchworkHomeLocators.SHOW_PATCH_FILTERS
        )
        show_patch_filters.click()
        show_patch_filters.click()

    def filter_form_is_displayed(self):

        ff_display_value = self.browser.find_element(
            *PatchworkHomeLocators.FILTER_FORM
        ).get_attribute("style")

        if ff_display_value == "padding-top: 1em; display: block;":
            return True

    def filter_form_is_hidden(self):

        ff_display_value = self.browser.find_element(
            *PatchworkHomeLocators.FILTER_FORM
        ).get_attribute("style")

        if ff_display_value == "padding-top: 1em; display: none;":
            return True

    def navigate_home(self):
        home_icon = self.browser.find_element(*PatchworkHomeLocators.HOME_ICON)
        home_icon.click()

    def navigate_to_bundles(self):
        bundles_icon = self.browser.find_element(*PatchworkHomeLocators.BUNDLES)
        bundles_icon.click()

    def show_project_information(self):
        information_icon = self.browser.find_element(
            *PatchworkHomeLocators.PROJECT_INFORMATION
        )
        information_icon.click()

    def navigate_to_login(self):
        login = self.browser.find_element(*PatchworkHomeLocators.LOGIN)
        login.click()

    def navigate_to_registration(self):
        register = self.browser.find_element(*PatchworkHomeLocators.REGISTER)
        register.click()

    def navigate_to_mail_settings(self):
        mail_settings = self.browser.find_element(*PatchworkHomeLocators.MAIL_SETTINGS)
        mail_settings.click()

    def hide_toolbar(self):
        hide_panel = self.browser.find_element(*PatchworkHomeLocators.HIDE_TOOLBAR)
        hide_panel.click()
