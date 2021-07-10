import pygame as pg
import random


orig_set = [1,2,3,4,5,6,7,8,0]

def swap(loc1, loc2):
    temp = orig_set[loc1]
    orig_set[loc1] = orig_set[loc2]
    orig_set[loc2] = temp
    print(str(orig_set[loc1]) + " swapped to " + str(orig_set[loc2]))

def random_swap():
    empty_square = orig_set.index(0)
    if empty_square == 0:
        rand_swap = random.randint(0,1)
        if rand_swap == 0:
            swap(empty_square, (1))
        if rand_swap == 1:
            swap(empty_square, (3))
    if empty_square == 1:
        rand_swap = random.randint(0,2)
        if rand_swap == 0:
            swap(empty_square, (0))
        if rand_swap == 1:
            swap(empty_square, (2))
        if rand_swap == 2:
            swap(empty_square, (4))
    if empty_square == 2:
        rand_swap = random.randint(0,1)
        if rand_swap == 0:
            swap(empty_square, (1))
        if rand_swap == 1:
            swap(empty_square, (5))
    if empty_square ==3:
        rand_swap = random.randint(0,2)
        if rand_swap == 0:
            swap(empty_square, (0))
        if rand_swap == 1:
            swap(empty_square, (4))
        if rand_swap == 2:
            swap(empty_square, (6))
    if empty_square == 4:
        rand_swap = random.randint(0,3)
        if rand_swap == 0:
            swap(empty_square, (1))
        if rand_swap == 1:
            swap(empty_square, (3))
        if rand_swap == 2:
            swap(empty_square, (5))
        if rand_swap == 3:
            swap(empty_square, (7))
    if empty_square == 5:
        rand_swap = random.randint(0,2)
        if rand_swap == 0:
            swap(empty_square, (2))
        if rand_swap == 1:
            swap(empty_square, (4))
        if rand_swap == 2:
            swap(empty_square, (8))
    if empty_square == 6:
        rand_swap = random.randint(0,1)
        if rand_swap == 0:
            swap(empty_square, (3))
        if rand_swap == 1:
            swap(empty_square, (7))
    if empty_square == 7:
        rand_swap = random.randint(0,2)
        if rand_swap == 0:
            swap(empty_square, (4))
        if rand_swap == 1:
            swap(empty_square, (6))
        if rand_swap == 2:
            swap(empty_square, (8))
    if empty_square == 8:
        rand_swap = random.randint(0,1)
        if rand_swap == 0:
            swap(empty_square, (7))
        if rand_swap == 1:
            swap(empty_square, (5))
    


for i in range(100):
    random_swap()










pg.init()

window = pg.display.set_mode((500,500))
pg.display.set_caption("Dad's Game")

end_running = True
running = True
class Block:
    def __init__(self,blockNumber):
        self.blockNumber = blockNumber

boxes = []

tl_cord = 165
m_cord = 225
br_cord = 285

cords = [165,225,285]

for i in range(9):
    boxes.append(Block(orig_set[i]))


font = pg.font.SysFont(None, 50)
img = font.render("Dad's Game", True, (255,255,255))
window.blit(img, (150, 70))

def switch_boxes(box1, box2):
    loc_box1 = boxes.index(box1)
    loc_box2 = boxes.index(box2)
    boxes[loc_box1] = box2
    boxes[loc_box2] = box1
win = False


while running:
    pg.time.delay(100)

    pos = (0,0)

    for event in pg.event.get():
        if event.type == pg.QUIT:
            running = False
        if event.type == pg.MOUSEBUTTONUP:
            pos = pg.mouse.get_pos()
            print(str(pos))

    blank_loc = 0
    for i in range(9):
        if boxes[i].blockNumber == 0:
            blank_loc = i

    if pos[0]>tl_cord and pos[0]<tl_cord+50:
        if pos[1]>tl_cord and pos[1]<tl_cord+50:
            if blank_loc == 1 or blank_loc == 3:
                switch_boxes(boxes[blank_loc], boxes[0])
        if pos[1]>m_cord and pos[1]<m_cord+50:
            if blank_loc == 0 or blank_loc == 4 or blank_loc == 6:
                switch_boxes(boxes[blank_loc], boxes[3])
        if pos[1]>br_cord and pos[1]<br_cord+50:
            if blank_loc == 3 or blank_loc == 7:
                switch_boxes(boxes[blank_loc], boxes[6])
    if pos[0]>m_cord and pos[0]<m_cord+50:
        if pos[1]>tl_cord and pos[1]<tl_cord+50:
            if blank_loc == 0 or blank_loc == 2 or blank_loc == 4:
                switch_boxes(boxes[blank_loc], boxes[1])
        if pos[1]>m_cord and pos[1]<m_cord+50:
            if blank_loc == 1 or blank_loc == 3 or blank_loc == 5 or blank_loc == 7:
                switch_boxes(boxes[blank_loc], boxes[4])
        if pos[1]>br_cord and pos[1]<br_cord+50:
            if blank_loc == 4 or blank_loc == 6 or blank_loc == 8:
                switch_boxes(boxes[blank_loc], boxes[7])
    if pos[0]>br_cord and pos[0]<br_cord+50:
        if pos[1]>tl_cord and pos[1]<tl_cord+50:
            if blank_loc == 1 or blank_loc == 5:
                switch_boxes(boxes[blank_loc], boxes[2])
        if pos[1]>m_cord and pos[1]<m_cord+50:
            if blank_loc == 2 or blank_loc == 4 or blank_loc == 8:
                switch_boxes(boxes[blank_loc], boxes[5])
        if pos[1]>br_cord and pos[1]<br_cord+50:
            if blank_loc == 5 or blank_loc == 7:
                switch_boxes(boxes[blank_loc], boxes[8])

  
    for j in range(3):
        for k in range(3):
            if(boxes[3*k+j].blockNumber!=0):
                pg.draw.rect(window, (255,255,255), (cords[j],cords[k],50,50))
                num_font = pg.font.SysFont(None, 50)
                num_img = num_font.render(str(boxes[j+3*k].blockNumber), True, (0,0,0))
                window.blit(num_img, (cords[j]+15,cords[k]+10))
            else:
                pg.draw.rect(window, (50,50,50), (cords[j],cords[k],50,50))

    win = True

    for i in range(8):
        if i+1 != boxes[i].blockNumber:
            win = False
    
    if win:
        running = False


    
    pg.display.update()

if(win == True):
    winner_banner = True
    while end_running:
        pg.time.delay(500)
        if winner_banner:
            num_font = pg.font.SysFont(None, 50)
            num_img = num_font.render("WINNER", True, (255,255,255))
            window.blit(num_img, (175,400))
            winner_banner = False
        else:
            num_font = pg.font.SysFont(None, 50)
            num_img = num_font.render("WINNER", True, (0,0,0))
            window.blit(num_img, (175,400))
            winner_banner = True


        for event in pg.event.get():
            if event.type == pg.QUIT:
                end_running = False
        pg.display.update()


pg.quit()