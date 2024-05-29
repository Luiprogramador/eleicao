from time import sleep


def votar(lista_votos):
    votos_nulos = lista_votos.count("0")
    primeiro = lista_votos.count('1')
    segundo = lista_votos.count('2')
    terceiro = lista_votos.count('3')
    branco = lista_votos.count(' ')
    pct_nulo = (lista_votos.count('0') / len(lista_votos)) * 100
    pct_branco = (lista_votos.count(' ') / len(lista_votos)) * 100
    pct_1 = (lista_votos.count('1') / len(lista_votos)) * 100
    pct_2 = (lista_votos.count('2') / len(lista_votos)) * 100
    pct_3 = (lista_votos.count('3') / len(lista_votos)) * 100
    print('-' * 30)
    sleep(1)
    print(f'O total de votos é {len(lista_votos)}')
    sleep(0.4)
    print(f'Votos nulos: {votos_nulos}')
    sleep(0.4)
    print(f'Votos para o primeiro candidato: {primeiro} votos')
    sleep(0.4)
    print(f'Votos para o segundo candidato: {segundo} votos')
    sleep(0.4)
    print(f'Votos para o terceiro candidato: {terceiro} votos')
    sleep(0.4)
    print(f'Votos em branco: {branco}')
    print('-' * 30)
    sleep(0.4)
    print(f'A pct de votos nulos é {pct_nulo:.3f}%')
    sleep(0.4)
    print(f'A pct de votos em braco é {pct_branco:.3f}%')
    sleep(0.4)
    print(f'A pct de votos do 1° candidato é {pct_1:.3f}%')
    sleep(0.4)
    print(f'A pct de votos em braco é {pct_2:.3f}%')
    sleep(0.4)
    print(f'A pct de votos nulos é {pct_3:.3f}%')
    print('-' * 30)


def resultado(listi):
    primeiro = listi.count('1')
    segundo = listi.count('2')
    terceiro = listi.count('3')
    if primeiro > segundo and primeiro > terceiro:
        sleep(0.4)
        print('O 1° candidato ganhou.')
    elif segundo > primeiro and segundo > terceiro:
        sleep(0.4)
        print('O 2° candidato ganhou.')
    elif terceiro > primeiro and terceiro > segundo:
        sleep(0.4)
        print('O 3° candidato ganhou.')
    elif primeiro > segundo and primeiro == terceiro:
        sleep(0.4)
        print('O 1° e o 3° candidato empataram')
    elif primeiro > terceiro and primeiro == segundo:
        sleep(0.4)
        print('O 1° e o 2° candidato empataram')
    elif segundo > primeiro and segundo == terceiro:
        sleep(0.4)
        print('O 2° e o 3° candidato empataram')
    else:
        sleep(0.4)
        print('todos empataram.')


if __name__ == '__main__':
    votos = []
    try:
        while True:
            vote = input("Digite o seu voto(Utilize 's' para sair): [1], [2], [3], [0], [ ]: ")
            if vote == 's':
                break
            elif vote not in ['1', '2', '3', '0', ' ']:
                sleep(0.4)
                print("Digite um valor válido para votação.")
                continue
            votos.append(vote)
        if len(votos) == 0:
            sleep(0.4)
            print('Não houve votos')
        else:
            print('\033[7;49;93m processando \033[m')
            votar(votos)
            resultado(votos)
    except KeyboardInterrupt:
        sleep(0.4)
        print('\nO programa foi interrompido manualmente')
