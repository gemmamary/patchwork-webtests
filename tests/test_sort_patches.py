import pytest
import json

from main.sort_patches import SortPatches
from main.sort_patches_locators import SortPatchesLocators


def test_sort_patches(browser, base_url):

    homepage = SortPatches(browser)
    homepage.load(base_url)

    homepage.sort_patches(SortPatchesLocators.SORT_BY_PATCH)

    assert SortPatchesLocators.SORTED_BY_PATCHES