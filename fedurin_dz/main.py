import tkinter as tk
from tkinter import messagebox, simpledialog
import random
import string
import time

# Функции для сортировки и измерения времени
def read_array_from_file(file_path):
    with open(file_path, 'r') as file:
        content = file.read().strip()
        if content.startswith('[') and content.endswith(']'):
            content = content[1:-1]
        array = list(map(int, content.split(',')))
    return array

# Сортировка пузырьком: Простая сортировка, которая многократно проходит по списку,
# сравнивая соседние элементы и меняя их местами, если они в неправильном порядке.
def bubble_sort(arr):
    n = len(arr)
    for i in range(n):
        for j in range(0, n-i-1):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]

# Сортировка вставками: Строит отсортированный массив один элемент за раз,
# перемещая каждый новый элемент в подходящее место среди уже отсортированных элементов.
def insertion_sort(arr):
    for i in range(1, len(arr)):
        key = arr[i]
        j = i-1
        while j >= 0 and key < arr[j]:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key

# Сортировка слиянием: Рекурсивная сортировка, которая делит массив на две половины,
# сортирует каждую половину и затем объединяет отсортированные половины.
def merge_sort(arr):
    if len(arr) > 1:
        mid = len(arr) // 2
        L = arr[:mid]
        R = arr[mid:]

        merge_sort(L)
        merge_sort(R)

        i = j = k = 0

        while i < len(L) and j < len(R):
            if L[i] < R[j]:
                arr[k] = L[i]
                i += 1
            else:
                arr[k] = R[j]
                j += 1
            k += 1

        while i < len(L):
            arr[k] = L[i]
            i += 1
            k += 1

        while j < len(R):
            arr[k] = R[j]
            j += 1
            k += 1

# Быстрая сортировка: Выбирает опорный элемент и делит массив на подмассивы
# с элементами, меньшими и большими опорного, затем рекурсивно сортирует подмассивы.
def quick_sort(arr):
    if len(arr) <= 1:
        return arr
    else:
        pivot = arr[len(arr) // 2]
        left = [x for x in arr if x < pivot]
        middle = [x for x in arr if x == pivot]
        right = [x for x in arr if x > pivot]
        return quick_sort(left) + middle + quick_sort(right)

# Сортировка подсчетом: Сортировка, которая подсчитывает количество вхождений каждого элемента
# и использует эти подсчеты для определения позиций элементов в отсортированном массиве.
def counting_sort(arr):
    max_val = max(arr)
    m = max_val + 1
    count = [0] * m

    for a in arr:
        count[a] += 1

    i = 0
    for a in range(m):
        for c in range(count[a]):
            arr[i] = a
            i += 1

# Измерение времени выполнения сортировки
def measure_time(sort_function, arr):
    start_time = time.time()
    sorted_arr = sort_function(arr) if sort_function == quick_sort else sort_function(arr.copy())
    end_time = time.time()
    return end_time - start_time

class App:
    def __init__(self, root):
        self.root = root
        self.root.title("Задания")
        self.create_widgets()

    def create_widgets(self):
        self.task_selection = tk.StringVar(self.root)
        self.task_selection.set("Выберите задание")

        self.tasks = [
            "02.03 Задание 1.1: Генерация случайных вопросов и ответов",
            "02.03 Задание 1.2: Управление инвентарем",
            "02.03 Задание 1.3: Генерация случайных паролей",
            "16.03 Симулятор кассы. Часть 1",
            "16.03 Симулятор кассы. Часть 2",
            "20.04 Поиск места разделения 0 и 1 в массиве",
            "27.04 Сортировки в массиве",
            "Задача 1: Проверка простого числа",
            "Задача 2: Сумма чисел в массиве",
            "Задача 3: Подсчет положительных и отрицательных чисел в массиве",
            "Задача 4: Найти наибольшее и наименьшее число в массиве"
        ]

        self.dropdown = tk.OptionMenu(self.root, self.task_selection, *self.tasks)
        self.dropdown.pack(pady=20)

        self.select_button = tk.Button(self.root, text="Выбрать задание", command=self.select_task)
        self.select_button.pack(pady=20)

    def select_task(self):
        task = self.task_selection.get()
        if task == "02.03 Задание 1.1: Генерация случайных вопросов и ответов":
            self.random_question_answer()
        elif task == "02.03 Задание 1.2: Управление инвентарем":
            self.inventory_management()
        elif task == "02.03 Задание 1.3: Генерация случайных паролей":
            self.password_generator()
        elif task == "16.03 Симулятор кассы. Часть 1":
            self.cash_register_simulator_part1()
        elif task == "16.03 Симулятор кассы. Часть 2":
            self.cash_register_simulator_part2()
        elif task == "20.04 Поиск места разделения 0 и 1 в массиве":
            self.find_split_point()
        elif task == "27.04 Сортировки в массиве":
            self.sorting_algorithms()
        elif task == "Задача 1: Проверка простого числа":
            self.check_prime()
        elif task == "Задача 2: Сумма чисел в массиве":
            self.sum_of_array()
        elif task == "Задача 3: Подсчет положительных и отрицательных чисел в массиве":
            self.count_positive_negative()
        elif task == "Задача 4: Найти наибольшее и наименьшее число в массиве":
            self.find_max_min()
        else:
            messagebox.showinfo("Ошибка", "Пожалуйста, выберите задание из списка.")

    # Задание 1.1: Генерация случайных вопросов и ответов
    def random_question_answer(self):
        questions = {}

        def add_question():
            question = simpledialog.askstring("Добавить вопрос", "Введите вопрос:")
            answer = simpledialog.askstring("Добавить ответ", "Введите ответ:")
            if question and answer:
                questions[question] = answer
                messagebox.showinfo("Успех", "Вопрос и ответ добавлены!")

        def edit_question():
            question = simpledialog.askstring("Редактировать вопрос", "Введите вопрос для редактирования:")
            if question in questions:
                new_answer = simpledialog.askstring("Редактировать ответ", "Введите новый ответ:")
                if new_answer:
                    questions[question] = new_answer
                    messagebox.showinfo("Успех", "Ответ обновлен!")
            else:
                messagebox.showerror("Ошибка", "Вопрос не найден!")

        def delete_question():
            question = simpledialog.askstring("Удалить вопрос", "Введите вопрос для удаления:")
            if question in questions:
                del questions[question]
                messagebox.showinfo("Успех", "Вопрос удален!")
            else:
                messagebox.showerror("Ошибка", "Вопрос не найден!")

        def answer_question():
            if questions:
                question = random.choice(list(questions.keys()))
                answer = questions[question]
                messagebox.showinfo("Вопрос", f"Вопрос: {question}\nОтвет: {answer}")
            else:
                messagebox.showinfo("Вопросы отсутствуют", "Добавьте вопросы, чтобы продолжить.")

        root = tk.Toplevel(self.root)
        root.title("Генерация случайных вопросов и ответов")

        add_button = tk.Button(root, text="Добавить вопрос", command=add_question)
        add_button.pack(pady=10)

        edit_button = tk.Button(root, text="Редактировать вопрос", command=edit_question)
        edit_button.pack(pady=10)

        delete_button = tk.Button(root, text="Удалить вопрос", command=delete_question)
        delete_button.pack(pady=10)

        answer_button = tk.Button(root, text="Ответить на случайный вопрос", command=answer_question)
        answer_button.pack(pady=10)

    # Задание 1.2: Управление инвентарем
    def inventory_management(self):
        inventory = {}

        def add_item():
            item = simpledialog.askstring("Добавить предмет", "Введите название предмета:")
            description = simpledialog.askstring("Описание предмета", "Введите описание предмета:")
            if item and description:
                inventory[item] = description
                messagebox.showinfo("Успех", "Предмет добавлен!")

        def remove_item():
            item = simpledialog.askstring("Удалить предмет", "Введите название предмета для удаления:")
            if item in inventory:
                del inventory[item]
                messagebox.showinfo("Успех", "Предмет удален!")
            else:
                messagebox.showerror("Ошибка", "Предмет не найден!")

        def view_item():
            item = simpledialog.askstring("Просмотреть предмет", "Введите название предмета для просмотра:")
            if item in inventory:
                description = inventory[item]
                messagebox.showinfo("Описание предмета", f"{item}: {description}")
            else:
                messagebox.showerror("Ошибка", "Предмет не найден!")

        def list_inventory():
            if inventory:
                items = "\n".join([f"{item}: {description}" for item, description in inventory.items()])
                messagebox.showinfo("Инвентарь", items)
            else:
                messagebox.showinfo("Инвентарь пуст", "Добавьте предметы, чтобы продолжить.")

        root = tk.Toplevel(self.root)
        root.title("Управление инвентарем")

        add_button = tk.Button(root, text="Добавить предмет", command=add_item)
        add_button.pack(pady=10)

        remove_button = tk.Button(root, text="Удалить предмет", command=remove_item)
        remove_button.pack(pady=10)

        view_button = tk.Button(root, text="Просмотреть предмет", command=view_item)
        view_button.pack(pady=10)

        list_button = tk.Button(root, text="Список инвентаря", command=list_inventory)
        list_button.pack(pady=10)

    # Задание 1.3: Генерация случайных паролей
    def password_generator(self):
        def generate_passwords():
            length = simpledialog.askinteger("Длина пароля", "Введите желаемую длину пароля:")
            use_digits = messagebox.askyesno("Использовать цифры", "Хотите использовать цифры в пароле?")
            use_symbols = messagebox.askyesno("Использовать символы", "Хотите использовать символы в пароле?")
            use_uppercase = messagebox.askyesno("Использовать заглавные буквы", "Хотите использовать заглавные буквы в пароле?")

            if not length:
                return

            characters = string.ascii_lowercase
            if use_digits:
                characters += string.digits
            if use_symbols:
                characters += string.punctuation
            if use_uppercase:
                characters += string.ascii_uppercase

            passwords = []
            for _ in range(5):
                password = ''.join(random.choice(characters) for _ in range(length))
                passwords.append(password)

            messagebox.showinfo("Сгенерированные пароли", "\n".join(passwords))

        root = tk.Toplevel(self.root)
        root.title("Генерация случайных паролей")

        generate_button = tk.Button(root, text="Сгенерировать пароли", command=generate_passwords)
        generate_button.pack(pady=20)

    # Симулятор кассы. Часть 1
    def cash_register_simulator_part1(self):
        products = {
            "молоко": 20,
            "хлеб": 15,
            "сахар": 30,
            "соль": 10,
            "масло": 50,
            "яйца": 40,
            "мясо": 100,
            "рыба": 120,
            "колбаса": 70,
            "сыр": 80
        }

        coins = [1, 5, 7, 10, 15]

        def calculate_change():
            product = simpledialog.askstring("Выбор продукта", "Введите название продукта:")
            if product not in products:
                messagebox.showerror("Ошибка", "Продукт не найден!")
                return

            price = products[product]
            amount_paid = simpledialog.askinteger("Оплата", f"Цена продукта: {price} руб. Введите сумму оплаты:")
            if not amount_paid or amount_paid < price:
                messagebox.showerror("Ошибка", "Недостаточная сумма оплаты!")
                return

            change = amount_paid - price
            change_coins = []
            for coin in sorted(coins, reverse=True):
                while change >= coin:
                    change -= coin
                    change_coins.append(coin)

            messagebox.showinfo("Сдача", f"Сдача: {change_coins} монет")

        root = tk.Toplevel(self.root)
        root.title("Симулятор кассы. Часть 1")

        calculate_button = tk.Button(root, text="Рассчитать сдачу", command=calculate_change)
        calculate_button.pack(pady=20)

    # Симулятор кассы. Часть 2
    def cash_register_simulator_part2(self):
        products = {
            "молоко": 20,
            "хлеб": 15,
            "сахар": 30,
            "соль": 10,
            "масло": 50,
            "яйца": 40,
            "мясо": 100,
            "рыба": 120,
            "колбаса": 70,
            "сыр": 80
        }

        coins = {1: 10, 5: 10, 7: 10, 10: 10, 15: 10}

        def calculate_change():
            product = simpledialog.askstring("Выбор продукта", "Введите название продукта:")
            if product not in products:
                messagebox.showerror("Ошибка", "Продукт не найден!")
                return

            price = products[product]
            amount_paid = simpledialog.askinteger("Оплата", f"Цена продукта: {price} руб. Введите сумму оплаты:")
            if not amount_paid or amount_paid < price:
                messagebox.showerror("Ошибка", "Недостаточная сумма оплаты!")
                return

            change = amount_paid - price
            change_coins = []
            for coin in sorted(coins.keys(), reverse=True):
                while change >= coin and coins[coin] > 0:
                    change -= coin
                    coins[coin] -= 1
                    change_coins.append(coin)

            if change > 0:
                messagebox.showerror("Ошибка", "Недостаточно монет для сдачи!")
                return

            messagebox.showinfo("Сдача", f"Сдача: {change_coins} монет\nОставшиеся монеты: {coins}")

        root = tk.Toplevel(self.root)
        root.title("Симулятор кассы. Часть 2")

        calculate_button = tk.Button(root, text="Рассчитать сдачу", command=calculate_change)
        calculate_button.pack(pady=20)

    # Поиск места разделения 0 и 1 в массиве
    def find_split_point(self):
        def find_split():
            array_str = simpledialog.askstring("Введите массив", "Введите упорядоченный массив из 0 и 1 через запятую:")
            if not array_str:
                return
            try:
                array = list(map(int, array_str.strip().split(',')))
            except ValueError:
                messagebox.showerror("Ошибка", "Некорректный формат массива!")
                return

            def find_division(arr):
                low, high = 0, len(arr) - 1
                while low <= high:
                    mid = (low + high) // 2
                    if arr[mid] == 0:
                        low = mid + 1
                    else:
                        high = mid - 1
                return low if low < len(arr) and arr[low] == 1 else -1

            index = find_division(array)
            messagebox.showinfo("Результат", f"Индекс разделения: {index}")

        root = tk.Toplevel(self.root)
        root.title("Поиск места разделения 0 и 1 в массиве")

        find_button = tk.Button(root, text="Найти место разделения", command=find_split)
        find_button.pack(pady=20)

    # Сортировки в массиве
    def sorting_algorithms(self):
        def sort_array():
            file_path = "mas-1.txt"
            try:
                array = read_array_from_file(file_path)
            except ValueError:
                messagebox.showerror("Ошибка", "Некорректный формат данных в файле!")
                return

            algorithms = {
                "Сортировка пузырьком": bubble_sort,
                "Сортировка вставками": insertion_sort,
                "Сортировка слиянием": merge_sort,
                "Быстрая сортировка": lambda arr: quick_sort(arr),
                "Сортировка подсчетом": counting_sort
            }

            results = {}
            for name, func in algorithms.items():
                array_copy = array[:]
                exec_time = measure_time(func, array_copy)
                results[name] = exec_time

            result_message = "\n".join([f"{name}: {time:.6f} секунд" for name, time in results.items()])
            messagebox.showinfo("Результаты сортировки", result_message)

        root = tk.Toplevel(self.root)
        root.title("Сортировки в массиве")

        sort_button = tk.Button(root, text="Сортировать массив", command=sort_array)
        sort_button.pack(pady=20)

    # Проверка простого числа
    def check_prime(self):
        def is_prime(n):
            if n <= 1:
                return False
            for i in range(2, int(abs(n)**0.5) + 1):
                if n % i == 0:
                    return False
            return True

        numbers = [12, -45, 67, -34, 89, -100, 23, -5, 34]
        primes = [num for num in numbers if is_prime(num)]
        messagebox.showinfo("Простые числа", f"Простые числа: {primes}")

    # Сумма чисел в массиве
    def sum_of_array(self):
        array = [-90, 56, -23, 12, 45, -67, 89, -32, 11, -76, 54]
        array_sum = sum(array)
        messagebox.showinfo("Сумма чисел", f"Сумма чисел в массиве: {array_sum}")

    # Подсчет положительных и отрицательных чисел в массиве
    def count_positive_negative(self):
        array = [3, -15, 27, -48, 59, -6, 14, -38, 72, -94, 18, -12]
        positive_count = sum(1 for x in array if x > 0)
        negative_count = sum(1 for x in array if x < 0)
        messagebox.showinfo("Подсчет чисел", f"Положительных чисел: {positive_count}\nОтрицательных чисел: {negative_count}")

    # Найти наибольшее и наименьшее число в массиве
    def find_max_min(self):
        array = [-22, 45, -67, 34, -89, 100, -23, 5, -34, 78]
        max_num = max(array)
        min_num = min(array)
        messagebox.showinfo("Максимум и минимум", f"Наибольшее число: {max_num}\nНаименьшее число: {min_num}")

root = tk.Tk()
app = App(root)
root.mainloop()
