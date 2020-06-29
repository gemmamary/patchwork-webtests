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

