from tests.pages import todomvc


def test_add():
    todomvc.visit()

    todomvc.add('a', 'b', 'c')

    todomvc.should_have('a', 'b', 'c')
    todomvc.should_have_items_left(3)


def test_edit_by_enter():
    todomvc.visit()
    todomvc.add('a', 'b', 'c')

    todomvc.edit('b', 'b edited')

    todomvc.should_have('a', 'b edited', 'c')\
        .should_have_items_left(3)


def test_edit_by_tab():
    todomvc.visit()
    todomvc.add('a', 'b', 'c')

    todomvc.edit_by_tab('b', 'b edited')

    todomvc.should_have('a', 'b edited', 'c')\
        .should_have_items_left(3)


def test_cancel_edit():
    todomvc.visit()
    todomvc.add('a', 'b', 'c')

    todomvc.cancel_edit('b', 'b to be cancelled')

    todomvc.should_have('a', 'b', 'c')\
        .should_have_items_left(3)


def test_delete_by_edit_to_empty_field():
    todomvc.visit()
    todomvc.add('a', 'b', 'c')

    todomvc.edit('b', '')

    todomvc.should_have('a', 'c')\
        .should_have_items_left(2)


def test_complete_one():
    todomvc.visit()
    todomvc.add('a', 'b', 'c')

    todomvc.toggle('b')

    todomvc.should_have_completed('b')
    todomvc.should_have_active('a', 'c')
    todomvc.should_have_items_left(2)


def test_activate_one():
    todomvc.visit()
    todomvc.add('a', 'b', 'c')
    todomvc.toggle_all()

    todomvc.toggle('b')

    todomvc.should_have_active('b')\
        .should_have_completed('a', 'c')\
        .should_have_items_left(1)


def test_complete_all():
    todomvc.visit()
    todomvc.add('a', 'b', 'c')

    todomvc.toggle_all()

    todomvc.should_have_active()\
        .should_have_completed('a', 'b', 'c')\
        .should_have_items_left(0)


def test_activate_all():
    todomvc.visit()
    todomvc.add('a', 'b', 'c')
    todomvc.toggle_all()

    todomvc.toggle_all()

    todomvc.should_have_active('a', 'b', 'c')\
        .should_have_completed()\
        .should_have_items_left(3)


def test_clear_completed():
    todomvc.visit()
    todomvc.add('a', 'b', 'c', 'd')
    todomvc.toggle('b')
    todomvc.toggle('c')

    todomvc.clear_completed()

    todomvc.should_have_active('a', 'd')\
        .should_have_items_left(2)


def test_by_button_delete():
    todomvc.visit()
    todomvc.add('a', 'b', 'c')

    todomvc.delete('b')

    todomvc.should_have('a', 'c')\
        .should_have_items_left(2)



