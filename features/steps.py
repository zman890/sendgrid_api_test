from lettuce import *
from lettuce_webdriver.util import *
from selenium.webdriver.common.keys import Keys
import time

@step('I go to the (.*) page')
def visit_page(step,url):
   world.browser.get(url)
   world.browser.maximize_window()

   
@step('I login as user "(.*)" with password "(.*)"')
def enter_credentials(step,username,password):
        world.browser.switch_to_frame(world.browser.find_element_by_css_selector("div#content>article>iframe"))
	user_field = world.browser.find_element_by_css_selector("input#key")
	password_field = world.browser.find_element_by_css_selector("input#secret")
	user_field.clear()
	password_field.clear()
	user_field.send_keys(username)
	password_field.send_keys(password)

@step('I display the mail form')
def expand_form(step):
  expand_link = world.browser.find_element_by_css_selector("div#body-container>ul>li:nth-of-type(6)>h3>div.action-container>ul>li.expand-methods>a")
  expand_link.click()
  time.sleep(5)	

@step('I fill in the \'(.*?)\' field with \'(.*?)\'')
def fill_in_field(step, fieldname, fieldvalue):
    if fieldname == "date":
       fieldlocator = world.browser.find_element_by_css_selector('body>div>ul>li:nth-of-type(6)>ul>li>form>table>tbody>tr:nth-of-type(10)>td>input')
    else:
       full_field_name = "params[" + fieldname + "]"
       fieldlocator = world.browser.find_element_by_name(full_field_name)
    fieldlocator.clear()
    fieldlocator.send_keys(fieldvalue)


@step('And submit the form')
def submit_form(step):
    world.browser.find_element_by_css_selector("input#Mail").click()
    #time.sleep(3)

@step('Then the response should indicate success')
def then_the_response_should_indicate_success(step):
    response_field = world.browser.find_element_by_css_selector("pre.response>span.str:nth-of-type(6)")
    response_text = response_field.text
    assert response_text == "\"success\""
    
    

