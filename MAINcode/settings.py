from pygame.math import Vector2

# layar
LAYAR_LEBAR = 640
LAYAR_TINGGI = 360
TILE_SIZE = 64

#posisi UI
OVERLAY_POSITIONS = {
    'tool' : (40, LAYAR_LEBAR - 15),
    'seed' : (70, LAYAR_LEBAR - 5)
}

PLAYER_TOOL_OFFSET = {
    'left': Vector2(-50,40),
    'right': Vector2(50,40),
    'up': Vector2(0,-10),
    'down': Vector2(0,59),
}

LAYERS = {
    'water': 0,
    'ground': 1,
    'soil': 2,
    'soil water': 3,
    'rain floor': 4,
    'house bottom': 5,
    'ground plant': 6,
    'main': 7,
    'house top': 8,
    'fruit': 9,
    'rain drops': 10,
}
