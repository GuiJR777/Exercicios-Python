from calculadora_media_escolar import CalculoDeMediaEscolar
from constants import NOTA_MAXIMA, NOTA_MINIMA
from utils import Colors


class App:
    def __pega_nota_do_aluno(self, mensagem: str) -> float:
        while True:
            try:
                nota = float(input(f"{mensagem}: "))
                if nota < NOTA_MINIMA or nota > NOTA_MAXIMA:
                    raise ValueError
                break
            except ValueError:
                print(Colors.vermelho + "Valor inválido, digite novamente." + Colors.limpa)

        return nota

    def execute(self) -> None:
        nome_do_aluno = input("Qual o seu nome? ")
        print(f"Bem vindo {nome_do_aluno} ao programa de cálculo de média!")

        notas = []
        numero_de_avaliacoes = int(input("Quantas avaliações você fez? "))

        for avaliacao in range(numero_de_avaliacoes):
            nota = self.__pega_nota_do_aluno(f"Digite a nota da avaliação {avaliacao + 1}")
            notas.append(nota)

        resultado = CalculoDeMediaEscolar(notas)

        print(f"Sua média foi: {resultado.media}")

        if resultado.foi_aprovado():
            mensagem_final = Colors.verde + "Você foi aprovado!" + Colors.limpa
        else:
            mensagem_final = Colors.vermelho + "Você foi reprovado!" + Colors.limpa

        print(mensagem_final)

if __name__ == "__main__":
    App().execute()
