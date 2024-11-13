from project.models.Endereco import Endereco
from project.models.Pessoa import Pessoa
from project.models.enums.UnidadeFederativa import UnidadeFederativa

class Juridica(Pessoa):
    def __init__(self, nome: str, telefone: str, email: str, endereco: Endereco, cnpj: str, inscricaoEstadual: str):
        super().__init__(nome, telefone, email, endereco)
        self.cnpj = cnpj
        self.inscricaoEstadual = inscricaoEstadual

    def __str__(self) -> str:
                return(
                f"{super().__str__()}"
                f"\nCnpj: {self.cnpj}"
                f"\nInscrição Estadual: {self.inscricaoEstadual}")
    
j1 = Juridica("Bruno", "71992328283", "bruno09bahia@gmail.com", Endereco("Mirantes, Rua 1", "78a", "Apartamento 104", "40725360", "Salvador",UnidadeFederativa.BAHIA), "122342343232", "ABCDE")

print(j1)