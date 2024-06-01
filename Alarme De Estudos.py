import pygame
import time
pygame.init()

som = pygame.mixer.Sound("alarme.wav")

print("\n" * 3)


def iniciar_tempo(tempo_segundos):
    print(f"Iniciando temporizador para {tempo_segundos // 60} minutos de estudo.")
    time.sleep(tempo_segundos)
    som.play()


while True:
    print("                     =-=-= ALARME DE ESTUDOS =-=-=")
    print(" - A ideia desse alarme é você estudar ininterruptamente durante o tempo escolhido,\ntente ao máximo cumprir o tempo desejado para obter melhor resultado nos estudos.")
    print(" Quanto tempo deseja estudar: ")
    print("[ 1 ] - 15 Minutos")
    print("[ 2 ] - 30 Minutos")
    print("[ 3 ] - 1 Hora")
    print("[ 4 ] - Encerrar Programa")
    opcao = int(input("Opção: "))

    if opcao == 1:
        iniciar_tempo(900)
        print("Você completou os seus 15 minutos de estudo, parabéns!!")
        time.sleep(10)
        break
    elif opcao == 2:
        iniciar_tempo(1800)
        print("Você completou os seus 30 minutos de estudo, parabéns!!")
        time.sleep(10)
        break
    elif opcao == 3:
        iniciar_tempo(3600)
        print("Você completou a sua 1 hora de estudo, parabéns!!")
        time.sleep(10)
        break
    elif opcao == 4:
        print("Encerrando Programa!")
        break
    elif 0 >= opcao > 4:
        print("Opção Inválida, tente novamente.")

while pygame.mixer.get_busy():
    pygame.time.wait(100)

pygame.quit()
