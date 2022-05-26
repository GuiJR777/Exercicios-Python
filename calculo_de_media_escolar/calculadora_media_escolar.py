from constants import MEDIA_NECESSARIA


class CalculoDeMediaEscolar:
    def __init__(self, notas: list):
        self.notas = notas
        self.media = round(self.__calcular_media(), 1)

    def __calcular_media(self) -> float:
        return sum(self.notas) / len(self.notas)

    def foi_aprovado(self) -> bool:
        return self.__calcular_media() >= MEDIA_NECESSARIA
