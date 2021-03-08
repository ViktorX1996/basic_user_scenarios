from tests.variables import todos


def test_basic_case():
    todos.go_to()

    todos.typing('a', 'b', 'c')
    todos.should_have('a', 'b', 'c')

    todos.edit('b', ' edited')

    todos.toggle('b edited')
    todos.clear_completed()
    todos.should_have('a', 'c')

    todos.cancel_edit('c', ' to be cancelled')

    todos.delete('c')
    todos.should_have('a')
