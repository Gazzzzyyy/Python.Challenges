"""
You have an array of product records. Each record is a string containing a product's category, name, and price.
You need to reorder the records so that:

Products are sorted by their categories in ascending alphabetical order.
Within each category, products are sorted by their prices in ascending numerical order.
If two products have the same category and price, they should be sorted by their names in ascending alphabetical order.
Return the final order of the product records.
"""

from typing import List, AnyStr


def sort_product_records(array: List[AnyStr]):

    def sorting_function(record: AnyStr):

        category, name, price = record.split(" ")

        return category, price, name

    array.sort(key=sorting_function)
    return array


if __name__ == "__main__":

    print(
        sort_product_records(
            [
                "Electronics iPhone 999",
                "Furniture Sofa 500",
                "Electronics SamsungTV 700",
                "Furniture Table 300",
                "Clothing TShirt 20",
                "Clothing Jeans 40",
                "Electronics Android 700",
            ]
        )
    )
    # returns [
    #     "Clothing TShirt 20",
    #     "Clothing Jeans 40",
    #     "Electronics Android 700",
    #     "Electronics SamsungTV 700",
    #     "Electronics iPhone 999",
    #     "Furniture Table 300",
    #     "Furniture Sofa 500"
    # ]
