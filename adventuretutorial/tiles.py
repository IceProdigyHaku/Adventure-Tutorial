import Items, Enemy, Actions, World

class MapTile:
	def __init__(self, x, y):
		self.x = x
		self.y = y
	
	def intro_text(self):
		raise NotImplementedError()
	
	def adjacent_moves(self):
		"""Returns all move actions for adjacent tiles."""
		moves =[]
		if World.tile_exists(self.x + 1, self.y):
			moves.append(Actions.MoveEast())
		if World.tile_exists(self.x - 1, self.y):
			moves.append(Actions.MoveWest())
		if World.tile_exists(self.x, self.y + 1):
			moves.append(Actions.MoveNorth())
		if World.tile_exists(self.x, self.y - 1):
			moves.append(Actions.MoveSouth())
		return moves

	def available_actions(self):
		"""Returns all of the available actions in this room."""
		moves = self.adjacent_moves()
		moves.append(Actions.ViewInventory())
		
		return moves
	
	def modify_Player(self, player):
		raise NotImplementedError()
	
class StartingRoom(MapTile):
	def intro_text(self):"""
	You find yourself in a cave with a flickering torch on the wall.
	You can make out four paths, each equally as dark and foreboding.
	"""
	
	def modify_Player(self, player):
	#room has no action on player
		pass
	
class LootRoom(MapTile):
	def __init__(self, x, y, item):
		self.item = item
		super().__init__(x, y)
	
	def add_loot(self, player):
		player.inventory.append(self.item)
		
	def modify_Player(self, player):
		self.add_loot(player)
	

class Find5GoldRoom(LootRoom):
	def __init__(self, x, y):
		super().__init__(x, y, Items.Gold(5))
	
	def intro_text(self):
		return """
		Someone dropped 5 gold pieces. You pick it up.
		"""


class FindDaggerRoom(LootRoom):
	def __init__(self, x, y):
		super().__init__(x, y, Items.Dagger())
	
	def intro_text(self):
		return """
		You notice something shiny in the corner.
		It's a dagger! you pick it up.
		"""
		


class EnemyRoom(MapTile):
	def __init__(self, x, y, enemy):
		self.enemy = enemy
		super().__init__(x, y)
		
	def modify_Player(self, player):
		if self.enemy.is_alive():
			player.hp = player.hp - self.enemy.damage
			print("Enemy does {} damage. You have {} HP remaining.".format(self.enemy.damage, player.hp))
	
	def available_actions(self):
		if self.enemy.is_alive():
			return[Actions.Flee(tile=self), Actions.Attack(enemy=self.enemy)]
		else:
			return self.adjacent_moves()


			
class EmptyCavePath(MapTile):
	def intro_text(self):
		return"""
		Another unremarkable part of the cave. You must forge onwards.
		"""
	
	def modify_Player(self, player):
		#room has no action on player
		pass

	
class GiantSpiderRoom(EnemyRoom):
	def __init__(self, x, y):
		super().__init__(x, y, Enemy.GiantSpider())
		
	def intro_text(self):
		if self.enemy.is_alive():
			return """
			A giant spider jumps down from its web in front of you!
			"""
		else:
			return """
			The corpse of a dead spider rots on the ground.
			"""
			
class OgreRoom(EnemyRoom):
	def __init__(self, x, y):
		super().__init__(x, y, Enemy.Ogre())
		
	def intro_text(self):
		if self.enemy.is_alive():
			return """
			A massive Ogre blocks the way!
			"""
		else:
			return """
			A smelly Ogre corpse lays at your feet.
			"""
class GoblinRoom(EnemyRoom):
	def __init__(self, x, y):
		super().__init__(x, y, Enemy.Goblin())
		
	def intro_text(self):
		if self.enemy.is_alive():
			return """
			An ugly Goblin attacks!
			"""
		else:
			return """
			The Goblin is dead!
			"""
			

class SnakePitRoom(EnemyRoom):
	def __init__(self, x, y):
		super().__init__(x, y, Enemy.SnakePit())
		
	def intro_text(self):
		if self.enemy.is_alive():
			return """
			You stumble into a pit of snakes! thankfully they look non venemous.
			but they are dangerous none the less.
			"""
		else:
			return """
			All the snakes are dead and you may continue on.
			"""
			
class LeaveCaveRoom(MapTile):
	def intro_text(self):
		return """
		You see a bright light in the distance...
		... it grows as you get closer! It's sunlight!
		
		Victory is yours!
		"""
	
	def modify_Player(self, player):
		player.victory = True