from selene import have, command
from selene.support.shared import browser


def go_to():
    browser.open('https://todomvc4tasj.herokuapp.com/')
    script_on_clear_completed = "return 'click' in $._data($('#clear-completed')[0],'events')"
    browser.should(have.js_returned(True, script_on_clear_completed))


def typing(*texts: str):
    for text in texts:
        browser.element('#new-todo').type(text).press_enter()


def should_have(*texts: str):
    browser.all('#todo-list>li').should(have.exact_texts(*texts))


def edit(text: str, new_text: str):
    browser.all('#todo-list>li').element_by(have.exact_text(text)).double_click()
    browser.all('#todo-list>li').element_by(have.css_class('editing')) \
        .element('.edit').type(new_text).press_enter()


def toggle(text: str):
    browser.all('#todo-list>li').element_by(have.exact_text(text)).element(".toggle").click()


def clear_completed():
    browser.element('#clear-completed').click()


def cancel_edit(text: str, new_text: str):
    browser.all('#todo-list>li').element_by(have.exact_text(text)).double_click()
    browser.all('#todo-list>li').element_by(have.css_class('editing')) \
        .element('.edit').type(new_text).press_escape()


def delete(text: str):
    browser.all('#todo-list>li').element_by(have.exact_text(text)) \
        .hover().element(".destroy").click()