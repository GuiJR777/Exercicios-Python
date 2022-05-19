"""
Autor: Guilherme J. Ramires

Para esse exercicio optei por criar uma classe Joana, que possui um metodo publico
chamado "hear_the_phrase" para simular Joana ouvindo a frase dita por seus amigos.
Após ouvir a frase, um metodo privado chamado "__react" é chamado, que simula a reação da Joana.
Joana tambem possui um metodo publico chamado "mapping_reactions" que mapeia as reações da Joana
de acordo com as palavras gatilho dita por seus amigos, esse metodo recebe o input no padrão
imposto no enunciado
O método execute executa a coleta dos inputs e os passa a Joana.
"""


class Joana:
    def __init__(self):
        self.__reactions_map = {}

    def mapping_reactions(self, trigger_word_and_reaction: str) -> None:
        trigger_and_reaction = trigger_word_and_reaction.split(" ")

        trigger = trigger_and_reaction[0]
        reaction = trigger_and_reaction[1]

        self.__reactions_map[trigger] = reaction

    def hear_the_phrase(self, phrase: str) -> str:
        return self.__react(phrase)

    def __react(self, phrase: str) -> str:
        reactions = []

        for trigger, reaction in self.__reactions_map.items():
            if trigger in phrase:
                reactions.append(reaction)

        if not reactions:
            return "Tudo bem!"

        reactions.reverse()

        return " ".join(reactions)


def execute():
    joana = Joana()

    number_of_triggers_words = int(input())

    for trigger_word_and_reaction in range(number_of_triggers_words):
        joana.mapping_reactions(input())

    sentence = input()

    reaction = joana.hear_the_phrase(sentence)

    print(reaction)


if __name__ == "__main__":
    execute()
