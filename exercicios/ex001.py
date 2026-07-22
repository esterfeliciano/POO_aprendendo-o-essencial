# Declaração de classe 
class Gafanhoto:
    def __init__(self, n = "", i = 0): # Método Constutor
         # Atributos de Instãncia
         self.nome = n
         self.idade = i

    # Métodos de Instâcia
    def aniversario(self):
            self.idade = self.idade + 1

    def __str__(self):
        return f"{self.nome} é Gafanhoto(a) e tem {self.idade} anos de idade."
    def __getstate__(self):
         return f"Estado:" nome = {self.nome} ; idade = {self.idade}
# Declaração de objetos
g1 = Gafanhoto(n="Maria", i =17)
g1.aniversario()
print(g1())

g2 = Gafanhoto(n="José", i =45)
print(g2())

g3 = Gafanhoto(n="Antônio", i =67)
print(g3)

# print (g1)
print(g1.dict__) #Attribute
print(g1.__getstate__())

# print(g1.__doc__) # Dunder Attribute

g2 = Gafanhoto nome:"Mauro