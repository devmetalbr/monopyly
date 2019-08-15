from dataclasses import dataclass
from models.player import Player
import random


@dataclass
class Propertie:
    player: Player = None
    sale_price: float = 0.0
    rent_value: float = 0.0

    @classmethod
    def create(cls, min_value: float = 300, max_value: float = 30000.0):
        """Create new `Propertie` random values.

        Args:
            :param min_value: Minimum amount for `sale_price`
            :param max_value: Maximun amount for `sale_price`
            :param rent_value: Percentage of `rent_value` based on `sale_price`

        Examples:
            >>> propertie = Propertie.create()
            >>> print(propertie)
            Propertie(owner=None, sale_price=60.01903019134575, rent_value=6.001903019134574)
        """
        assert min_value < max_value  # TODO: handle exception
        sale_price = random.uniform(min_value, max_value)
        rent_value = random.uniform(1, 100)
        return cls(sale_price=sale_price, rent_value=rent_value)


if __name__ == '__main__':
    propertie = Propertie.create()
    print(propertie)
