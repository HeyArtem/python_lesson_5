from module import CAT, DOG as _DOG, _FISH  #!!! _DOG здесь дог с подчеркиванием? мы сделали ее системной

APPLE = 'apple'
MEAT = 'meat'
_CARROT = 'carrot'

__all__ = ('APPLE', '__CARROT')
print(_DOG)