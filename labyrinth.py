import random
import time
import sys

# define the size of the labyrinth
width = 10
height = 10

# define the starting position of the player
start_x = 0
start_y = 0

# define the ending position of the labyrinth
end_x = 9
end_y = 9

# define the current position of the player
current_x = 0
current_y = 0



def generate_labyrinth(difficulty):
  # create an empty labyrinth
  labyrinth = []
  for i in range(height):
    row = []
    for j in range(width):
      row.append(0)
    labyrinth.append(row)
    # generate the walls of the labyrinth based on the specified difficulty level
  for i in range(height):
    for j in range(width):
      if random.random() > difficulty:
        labyrinth[i][j] = 1

  # make sure there is a path from the starting position to the ending position
  labyrinth[start_x][start_y] = 0
  labyrinth[end_x][end_y] = 0

  return labyrinth

labyrinth = generate_labyrinth(0.9)

def check_labyrinth(labyrinth, start_x, start_y, end_x, end_y):
  # create a queue to store the positions of the cells that need to be explored
  queue = []
  queue.append((start_x, start_y))

  # create a set to store the positions of the cells that have been visited
  visited = set()

  # create a dictionary to store the parent of each cell
  parents = {}
  parents[(start_x, start_y)] = None

  # continue the search until the queue is empty
  while len(queue) > 0:
    # get the position of the next cell to be explored
    current_x, current_y = queue.pop(0)

    # check if the current cell is the ending position
    if current_x == end_x and current_y == end_y:
      # create a list to store the solution
      solution = []

      # traverse the parent chain to create the solution
      while current_x != start_x or current_y != start_y:
        solution.append((current_x, current_y))
        current_x, current_y = parents[(current_x, current_y)]
      solution.append((start_x, start_y))

      # reverse the solution list to get the correct order of the positions
      solution = solution[::-1]

      # return the solution
      return solution

    # explore the neighboring cells of the current cell
    for dx, dy in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
      next_x = current_x + dx
      next_y = current_y + dy

      # check if the next cell is within the bounds of the labyrinth
      if next_x >= 0 and next_x < len(labyrinth) and next_y >= 0 and next_y < len(labyrinth[0]):
        # check if the next cell is a path and has not been visited
        if labyrinth[next_x][next_y] == 0 and (next_x, next_y) not in visited:
          # add the next cell to the queue and mark it as visited
          queue.append((next_x, next_y))
          visited.add((next_x, next_y))

          # store the parent of the next cell
          parents[(next_x, next_y)] = (current_x, current_y)

  # if the search has reached this point, it means that the ending position was not found
  return False

print(check_labyrinth(labyrinth, start_x, start_y, end_x, end_y))
    



def print_labyrinth(labyrinth, current_x, current_y):
  for i in range(height):
    for j in range(width):
      if i == current_x and j == current_y:
        # print the player's position
        print("X", end="")
      elif labyrinth[i][j] == 1:
        # print a wall
        print("#", end="")
      else:
        # print a path
        print(".", end="")
    print()

def check_wall(labyrinth, current_x, current_y, direction):
  # check if the player is moving up
  if direction == "up":
    next_x = current_x - 1
    next_y = current_y
  # check if the player is moving down
  elif direction == "down":
    next_x = current_x + 1
    next_y = current_y
  # check if the player is moving left
  elif direction == "left":
    next_x = current_x
    next_y = current_y - 1
  # check if the player is moving right
  elif direction == "right":
    next_x = current_x
    next_y = current_y + 1

  # check if the next position of the player is within the bounds of the labyrinth
  if next_x >= 0 and next_x < len(labyrinth) and next_y >= 0 and next_y < len(labyrinth[0]):
    # check if the next position of the player is a wall
    if labyrinth[next_x][next_y] != 1:
      return True

def move_player(labyrinth, current_x, current_y, direction):
  # update the current position of the player based on the input direction
    print("whoin")
    if (check_wall(labyrinth, current_x, current_y, direction)):
        if direction == "up":
            print("whoap")
            current_x = current_x-1
        elif direction == "down":
            print("whodown")
            current_x = 1+current_x
        elif direction == "left":
            current_y = current_y - 1
        elif direction == "right":
            current_y = 1+current_y
        if current_x == end_x and current_y == end_y:
            return [True,current_x, current_y]
        else:
            return [False,current_x, current_y]
    else:
        return [False,current_x, current_y]

    
   
    
game_over = False
while not game_over:
    print_labyrinth(labyrinth, current_x, current_y)
    print("Enter a direction (up, down, left, right): ")
    direction = input()
    game_over, current_x, current_y = move_player(labyrinth, current_x, current_y, direction)
    print(current_x)
print("Congratulations! You have reached the ending position.")
