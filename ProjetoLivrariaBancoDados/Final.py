import copy  
import math  
from asciimatics.effects import Cycle, Print  
from asciimatics.renderers import SpeechBubble, FigletText  
from asciimatics.scene import Scene  
from asciimatics.screen import Screen  
from asciimatics.sprites import Arrow  
from asciimatics.paths import Path  
from asciimatics.exceptions import ResizeScreenError  
import sys  

def run_asciimatics_demo():  
    def _speak(screen, text, pos, start):  
        return Print(  
            screen,  
            SpeechBubble(text, "L", uni=screen.unicode_aware),  
            x=pos[0] + 4, y=pos[1] - 4,  
            colour=Screen.COLOUR_CYAN,  
            clear=True,  
            start_frame=start,  
            stop_frame=start + 50  
        )  

    def demo(screen):  
        scenes = []  
        centre = (screen.width // 2, screen.height // 2)  
        podium = (8, 5)  

        # Scene 7.  
        path = Path()  
        path.jump_to(podium[0], podium[1])  
        path.wait(60)  
        path.move_straight_to(-5, podium[1], 20)  
        path.wait(300)  

        effects = [  
            Arrow(screen, path, colour=Screen.COLOUR_GREEN),  
            _speak(screen, "Até logo!", podium, 10),  
            Cycle(screen,  
                  FigletText("FIM!"),  
                  centre[1] - 4,  
                  start_frame=100),  
            Print(screen, SpeechBubble("Pressione X para sair"), centre[1] + 6,  
                  start_frame=150)  
        ]  
        scenes.append(Scene(effects, 500))  

        screen.play(scenes, stop_on_resize=True)  

    while True:  
        try:  
            Screen.wrapper(demo)  
            sys.exit(0)  # Saindo após execução bem-sucedida  
        except ResizeScreenError:  
            pass  

if __name__ == "__main__":  
    run_asciimatics_demo()