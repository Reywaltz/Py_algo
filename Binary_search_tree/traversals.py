# Методы обхода BST дерева
# Временная сложность => O(N)
# Пространственная сложности => O(N)/O(D),
# Где D => кол-во вызовов функции(кол-во уровеней дерева)


def inorder_traverse(tree, lst: list) -> list:
    """
    In-order - обход "сверху-вниз" по левому поддереву
    Ex:
        3
       / \
      1   5   ===> Res: [-5, 1, 2, 3, 5]
     / \
    -5  2

    :param tree: BST-дерево
    :type tree: BST
    :param lst: Список вывода элементов дерева
    :type lst: list
    :return: Список вывода элементов дерева
    :rtype: list
    """
    if tree is not None:
        # Пробегаемся по левым поддеревьям
        inorder_traverse(tree.left, lst)
        # Добавляем последний лист в список
        lst.append(tree.value)
        # Пробегаемся по правым поддеревьям
        inorder_traverse(tree.right, lst)
    return lst


def preorder_traverse(tree, lst: list) -> list:
    """
    Pre-order - обход "снизу-вверх" по возрастанию
    Ex:
        3
       / \
      1   5   ===> Res: [3, 1, -5, 2, 5]
     / \
    -5  2

    :param tree: BST-дерево
    :type tree: BST
    :param lst: Список вывода элементов дерева
    :type lst: list
    :return: Список вывода элементов дерева
    :rtype: list
    """
    if tree is not None:
        # Добавляем текущий лист в список
        lst.append(tree.value)
        # Пробегаемся по левым поддеревьям
        preorder_traverse(tree.left, lst)
        # Пробегаемся по правым поддеревьям
        preorder_traverse(tree.right, lst)
    return lst


def postorder_traverse(tree, lst: list) -> list:
    """
    Post_order - обход "снизу-вверх" по уровню дерева
    Ex:
        3
       / \
      1   5   ===> Res: [-5, 2, 1, 5, 3]
     / \
    -5  2

    :param tree: BST-дерево
    :type tree: BST
    :param lst: Список вывода элементов дерева
    :type lst: list
    :return: Список вывода элементов дерева
    :rtype: list
    """
    if tree is not None:
        # Пробегаемся по левым поддеревьям
        postorder_traverse(tree.left, lst)
        # Пробегаемся по правым поддеревьям
        postorder_traverse(tree.right, lst)
        # Добавляем лист текущего уровня в список
        lst.append(tree.value)
    return lst
