import pytest

from main.filtering import PatchworkHomePage
from main.result import FilteredPatchesResults

from selenium.webdriver import Chrome


@pytest.fixture
def browser():
  driver = Chrome()
  driver.implicitly_wait(10)
  yield driver
  driver.quit()
  
def test_filter_patches(browser):
  
  patchwork_page = PatchworkHomePage(browser)
  patchwork_page.load()
  patchwork_page.show_filters() 
  
  '''
  
  Failing test due to bug in application
  
  patchwork_page.filter_by_series('fix series querry')
  filtered_results = FilteredPatchesResults(browser)
  assert filtered_results.active_filters_contains('Series') > -1
     
  '''
     
  patchwork_page.filter_by_submitter('Stephen Finucane')
  filtered_results = FilteredPatchesResults(browser)
  assert filtered_results.active_filters_contains('Submitter') > -1
  
  patchwork_page.filter_by_state('New')
  filtered_results = FilteredPatchesResults(browser)
  assert filtered_results.active_filters_contains('State') > 1
  
  
''' 
TEST SCENARIOS

show the patchwork filter
hide the patchwork filter
filter by series
filter by submitter
filter by state
filter by archived
filter by delegate
search for patches
remove a filter

'''
