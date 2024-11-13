from project.models.Endereco import Endereco
from project.models.Pessoa import Pessoa
from project.models.enums.Genero import Sexo
from abc import ABC, abstractmethod

class Fisica(Pessoa, ABC):
    def __init__(self, nome: str, telefone: str, email: str, endereco: Endereco, cpf: str, rg: str, dataNascimento: str, sexo: Sexo):
        super().__init__(nome, telefone, email, endereco)
        self.cpf = cpf
        self.rg = rg
        self.dataNascimento = dataNascimento
        self.sexo = sexo

    def __str__(self) -> str:
        return (f"{super().__str__()}"
               f"\nCpf: {self.cpf}"
               f"\nRg: {self.rg}"
               f"\nData de Nascimento: {self.dataNascimento}"
               f"{self.sexo}")