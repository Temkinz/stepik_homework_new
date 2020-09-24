import random
import time

main_page = "http://selenium1py.pythonanywhere.com/ru"
locator_login_link = "a#login_link"
locator_reg_input_email = "input#id_registration-email"
locator_reg_input_password1 = "input#id_registration-password1"
locator_reg_input_password2 = "input#id_registration-password2"
locator_reg_submit = "button[name = 'registration_submit']"
locator_login_message = "alertinner.wicon"


def test_registration(browser):
	#Data

    def emails():
        email = ''
        for x in range(12):
            email = email + random.choice(list('1234567890qwertyuiopASDFGHJKLZXCVBMNMNM'))
        email = email + '@gmail.com'
        return email

    password = "Test202020"        

    #Arrange      
    browser.implicitly_wait(3)
    browser.get(main_page)

    #Act
    browser.find_element_by_css_selector(locator_login_link).click()
    browser.find_element_by_css_selector(locator_reg_input_email).send_keys(emails())
    browser.find_element_by_css_selector(locator_reg_input_password1).send_keys(password)
    browser.find_element_by_css_selector(locator_reg_input_password2).send_keys(password)
    browser.find_element_by_css_selector(locator_reg_submit).click()

    message_reg = browser.find_element_by_class_name(locator_login_message)

    #Asserts
    assert "Спасибо за регистрацию" in message_reg.text, 'The user is not registered'
