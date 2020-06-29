import pytest
import json

from main.filtering import PatchworkFilterForm
    

# fails due to bug in application

def test_filter_by_series(browser, base_url):

    homepage = PatchworkFilterForm(browser)
    homepage.load(base_url)
    homepage.show_filters()

    homepage.filter_by_series("fix series querry")
    
    assert homepage.active_filters_contains("Series") > -1


# fails due to bug in application

def test_filter_by_submitter(browser, base_url):

    homepage = PatchworkFilterForm(browser)
    homepage.load(base_url)
    homepage.show_filters()

    homepage.filter_by_submitter("Stephen Finucane")

    assert homepage.active_filters_contains("Submitter") > -1


def test_filter_by_state(browser, base_url):

    homepage = PatchworkFilterForm(browser)
    homepage.load(base_url)
    homepage.show_filters()

    homepage.filter_by_state("New")

    assert homepage.active_filters_contains("State") > 1


def test_filter_by_search_term(browser, base_url):

    homepage = PatchworkFilterForm(browser)
    homepage.load(base_url)
    homepage.show_filters()

    homepage.filter_by_search_term("query")

    assert homepage.active_filters_contains("Search") > 1


def test_filter_by_archived(browser, base_url):

    homepage = PatchworkFilterForm(browser)
    homepage.load(base_url)
    homepage.show_filters()

    homepage.filter_by_archived("both")

    assert homepage.active_filters_contains("Archived") > 1


def test_filter_by_delegate(browser, base_url):

    homepage = PatchworkFilterForm(browser)
    homepage.load(base_url)
    homepage.show_filters()

    homepage.filter_by_delegate("Nobody")

    assert homepage.active_filters_contains("Delegate") > 1
