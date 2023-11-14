class Pokemon:

	def __init__(self, tipo, especie, level=1, nome=None):
		self.tipo = tipo
		self.especie = especie
		self.level = level

		if nome:
			self.nome = nome
		else:
			self.nome = especie


	def __str__(self):
		return f'{self.nome} ({self.level})'
	

	def atacar(self, pokemon):
		print(f'{self.especie} atacou {pokemon.especie}!')



meu_pokemon = Pokemon('fogo', 'charmander', nome='Gui')

print(meu_pokemon)
