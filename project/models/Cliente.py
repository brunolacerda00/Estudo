from project.models.Endereco import Endereco
from project.models.Fisica import Fisica
from project.models.enums.Genero import Sexo

class Cliente(Fisica):
    def __init__(self, nome: str, telefone: str, email: str, endereco: Endereco, cpf: str, rg: str, dataNascimento: str, sexo: Sexo, protocoloAtendimento: int):
        super().__init__(nome, telefone, email, endereco, cpf, rg, dataNascimento, sexo)
        self.protocoloAtendimento = protocoloAtendimento

    def __str__(self) -> str:
        return(f"{super().__str__()}"
               f"\nProtocolo de Atendimento: {self.protocoloAtendimento}")