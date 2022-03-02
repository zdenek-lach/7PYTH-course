from pprint import pprint


def is_number(value_to_check, do_return_value):
    try:
        int(value_to_check)
        if do_return_value:
            return int(value_to_check)
        else:
            return True
    except ValueError:
        try:
            float(value_to_check)
            if do_return_value:
                return float(value_to_check)
            else:
                return True
        except ValueError:
            print("Error! Input is not a number. Try again.")
            if do_return_value:
                return -1
            else:
                return False


def get_numbers(count):
    array = []
    numbers_left = count
    while numbers_left > 0:
        input_value = input("Insert number: ")
        if is_number(input_value, False):
            if ENABLE_VERBOSE:
                print("Debug: Valid number? ", is_number(input_value, False))
            array.append(int(input_value))
            numbers_left -= 1
            if ENABLE_VERBOSE:
                print("Debug: numbers_left: ", numbers_left)
    return array


def custom_sort(array_to_sort):
    if ENABLE_VERBOSE:
        print("Sorting with Bubble sort to enable VERBOSE_MODE")
        arr = array_to_sort
        n = len(arr)
        for i in range(n - 1):
            for j in range(0, n - i - 1):
                if arr[j] > arr[j + 1]:
                    print(arr[j], "is bigger than", arr[j + 1], "therefore swapping places!")
                    pprint(arr)
                    arr[j], arr[j + 1] = arr[j + 1], arr[j]
                else:
                    print(arr[j], "is is not bigger than", arr[j + 1], "therefore doing nothing!")
                    pprint(arr)
    else:
        print("Sorting using embedded Python function")
        array_to_sort.sort()


if __name__ == '__main__':
    KEEP_GOING = "y"
    ENABLE_VERBOSE = input("Enable verbose mode? y / n") == "y"
    while KEEP_GOING == "y":
        inputSize = is_number(input("How many numbers do you want to insert? \n"), True)
        numArray = get_numbers(inputSize)
        custom_sort(numArray)
        pprint(numArray)
        KEEP_GOING = input("Run again? y / n ") if "y" else "n"

    print(
        "\n\n---------------------------------------------\n"
        "|\t\t\t\tGoodbye!\t\t\t\t\t|"
        "\n_____________________________________________\n\n")
