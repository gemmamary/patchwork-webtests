from selenium.webdriver.common.by import By

class FilteredPatchResults:

    ACTIVE_FILTERS = (By.ID, "filtersummary")

    def FILTERED_PATCHES(cls, phrase):
        xpath = f"//tbody//*[contains(text(), '{phrase}')]"
        return (By.XPATH, xpath)

    def __init__(self, browser):
        self.browser = browser

    def active_filters_contains(self, filter_type):
        active_filters = self.browser.find_element(*self.ACTIVE_FILTERS).text
        return active_filters.find(filter_type)
