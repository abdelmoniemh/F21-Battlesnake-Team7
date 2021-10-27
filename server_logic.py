import random
import math
from typing import List, Dict


"""
This file can be a nice home for your move logic, and to write helper functions.

We have started this for you, with a function to help remove the 'neck' direction
from the list of possible moves!
"""


def avoid_my_neck(my_head: Dict[str, int], my_body: List[dict], possible_moves: List[str]) -> List[str]:
    """
    my_head: Dictionary of x/y coordinates of the Battlesnake head.
            e.g. {"x": 0, "y": 0}
    my_body: List of dictionaries of x/y coordinates for every segment of a Battlesnake.
            e.g. [ {"x": 0, "y": 0}, {"x": 1, "y": 0}, {"x": 2, "y": 0} ]
    possible_moves: List of strings. Moves to pick from.
            e.g. ["up", "down", "left", "right"]

    return: The list of remaining possible_moves, with the 'neck' direction removed
    """
    my_neck = my_body[1]  # The segment of body right after the head is the 'neck'

    if my_neck["x"] < my_head["x"]:  # my neck is left of my head
        possible_moves.remove("left")
    elif my_neck["x"] > my_head["x"]:  # my neck is right of my head
        possible_moves.remove("right")
    elif my_neck["y"] < my_head["y"]:  # my neck is below my head
        possible_moves.remove("down")
    elif my_neck["y"] > my_head["y"]:  # my neck is above my head
        possible_moves.remove("up")

    return possible_moves


def choose_move(data: dict) -> str:
    """
    data: Dictionary of all Game Board data as received from the Battlesnake Engine.
    For a full example of 'data', see https://docs.battlesnake.com/references/api/sample-move-request

    return: A String, the single move to make. One of "up", "down", "left" or "right".

    Use the information in 'data' to decide your next move. The 'data' variable can be interacted
    with as a Python Dictionary, and contains all of the information about the Battlesnake board
    for each move of the game.

    """
    my_head = data["you"]["head"]  # A dictionary of x/y coordinates like {"x": 0, "y": 0}
    my_body = data["you"]["body"]  # A list of x/y coordinate dictionaries like [ {"x": 0, "y": 0}, {"x": 1, "y": 0}, {"x": 2, "y": 0} ]

    # TODO: uncomment the lines below so you can see what this data looks like in your output!
    print(f"~~~ Turn: {data['turn']}  Game Mode: {data['game']['ruleset']['name']} ~~~")
    print(f"All board data this turn: {data}")
    print(f"My Battlesnakes head this turn is: {my_head}")
    print(f"My Battlesnakes body this turn is: {my_body}")

    possible_moves = ["up", "down", "left", "right"]

    # Don't allow your Battlesnake to move back in on it's own neck
    possible_moves = avoid_my_neck(my_head, my_body, possible_moves)

    # TODO: Using information from 'data', find the edges of the board and don't let your Battlesnake move beyond them
    board_height = data['board']['height']
    board_width = data['board']['height']

    if (my_head['x'] + 1 >= board_width): 
        possible_moves.remove('right')
    if (my_head['x'] - 1 < 0):
        possible_moves.remove('left')
    if (my_head['y'] + 1 >= board_height):
        possible_moves.remove('up')
    if (my_head['y'] - 1 < 0):
        possible_moves.remove('down')

    # TODO Using information from 'data', don't let your Battlesnake pick a move that would hit its own body

    for block in my_body:
        if (my_head['x'] + 1 == block['x'] and my_head['y'] == block['y']):
            if 'right' in possible_moves: possible_moves.remove('right')
        if (my_head['x'] - 1 == block['x'] and my_head['y'] == block['y']):
            if 'left' in possible_moves: possible_moves.remove('left')
        if (my_head['x'] == block['x'] and my_head['y'] + 1 == block['y']):
            if 'up' in possible_moves: possible_moves.remove('up')
        if (my_head['x'] == block['x'] and my_head['y'] - 1 == block['y']):
            if 'down' in possible_moves: possible_moves.remove('down')

    # TODO: Using information from 'data', don't let your Battlesnake pick a move that would collide with another Battlesnake

    for snake in data['board']['snakes']:
        for block in snake['body']:
            if (my_head['x'] + 1 == block['x'] and my_head['y'] == block['y']):
                if 'right' in possible_moves: possible_moves.remove('right')
            if (my_head['x'] - 1 == block['x'] and my_head['y'] == block['y']):
                if 'left' in possible_moves: possible_moves.remove('left')
            if (my_head['x'] == block['x'] and my_head['y'] + 1 == block['y']):
                if 'up' in possible_moves: possible_moves.remove('up')
            if (my_head['x'] == block['x'] and my_head['y'] - 1 == block['y']):
                if 'down' in possible_moves: possible_moves.remove('down')
        block = snake['head']
        if (my_head['x'] + 1 == block['x'] and my_head['y'] == block['y']):
            if 'right' in possible_moves: possible_moves.remove('right')
        if (my_head['x'] - 1 == block['x'] and my_head['y'] == block['y']):
            if 'left' in possible_moves: possible_moves.remove('left')
        if (my_head['x'] == block['x'] and my_head['y'] + 1 == block['y']):
            if 'up' in possible_moves: possible_moves.remove('up')
        if (my_head['x'] == block['x'] and my_head['y'] - 1 == block['y']):
            if 'down' in possible_moves: possible_moves.remove('down')

        if len(snake['body']) >= len(my_body):
            if (my_head['x'] + 1 == block['x'] + 1 and my_head['y'] == block['y']):
                if 'right' in possible_moves: possible_moves.remove('right')
            if (my_head['x'] - 1 == block['x'] + 1 and my_head['y'] == block['y']):
                if 'left' in possible_moves: possible_moves.remove('left')
            if (my_head['x'] == block['x'] + 1 and my_head['y'] + 1 == block['y']):
                if 'up' in possible_moves: possible_moves.remove('up')
            if (my_head['x'] == block['x'] + 1 and my_head['y'] - 1 == block['y']):
                if 'down' in possible_moves: possible_moves.remove('down')

            if (my_head['x'] + 1 == block['x'] -1 and my_head['y'] == block['y']):
                if 'right' in possible_moves: possible_moves.remove('right')
            if (my_head['x'] - 1 == block['x'] -1 and my_head['y'] == block['y']):
                if 'left' in possible_moves: possible_moves.remove('left')
            if (my_head['x'] == block['x'] -1 and my_head['y'] + 1 == block['y']):
                if 'up' in possible_moves: possible_moves.remove('up')
            if (my_head['x'] == block['x']-1 and my_head['y'] - 1 == block['y']):
                if 'down' in possible_moves: possible_moves.remove('down')

            if (my_head['x'] + 1 == block['x'] and my_head['y'] == block['y'] + 1):
                if 'right' in possible_moves: possible_moves.remove('right')
            if (my_head['x'] - 1 == block['x'] and my_head['y'] == block['y'] + 1):
                if 'left' in possible_moves: possible_moves.remove('left')
            if (my_head['x'] == block['x'] and my_head['y'] + 1 == block['y'] + 1):
                if 'up' in possible_moves: possible_moves.remove('up')
            if (my_head['x'] == block['x'] and my_head['y'] - 1 == block['y'] + 1):
                if 'down' in possible_moves: possible_moves.remove('down')

            if (my_head['x'] + 1 == block['x'] and my_head['y'] == block['y'] - 1):
                if 'right' in possible_moves: possible_moves.remove('right')
            if (my_head['x'] - 1 == block['x'] and my_head['y'] == block['y'] - 1):
                if 'left' in possible_moves: possible_moves.remove('left')
            if (my_head['x'] == block['x'] and my_head['y'] + 1 == block['y'] - 1):
                if 'up' in possible_moves: possible_moves.remove('up')
            if (my_head['x'] == block['x'] and my_head['y'] - 1 == block['y'] - 1):
                if 'down' in possible_moves: possible_moves.remove('down')


    # TODO: Using information from 'data', make your Battlesnake move towards a piece of food on the board
    ideal_moves = possible_moves.copy()
    if len(data['board']['food']) > 0:
        closest_food = data['board']['food'][0]
        food_distance = lambda head, food: math.sqrt((head['x'] - food['x'])**2 + (head['y'] - food['y'])**2)
        min_distance = food_distance(my_head, closest_food)
        for food in data['board']['food']:
            temp_distance = food_distance(my_head, food)
            if temp_distance < min_distance:
                closest_food = food
                min_distance = temp_distance
        #choose move that will move you towards the closest food item
        
        next_move = [
            ('up', food_distance({'x':my_head['x'], 'y':my_head['y'] + 1}, closest_food)),
            ('down', food_distance({'x':my_head['x'], 'y':my_head['y'] - 1}, closest_food)),
            ('left', food_distance({'x':my_head['x'] - 1, 'y':my_head['y']}, closest_food)),
            ('right', food_distance({'x':my_head['x'] + 1, 'y':my_head['y']}, closest_food)),
        ]
        next_move_head = {
            'up': {'x':my_head['x'], 'y':my_head['y'] + 1},
            'down': {'x':my_head['x'], 'y':my_head['y'] - 1},
            'left':{'x':my_head['x'] - 1, 'y':my_head['y']},
            'right':{'x':my_head['x'] + 1, 'y':my_head['y']}
        }
        next_move.sort(key=lambda x:x[1])
        
        for move in next_move:
            next_status = choose_move_next(data, next_move_head[move[0]], False)
            if move[0] in possible_moves and len(next_status) > 0: 
                if move[0] in next_status and next_status[move[0]] > 0:
                    print(f"{move} from {possible_moves}")
                    return move[0]

        for move in next_move:
            next_status = choose_move_next(data, next_move_head[move[0]], False)
            if move[0] in possible_moves and len(next_status) > 0: 
                return move[0]

        for move in next_move:
            if move[0] in possible_moves: 
                print(f"{move} from {possible_moves}")
                return move[0]
 
    # Choose a random direction from the remaining possible_moves to move in, and then return that move
    move = random.choice(possible_moves)
    
    # TODO: Explore new strategies for picking a move that are better than random

    print(f"{data['game']['id']} MOVE {data['turn']}: {move} picked from all valid options in {possible_moves}")

    return move

def choose_move_next(data: dict, head: dict, recr: bool) -> str:
    my_head = head # A dictionary of x/y coordinates like {"x": 0, "y": 0}
    my_body = data["you"]["body"]  # A list of x/y coordinate dictionaries like [ {"x": 0, "y": 0}, {"x": 1, "y": 0}, {"x": 2, "y": 0} ]

    possible_moves = ["up", "down", "left", "right"]

    
    possible_moves = avoid_my_neck(my_head, my_body, possible_moves)

    
    board_height = data['board']['height']
    board_width = data['board']['height']

    if (my_head['x'] + 1 >= board_width): 
        possible_moves.remove('right')
    if (my_head['x'] - 1 < 0):
        possible_moves.remove('left')
    if (my_head['y'] + 1 >= board_height):
        possible_moves.remove('up')
    if (my_head['y'] - 1 < 0):
        possible_moves.remove('down')

    for block in my_body:
        if (my_head['x'] + 1 == block['x'] and my_head['y'] == block['y']):
            if 'right' in possible_moves: possible_moves.remove('right')
        if (my_head['x'] - 1 == block['x'] and my_head['y'] == block['y']):
            if 'left' in possible_moves: possible_moves.remove('left')
        if (my_head['x'] == block['x'] and my_head['y'] + 1 == block['y']):
            if 'up' in possible_moves: possible_moves.remove('up')
        if (my_head['x'] == block['x'] and my_head['y'] - 1 == block['y']):
            if 'down' in possible_moves: possible_moves.remove('down')

    for snake in data['board']['snakes']:
        for block in snake['body']:
            if (my_head['x'] + 1 == block['x'] and my_head['y'] == block['y']):
                if 'right' in possible_moves: possible_moves.remove('right')
            if (my_head['x'] - 1 == block['x'] and my_head['y'] == block['y']):
                if 'left' in possible_moves: possible_moves.remove('left')
            if (my_head['x'] == block['x'] and my_head['y'] + 1 == block['y']):
                if 'up' in possible_moves: possible_moves.remove('up')
            if (my_head['x'] == block['x'] and my_head['y'] - 1 == block['y']):
                if 'down' in possible_moves: possible_moves.remove('down')
        block = snake['head']
        if (my_head['x'] + 1 == block['x'] and my_head['y'] == block['y']):
            if 'right' in possible_moves: possible_moves.remove('right')
        if (my_head['x'] - 1 == block['x'] and my_head['y'] == block['y']):
            if 'left' in possible_moves: possible_moves.remove('left')
        if (my_head['x'] == block['x'] and my_head['y'] + 1 == block['y']):
            if 'up' in possible_moves: possible_moves.remove('up')
        if (my_head['x'] == block['x'] and my_head['y'] - 1 == block['y']):
            if 'down' in possible_moves: possible_moves.remove('down')

    next_move_head = {
            'up': {'x':my_head['x'], 'y':my_head['y'] + 1},
            'down': {'x':my_head['x'], 'y':my_head['y'] - 1},
            'left':{'x':my_head['x'] - 1, 'y':my_head['y']},
            'right':{'x':my_head['x'] + 1, 'y':my_head['y']}
        }
    if not recr:
        new_moves = {}
        for x in possible_moves:
            new_moves[x] = len(choose_move_next(data, next_move_head[x], True))
        return new_moves
    return possible_moves