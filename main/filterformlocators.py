
class FilterFormLocators: 

    submitter_xpath = (
        '//div[@id="filterform"]//form//div[@class="form-group"][2]//div//div//div'
    )

    state_xpath = (
        '//div[@id="filterform"]//form//div[@class="form-group"][3]//div//select'
    )

    search_xpath = (
        '//div[@id="filterform"]//form//div[@class="form-group"][4]//div//input'
    )

    archived_xpath = '//div[@id="filterform"]//form//div[@class="form-group"][5]//div'

    delegate_xpath = (
        '//div[@id="filterform"]//form//div[@class="form-group"][6]//div//select'
    )
    
    submit_filter = '//button[@type="submit"]'