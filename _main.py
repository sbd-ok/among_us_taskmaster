print("Loading...")
from keyboard import is_pressed
import pygame
from time import perf_counter
import detector,performer

key = "r"

clock = pygame.time.Clock()

def main():
    print(f"Initialized Taskmaster!\nPress [{key}] to detect and perform a task.\nNote: Play Among Us in fullscreen for this to work.")
    while 1:
        if is_pressed(key): 
            t = perf_counter()
            current_task = detector.detect_task()
            if current_task:
                print(current_task)
                print(f"Task detected in {perf_counter()-t} seconds.")
                performer.perform_task(current_task) 
            else: print("Couldn't detect the task...")
        clock.tick(30)

if __name__ == "__main__": main()