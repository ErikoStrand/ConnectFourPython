# red gul
# 1   2
# width height
# 1000, 600
import pygame, sys
import numpy as np
import time
move = 350
row_count = 7
col_count = 6
clock = pygame.time.Clock()
top_row_color = (249, 255, 213)
bg = (38, 205, 255)
hole_color = (0, 111, 255)
red_circle = (235, 10, 10)
yellow_circle = (205, 235, 56)
win_color = (255, 255, 255)
pygame.init()
screen = pygame.display.set_mode((700, 700))
# col, row
board = np.zeros((col_count, row_count))
pygame.display.set_caption("Connect 4")

def check_win(player):
    # h check
    for col in range(col_count - 3):
        for row in range(row_count):
            if board[col][row] == player and board[col + 1][row] == player and board[col + 2][row] == player and board[col + 3][row] == player:
                hwinline(col, row)
                return True
    # v check
    for col in range(col_count):
        for row in range(row_count - 3):
            if board[col][row] == player and board[col][row + 1] == player and board[col][row + 2] == player and board[col][row + 3] == player:
                vwinline(col, row)
                return True
    # pos slope
    for col in range(col_count - 3):
        for row in range(row_count - 3):
            if board[col][row] == player and board[col + 1][row + 1] == player and board[col + 2][row + 2] == player and board[col + 3][row + 3] == player:
                poswinline(col, row)
                return True
    # neg slope
    for col in range(col_count - 3):
        for row in range(row_count):
            if board[col][row] == player and board[col + 1][row - 1] == player and board[col + 2][row - 2] == player and board[col + 3][row - 3] == player:
                negwinline(col, row)
                return True

def hwinline(col, row):
    pygame.draw.line(screen, win_color, (row * 100 + 50, col * 100 + 100), (row * 100 + 50, col * 100 + 500), 15)

def vwinline(col, row):
    pygame.draw.line(screen, win_color, (row * 100, col * 100 + 150), (row * 100 + 400, col * 100 + 150), 15)

def negwinline(col, row):
    pygame.draw.line(screen, win_color, (row * 100 + 100, col * 100 + 100), (row * 100 - 300, col * 100 + 500), 15)

def poswinline(col, row):
    pygame.draw.line(screen, win_color, (row * 100, col * 100 + 100), (row * 100 + 400, col * 100 + 500), 15)

def asquare(col, row):
    return board[col][row] == 0

def drop_circle(row):
    mark = True
    for col in range(6):
        if asquare(5 - col, row):
            if mark:
                board[5 - col][row] = player
                mark = False

def draw_circles():
    for col in range(6):
        for row in range(7):
            if board[col][row] == 1:
                pygame.draw.circle(screen, red_circle, (row * 100 + 50, col * 100 + 150), 40)
            if board[col][row] == 2:
                pygame.draw.circle(screen, yellow_circle, (row * 100 + 50, col * 100 + 150), 40)

def move_circle():
    if player == 1:
        color = red_circle
    elif player == 2:
        color = yellow_circle

    pygame.draw.circle(screen, color, (move, 50), 40)

def draw_board():
    pygame.draw.rect(screen, bg, (0, 100, 700, 600))
    for i in range(7):
        for x in range(6):
            pygame.draw.circle(screen, hole_color, (50 + 100 * i, 150 + 100 * x), 40)


draw_board()
player = 1
pressed = False
gameover = True
while 1:
    clock.tick(60)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()

    if event.type == pygame.KEYDOWN and gameover:
        if event.key == pygame.K_RIGHT and not pressed:
            if 50 <= move < 650:
                move += 100
            pressed = True
        if event.key == pygame.K_LEFT and not pressed:
            if 50 < move <= 650:
                move -= 100
            pressed = True
        if event.key == pygame.K_DOWN and not pressed:
            row_drop = int(move // 100)
            if asquare(0, row_drop):
                drop_circle(row_drop)
                draw_circles()
                if check_win(player):
                    gameover = False
                    print("someone won")
                player = player % 2 + 1
            pressed = True

    if event.type == pygame.KEYUP:
        if event.key == pygame.K_LEFT:
            pressed = False
        if event.key == pygame.K_RIGHT:
            pressed = False
        if event.key == pygame.K_DOWN:
            pressed = False

    # game movethings
    if gameover:
        pygame.draw.rect(screen, top_row_color, (0, 0, 700, 100))
        draw_board()
        draw_circles()
        move_circle()
    pygame.display.update()