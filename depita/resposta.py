"""
Autor: Guilherme J. Ramires

Para esse exercicio optei por criar uma classe Depita, que possui a propriedade privada "lunchboxes"
e os metodos publicos "add_lunchbox" e "get_clients_amount" para adicionar e retornar o numero de clientes,
tambem possui o metodo publico "show_all_lunchboxes" que mostra todas as lunchboxes em ordem alfabetica
do nome dos clientes.
O método execute executa a coleta dos inputs de acordo com o enunciado e os passa a Depita.
"""


class Depita:
    def __init__(self):
        self.__lunchboxes = {}

    def add_lunchbox(self, client_name_and_lunchbox: str) -> None:
        data = client_name_and_lunchbox.split(" ")
        client_name = data[0]
        packed_lunch = " ".join(data[1:])

        self.__lunchboxes[client_name] = packed_lunch

    def get_clients_amount(self) -> int:
        return len(self.__lunchboxes)

    def show_all_lunchboxes(self) -> None:
        sorted(self.__lunchboxes)
        for client_name, lunchbox in self.__lunchboxes.items():
            print(lunchbox)

def execute():
    depita = Depita()

    number_of_additions = int(input())

    for addition in range(number_of_additions):
        depita.add_lunchbox(input())

    print(depita.get_clients_amount())
    depita.show_all_lunchboxes()

if __name__ == "__main__":
    execute()
