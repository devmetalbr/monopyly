from random import (
    randint,
    shuffle)
from dataclasses import dataclass
from typing import List, Tuple

from models.player import (
    Player,
    IMPULSIVE,
    PICKY,
    WARY,
    RANDOM)
from models.propertie import Propertie


def roll_dice():
    return randint(1, 6)


@dataclass
class Gamer:
    player: int
    current_position: int = 0
    amount: float = 300.0
    shifts: int = 0


class Board(object):
    default_gamers = [
        Gamer(Player(behavior=IMPULSIVE)),
        Gamer(Player(behavior=PICKY)),
        Gamer(Player(behavior=WARY)),
        Gamer(Player(behavior=RANDOM)),
    ]
    qty_properties: int
    properties = List[Propertie]
    gamers = List[Gamer]
    excludes = []
    players = List[Tuple]
    result = List[tuple]
    timeout = 0
    inner = None

    def __init__(self, qty_properties):
        self.qty_properties = qty_properties
        self.__create_board()
        self.__shuffle_players()

    def __create_board(self):
        self.properties = [Propertie()]  # Propriedade de indice 0 (Marca o ponto de Partida)
        properties = map(lambda x: Propertie.create(), range(self.qty_properties))
        self.properties += list(properties)

    def __shuffle_players(self):
        gamers = self.default_gamers
        shuffle(gamers)
        self.gamers = gamers

    def play(self, number=1000):
        count = 1
        is_continue = True

        while (count <= number) and is_continue:
            for x in range(0, len(self.gamers)):
                gamer = self.gamers[x]
                # POSITIONS
                if gamer in self.excludes:
                    continue
                current_position = gamer.current_position
                next_position, is_complete = self._update_position(current_position)
                gamer.current_position = next_position  # Posição no tabuleiro
                gamer.shifts += 1

                propertie = self.properties[next_position]
                if next_position:  # Se posiçao diferente de 0 (zero)
                    player_behavior = gamer.player.behavior
                    propertie_owner = propertie.player
                    if not propertie_owner and gamer.amount >= propertie.sale_price:
                        if player_behavior == IMPULSIVE:
                            # compra qualquer propriedade sobre a qual ele parar.
                            propertie.player = gamer.player
                            gamer.amount -= propertie.sale_price
                        elif player_behavior == PICKY:
                            # e compra qualquer propriedade, desde que o valor do aluguel
                            # dela seja maior do que 50.
                            if 50.0 < propertie.rent_value <= gamer.amount:
                                propertie.player = gamer.player
                                gamer.amount -= propertie.sale_price
                        elif player_behavior == WARY:
                            # compra qualquer propriedade desde que ele tenha uma reserva de 80
                            # saldo sobrando depois de realizada a compra.
                            if gamer.amount - propertie.sale_price >= 80.0:
                                propertie.player = gamer.player
                                gamer.amount -= propertie.sale_price
                        elif player_behavior == RANDOM:
                            # compra a propriedade que ele parar em cima com probabilidade de 50%.
                            if randint(0, 1):
                                propertie.player = gamer.player
                                gamer.amount -= propertie.sale_price
                    elif propertie_owner and propertie_owner != gamer:
                        #  pagar aluguel
                        gamer.amount -= propertie.rent_value
                self.properties[next_position] = propertie  # Atualizar

                if is_complete:  # Completou uma rodada e acumulou +100 de saldo
                    gamer.amount += 100.00
                if gamer.amount <= 0.0:
                    self._clear_owner_propertie(gamer)
                self.gamers[x] = gamer

            if len(self.excludes) == 3:
                self.inner = gamer
                break
            elif count == number:
                matches = [x for x in self.gamers if x not in self.excludes]
                self.inner = max(matches, key=lambda k: k.shifts)
                self.timeout = 1
            count += 1
        return [self.inner.player.behavior, self.timeout, self.inner.shifts]

    def _clear_owner_propertie(self, gamer):
        self.excludes.append(gamer)
        for x in range(0, len(self.properties)):
            if self.properties[x].player == gamer.player:
                self.properties[x].player = None

    def _update_position(self, current):
        is_complete = False
        end_position = len(self.properties)
        rolldice = roll_dice()
        new_position = current + rolldice
        if new_position == end_position:
            new_position = 0
            is_complete = True
        if new_position > end_position:
            new_position = new_position - end_position - 1
            is_complete = True
        return new_position, is_complete
