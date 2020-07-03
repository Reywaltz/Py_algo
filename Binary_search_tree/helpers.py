def validateBst(tree):
    return validateBstHelper(tree, float("-inf"), float("inf"))


def validateBstHelper(tree, minvalue: int, maxvalue: int) -> bool:
    """Метод проверки дерева на условия бинарного дерево

    :param tree: Проверяемое дерево
    :type tree: BST
    :param minvalue: диапазон минимального условия узла
    :type minvalue: int
    :param maxvalue: диапазон максимального условия узла
    :type maxvalue: int
    :return: Результат проерки
    :rtype: bool
    """
    if tree is None:
        return True
    if tree.value < minvalue or tree.value >= maxvalue:
        return False
    # Проверка левего поддерева
    leftIsValid = validateBstHelper(tree.left, minvalue, tree.value)
    # Проверка правого поддерева и вывод результата
    return leftIsValid and validateBstHelper(tree.right, tree.value, maxvalue)
