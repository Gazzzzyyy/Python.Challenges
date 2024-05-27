"""
You have an array of product records. Each record is a string containing a product's category, name, price, and
stock status (either "in-stock" or "out-of-stock"). You need to perform the following tasks:

Filter out products that are "out-of-stock".
Sort the remaining products by their categories in ascending alphabetical order.
Within each category, sort the products by their prices in ascending numerical order.
If two products have the same category and price, they should be sorted by their names in ascending alphabetical order.
Return the final order of the filtered and sorted product records.
"""

from typing import List, AnyStr


def filter_and_sort_product_records(array: List[AnyStr]):

    new_array = [el for el in array if el.endswith("in-stock")]

    def sorting_function(record: AnyStr):
        category, name, price, _ = record.split(" ")

        return (category, int(price), name)

    new_array.sort(key=sorting_function)

    return new_array


if __name__ == "__main__":
    print(
        filter_and_sort_product_records(
            [
                "Electronics iPhone 999 in-stock",
                "Furniture Sofa 500 out-of-stock",
                "Electronics SamsungTV 700 in-stock",
                "Furniture Table 300 in-stock",
                "Clothing TShirt 20 in-stock",
                "Clothing Jeans 40 in-stock",
            ]
        )
    )
    # returns [
    #     "Clothing Jeans 40 in-stock",
    #     "Clothing TShirt 20 in-stock",
    #     "Electronics SamsungTV 700 in-stock",
    #     "Electronics iPhone 999 in-stock",
    #     "Furniture Table 300 in-stock"
    # ]
