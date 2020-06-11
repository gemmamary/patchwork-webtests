from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.ui import Select

class PatchworkHomePage:
  URL = 'http://127.0.0.1:8000/project/patchwork/list/'
  
  submitter_xpath = '//div[@id="filterform"]//form//div[@class="form-group"][2]//div//div//div'
  
  state_xpath = '//div[@id="filterform"]//form//div[@class="form-group"][3]//div//select'
  
  SHOW_PATCH_FILTERS = (By.LINK_TEXT, 'Show patches with') 
  SERIES_INPUT = (By.ID, 'series_input')
  SUBMITTER_INPUT = (By.XPATH, submitter_xpath)
  STATE_INPUT = (By.XPATH, state_xpath)
  
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
    
  # WIP
  def filter_by_submitter(self, name):
    submitter_input = Select(self.browser.find_element(*self.SUBMITTER_INPUT))
    submitter_input.select_by_index(1)
       
  def filter_by_state(self, state):
    state_input = Select(self.browser.find_element(*self.STATE_INPUT))
    state_input.select_by_visible_text(state)
    
 
  
  '''
  
  def filter_by_archived(self, archived):
  
  def filter_by_delegate(self, name):
  
  '''
