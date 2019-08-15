from dataclasses import dataclass, field

IMPULSIVE, PICKY, WARY, RANDOM = range(4)
BEHAVIOR_NAMES = {
    IMPULSIVE: 'Impulsivo',
    PICKY: 'Exigente',
    WARY: 'Cauteloso',
    RANDOM: 'Aleatório'
}


@dataclass
class Player:
    behavior: int

    @property
    def title(self):
        return BEHAVIOR_NAMES.get(self.behavior)


if __name__ == '__main__':
    player = Player(0)
    print(player)
    print(player.title)
