import pygame as py
import os
import random
py.font.init()

#window info
WIDTH, HEIGHT = 900,  500
WIN = py.display.set_mode((WIDTH, HEIGHT))
py.display.set_caption("i don't know the name")

#background
BG = py.transform.scale(py.image.load(os.path.join("assests", "bg.jpg")), (WIDTH +100 , HEIGHT + 150))

#player
ship = py.image.load(os.path.join("assests", "player.png"))

#obstacales
tridown = py.image.load(os.path.join("assests", "tridown.png"))
triup = py.image.load(os.path.join("assests", "triup.png"))

class player():
    def __init__(self, x, y, health = 1):
        self.x = x
        self.y = y
        self.health = health
        self.image = ship

    def draw(self):
        WIN.blit(self.image, (self.x, self.y))
        
    def get_width(self):
        return self.image.get_width()

    def get_height(self):
        return self.image.get_height()

class  oblstacalse():
    


def main():
    run = True
    FPS = 60
    clock = py.time.Clock()
    player_vel = 15


    
    def movement():
        keys = py.key.get_pressed()
        if keys[py.K_SPACE] and p.y - player_vel + ship.get_height() / 2 > 0:
            p.y -= player_vel 
        else:
            dt = clock.tick(FPS) /2*1.5
            if p.y + ship.get_height() < HEIGHT :
                vel = 2 * dt
                p.y += vel


    def redraw(p):
        WIN.blit(BG, (-50, -80)) 

        p.draw()

        py.display.update()
        
    p = player(WIDTH/4, (HEIGHT/2) - ship.get_height()/2)

    while run:
        redraw(p)
        clock.tick(FPS)
        for event in py.event.get():
            if event.type == py.QUIT:
                quit()
        
        movement()




def main_menu():
    FPS = 60
    clock = py.time.Clock()
    title_font = py.font.SysFont("comicsans", 70, bold=False, italic=False)
    start_font = py.font.SysFont("comicsans",50)
    start_in = 3
    start = False
    run = True
    while run:
        clock.tick(FPS)
        WIN.blit(BG, (-50, -80)) 
        title_label = title_font.render("Press the mouse to begin...", 1, (255,255,255))
        WIN.blit(title_label, (WIDTH/2 - title_label.get_width()/2, HEIGHT/2))
        py.display.update()
        for event in py.event.get():
            if event.type == py.QUIT:
                run = False
            if event.type == py.MOUSEBUTTONDOWN:
                while start_in > 0:
                    if start:
                        start_label = start_font.render(str(start_in), 1, (255,255,255))
                        WIN.blit(start_label, (WIDTH/2 - start_label.get_width()/2, HEIGHT/2))
                        start_in -=1
                    
                    continue

                main()
    py.quit()



if __name__ == "__main__":
    main_menu()
