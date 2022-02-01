import sys
try:
    import pygame

    from constants import *

    from objects.button import ButtonObj
    
    from libs.inputbox.inputbox import InputBox

    pygame.init()

    SIZE = WIDTH, HEIGHT = 720, 540
    screen = pygame.display.set_mode(SIZE)
    font = pygame.font.SysFont('arial', 32)

    FPS = 30
    clock = pygame.time.Clock()

    stop_app = False
    update_field = False

    def start():
        global update_field
        update_field = not(update_field)
        
    def clear():
        global field
        field = [[0] * width]
        field[0][width//2] = 1
    
    def draw(screen, field, size=2, barrier=5):
        for i in range(len(field)):
            for j in range(len(field[i])):
                color = WHITE if field[i][j] else BLACK
                pygame.draw.rect(screen, color,
                    (barrier + j*size, barrier + i*size, size, size))
    
    def draw_barrier(screen, width=355, height=200, size=2, barrier=5):
        pygame.draw.rect(screen, modRED,
            (0, 0, barrier, size*height+2*barrier))
        pygame.draw.rect(screen, modRED,
            (0, size*height+2*barrier, size*width+2*barrier, barrier))
        pygame.draw.rect(screen, modRED,
            (0, 0, size*width+2*barrier, barrier))
        pygame.draw.rect(screen, modRED,
            (size*width+barrier, 0, barrier, size*height+2*barrier))
    
    
    def get_value(key, rule=[0, 0, 0, 1, 1, 1, 1, 0]):
        key = key[0]*4 + key[1]*2 + key[2]
        return rule[len(rule) - key - 1]
        
    
    def logic(field, rule, max_height=202):
        if len(field) % max_height == 0:
            field = [field[-1].copy()]
        field.append([])
        for j in range(len(field[0])):
            print(j)
            value = get_value(
                (
                field[-2][j-1],
                field[-2][j],
                field[-2][(j+1)%len(field[0])]
                ),
                rule
            )
            print('/j')
            field[-1].append(value)
        return field
    
    
    size = width, height, = 355, 200
    
    field = [[0] * width]
    field[0][width//2] = 1

    button_start = ButtonObj(WIDTH - 90, HEIGHT - 60, 70, 40, modGREEN, start, 'start', font)
    
    button_clear = ButtonObj(WIDTH - 170, HEIGHT - 60, 70, 40, modGREEN, clear, 'clear', font)
    
    rect_inputbox = [10, HEIGHT - 80, 50, 50]
    
    inputbox = InputBox(*rect_inputbox, font)
    
    
    rule = 15
    rule = [int(x) for x in f"{rule:08b}"]
    while not stop_app:
        pygame.display.set_caption(f'Rule-{rule}: '+str(int(clock.get_fps())))
        
        for event in pygame.event.get():
            button_start.process_event(event)
            button_clear.process_event(event)
            if not update_field:
                inputbox.handle_event(event)
            if event.type == pygame.QUIT:
                stop_app = True
         
        if update_field:
            field = logic(field, rule)
        else:
            inputbox.update()
            text = inputbox.text
            if text.isdigit():
                text = int(text)
                rule = [int(x) for x in f"{text:08b}"]
        
        screen.fill(BLACK)
        draw_barrier(screen)
        draw(screen, field)
        button_start.process_draw(screen)
        button_clear.process_draw(screen)
        inputbox.draw(screen)
        
        pygame.display.flip()
        clock.tick(FPS)
        
except Exception as e:
    input(e)
except SyntaxError as e:
    input(e)

sys.exit()