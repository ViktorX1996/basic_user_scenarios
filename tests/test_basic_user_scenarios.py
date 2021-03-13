from tests.pages import todomvc


def test_basic_case():
    todomvc.visit()

    todomvc.add('a', 'b', 'c')
    todomvc.should_have('a', 'b', 'c')

    todomvc.edit('b', 'b edited')

    todomvc.toggle('b edited')
    todomvc.clear_completed()
    todomvc.should_have('a', 'c')

    todomvc.cancel_edit('c', 'c to be cancelled')

    todomvc.delete('c')
    todomvc.should_have('a')
