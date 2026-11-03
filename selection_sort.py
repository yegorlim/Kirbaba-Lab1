def selection_sort(arr, verbose=False, key=None):
    say = print if verbose else (lambda *a: None)
    kf = key if key is not None else (lambda x: x)
    n = len(arr)
    comparisons = 0
    assignments = 0

    for i in range(n - 1):
        say("------------------------------")
        say("Ітерація", i)
        say(f"  Поточний елемент: arr[{i}] = {arr[i]}")
        min_index = i
        assignments += 1
        say("  Шукаємо мінімум у частині:", arr[i:])

        for j in range(i + 1, n):
            comparisons += 1
            if kf(arr[j]) < kf(arr[min_index]):
                min_index = j
                assignments += 1

        say(f"  Мінімум: arr[{min_index}] = {arr[min_index]}")
        comparisons += 1
        if min_index != i:
            say(f"  Обмін arr[{i}] і arr[{min_index}]")
            arr[i], arr[min_index] = arr[min_index], arr[i]
            assignments += 3
        say(f"  Масив після ітерації {i}:", arr)
    say("------------------------------")
    return arr, comparisons, assignments

if __name__ == "__main__":
    my_list = [69, 52, 97, 27, 10, 88, 29, 1, 24]
    print("Оригінальний список:", my_list)
    sorted_list, comps, assigs = selection_sort(my_list.copy(),
                                                verbose=True)
    print("Відсортований список:", sorted_list)
    print(f"Кількість порівнянь: {comps}")
    print(f"Кількість присвоєнь: {assigs}")
