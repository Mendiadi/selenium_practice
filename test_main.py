from functions import *
from selenium.webdriver import Chrome
import pytest
import  logging
LOGGER = logging.getLogger(__name__)


@pytest.fixture
def init_driver():
    driver = Chrome()
    yield driver
    driver.quit()


def test_drag_and_drop(init_driver):
    actual, excepted = drag_drop(driver=init_driver)
    LOGGER.info(f"actual results: {actual}, excepted result: {excepted}")
    assert actual == excepted


def test_alert(init_driver):
    actual, excepted = alert(driver=init_driver)
    LOGGER.info(f"actual results: {actual}, excepted result: {excepted}")
    for index,msg in enumerate(actual):
        assert msg == excepted[index]

def test_selection_register(init_driver):
    actual, excepted = selection_register(driver=init_driver)
    LOGGER.info(f"actual results: {actual}, excepted result: {excepted}")
    for msg in excepted:
        assert msg in actual

def test_iframe(init_driver):
    actual, excepted = iframe(driver=init_driver)
    LOGGER.info(f"actual results: {actual}, excepted result: {excepted}")
    for index, msg in enumerate(excepted):
        assert msg in actual[index]