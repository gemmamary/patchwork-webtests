import pytest
import json

from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
from main.filter_form_locators import FilterFormLocators
from main.patchwork_home_locators import PatchworkHomeLocators


class PatchworkFilterForm:
    def __init__(self, browser):
        self.browser = browser

    def load(self, base_url):
        self.browser.get(base_url)

    def show_filters(self):
        show_patch_filters = self.browser.find_element(
            *PatchworkHomeLocators.SHOW_PATCH_FILTERS
        )
        show_patch_filters.click()

    def filter_by_series(self, title):
        series_input = self.browser.find_element(*FilterFormLocators.SERIES_INPUT)
        series_input.send_keys(title + Keys.RETURN)

    def filter_by_submitter(self, name):
        submitter_input = Select(
            self.browser.find_element(*FilterFormLocators.SUBMITTER_INPUT)
        )
        submitter_input.select_by_index(1)

    def filter_by_state(self, state):
        state_input = Select(self.browser.find_element(*FilterFormLocators.STATE_INPUT))
        state_input.select_by_visible_text(state)

    def filter_by_search_term(self, term):
        search_input = self.browser.find_element(*FilterFormLocators.SEARCH_INPUT)
        search_input.send_keys(term + Keys.RETURN)

    def filter_by_archived(self, archived):
        archived_input = self.browser.find_element(
            *FilterFormLocators.ARCHIVED_INPUT
        ).find_elements_by_tag_name("input")
        submit_filter = self.browser.find_element(*FilterFormLocators.SUBMIT_FILTER)

        for input in archived_input:
            input.get_attribute("value")
            if input == archived:
                input.click()

        submit_filter.click()

    def filter_by_delegate(self, name):
        delegate_filter = Select(
            self.browser.find_element(*FilterFormLocators.DELEGATE_FILTER)
        )
        submit_filter = self.browser.find_element(*FilterFormLocators.SUBMIT_FILTER)
        delegate_filter.select_by_value(name)

        submit_filter.click()

    def remove_active_filters(self):
        remove_active_filter = self.browser.find_element(
            *FilterFormLocators.REMOVE_ACTIVE_FILTER
        )

        remove_active_filter.click()

    def active_filters_contains(self, filter_type):
        active_filters = self.browser.find_element(
            *FilterFormLocators.ACTIVE_FILTERS
        ).text
        return active_filters.find(filter_type)
