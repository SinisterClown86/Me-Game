import random

def display_intro():
    print("""
    Welcome to the Dungeon Escape!
    You are trapped in a dark dungeon with only one way out.
    Find the key and avoid the traps to escape.
    """)

def generate_dungeon(size):
    dungeon = [['.' for _ in range(size)] for _ in range(size)]
    key_x, key_y = random.randint(0, size - 1), random.randint(0, size - 1)
    exit_x, exit_y = size - 1, size - 1
    dungeon[key_x][key_y] = 'K'  # Key placement
    dungeon[exit_x][exit_y] = 'E'  # Exit placement
    
    # Add traps
    for _ in range(size):
        trap_x, trap_y = random.randint(0, size - 1), random.randint(0, size - 1)
        if (trap_x, trap_y) not in [(key_x, key_y), (exit_x, exit_y)]:
            dungeon[trap_x][trap_y] = 'T'
    
    return dungeon, key_x, key_y, exit_x, exit_y

def print_dungeon(dungeon, player_x, player_y):
    for i in range(len(dungeon)):
        for j in range(len(dungeon[i])):
            if i == player_x and j == player_y:
                print('P', end=' ')
            else:
                print(dungeon[i][j], end=' ')
        print()

def move_player(player_x, player_y, direction, size):
    if direction == 'w' and player_x > 0:
        player_x -= 1
    elif direction == 's' and player_x < size - 1:
        player_x += 1
    elif direction == 'a' and player_y > 0:
        player_y -= 1
    elif direction == 'd' and player_y < size - 1:
        player_y += 1
    return player_x, player_y

def play_game():
    size = 5  # Dungeon size
    dungeon, key_x, key_y, exit_x, exit_y = generate_dungeon(size)
    player_x, player_y = 0, 0
    has_key = False
    
    display_intro()
    
    while True:
        print_dungeon(dungeon, player_x, player_y)
        move = input("Move (WASD): ").lower()
        player_x, player_y = move_player(player_x, player_y, move, size)
        
        if (player_x, player_y) == (key_x, key_y):
            print("You found the key! Now find the exit.")
            has_key = True
            dungeon[key_x][key_y] = '.'
        
        if (player_x, player_y) == (exit_x, exit_y):
            if has_key:
                print("Congratulations! You escaped the dungeon!")
                break
            else:
                print("The exit is locked! Find the key first.")
        
        if dungeon[player_x][player_y] == 'T':
            print("You stepped on a trap! Game over.")
            break

if __name__ == "__main__":
  play_game()
  ###
  Type in your message here 
  Type in your message here 
  Type in your message here 
  Type in your message here 
  Type in your message here 
  Type in your message here 
  Type in your message here 
  Type in your message here 
  Type in your message here 
  Type in your message here 
  Type in your message here 
  Type in your message here 
  Type in your message here 
  Type in your message here 
  Type in your message here 
  Type in your message here 
  Type in your message here 
  Type in your message here 
  Type in your message here 
  Type in your message here 
  Type in your message here 
  Type in your message here 
  Type in your message here 
  Type in your message here 
  Type in your message here 
  Type in your message here 
  Type in your message here 
  Type in your message here 
  Type in your message here 
  Type in your message here 
  Type in your message here 
  Type in your message here 
  Type in your message here 
  Type in your message here 
  Type in your message here 
  Type in your message here 
  Type in your message here 
  Type in your message here 
  Type in your message here 
  Type in your message her
