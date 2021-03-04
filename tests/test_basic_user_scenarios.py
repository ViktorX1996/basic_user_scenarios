
from selene.support.conditions import have
from selene.support.shared import browser


def test_basic_case():
    browser.open('https://todomvc4tasj.herokuapp.com/')
    script_on_clear_completed = "return 'click' in $._data($('#clear-completed')[0],'events')"
    browser.should(have.js_returned(True, script_on_clear_completed))

    # add
    browser.element('#new-todo').type('a').press_enter()
    browser.element('#new-todo').type('b').press_enter()
    browser.element('#new-todo').type('c').press_enter()
    browser.all('#todo-list>li').should(have.exact_texts('a', 'b', 'c'))

    # edit
    browser.all('#todo-list>li').element_by(have.exact_text('b')).double_click()
    browser.all('#todo-list>li').element_by(have.css_class('editing')) \
        .element('.edit').type(' edited').press_enter()

    # complete & clear
    browser.all('#todo-list>li').element_by(have.exact_text('b edited')) \
        .element(".toggle").click()
    browser.element('#clear-completed').click()
    browser.all('#todo-list>li').should(have.exact_texts('a', 'c'))

    # cancel edit
    browser.all('#todo-list>li').element_by(have.exact_text('c')).double_click()
    browser.all('#todo-list>li').element_by(have.css_class('editing')) \
        .element('.edit').type(' to be canceled').press_escape()

    # delete
    browser.all('#todo-list>li').element_by(have.exact_text('c')) \
        .hover().element(".destroy").click()
    browser.all('#todo-list>li').should(have.exact_texts('a'))
