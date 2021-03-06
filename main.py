import pygame as py
import os
import random
import time
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
TRIDOWN = py.image.load(os.path.join("assests", "tridown.png"))
TRIUP = py.image.load(os.path.join("assests", "triup.png"))

class player():


    def __init__(self, x, y, health = 1):
        self.x = x
        self.y = y
        self.health = health
        self.image = ship
        self.mask = py.mask.from_surface(ship)
        
    def draw(self):
        WIN.blit(self.image, (self.x, self.y))
        
    def get_width(self):
        return self.image.get_width()

    def get_height(self):
        return self.image.get_height()




class  Oblstacale():
    ORINTAION = {
        'a': TRIUP,
        'b': TRIDOWN

    }
    def __init__(self, downy, upy, x, y, type):
        self.img = self.ORINTAION[type] 
        self.mask = py.mask.from_surface(self.img)
        self.upy = upy
        self.downy = downy
        self.x = x
        
        

    def move(self, vel):
        self.x += vel
    def draw(self, window):
        if self.img ==  TRIUP:
            WIN.blit(TRIUP, (self.x, self.upy))
        if self.img == TRIDOWN:
            WIN.blit(TRIDOWN, (self.x, self.downy))
    

    
    


def main():
    run = True
    FPS = 60
    clock = py.time.Clock()
    player_vel = 15
    main_font = py.font.SysFont("comicsans", 50)
    level = 0


    oblstacales = []
    wave_len = 10
    enemy_vel = -50
    rang = 1200

    
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

        level_label = main_font.render(f"level: {level}", 1, (255,255,255))

        WIN.blit(level_label, (10, 10))

        for oblstacale in oblstacales:
            oblstacale.draw(WIN)

        p.draw()



        py.display.update()
        
    p = player(WIDTH//4, (HEIGHT//2) - ship.get_height()//2)

    while run:
        redraw(p)
        clock.tick(FPS)

        if len(oblstacales) == 0:
            level += 1
            wave_len += 5
            for oblstacale in range(wave_len):
                oblstacale = Oblstacale(random.randrange(-600, 0), random.randrange(500, 600), random.randrange(900, rang),0, random.choice(('a', 'b')))
                oblstacales.append(oblstacale)
        
        for oblstacale in oblstacales[:]:
            oblstacale.move(enemy_vel)
       
        offset_x = oblstacale.x - p.x
        offset_y = oblstacale.y - p.y        
        if p.mask.overlap(oblstacale.mask(offset_x, offset_y)):

            print('works')

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
                    
                    py.display.update()

                    time.sleep(1) 

                if start_in == 0:
                        start = True

                    
                    
            if start == True:
                  

                main()
    py.quit()



if __name__ == "__main__":
    main_menu()
