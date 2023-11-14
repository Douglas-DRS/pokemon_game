class Pokemon:

	def __init__(self, tipo, especie):
		self.tipo = tipo
		self.especie = especie




meu_pokemon = Pokemon('fogo', 'charmander')

pokemon_amigo = Pokemon('eletrico', 'pikachu')

print(meu_pokemon.tipo, meu_pokemon.especie)

print(pokemon_amigo.tipo, pokemon_amigo.especie)