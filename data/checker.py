from pool import Var


## check_basic_init(name, pos)


def check_basic_init(name, pos):
    if type(name) != str:
        raise TypeError("Characters erstes Arg. muss str sein (=name)")
    if type(pos) != list:
        raise TypeError("Characters zweites Arg. muss Liste sein (=pos)")
    if not (len(pos) == 2):
        raise IndexError("Characters zweites Arg. (='pos'): Liste muss genau 2 Elemente haben")
    for i in pos:
        if type(i) != int:
            raise TypeError("Characters zweites Arg. (='pos'): Liste muss Integer als Elemente haben")
