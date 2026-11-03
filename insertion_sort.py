def insertion_sort(arr, verbose=False, key=None):
    say = print if verbose else (lambda *a: None)
    kf = key if key is not None else (lambda x: x)
    n = len(arr)
    comparisons = 0
    assignments = 0

    for i in range(1, n):
        say("------------------------------")
        say(f"Ітерація {i}:")
        current = arr[i]
        assignments += 1
        say("  Елемент для вставки:", current)
        say("  Відсортована частина:", arr[:i])
        j = i - 1
        assignments += 1

        while j >= 0 and kf(arr[j]) > kf(current):
            say(f"  Порівняння: {arr[j]} > {current}: так, зсув")
            comparisons += 1
            arr[j + 1] = arr[j]
            assignments += 1
            j -= 1
            assignments += 1

        if j < 0:
            say("  Початок масиву. Цикл завершено.")
        else:
            say(f"  Порівняння: {arr[j]} > {current}: ні, кінець")
            comparisons += 1
        say(f"  Вставка {current} на позицію {j + 1}.")
        arr[j + 1] = current
        assignments += 1
        say(f"  Масив після ітерації {i}:", arr)
    say("------------------------------")
    return arr, comparisons, assignments

if __name__ == "__main__":
    my_list = [69, 52, 97, 27, 10, 88, 29, 1, 24]
    print("Оригінальний список:", my_list)
    sorted_list, comps, assigs = insertion_sort(my_list.copy(),
                                                verbose=True)
    print("Відсортований список:", sorted_list)
    print(f"Кількість порівнянь: {comps}")
    print(f"Кількість присвоєнь: {assigs}")
