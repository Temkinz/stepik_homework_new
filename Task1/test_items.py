
import time


locator_add_to_cart = "button.btn.btn-lg.btn-primary.btn-add-to-basket"


def test_page_language(browser):
	#Action
	language_link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"
	browser.get(language_link)
	time.sleep(30)
	button_exist = len(browser.find_elements_by_css_selector(locator_add_to_cart))

	#Assert
	assert  button_exist > 0, 'There is no AddtoTheCart button'
  