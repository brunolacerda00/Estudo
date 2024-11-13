from abc import ABC, abstractmethod
from project.models.Endereco import Endereco

class Pessoa(ABC):
    def __init__(self, nome:str, telefone:str, email:str, endereco: Endereco):
        self.nome = nome
        self.telefone = telefone
        self.email = email
        self.endereco = endereco
    def __str__(self) -> str:
        return (f"\nNome: {self.nome}"
                f"\nTelefone: {self.telefone}"
                f"\nEmail: {self.email}"
                f"\nEndereço: {self.endereco}")