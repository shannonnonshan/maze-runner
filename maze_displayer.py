import json
import pygame

# Kích thước màn hình
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 700

# Tạo màn hình
pygame.init()
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption('Maze Game')

# Đọc dữ liệu từ file maze_metadata.json
with open('maze_metadata.json', 'r') as f:
    maze_data = json.load(f)

# Load images and scale them to appropriate size
bot_img = pygame.image.load(r'C:\Users\Hi\Pictures\assets\superhero.png')
bot_size = int(min(SCREEN_WIDTH/maze_data['width'], SCREEN_HEIGHT/maze_data['height']))
bot_img = pygame.transform.scale(bot_img, (bot_size, bot_size))

coin_img = pygame.image.load(r'C:\Users\Hi\Pictures\assets\coin.png')
coin_img = pygame.transform.scale(coin_img, (int(SCREEN_WIDTH/13), int(SCREEN_WIDTH/18)))

tree_img = pygame.image.load(r'C:\Users\Hi\Pictures\assets\apple-tree.png')
tree_size = int(min(SCREEN_WIDTH/maze_data['width'], SCREEN_HEIGHT/maze_data['height']))
tree_img = pygame.transform.scale(tree_img, (tree_size, tree_size))

background_img = pygame.image.load(r'C:\Users\Hi\Pictures\assets\background.jpg')
background_img = pygame.transform.scale(background_img, (SCREEN_WIDTH, SCREEN_HEIGHT))

# Lấy thông tin về ma trận maze, robot và đồng xu từ maze_data
matrix = [[' ' for _ in range(maze_data['width'])] for _ in range(maze_data['height'])]
bot_pos = maze_data['bot'][::1] # Đảo ngược vị trí của robot


coin_pos = maze_data['coin'][::1] # Đảo ngược vị trí của đồng xu


for obs in maze_data['obstacles']:
    matrix[obs[0]][obs[1]] = '*' # Đảo ngược tọa độ của vật cản
   # matrix[obs[0]][obs[1]] += 150  # Add 150 to obstacle's x position

# Hiển thị ma trận maze trên màn hình
cell_width = SCREEN_WIDTH // maze_data['width']
cell_height = SCREEN_HEIGHT // maze_data['height']
for i in range(maze_data['height']):
    for j in range(maze_data['width']):
        x = j * cell_width 
        y = i * cell_height + 70
        if matrix[i][j] == '*':
            screen.blit(tree_img, (x + cell_width//2 - tree_img.get_width()//2, y + cell_height//2 - tree_img.get_height()//2))
        elif (i, j) == tuple(bot_pos):
            screen.blit(bot_img, (x + cell_width//2 - bot_img.get_width()//2, y + cell_height//2 - bot_img.get_height()//2))
        elif (i, j) == tuple(coin_pos):
            screen.blit(coin_img, (x + cell_width//2 - coin_img.get_width()//2, y + cell_height//2 - coin_img.get_height()//2))
        else:
            screen.blit(background_img, (x, y))
        pygame.draw.rect(screen, pygame.Color('black'), pygame.Rect(x, y, cell_width, cell_height), 1)

# Vòng lặp chính của game
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    # Cập nhật màn hình
    pygame.display.flip()

# Đóng cửa sổ
pygame.quit()