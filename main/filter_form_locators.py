from selenium.webdriver.common.by import By


class FilterFormLocators:

    submitter_xpath = (
        '//div[@id="filterform"]//form//div[@class="form-group"][2]//div//div//div'
    )
    SUBMITTER_INPUT = (By.XPATH, submitter_xpath)

    state_xpath = (
        '//div[@id="filterform"]//form//div[@class="form-group"][3]//div//select'
    )
    STATE_INPUT = (By.XPATH, state_xpath)

    search_xpath = (
        '//div[@id="filterform"]//form//div[@class="form-group"][4]//div//input'
    )
    SEARCH_INPUT = (By.XPATH, search_xpath)

    archived_xpath = '//div[@id="filterform"]//form//div[@class="form-group"][5]//div'
    ARCHIVED_INPUT = (By.XPATH, archived_xpath)

    delegate_xpath = (
        '//div[@id="filterform"]//form//div[@class="form-group"][6]//div//select'
    )
    DELEGATE_FILTER = (By.XPATH, delegate_xpath)

    submit_filter = '//button[@type="submit"]'
    SUBMIT_FILTER = (By.XPATH, submit_filter)

    SERIES_INPUT = (By.ID, "series_input")

    ACTIVE_FILTERS = (By.ID, "filtersummary")

    remove_active_filter = '//a[@class="filter-action"]//span'
    REMOVE_ACTIVE_FILTER = (By.XPATH, remove_active_filter)
