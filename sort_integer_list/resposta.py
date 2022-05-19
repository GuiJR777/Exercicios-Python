"""
Autor: Guilherme J. Ramires

Para esse exercicio optei por criar uma classe chamada SortIntegerList, que possui um metodo estatico
chamado "sort_list_without_sort_function" que recebe uma lista de inteiros e os ordena
sem utilizar o metodo "sort" do python.
"""
from typing import List


class SortIntegerList:
    @staticmethod
    def sort_list_without_sort_function(list_to_sort: List[int]) -> List[int]:
        new_list = list_to_sort

        for index, number in enumerate(list_to_sort):
            new_index = 0
            while number > list_to_sort[new_index]:
                new_index += 1

            del(new_list[index])
            new_list.insert(new_index, number)

            print(new_list)

        return new_list


if __name__ == "__main__":
    list_to_sort = input().split(" ")

    print(f'Lista Original: {" ".join(list_to_sort)}')

    sorted_list = SortIntegerList.sort_list_without_sort_function([int(number) for number in list_to_sort])

    print(f'Lista Ordenada: {" ".join([str(number) for number in sorted_list])}')
