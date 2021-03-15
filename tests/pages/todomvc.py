from selene import have, command
from selene.support.shared import browser


class TodoMvc:
    def __init__(self):
        self.todo_list = browser.all('#todo-list>li')

    def visit(self):
        browser.open('https://todomvc4tasj.herokuapp.com/')
        script_on_clear_completed = "return 'click' in $._data($('#clear-completed')[0],'events')"
        browser.should(have.js_returned(True, script_on_clear_completed))
        return self

    def add(self, *texts):
        for text in texts:
            browser.element('#new-todo').type(text).press_enter()
        return self

    def should_have(self, *texts):
        self.todo_list.should(have.exact_texts(*texts))
        return self

    def should_have_items_left(self, amount: int):
        browser.element('#todo-count>strong')\
            .should(have.exact_text(str(amount)))
        return self

    def start_editing(self, text, new_text):
        self.todo_list.element_by(have.exact_text(text)).double_click()
        return self.todo_list.element_by(have.css_class('editing')) \
            .element('.edit').perform(command.js.set_value(new_text))

    def edit(self, text, new_text):
        self.start_editing(text, new_text).press_enter()
        return self

    def edit_by_tab(self, text, new_text):
        self.start_editing(text, new_text).press_tab()
        return self

    def cancel_edit(self, text, new_text):
        self.start_editing(text, new_text).press_escape()
        return self

    def toggle(self, text):
        self.todo_list.element_by(have.exact_text(text))\
            .element(".toggle").click()
        return self

    def should_have_completed(self, *texts):
        self.todo_list.filtered_by(have.css_class('completed'))\
            .should(have.exact_texts(*texts))
        return self

    def should_have_active(self, *texts):
        self.todo_list.filtered_by(have.no.css_class('completed'))\
            .should(have.exact_texts(*texts))
        return self

    def toggle_all(self):
        browser.element('#toggle-all').click()
        return self

    def delete(self, text):
        self.todo_list.element_by(have.exact_text(text)).hover() \
            .element('.destroy').click()
        return self

    def clear_completed(self):
        browser.element('#clear-completed').click()
        return self

