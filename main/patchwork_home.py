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

    def filter_form_is_displayed(self):

        ff_display_value = self.browser.find_element(*PatchworkHomeLocators.FILTER_FORM).get_attribute('style')

        if ff_display_value == 'padding-top: 1em; display: block;':
            return True

    def filter_form_is_hidden(self):

        ff_display_value = self.browser.find_element(*PatchworkHomeLocators.FILTER_FORM).get_attribute('style')

        if ff_display_value == 'padding-top: 1em; display: none;':
            return True

    def navigate_home(self):
        home_icon = self.browser.find_element(*PatchworkHomeLocators.HOME_ICON)
        home_icon.click()

    def navigate_to_bundles(self):
        bundles_icon = self.browser.find_element(*PatchworkHomeLocators.BUNDLES)
        bundles_icon.click()
        