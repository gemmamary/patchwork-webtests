from selenium.webdriver.common.keys import Keys
from main.sort_patches_locators import SortPatchesLocators

class SortPatches:

    def __init__(self, browser):
        self.browser = browser

    def load(self, base_url):
        self.browser.get(base_url)

    def sort_by_patches(self):
        patches_title = self.browser.find_element(*SortPatchesLocators.SORT_BY_PATCH)
        patches_title.click()

    def sort_by_date(self):
        date_title = self.browser.find_element(*SortPatchesLocators.SORT_BY_DATE)
        date_title.click()

    def sort_by_submitter(self):
        submitter_title = self.browser.find_element(*SortPatchesLocators.SORT_BY_SUBMITTER)
        submitter_title.click()

    def sort_by_delegate(self):
        delegate_title = self.browser.find_element(*SortPatchesLocators.SORT_BY_DELEGATE)
        delegate_title.click()

    def sort_by_state(self):
        state_title = self.browser.find_element(*SortPatchesLocators.SORT_BY_STATE)
        state_title.click()