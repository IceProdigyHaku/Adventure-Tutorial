class Items:
	"""the base class for all items"""
	def __init__(self, name, description, value):
		self.name = name
		self.description = description
		self.value = value
		
	def __str__(self):
		return "{}\n=====n\{}\nValue: {}\n".format(self.name, self.description, self.value)

class Gold(Items):
	def __init__(self, amt):
		self.amt = amt
		super().__init__(name="Gold",
						 description="A round coin with {} stamped on the front.".format(str(self.amt)),
						 value=self.amt)

class Weapon(Items):
	def __init__(self, name, description, value, damage):
		self.damage = damage
		super().__init__(name, description, value)
		
		def __str__(self):
			return "{}\n=====\n{}\nValue: {}\nDamage: {}".format(self.name, self.description, self.value, self.damage)
			
class Rock(Weapon):
	def __init__(self):
		super().__init__(name="Rock",
						 description="A sturdy rock that can be used to bludgeon someone across the head.",
						 value=0,
						 damage=5)
						 
class Dagger(Weapon):
	def __init__(self):
		super().__init__(name="Dagger",
						 description="A sharp dagger, more reliable and dangerous then a rock.",
						 value=5,
						 damage=10)