from selenium.webdriver.common.by import By

class SortPatchesLocators: 

    patches_sort = '//table[@id="patchlist"]//thead//tr//th[1]//a'
    date_sort = '//table[@id="patchlist"]//thead//tr//th[5]//a[2]'
    submitter_sort = '//table[@id="patchlist"]//thead//tr//th[6]//a'
    delegate_sort = '//table[@id="patchlist"]//thead//tr//th[7]//a'
    state_sort = '//table[@id="patchlist"]//thead//tr//th[8]//a'


    SORT_BY_PATCH = (By.XPATH, patches_sort)

    SORT_BY_DATE = (By.XPATH, date_sort)

    SORT_BY_SUBMITTER = (By.XPATH, submitter_sort)

    SORT_BY_DELEGATE = (By.XPATH, delegate_sort)

    SORT_BY_STATE = (By.XPATH, state_sort)
    