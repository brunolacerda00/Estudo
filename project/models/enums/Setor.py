from enum import Enum

class Setor(Enum):

    ENGENHARIA = ("Engenharia")
    SAUDE = ("Saúde")
    JURIDICO = ("Juridica")
    OPERACOES = ("Operações")

    def __init__(self, nome: str):
        self.nome

    def __str__(self) -> str:
        return (f"{super().__str__()}"
                f"Engenharia: {self.engenharia}"
                f"Saúde: {self.saude}"
                f"Juridico: {self.juridico}"
                f"Operações: {self.operacoes}")