def is_number(value_to_check, do_return_value):
    try:
        int(value_to_check)
        if do_return_value:
            return int(value_to_check)
        else:
            return True
    except ValueError:
        # Disabling out float check, because only integers are allowed
        # try:
        #     float(value_to_check)
        #     if do_return_value:
        #         return float(value_to_check)
        #     else:
        #         return True
        # except ValueError:
            print("Error! Input is not a valid number (integer). ")
            if do_return_value:
                new_number = input("Try again: ")
                if is_number(new_number, False):
                    return True
                else:
                    return False
            else:
                new_number = input("Try again: ")
                if is_number(new_number, True):
                    return new_number
                else:
                    return None


def calculate_sum(array_to_sum):
    sum_result = 0
    for num in array_to_sum:
        sum_result += num
    return sum_result


def calculate_avg(array_to_average):
    return calculate_sum(array_to_average) / len(array_to_average)


if __name__ == '__main__':
    print("Načtěte deset celých čísel typu int a vypočtěte jejich součet a průměr. "
          "Průměr zaokrouhlete na dvě desetinná místa.")
    array = []
    RANGE = 10
    for thing in range(RANGE):
        array.append(int(is_number(input("Zadej cislo: "), True)))

    print("Sum = ", calculate_sum(array))
    print("Average = ", calculate_avg(array))
    avg_to_format = round(calculate_avg(array))

    print("Rounded to 2 places = {average: .2f}!".format(average=avg_to_format))


