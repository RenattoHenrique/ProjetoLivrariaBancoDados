from asciimatics.effects import Cycle, Print  
from asciimatics.renderers import SpeechBubble, FigletText  
from asciimatics.scene import Scene  
from asciimatics.screen import Screen  
from asciimatics.sprites import Arrow  
from asciimatics.paths import Path  
from asciimatics.exceptions import ResizeScreenError  
import sys  

def _speak(screen, text, pos, start):  
    return Print(  
        screen,  
        SpeechBubble(text, "L", uni=screen.unicode_aware),  
        x=pos[0] + 4, y=pos[1] - 4,  
        colour=Screen.COLOUR_CYAN,  
        clear=True,  
        start_frame=start,  
        stop_frame=start + 50)  

def cena_inicial(screen, centre, podium):  
    path = Path()  
    path.jump_to(-20, centre[1])  
    path.move_straight_to(centre[0], centre[1], 10)  
    path.wait(30)  
    path.move_straight_to(podium[0], podium[1], 10)  
    path.wait(100)  

    return [  
        Arrow(screen, path, colour=Screen.COLOUR_GREEN),  
        _speak(screen, "Bem-vindo à Bookland!", centre, 30),  
        _speak(screen, "Oi, eu sou o João! Vou te mostrar o nosso ótimo software de gerenciamento para a Livraria.", podium, 110),  
    ]  

def cena_funcionalidades(screen, podium, centre):  
    path = Path()  
    path.jump_to(podium[0], podium[1])  

    return [  
        Arrow(screen, path, colour=Screen.COLOUR_GREEN),  
        _speak(screen, "O sistema conta com várias funcionalidades interessantes. Aproveite!", podium, 10),  
        Cycle(screen,  
            FigletText("Livraria Bookland!"),  
            centre[1] - 5,  
            start_frame=100),  
    ]  

def abertura(screen):  
    """Exibe a animação de introdução com controle de duração."""
    centre = (screen.width // 2, screen.height // 2)  
    podium = (8, 5)  

    # Cria as cenas
    scenes = [  
        Scene(cena_inicial(screen, centre, podium), 200),  
        Scene(cena_funcionalidades(screen, podium, centre), 150),  # Tempo ajustado para incluir os 10 segundos finais  
    ]  

    # Executa as cenas e força o término após 10 segundos de letreiro
    screen.play(scenes, stop_on_resize=True, repeat=False)  

def animacao_intro():  
    """Função para executar a animação de introdução e encerrar após o letreiro."""
    try:  
        Screen.wrapper(abertura)  
    except ResizeScreenError:  
        pass  
    finally:  
        # Animação finalizada após 10 segundos
        print("")