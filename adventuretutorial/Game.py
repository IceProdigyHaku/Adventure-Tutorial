#Game.py
import World
from Player import Player

def play():
	World.load_tiles()
	player = Player()
	#These lines load the starting room and display the text
	while player.is_alive() and not player.victory:
		room = World.tile_exists(player.location_x, player.location_y)
		room.modify_Player(player)
		#check again since the room could have changed the player's state
		print("choose an action:\n")
		available_actions = room.available_actions()
		for action in available_actions:
			print(action)
		action_input = input('action: ')
		for action in available_actions:
			if action_input == action.hotkey:
				player.do_action(action, **action.kwargs)
				break
					
if __name__ == "__main__":
	play()