from selene import have
from selene.support.shared import browser

todo_list = browser.all('#todo-list>li')


def go_to():
    browser.open('https://todomvc4tasj.herokuapp.com/')
    script_on_clear_completed = "return 'click' in $._data($('#clear-completed')[0],'events')"
    browser.should(have.js_returned(True, script_on_clear_completed))


def adding(*texts: str):
    for text in texts:
        browser.element('#new-todo').type(text).press_enter()


def should_have(*texts: str):
    todo_list.should(have.exact_texts(*texts))


def start_editing(text: str, new_text: str):
    todo_list.element_by(have.exact_text(text)).double_click()
    return todo_list.element_by(have.css_class('editing')) \
        .element('.edit').type(new_text)


def edit(text: str, new_text: str):
    start_editing(text, new_text).press_enter()


def toggle(text: str):
    todo_list.element_by(have.exact_text(text)).element(".toggle").click()


def clear_completed():
    browser.element('#clear-completed').click()


def cancel_edit(text: str, new_text: str):
    start_editing(text, new_text).press_escape()


def delete(text: str):
    todo_list.element_by(have.exact_text(text)) \
        .hover().element(".destroy").click()