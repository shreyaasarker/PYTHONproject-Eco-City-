import pygame
import random
import time

# Initialize Pygame
pygame.init()

# Set up display
width, height = 800, 600
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption("Eco-City")

# Colors
white = (255, 255, 255)
black = (0, 0, 0)
green = (0, 255, 0)
red = (255, 0, 0)
blue = (0, 0, 255)
grey = (128, 128, 128)

# Tile size
tile_size = 20

# Game variables
pollution_level = 0
population = 100
resources = 1000
happiness = 100

# Tile types
EMPTY = 0
RESIDENTIAL = 1
COMMERCIAL = 2
INDUSTRIAL = 3
PARK = 4

# Create a 2D array to represent the city grid
grid = [[EMPTY for x in range(width // tile_size)] for y in range(height // tile_size)]

# Function to draw the grid
def draw_grid():
    for x in range(0, width, tile_size):
        pygame.draw.line(screen, grey, (x, 0), (x, height))
    for y in range(0, height, tile_size):
        pygame.draw.line(screen, grey, (0, y), (width, y))

# Function to draw tiles
def draw_tiles():
    for x in range(len(grid)):
        for y in range(len(grid[0])):
            if grid[x][y] == RESIDENTIAL:
                pygame.draw.rect(screen, grey, (x * tile_size, y * tile_size, tile_size, tile_size))
            elif grid[x][y] == COMMERCIAL:
                pygame.draw.rect(screen, blue, (x * tile_size, y * tile_size, tile_size, tile_size))
            elif grid[x][y] == INDUSTRIAL:
                pygame.draw.rect(screen, red, (x * tile_size, y * tile_size, tile_size, tile_size))
            elif grid[x][y] == PARK:
                pygame.draw.rect(screen, green, (x * tile_size, y * tile_size, tile_size, tile_size))

# Function to handle user input
def handle_input():
    global grid
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            quit()
        if event.type == pygame.MOUSEBUTTONDOWN:
            mouse_pos = pygame.mouse.get_pos()
            grid_x = mouse_pos[0] // tile_size
            grid_y = mouse_pos[1] // tile_size
            if grid[grid_x][grid_y] == EMPTY:
                if event.button == 1:  # Left click: Residential
                    grid[grid_x][grid_y] = RESIDENTIAL
                elif event.button == 3:  # Right click: Commercial
                    grid[grid_x][grid_y] = COMMERCIAL
                elif event.button == 2:  # Middle click: Industrial
                    grid[grid_x][grid_y] = INDUSTRIAL

# Function to update game state
def update():
    global pollution_level, population, resources, happiness
    pollution_level = 0
    population = 0
    resources = 0

    for x in range(len(grid)):
        for y in range(len(grid[0])):
            if grid[x][y] == INDUSTRIAL:
                pollution_level += 1
            elif grid[x][y] == RESIDENTIAL:
                population += 1
            elif grid[x][y] == COMMERCIAL:
                resources += 1

    # Calculate happiness (consider pollution and resources)
    happiness = 100 - pollution_level + resources // 10

# Function to display game information
def display_info():
    font = pygame.font.Font(None, 24)
    text_pollution = font.render("Pollution: " + str(pollution_level), True, red)
    text_population = font.render("Population: " + str(population), True, white)
    text_resources = font.render("Resources: " + str(resources), True, green)
    text_happiness = font.render("Happiness: " + str(happiness), True, white)
    screen.blit(text_pollution, (10, 10))
    screen.blit(text_population, (10, 40))
    screen.blit(text_resources, (10, 70))
    screen.blit(text_happiness, (10, 100))

# Game loop
while True:
    screen.fill(black)
    draw_grid()
    draw_tiles()
    handle_input()
    update()
    display_info()
    pygame.display.update()
    time.sleep(0.1)

#Gameplay
#City Building:
#Left-click: Build residential zones (grey tiles).
#Right-click: Build commercial zones (blue tiles).
#Middle-click: Build industrial zones (red tiles).
#Game Progression:
#As you build residential zones, the population will increase.
#As you build commercial zones, resources will increase.
#As you build industrial zones, pollution will increase.
#The game will automatically calculate and display pollution levels, population, resources, and happiness.
#Observe the Impact:
#See how pollution affects happiness.
#See how resources contribute to happiness.
#Experiment with different city layouts to maximize happiness and minimize pollution.
#Basic Economics: It introduces basic economic concepts like resource production and consumption.
#Environmental Impact: You can directly observe the impact of industrialization on the environment.
#Park Zones: Add park zones (green tiles) to reduce pollution.
#Pollution Spread: Implement more realistic pollution spread mechanisms.
#Resource Consumption: Model resource consumption by the population.
#Policy Implementation: Introduce policies (e.g., pollution taxes, renewable energy subsidies).
#Environmental Disasters: Simulate events like floods, droughts, or pollution outbreak.
#Visual Enhancements: Improve the visual appeal of the game.
