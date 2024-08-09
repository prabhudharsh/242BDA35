"""
Algorithm No : 01
Algorithm Name : Linear Search
Script Author : Prabhu Dharsh Antony
"""


# Defining The function for Linear Search Algorithm
def linear_search(target_element: int, array: list) -> str:
    """
    Linear Search Algorithm searches each element in a list
    One by one by increasing index numbers
    Until the target element is found.
    The Complexity is n.
    """
    for list_index in range(len(array)):
        # Loop through each element using For loop
        if target_element == array[list_index]:
            # Checking each element if it's similar to the target_element
            return f"The Target Element, {target_element} was found at the index {list_index} of the Array."
        else:
            # If Target not present in the current index. The loop continues.
            continue
    else:
        # If the Target Element was not present, Not found message is returned.
        return f"The Target Element, {target_element} was not found in the Array."


def main() -> None:
    """This is the main function of the program."""
    array = [1, 5, 3, 6, 4, 7, 9, 2]
    target_element = 4
    print(linear_search(target_element=target_element, array=array))
    # The Linear search Function is called.


if __name__ == "__main__":
    main()
