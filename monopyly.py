import operator
import statistics
from utils import Colors
from models.board import Board
from models.player import (
    BEHAVIOR_NAMES,
    IMPULSIVE,
    PICKY,
    WARY,
    RANDOM)
from utils import print_line, print_header

if __name__ == '__main__':
    results = []
    for x in range(0, 300):
        b = Board(20)
        result = b.play(1000)
        results.append(result)
    print(Colors.clear)  # Limpar terminal
    # Quantas partidas terminam por time out (1000 rodadas)
    print_header('🎲 Quantas partidas terminam por time out (1000 rodadas)')
    timeout_count = [x for x in results if x[1] == 1]
    print_line('Total', len(timeout_count))

    # Quantos turnos em média demora uma partida
    shifts = [x[2] for x in results]
    mean = statistics.mean(shifts)  # or sum(shifts) / len(shifts)
    print_header('⏳ Quantos turnos em média demora uma partida')
    print_line('Média', f'{mean:.2f}')
    print_line('Máximo', f'{max(shifts):.2f}')

    # Qual a porcentagem de vitórias por comportamento dos jogadores
    print_header('➗ Qual a porcentagem de vitórias por comportamento dos jogadores')
    impulsive_count = len([x for x in results if x[0] == IMPULSIVE])
    picky_count = len([x for x in results if x[0] == PICKY])
    wary_count = len([x for x in results if x[0] == WARY])
    random_count = len([x for x in results if x[0] == RANDOM])
    inners_sort = sorted({
        IMPULSIVE: impulsive_count,
        PICKY: picky_count,
        WARY: wary_count,
        RANDOM: random_count
    }.items(), key=operator.itemgetter(1), reverse=True)
    for inner in inners_sort:
        behavior = BEHAVIOR_NAMES[inner[0]]
        percent = inner[1] / len(results) * 100
        print_line(behavior, f'{percent:.2f}%')

    # Qual o comportamento que mais vence
    print_header('🏆 Qual o comportamento que mais vence')
    inner_behavior = BEHAVIOR_NAMES.get(inners_sort[0][0])
    print_line('Comportamento', inner_behavior)
    print('\n 🤘 👽 🚀 \n')
