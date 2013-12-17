from lettuce import before, world, after
from selenium import webdriver
import lettuce_webdriver.webdriver

@before.all
def setup_browser():
    world.browser = webdriver.Firefox()
    world.browser.implicitly_wait(5)

@after.all
def tear_down_feature(feature):
    world.browser.quit()
