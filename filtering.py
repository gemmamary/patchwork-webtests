from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

class PatchworkHomePage:
  URL = 'http://127.0.0.1:8000/project/patchwork/list/'
  
  SHOW_PATCH_FILTERS = (By.LINK_TEXT, 'Show patches with') 
  SERIES_INPUT = (By.ID, 'series_input')
  SUBMITTER_INPUT = (By.ID, 'submitter_input')
  APPLY_FILTER = (By.XPATH, '//button[@type="submit"]')
  
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
    submitter_input = self.browser.find_element(*self.SUBMITTER_INPUT)
    apply_filter = self.browser.find_element(*self.APPLY_FILTER)
    submitter_input.execute_script("setAttribute('value', '70')", submitter_input)
    apply_filter.click()
    
    
    
    
  
  '''
    
  def filter_by_state(self, state):
  
  def filter_by_archived(self, archived):
  
  def filter_by_delegate(self, name):
  
  '''
