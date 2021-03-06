import json
import pytest

from selenium import webdriver
from selenium.webdriver import Chrome, Firefox


CONFIG_PATH = "tests/config.json"
DEFAULT_WAIT_TIME = 10
SUPPORTED_BROWSERS = ["chrome", "firefox"]


@pytest.fixture(scope="session")
def config():
    with open(CONFIG_PATH) as config_file:
        data = json.load(config_file)
    return data


@pytest.fixture(scope="session")
def config_browser(config):
    if "browser" not in config:
        raise Exception('The config file does not contain "browser"')
    elif config["browser"] not in SUPPORTED_BROWSERS:
        raise Exception('Not suppoerted browser')
    return config["browser"]


@pytest.fixture(scope="session")
def config_wait_time(config):
    return config["wait_time"] if "wait_time" in config else DEFAULT_WAIT_TIME


@pytest.fixture
def browser(config_browser, config_wait_time):
    if config_browser == "chrome":
        driver = Chrome()
    elif config_browser == "firefox":
        driver = Firefox()
    else:
        raise Exception('Not suppoerted browser')
    driver.implicitly_wait(config_wait_time)
    yield driver
    driver.quit()


@pytest.fixture
def base_url(config):
    if "base_url" not in config:
        raise Exception('The config file does not contain "base_url"')
    return config["base_url"]
