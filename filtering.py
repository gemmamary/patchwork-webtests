from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select

class PatchworkHomePage:

  URL = 'http://127.0.0.1:8000/project/patchwork/list/'
  
  submitter_xpath = '//div[@id="filterform"]//form//div[@class="form-group"][2]//div//div//div'
  state_xpath = '//div[@id="filterform"]//form//div[@class="form-group"][3]//div//select'
  search_xpath = '//div[@id="filterform"]//form//div[@class="form-group"][4]//div//input'
  archived_xpath = '//div[@id="filterform"]//form//div[@class="form-group"][5]//div'
  delegate_xpath = '//div[@id="filterform"]//form//div[@class="form-group"][6]//div//select'
  submit_filter = '//button[@type="submit"]'
  
  SHOW_PATCH_FILTERS = (By.LINK_TEXT, 'Show patches with') 
  SERIES_INPUT = (By.ID, 'series_input')
  
  SUBMITTER_INPUT = (By.XPATH, submitter_xpath)
  STATE_INPUT = (By.XPATH, state_xpath)
  SEARCH_INPUT = (By.XPATH, search_xpath)
  ARCHIVED_INPUT = (By.XPATH, archived_xpath)
  DELEGATE_FILTER = (By.XPATH, delegate_xpath)
  SUBMIT_FILTER = (By.XPATH, submit_filter)
  
  def __init__(self, browser):
    self.browser = browser
    
  def load(self):
    self.browser.get(self.URL)
    
  def show_filters(self):
    show_patch_filters = self.browser.find_element(*self.SHOW_PATCH_FILTERS)
    show_patch_filters.click()
    
  def filter_by_series(self, title):
    series_input = self.browser.find_element(*self.SERIES_INPUT)
    series_input.send_keys(title + Keys.RETURN)
  
  def filter_by_submitter(self, name):
    submitter_input = Select(self.browser.find_element(*self.SUBMITTER_INPUT))
    submitter_input.select_by_index(1)
       
  def filter_by_state(self, state):
    state_input = Select(self.browser.find_element(*self.STATE_INPUT))
    state_input.select_by_visible_text(state)
    
  def filter_by_search_term(self, term):
    search_input = self.browser.find_element(*self.SEARCH_INPUT)
    search_input.send_keys(term + Keys.RETURN)

  def filter_by_archived(self, archived):
    archived_input = self.browser.find_element(*self.ARCHIVED_INPUT).find_elements_by_tag_name('input')
    submit_filter = self.browser.find_element(*self.SUBMIT_FILTER)
    
    for input in archived_input:
      input.get_attribute('value')
      if(input == archived):
        input.click()
        
    submit_filter.click()
    
  def filter_by_delegate(self, name):
    delegate_filter = Select(self.browser.find_element(*self.DELEGATE_FILTER))
    submit_filter = self.browser.find_element(*self.SUBMIT_FILTER)
    delegate_filter.select_by_value(name)
    
    submit_filter.click()
