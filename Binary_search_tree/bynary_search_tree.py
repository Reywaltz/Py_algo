class BST:
    """
    Класс бинарного дерево поиска

    Основная идея данного дерева заключается в том, что элементы левого
    поддерева меньше своего родителя, а элементы правого - больше
    Пример:
        3
       / \
      1   5
     / \
    -5  2
    """
    def __init__(self, value: int):
        self.value = value
        self.left = None
        self.right = None

    def insert(self, value: int):
        """Метод вставки элемента в дерево.
        Сравниваем значение, которое нужно вставить со значением узла
        Если оно меньше, то обрасываем правое поддерево(или левое, если больше)
        и продолжаем итерации пока мы не дойдём по листа.
        Если у узла нет детей, то создаём узел слева или справа в зависимости
        от величины

        # Средний случай
        # Временная сложность -> O(log(n))
        # Пространтсвенная сложность -> O(1), так как алгоритм
        # выполнен итеративно
        # При рекурсивной реализации сложность -> O(log(n)) или O(D)
        # где D - величина вызова стека

        # Худший случай
        # Временная сложность -> O(N)
        # Пространтсвенная сложность -> O(1), так как алгоритм
        # выполнен итеративно
        # При рекурсивной реализации сложность -> O(N) или O(D)
        # где D - величина вызова стека

        :param value: Значение, которое необходимо вставить
        :type value: int
        :return: BST
        :rtype: BST
        """
        current_Node = self
        while True:
            if value < current_Node.value:
                if current_Node.left is None:
                    current_Node.left = BST(value)
                    break
                else:
                    current_Node = current_Node.left
            else:
                if current_Node.right is None:
                    current_Node.right = BST(value)
                    break
                else:
                    current_Node = current_Node.right
        return self

    def contains(self, value: int) -> bool:
        """Метод проверки наличия элемента в дереве

        :param value: Проверяемое значение
        :type value: int
        :return: Результат поиска
        :rtype: bool
        """
        current_Node = self
        while current_Node is not None:
            if value < current_Node.value:
                current_Node = current_Node.left
            elif value >= current_Node.value:
                current_Node = current_Node.right
            else:
                return True
        return False

    def remove(self, value: int, parent_Node=None):
        """Метод удаления элемента из дерева

        # Средний случай
        # Временная сложность -> O(log(n))
        # Пространтсвенная сложность -> O(1), так как алгоритм
        # выполнен итеративно
        # При рекурсивной реализации сложность -> O(log(n)) или O(D)
        # где D - величина вызова стека

        # Худший случай
        # Временная сложность -> O(N)
        # Пространтсвенная сложность -> O(1), так как алгоритм
        # выполнен итеративно
        # При рекурсивной реализации сложность -> O(N) или O(D)
        # где D - величина вызова стека

        :param value: Удаляемое значение
        :type value: int
        :param parent_Node: Узел-родитель текущего элемента, defaults to None
        :type parent_Node: BST, optional
        :return: Дерево без удалённым элемента
        :rtype: BST
        """
        current_Node = self
        # Добираемся до нужного элемента и храним значение родителя
        while current_Node is not None:
            if value < current_Node.value:
                parent_Node = current_Node
                current_Node = current_Node.left
            elif value > current_Node.value:
                parent_Node = current_Node
                current_Node = current_Node.right
            else:
                # Если у узла есть два ребёнка, ищем минимальное среди правых
                # поддеревьев, для соблюдения условия бинарного дерева
                if current_Node.left is not None and current_Node.right is not None:  # Noqa
                    current_Node.value = current_Node.right.get_Min_value()
                    # Удаляем минимальный найденный узел из дерева
                    current_Node.right.remove(current_Node.value, current_Node)
                # Если удаляем корень дерева
                elif parent_Node is None:
                    if current_Node.left is not None:
                        current_Node.value = current_Node.left.value
                        current_Node.right = current_Node.left.right
                        current_Node.left = current_Node.left.left
                    elif current_Node.right is not None:
                        current_Node.value = current_Node.right.value
                        current_Node.left = current_Node.right.left
                        current_Node.right = current_Node.right.right
                    else:
                        current_Node.value = None
                # Если удаляемый узел является листом
                elif parent_Node.left == current_Node:
                    parent_Node.left = current_Node.left if current_Node.left is not None else current_Node.right # Noqa
                elif parent_Node.right == current_Node:
                    parent_Node.right = current_Node.left if current_Node.left is not None else current_Node.right # Noqa
                break
        return self

    def get_Min_value(self):
        """Поиск минимального узла в дереве

        :return: Значение минимального узла
        :rtype: int
        """
        current_Node = self
        while current_Node.left is not None:
            current_Node = current_Node.left
        return current_Node.value
