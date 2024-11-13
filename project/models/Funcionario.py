from project.models.Endereco import Endereco
from project.models.Fisica import Fisica
from project.models.enums.Setor import Setor
from abc import ABC, abstractmethod

from project.models.enums.Genero import Sexo

class Funcionario(ABC, Fisica):
    def __init__(self, nome: str, telefone: str, email: str, endereco: Endereco, cpf: str, rg: str, dataNascimento: str, sexo: Sexo, matricula: str, setor: Setor, salario: float):
        super().__init__(nome, telefone, email, endereco, cpf, rg, dataNascimento, sexo)
        self.matricula = matricula
        self.setor = setor
        self.salario = salario

    def __str__(self) -> str:
        return (f"{super().__str__()}"
                f"Matricula: {self.matricula}"
                f"Setor: {self.setor}"
                f"Salario: {self.salario}"
        )
    @abstractmethod
    def salario_final(self)->float:
            pass