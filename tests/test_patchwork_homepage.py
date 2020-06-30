import pytest
import json

from main.patchwork_home import PatchworkHome
from main.patchwork_home_locators import PatchworkHomeLocators

def test_show_filters(browser, base_url):
    
    homepage = PatchworkHome(browser)
    homepage.load(base_url)
    homepage.show_filters()

    assert homepage.filter_form_is_displayed()

def test_hide_filters(browser, base_url):
    
    homepage = PatchworkHome(browser)
    homepage.load(base_url)

    if(homepage.filter_form_is_displayed()):
        homepage.show_filters()
    else: 
        homepage.show_filters()
        homepage.show_filters()

    assert homepage.filter_form_is_hidden()

def test_patchwork_home_icon(browser, base_url):

    homepage = PatchworkHome(browser)
    homepage.load(base_url)

    homepage.navigate_home()
    
    assert browser.current_url == base_url

def test_navigate_to_bundles_page(browser, base_url):

    homepage = PatchworkHome(browser)
    homepage.load(base_url)

    homepage.navigate_to_bundles()
    
    assert browser.current_url.find("user/login/?next=/project/patchwork/bundles/") > -1