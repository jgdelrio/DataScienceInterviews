# Created by Jose del Rio 2020/08/28
# Copyright 2020 Jose del Rio. All rights reserved.

# Problem statement:
# -----------------
#   Implement the IceCreamMachine's scoops method so that it returns all combinations of one ingredient
#   and one topping. If there are no ingredients or toppings, the method should return and empty list.
#
#   For example, IceCreamMachine(["vanilla", "chocolate"], ["chocolate sauce"]).scoops() should return
#   [['vanilla', 'chocolate sauce'], ['chocolate', 'chocolate sauce']]


class IceCreamMachine:

    def __init__(self, ingredients, toppings):
        self.ingredients = ingredients
        self.toppings = toppings

    def scoops(self):
        combinations = []
        for ing in self.ingredients:
            for top in self.toppings:
                combinations.append([ing, top])
        return combinations


def test_scoops():
    data_input = ["vanilla", "chocolate"], ["chocolate sauce"]
    expected_output = [['vanilla', 'chocolate sauce'], ['chocolate', 'chocolate sauce']]

    machine = IceCreamMachine(*data_input)
    result = machine.scoops()

    assert result == expected_output
    print(result)


if __name__ == "__main__":
    test_scoops()
