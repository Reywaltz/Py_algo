"""
Найти пару чисел списка, при котором их сумма будет равна искомому числу

Пример:
[3, 5, -4, 8, 11, 1, -1, 6], 10
Результирующая пара -> [11, -1]
"""


# Метод перебора всех величин списка
# Временная сложность -> O(n^2)
# Пространственная сложность -> O(1)
def one(lst, target_sum):
    for i in range(len(lst) - 1):
        for j in range(i+1, len(lst)):
            if lst[i] + lst[j] == target_sum:
                return (lst[i], lst[j])
    return None


# Метод поиска с использованием Хэш-таблиц
# Временная сложность -> O(n)
# Пространтсвенная сложность -> O(n)
def two(lst, target_sum):
    dct = {}
    for item in lst:
        if target_sum-item in dct:
            return (target_sum-item, item)
        else:
            dct[item] = True
    return None


# Метод поиска и использованием двух указателей, в отсортированном списке
# Временная сложность -> O(nlog(n))
# Пространственная сложность -> O(n)
def three(lst, target_sum):
    lst.sort()
    p_left, p_right = lst[0], lst[-1]
    while p_left + p_right != target_sum:
        if p_left + p_right > target_sum:
            p_right -= 1
        elif p_left + p_right < target_sum:
            p_left += 1
    return (p_left, p_right)


lst = [3, 5, -4, 8, 11, 1, -1, 6]
target_sum = 9

print(lst)
print(one(lst, target_sum))
print(two(lst, target_sum))
print(three(lst, target_sum))
