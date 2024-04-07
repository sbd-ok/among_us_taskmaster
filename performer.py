from pynput import mouse
from pyautogui import pixelMatchesColor,moveTo,pixel,moveRel,locateCenterOnScreen,screenshot
from time import sleep
import pygame

m = mouse.Controller()
left_button = mouse.Button.left

def contains_red(img:pygame.Surface):
    w,h = img.get_width(),img.get_height()
    for i in range(w):
        for j in range(h):
            if img.get_at((i,j)) == (255,0,0,255):return True
    return False

def remove_dups(array:list):
    new_list = []
    for i,element in enumerate(array):
        if not element in new_list: new_list.append(element)
    return new_list

def perform_task(task):
    match task:
        case "down/up":
            m.position = (1028,634)
            m.click(left_button)
        
        case "clean_vent":
            m.position = (933,371)
            m.click(left_button)
            sleep(0.5)
            screenshot("data/img_recog.png",[547,174,832,725])
            offset_x,offset_y = 547,174
            img = pygame.image.load("data/img_recog.png")
            size = 100
            positions = []
            for i in range(int(832)):
                for j in range(int(725)):
                    threshold = sum(img.get_at((i,j))[:3])
                    if threshold < 110:
                        pygame.draw.rect(img,(255,0,0),[i,j,1,1])
                        positions.append([i//size*size+15,j//size*size+15])
            positions = remove_dups(positions)
            for position in positions:
                m.position = (position[0]+offset_x,position[1]+offset_y)
                m.click(left_button)
                sleep(0.1)
            pygame.image.save(img,"data/img_recog_program.png")

        case "admin_swipe":
            m.position = (792,834)
            m.click(left_button)
            sleep(1)
            m.position = (648,473)
            m.press(left_button)
            moveRel(1000,0,0.8)
            m.release(left_button)

        case "refuel":
            m.position = (1470,884)
            m.press(left_button)
            sleep(3.2)
            m.release(left_button)

        case "prime_shield":
            delay = 0.1
            positions = [(1161,391),(966,335),(777,427),(758,642),(907,736),(1159,698),(983,535)]
            for position in positions:
                if pixel(position[0],position[1])[1] < 150:
                    m.position = position
                    m.click(left_button)
                    sleep(delay)

        case "divert_power":
            positions = [(632,788),(726,788),(824,788),(924,788),(1019,788),(1115,788),(1211,788),(1308,788)]
            for position in positions:
                if pixel(position[0],position[1])[0] > 150:
                    m.position = position
                    m.press(left_button)
                    moveRel(0,-100,0.2)
                    m.release(left_button)
                    break
        
        case "accept_power":
            m.position = (960,544)
            m.click(left_button)

        case "garbage":
            m.position = (1283,417)
            m.press(left_button)
            moveRel(0,250,0.1)
            sleep(2)
            m.release(left_button)

        case "stabilize_steering":
            m.position = (979,540)
            m.click(left_button)

        case "wires":
            positions = [272,460,645,831]
            for position in positions:
                color = pixel(568,position)
                if color == (38,38,255): destination = (1312,460)
                elif color == (255,235,4): destination = (1312,645)
                elif color == (255,0,0): destination = (1312,273)
                elif color == (255,0,255): destination = (1312,829)

                m.position = (568,position)
                m.press(left_button)
                moveTo(destination[0],destination[1],0.2)
                m.release(left_button)
                sleep(0.1)
        
        case "chart_course":
            ship_pos = locateCenterOnScreen("data/nav_ship.png",confidence=0.7)
            positions = [(710,254,105,567),(908,264,115,558),(1093,258,124,561),(1303,258,110,561)]
            for i in range(4):
                dest_pos = locateCenterOnScreen("data/nav.png",confidence=0.55,region=positions[i])
                m.position = ship_pos
                m.press(left_button)
                moveTo(dest_pos[0],dest_pos[1]+35,0.1)
                m.release(left_button)
                ship_pos = dest_pos
                sleep(0.3)

        case "calibrate_distributor":
            while 1:
                while pixelMatchesColor(1253,235,(0,0,0)): pass
                m.position = (1231,314)
                m.click(left_button)
                if pixelMatchesColor(1253,235,(0,0,0)): continue
                while pixelMatchesColor(1253,500,(0,0,0)): pass
                m.position = (1231,582)
                m.click(left_button)
                if pixelMatchesColor(1253,235,(0,0,0)): continue
                while pixelMatchesColor(1253,767,(0,0,0)): pass
                m.position = (1231,837)
                m.click(left_button)
                if pixelMatchesColor(1253,235,(0,0,0)): continue
                break

        case "align_output":
            screenshot("data/img_recog.png",[1150,115,240,845])
            offset_x,offset_y = 1150,115
            img = pygame.image.load("data/img_recog.png")
            size = 80
            positions = []
            for i in range(int(240)):
                for j in range(int(845)):
                    threshold = sum(img.get_at((i,j))[:3])
                    if threshold > 600:
                        pygame.draw.rect(img,(255,0,0),[i,j,1,1])
                        positions.append([i//size*size+40,j//size*size+40])
            positions = remove_dups(positions)
            m.position = (positions[0][0]+offset_x,positions[0][1]+offset_y)
            m.press(left_button)
            moveTo(1247,555,0.1)
            m.release(left_button)
            
            pygame.image.save(img,"data/img_recog_program.png")


        case "inspect_sample_1":
            m.position = (1262,935)
            m.click(left_button)
        
        case "inspect_sample_2":
            positions = [732,844,961,1072,1186]
            button_positions = [733,848,960,1072,1189]
            for i,position in enumerate(positions):
                if pixelMatchesColor(position,591,(246,134,134)): 
                    m.position = (button_positions[i],850)
                    m.click(left_button)
                    break