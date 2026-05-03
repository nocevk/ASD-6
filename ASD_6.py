import random

class TreeNode:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

class BinarySearchTree:
    """Клас для роботи з бінарним деревом пошуку."""
    def __init__(self):
        self.root = None

    def insert(self, data):
        """Вставка нового елементу в дерево."""
        self.root = self._insert_recursive(self.root, data)

    def _insert_recursive(self, node, data):
        if node is None:
            return TreeNode(data)
        if data < node.data:
            node.left = self._insert_recursive(node.left, data)
        elif data > node.data:
            node.right = self._insert_recursive(node.right, data)
        return node

    def _get_min_value_node(self, node):
        current = node
        while current.left is not None:
            current = current.left
        return current

    def delete(self, data):
        """Видалення елементу з дерева."""
        self.root = self._delete_recursive(self.root, data)

    def _delete_recursive(self, node, data):
        if not node:
            return None

        if data < node.data:
            node.left = self._delete_recursive(node.left, data)
        elif data > node.data:
            node.right = self._delete_recursive(node.right, data)
        else:
            # Якщо один або нуль нащадків
            if not node.left:
                return node.right
            elif not node.right:
                return node.left

            # Якщо два нащадки
            temp = self._get_min_value_node(node.right)
            node.data = temp.data
            node.right = self._delete_recursive(node.right, temp.data)

        return node

    def get_inorder(self):
        """Отримання списку елементів (відсортованого) за допомогою симетричного обходу."""
        res = []
        self._get_inorder_recursive(self.root, res)
        return res

    def _get_inorder_recursive(self, node, res):
        if node:
            self._get_inorder_recursive(node.left, res)
            res.append(str(node.data))
            self._get_inorder_recursive(node.right, res)

    def print_tree(self):
        """Консольне візуальне виведення вмісту дерева."""
        self._print_tree_recursive(self.root, 0)

    def _print_tree_recursive(self, node, level):
        if node is not None:
            self._print_tree_recursive(node.right, level + 1)
            print(' ' * 4 * level + '->', node.data)
            self._print_tree_recursive(node.left, level + 1)

    # --- ІНДИВІДУАЛЬНІ ЗАВДАННЯ (ВАРІАНТ 5) ---

    def multiply_by_two(self):
        """Завдання 1: Збільшити всі елементи дерева в 2 рази (Зворотній обхід)."""
        self._multiply_postorder(self.root)

    def _multiply_postorder(self, node):
        if node:
            # Зворотній обхід: Лівий -> Правий -> Корінь
            self._multiply_postorder(node.left)
            self._multiply_postorder(node.right)
            node.data *= 2

    def is_almost_complete(self):
        """
        Завдання 2: Визначити, чи є дерево майже повним (Зворотній обхід).
        Використовуємо індексацію вузлів. Якщо максимальний індекс дорівнює
        загальній кількості вузлів, дерево є майже повним.
        """
        def _check_complete_postorder(node, index):
            if not node:
                return 0, 0
            
            # Зворотній обхід: збираємо дані з лівого і правого піддерев
            left_count, left_max_idx = _check_complete_postorder(node.left, 2 * index)
            right_count, right_max_idx = _check_complete_postorder(node.right, 2 * index + 1)
            
            # Обробка поточного вузла
            count = 1 + left_count + right_count
            max_idx = max(index, left_max_idx, right_max_idx)
            
            return count, max_idx

        if not self.root:
            return True

        total_nodes, max_index = _check_complete_postorder(self.root, 1)
        return total_nodes == max_index


# --- ГОЛОВНА ПРОГРАМА ---
def main():
    bst = BinarySearchTree()
    
    # Генерація 30 чисел (25 + 5) у діапазоні [-50, 50]
    variant = 5
    n = 25 + variant
    random_numbers = [random.randint(-50, 50) for _ in range(n)]
    
    print(f"Згенеровані числа ({n} шт): {random_numbers} - ASD_6.py:130")
    for num in random_numbers:
        bst.insert(num)

    print("\n Вміст дерева (візуально) - ASD_6.py:134")
    bst.print_tree()

    print("\n Відсортований вміст дерева (Inorder) - ASD_6.py:137")
    print(", - ASD_6.py:138".join(bst.get_inorder()))

    # Додавання елемента
    new_element = 100
    bst.insert(new_element)
    print(f"\n Після додавання елемента {new_element} - ASD_6.py:143")
    print(", - ASD_6.py:144".join(bst.get_inorder()))

    # Видалення елемента
    delete_element = random_numbers[0] # Видалимо перше згенероване число
    bst.delete(delete_element)
    print(f"\n Після видалення елемента {delete_element} - ASD_6.py:149")
    print(", - ASD_6.py:150".join(bst.get_inorder()))

    # Виконання додаткових операцій згідно з варіантом 5
    print("\n Перевірка на майже повне дерево - ASD_6.py:153")
    is_complete = bst.is_almost_complete()
    print("Дерево є майже повним! - ASD_6.py:155" if is_complete else "Дерево НЕ є майже повним.")

    print("\n Множення всіх елементів на 2 - ASD_6.py:157")
    bst.multiply_by_two()
    print("Дерево після множення (відсортоване): - ASD_6.py:159")
    print(", - ASD_6.py:160".join(bst.get_inorder()))


if __name__ == "__main__":
    main()