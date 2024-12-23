from enum import Enum

class Sexo(Enum):
    
    MASCULINO = ("M", "Masculino")
    FEMININO = ("F", "Feminino")

    def __init__(self, caractere: str, texto: str):
        self.caractere = caractere
        self.texto = texto

    def __str__(self) -> str:
        return(f"\nSexo: {self.caractere}|{self.texto}")