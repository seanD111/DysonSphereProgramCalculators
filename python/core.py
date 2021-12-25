from items import Item, RECIPES
import numpy as np


def get_raw_materials(recipe_mat, product):

    def accumulate_materials(recipes, item_column, accum_column):
        next_col = np.zeros_like(item_column)

        for i in range(len(item_column)):
            if item_column[i] > 0.0:
                next_col = next_col + item_column[i]*recipes[:, i]

        if all(item_column == next_col):
            return item_column, accum_column
        else:
            acc_column = accum_column + next_col
            return accumulate_materials(recipe_mat, next_col, acc_column)

    product_col = recipe_mat[:, product]
    return accumulate_materials(recipe_mat, product_col, product_col)


def print_recipe_mat(mat):
    item_list = [item.name for item in Item]
    non_zero = np.nonzero(mat)[0]

    for i in non_zero:
        print(f"{item_list[i]}: {mat[i]}")


def main():
    a, b = get_raw_materials(RECIPES, Item.processor)

    print_recipe_mat(b)
    pass


if __name__ == "__main__":
    main()



