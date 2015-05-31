#player
import random
import Items, World

class Player:
	inventory = [Items.Gold(15), Items.Rock()]
	hp = 100
	location_x, location_y = (2, 2)
	victory = False
	
	def is_alive(self):
		return self.hp > 0
		
	def print_inventory(self):
		for item in self.inventory:
			print(item, '\n')
	
	def do_action(self, action, **kwargs):
		action_method = getattr(self, action.method.__name__)
		if action_method:
			action_method(**kwargs)
			
	def flee(self, tile):
		"""Moves the player randomly to an adjacent tile"""
		available_moves = tile.adjacent_moves()
		r = random.randint(0, len(available_moves) - 1)
		self.do_action(available_moves[r])
	
	def move(self, dx, dy):
		self.location_x += dx
		self.location_y += dy
		print(World.tile_exists(self.location_x, self.location_y).intro_text())

	def move_north(self):
		self.move(dx=0, dy=1)

	def move_south(self):
		self.move(dx=0, dy=-1)
	
	def move_east(self):
		self.move(dx=1, dy=0)
	
	def move_west(self):
		self.move(dx=-1, dy=0)
	
	def attack(self, enemy):
		best_Weapon = None
		max_dmg = 0
		for i in self.inventory:
			if isinstance(i, Items.Weapon):
				if i.damage > max_dmg:
					max_damage = i.damage
					best_Weapon = i
					
		print("You use {} against {}! and deal {}!".format(best_Weapon.name, enemy.name, best_Weapon.damage))
		enemy.hp -= best_Weapon.damage
		if not enemy.is_alive():
			print("You killed {}!".format(enemy.name))
		else:
			print("{} HP is {}.".format(enemy.name, enemy.hp))