from project.models.Endereco import Endereco
from project.models.Funcionario import Funcionario
from project.models.enums.Genero import Sexo
from project.models.enums.Setor import Setor

class Advogado(Funcionario):
    def __init__(self, nome: str, telefone: str, email: str, endereco: Endereco, cpf: str, rg: str, dataNascimento: str, sexo: Sexo, matricula: str, setor: Setor, salario: float, oab: str):
        super().__init__(nome, telefone, email, endereco, cpf, rg, dataNascimento, sexo, matricula, setor, salario)
        self.oab = oab
    
    def __str__(self) -> str:
        return (f"{super().__str__()}"
                f"Oab: {self.oab}")

    def salario_final(self) -> float:
        return self.salario