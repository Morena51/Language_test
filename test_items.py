link='http://selenium1py.pythonanywhere.com/ru/catalogue/coders-at-work_207/'

def test_check_addbasketbutton(browser):
    browser.get(link)
    button=browser.find_element_by_css_selector('button.btn-add-to-basket')
    assert len(button.text)>0