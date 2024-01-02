class Operation:
    def __init__(self, nombre1, nombre2):
        self.nombre1 = nombre1
        self.nombre2 = nombre2

operateur = Operation(10, 5)
print(f'Le nombre 1 est {operateur.nombre1}')
print(f'Le nombre 2 est {operateur.nombre2}')