import random
from inspect import signature as _mutmut_signature
from typing import Annotated
from typing import Callable
from typing import ClassVar


MutantDict = Annotated[dict[str, Callable], "Mutant"]


def _mutmut_trampoline(orig, mutants, call_args, call_kwargs, self_arg = None):
    """Forward call to original or mutated function, depending on the environment"""
    import os
    mutant_under_test = os.environ['MUTANT_UNDER_TEST']
    if mutant_under_test == 'fail':
        from mutmut.__main__ import MutmutProgrammaticFailException
        raise MutmutProgrammaticFailException('Failed programmatically')      
    elif mutant_under_test == 'stats':
        from mutmut.__main__ import record_trampoline_hit
        record_trampoline_hit(orig.__module__ + '.' + orig.__name__)
        result = orig(*call_args, **call_kwargs)
        return result
    prefix = orig.__module__ + '.' + orig.__name__ + '__mutmut_'
    if not mutant_under_test.startswith(prefix):
        result = orig(*call_args, **call_kwargs)
        return result
    mutant_name = mutant_under_test.rpartition('.')[-1]
    if self_arg is not None:
        # call to a class method where self is not bound
        result = mutants[mutant_name](self_arg, *call_args, **call_kwargs)
    else:
        result = mutants[mutant_name](*call_args, **call_kwargs)
    return result


class ShufflePuzzleLevelCustomized:

    def xǁShufflePuzzleLevelCustomizedǁ__init____mutmut_orig(self, number_of_shuffles):
        self.number_of_shuffles = number_of_shuffles;

    def xǁShufflePuzzleLevelCustomizedǁ__init____mutmut_1(self, number_of_shuffles):
        self.number_of_shuffles = None;
    
    xǁShufflePuzzleLevelCustomizedǁ__init____mutmut_mutants : ClassVar[MutantDict] = {
    'xǁShufflePuzzleLevelCustomizedǁ__init____mutmut_1': xǁShufflePuzzleLevelCustomizedǁ__init____mutmut_1
    }
    
    def __init__(self, *args, **kwargs):
        result = _mutmut_trampoline(object.__getattribute__(self, "xǁShufflePuzzleLevelCustomizedǁ__init____mutmut_orig"), object.__getattribute__(self, "xǁShufflePuzzleLevelCustomizedǁ__init____mutmut_mutants"), args, kwargs, self)
        return result 
    
    __init__.__signature__ = _mutmut_signature(xǁShufflePuzzleLevelCustomizedǁ__init____mutmut_orig)
    xǁShufflePuzzleLevelCustomizedǁ__init____mutmut_orig.__name__ = 'xǁShufflePuzzleLevelCustomizedǁ__init__'

    def xǁShufflePuzzleLevelCustomizedǁshuffle__mutmut_orig (self, puzzle_game):
        list_directions = [1, 2, 3, 4]
        for number in range(0, self.number_of_shuffles):
            changed = False
            while not changed:
                direction = random.choice(list_directions)
                if direction == 1:
                    changed = puzzle_game.move_empty_tile("UP")
                elif direction == 2:
                    changed = puzzle_game.move_empty_tile("DOWN")
                elif direction == 3:
                    changed = puzzle_game.move_empty_tile("LEFT")
                elif direction == 4:
                    changed = puzzle_game.move_empty_tile("RIGHT")

    def xǁShufflePuzzleLevelCustomizedǁshuffle__mutmut_1 (self, puzzle_game):
        list_directions = None
        for number in range(0, self.number_of_shuffles):
            changed = False
            while not changed:
                direction = random.choice(list_directions)
                if direction == 1:
                    changed = puzzle_game.move_empty_tile("UP")
                elif direction == 2:
                    changed = puzzle_game.move_empty_tile("DOWN")
                elif direction == 3:
                    changed = puzzle_game.move_empty_tile("LEFT")
                elif direction == 4:
                    changed = puzzle_game.move_empty_tile("RIGHT")

    def xǁShufflePuzzleLevelCustomizedǁshuffle__mutmut_2 (self, puzzle_game):
        list_directions = [2, 2, 3, 4]
        for number in range(0, self.number_of_shuffles):
            changed = False
            while not changed:
                direction = random.choice(list_directions)
                if direction == 1:
                    changed = puzzle_game.move_empty_tile("UP")
                elif direction == 2:
                    changed = puzzle_game.move_empty_tile("DOWN")
                elif direction == 3:
                    changed = puzzle_game.move_empty_tile("LEFT")
                elif direction == 4:
                    changed = puzzle_game.move_empty_tile("RIGHT")

    def xǁShufflePuzzleLevelCustomizedǁshuffle__mutmut_3 (self, puzzle_game):
        list_directions = [1, 3, 3, 4]
        for number in range(0, self.number_of_shuffles):
            changed = False
            while not changed:
                direction = random.choice(list_directions)
                if direction == 1:
                    changed = puzzle_game.move_empty_tile("UP")
                elif direction == 2:
                    changed = puzzle_game.move_empty_tile("DOWN")
                elif direction == 3:
                    changed = puzzle_game.move_empty_tile("LEFT")
                elif direction == 4:
                    changed = puzzle_game.move_empty_tile("RIGHT")

    def xǁShufflePuzzleLevelCustomizedǁshuffle__mutmut_4 (self, puzzle_game):
        list_directions = [1, 2, 4, 4]
        for number in range(0, self.number_of_shuffles):
            changed = False
            while not changed:
                direction = random.choice(list_directions)
                if direction == 1:
                    changed = puzzle_game.move_empty_tile("UP")
                elif direction == 2:
                    changed = puzzle_game.move_empty_tile("DOWN")
                elif direction == 3:
                    changed = puzzle_game.move_empty_tile("LEFT")
                elif direction == 4:
                    changed = puzzle_game.move_empty_tile("RIGHT")

    def xǁShufflePuzzleLevelCustomizedǁshuffle__mutmut_5 (self, puzzle_game):
        list_directions = [1, 2, 3, 5]
        for number in range(0, self.number_of_shuffles):
            changed = False
            while not changed:
                direction = random.choice(list_directions)
                if direction == 1:
                    changed = puzzle_game.move_empty_tile("UP")
                elif direction == 2:
                    changed = puzzle_game.move_empty_tile("DOWN")
                elif direction == 3:
                    changed = puzzle_game.move_empty_tile("LEFT")
                elif direction == 4:
                    changed = puzzle_game.move_empty_tile("RIGHT")

    def xǁShufflePuzzleLevelCustomizedǁshuffle__mutmut_6 (self, puzzle_game):
        list_directions = [1, 2, 3, 4]
        for number in range(None, self.number_of_shuffles):
            changed = False
            while not changed:
                direction = random.choice(list_directions)
                if direction == 1:
                    changed = puzzle_game.move_empty_tile("UP")
                elif direction == 2:
                    changed = puzzle_game.move_empty_tile("DOWN")
                elif direction == 3:
                    changed = puzzle_game.move_empty_tile("LEFT")
                elif direction == 4:
                    changed = puzzle_game.move_empty_tile("RIGHT")

    def xǁShufflePuzzleLevelCustomizedǁshuffle__mutmut_7 (self, puzzle_game):
        list_directions = [1, 2, 3, 4]
        for number in range(0, None):
            changed = False
            while not changed:
                direction = random.choice(list_directions)
                if direction == 1:
                    changed = puzzle_game.move_empty_tile("UP")
                elif direction == 2:
                    changed = puzzle_game.move_empty_tile("DOWN")
                elif direction == 3:
                    changed = puzzle_game.move_empty_tile("LEFT")
                elif direction == 4:
                    changed = puzzle_game.move_empty_tile("RIGHT")

    def xǁShufflePuzzleLevelCustomizedǁshuffle__mutmut_8 (self, puzzle_game):
        list_directions = [1, 2, 3, 4]
        for number in range(self.number_of_shuffles):
            changed = False
            while not changed:
                direction = random.choice(list_directions)
                if direction == 1:
                    changed = puzzle_game.move_empty_tile("UP")
                elif direction == 2:
                    changed = puzzle_game.move_empty_tile("DOWN")
                elif direction == 3:
                    changed = puzzle_game.move_empty_tile("LEFT")
                elif direction == 4:
                    changed = puzzle_game.move_empty_tile("RIGHT")

    def xǁShufflePuzzleLevelCustomizedǁshuffle__mutmut_9 (self, puzzle_game):
        list_directions = [1, 2, 3, 4]
        for number in range(0, ):
            changed = False
            while not changed:
                direction = random.choice(list_directions)
                if direction == 1:
                    changed = puzzle_game.move_empty_tile("UP")
                elif direction == 2:
                    changed = puzzle_game.move_empty_tile("DOWN")
                elif direction == 3:
                    changed = puzzle_game.move_empty_tile("LEFT")
                elif direction == 4:
                    changed = puzzle_game.move_empty_tile("RIGHT")

    def xǁShufflePuzzleLevelCustomizedǁshuffle__mutmut_10 (self, puzzle_game):
        list_directions = [1, 2, 3, 4]
        for number in range(1, self.number_of_shuffles):
            changed = False
            while not changed:
                direction = random.choice(list_directions)
                if direction == 1:
                    changed = puzzle_game.move_empty_tile("UP")
                elif direction == 2:
                    changed = puzzle_game.move_empty_tile("DOWN")
                elif direction == 3:
                    changed = puzzle_game.move_empty_tile("LEFT")
                elif direction == 4:
                    changed = puzzle_game.move_empty_tile("RIGHT")

    def xǁShufflePuzzleLevelCustomizedǁshuffle__mutmut_11 (self, puzzle_game):
        list_directions = [1, 2, 3, 4]
        for number in range(0, self.number_of_shuffles):
            changed = None
            while not changed:
                direction = random.choice(list_directions)
                if direction == 1:
                    changed = puzzle_game.move_empty_tile("UP")
                elif direction == 2:
                    changed = puzzle_game.move_empty_tile("DOWN")
                elif direction == 3:
                    changed = puzzle_game.move_empty_tile("LEFT")
                elif direction == 4:
                    changed = puzzle_game.move_empty_tile("RIGHT")

    def xǁShufflePuzzleLevelCustomizedǁshuffle__mutmut_12 (self, puzzle_game):
        list_directions = [1, 2, 3, 4]
        for number in range(0, self.number_of_shuffles):
            changed = True
            while not changed:
                direction = random.choice(list_directions)
                if direction == 1:
                    changed = puzzle_game.move_empty_tile("UP")
                elif direction == 2:
                    changed = puzzle_game.move_empty_tile("DOWN")
                elif direction == 3:
                    changed = puzzle_game.move_empty_tile("LEFT")
                elif direction == 4:
                    changed = puzzle_game.move_empty_tile("RIGHT")

    def xǁShufflePuzzleLevelCustomizedǁshuffle__mutmut_13 (self, puzzle_game):
        list_directions = [1, 2, 3, 4]
        for number in range(0, self.number_of_shuffles):
            changed = False
            while changed:
                direction = random.choice(list_directions)
                if direction == 1:
                    changed = puzzle_game.move_empty_tile("UP")
                elif direction == 2:
                    changed = puzzle_game.move_empty_tile("DOWN")
                elif direction == 3:
                    changed = puzzle_game.move_empty_tile("LEFT")
                elif direction == 4:
                    changed = puzzle_game.move_empty_tile("RIGHT")

    def xǁShufflePuzzleLevelCustomizedǁshuffle__mutmut_14 (self, puzzle_game):
        list_directions = [1, 2, 3, 4]
        for number in range(0, self.number_of_shuffles):
            changed = False
            while not changed:
                direction = None
                if direction == 1:
                    changed = puzzle_game.move_empty_tile("UP")
                elif direction == 2:
                    changed = puzzle_game.move_empty_tile("DOWN")
                elif direction == 3:
                    changed = puzzle_game.move_empty_tile("LEFT")
                elif direction == 4:
                    changed = puzzle_game.move_empty_tile("RIGHT")

    def xǁShufflePuzzleLevelCustomizedǁshuffle__mutmut_15 (self, puzzle_game):
        list_directions = [1, 2, 3, 4]
        for number in range(0, self.number_of_shuffles):
            changed = False
            while not changed:
                direction = random.choice(None)
                if direction == 1:
                    changed = puzzle_game.move_empty_tile("UP")
                elif direction == 2:
                    changed = puzzle_game.move_empty_tile("DOWN")
                elif direction == 3:
                    changed = puzzle_game.move_empty_tile("LEFT")
                elif direction == 4:
                    changed = puzzle_game.move_empty_tile("RIGHT")

    def xǁShufflePuzzleLevelCustomizedǁshuffle__mutmut_16 (self, puzzle_game):
        list_directions = [1, 2, 3, 4]
        for number in range(0, self.number_of_shuffles):
            changed = False
            while not changed:
                direction = random.choice(list_directions)
                if direction != 1:
                    changed = puzzle_game.move_empty_tile("UP")
                elif direction == 2:
                    changed = puzzle_game.move_empty_tile("DOWN")
                elif direction == 3:
                    changed = puzzle_game.move_empty_tile("LEFT")
                elif direction == 4:
                    changed = puzzle_game.move_empty_tile("RIGHT")

    def xǁShufflePuzzleLevelCustomizedǁshuffle__mutmut_17 (self, puzzle_game):
        list_directions = [1, 2, 3, 4]
        for number in range(0, self.number_of_shuffles):
            changed = False
            while not changed:
                direction = random.choice(list_directions)
                if direction == 2:
                    changed = puzzle_game.move_empty_tile("UP")
                elif direction == 2:
                    changed = puzzle_game.move_empty_tile("DOWN")
                elif direction == 3:
                    changed = puzzle_game.move_empty_tile("LEFT")
                elif direction == 4:
                    changed = puzzle_game.move_empty_tile("RIGHT")

    def xǁShufflePuzzleLevelCustomizedǁshuffle__mutmut_18 (self, puzzle_game):
        list_directions = [1, 2, 3, 4]
        for number in range(0, self.number_of_shuffles):
            changed = False
            while not changed:
                direction = random.choice(list_directions)
                if direction == 1:
                    changed = None
                elif direction == 2:
                    changed = puzzle_game.move_empty_tile("DOWN")
                elif direction == 3:
                    changed = puzzle_game.move_empty_tile("LEFT")
                elif direction == 4:
                    changed = puzzle_game.move_empty_tile("RIGHT")

    def xǁShufflePuzzleLevelCustomizedǁshuffle__mutmut_19 (self, puzzle_game):
        list_directions = [1, 2, 3, 4]
        for number in range(0, self.number_of_shuffles):
            changed = False
            while not changed:
                direction = random.choice(list_directions)
                if direction == 1:
                    changed = puzzle_game.move_empty_tile(None)
                elif direction == 2:
                    changed = puzzle_game.move_empty_tile("DOWN")
                elif direction == 3:
                    changed = puzzle_game.move_empty_tile("LEFT")
                elif direction == 4:
                    changed = puzzle_game.move_empty_tile("RIGHT")

    def xǁShufflePuzzleLevelCustomizedǁshuffle__mutmut_20 (self, puzzle_game):
        list_directions = [1, 2, 3, 4]
        for number in range(0, self.number_of_shuffles):
            changed = False
            while not changed:
                direction = random.choice(list_directions)
                if direction == 1:
                    changed = puzzle_game.move_empty_tile("XXUPXX")
                elif direction == 2:
                    changed = puzzle_game.move_empty_tile("DOWN")
                elif direction == 3:
                    changed = puzzle_game.move_empty_tile("LEFT")
                elif direction == 4:
                    changed = puzzle_game.move_empty_tile("RIGHT")

    def xǁShufflePuzzleLevelCustomizedǁshuffle__mutmut_21 (self, puzzle_game):
        list_directions = [1, 2, 3, 4]
        for number in range(0, self.number_of_shuffles):
            changed = False
            while not changed:
                direction = random.choice(list_directions)
                if direction == 1:
                    changed = puzzle_game.move_empty_tile("up")
                elif direction == 2:
                    changed = puzzle_game.move_empty_tile("DOWN")
                elif direction == 3:
                    changed = puzzle_game.move_empty_tile("LEFT")
                elif direction == 4:
                    changed = puzzle_game.move_empty_tile("RIGHT")

    def xǁShufflePuzzleLevelCustomizedǁshuffle__mutmut_22 (self, puzzle_game):
        list_directions = [1, 2, 3, 4]
        for number in range(0, self.number_of_shuffles):
            changed = False
            while not changed:
                direction = random.choice(list_directions)
                if direction == 1:
                    changed = puzzle_game.move_empty_tile("UP")
                elif direction != 2:
                    changed = puzzle_game.move_empty_tile("DOWN")
                elif direction == 3:
                    changed = puzzle_game.move_empty_tile("LEFT")
                elif direction == 4:
                    changed = puzzle_game.move_empty_tile("RIGHT")

    def xǁShufflePuzzleLevelCustomizedǁshuffle__mutmut_23 (self, puzzle_game):
        list_directions = [1, 2, 3, 4]
        for number in range(0, self.number_of_shuffles):
            changed = False
            while not changed:
                direction = random.choice(list_directions)
                if direction == 1:
                    changed = puzzle_game.move_empty_tile("UP")
                elif direction == 3:
                    changed = puzzle_game.move_empty_tile("DOWN")
                elif direction == 3:
                    changed = puzzle_game.move_empty_tile("LEFT")
                elif direction == 4:
                    changed = puzzle_game.move_empty_tile("RIGHT")

    def xǁShufflePuzzleLevelCustomizedǁshuffle__mutmut_24 (self, puzzle_game):
        list_directions = [1, 2, 3, 4]
        for number in range(0, self.number_of_shuffles):
            changed = False
            while not changed:
                direction = random.choice(list_directions)
                if direction == 1:
                    changed = puzzle_game.move_empty_tile("UP")
                elif direction == 2:
                    changed = None
                elif direction == 3:
                    changed = puzzle_game.move_empty_tile("LEFT")
                elif direction == 4:
                    changed = puzzle_game.move_empty_tile("RIGHT")

    def xǁShufflePuzzleLevelCustomizedǁshuffle__mutmut_25 (self, puzzle_game):
        list_directions = [1, 2, 3, 4]
        for number in range(0, self.number_of_shuffles):
            changed = False
            while not changed:
                direction = random.choice(list_directions)
                if direction == 1:
                    changed = puzzle_game.move_empty_tile("UP")
                elif direction == 2:
                    changed = puzzle_game.move_empty_tile(None)
                elif direction == 3:
                    changed = puzzle_game.move_empty_tile("LEFT")
                elif direction == 4:
                    changed = puzzle_game.move_empty_tile("RIGHT")

    def xǁShufflePuzzleLevelCustomizedǁshuffle__mutmut_26 (self, puzzle_game):
        list_directions = [1, 2, 3, 4]
        for number in range(0, self.number_of_shuffles):
            changed = False
            while not changed:
                direction = random.choice(list_directions)
                if direction == 1:
                    changed = puzzle_game.move_empty_tile("UP")
                elif direction == 2:
                    changed = puzzle_game.move_empty_tile("XXDOWNXX")
                elif direction == 3:
                    changed = puzzle_game.move_empty_tile("LEFT")
                elif direction == 4:
                    changed = puzzle_game.move_empty_tile("RIGHT")

    def xǁShufflePuzzleLevelCustomizedǁshuffle__mutmut_27 (self, puzzle_game):
        list_directions = [1, 2, 3, 4]
        for number in range(0, self.number_of_shuffles):
            changed = False
            while not changed:
                direction = random.choice(list_directions)
                if direction == 1:
                    changed = puzzle_game.move_empty_tile("UP")
                elif direction == 2:
                    changed = puzzle_game.move_empty_tile("down")
                elif direction == 3:
                    changed = puzzle_game.move_empty_tile("LEFT")
                elif direction == 4:
                    changed = puzzle_game.move_empty_tile("RIGHT")

    def xǁShufflePuzzleLevelCustomizedǁshuffle__mutmut_28 (self, puzzle_game):
        list_directions = [1, 2, 3, 4]
        for number in range(0, self.number_of_shuffles):
            changed = False
            while not changed:
                direction = random.choice(list_directions)
                if direction == 1:
                    changed = puzzle_game.move_empty_tile("UP")
                elif direction == 2:
                    changed = puzzle_game.move_empty_tile("DOWN")
                elif direction != 3:
                    changed = puzzle_game.move_empty_tile("LEFT")
                elif direction == 4:
                    changed = puzzle_game.move_empty_tile("RIGHT")

    def xǁShufflePuzzleLevelCustomizedǁshuffle__mutmut_29 (self, puzzle_game):
        list_directions = [1, 2, 3, 4]
        for number in range(0, self.number_of_shuffles):
            changed = False
            while not changed:
                direction = random.choice(list_directions)
                if direction == 1:
                    changed = puzzle_game.move_empty_tile("UP")
                elif direction == 2:
                    changed = puzzle_game.move_empty_tile("DOWN")
                elif direction == 4:
                    changed = puzzle_game.move_empty_tile("LEFT")
                elif direction == 4:
                    changed = puzzle_game.move_empty_tile("RIGHT")

    def xǁShufflePuzzleLevelCustomizedǁshuffle__mutmut_30 (self, puzzle_game):
        list_directions = [1, 2, 3, 4]
        for number in range(0, self.number_of_shuffles):
            changed = False
            while not changed:
                direction = random.choice(list_directions)
                if direction == 1:
                    changed = puzzle_game.move_empty_tile("UP")
                elif direction == 2:
                    changed = puzzle_game.move_empty_tile("DOWN")
                elif direction == 3:
                    changed = None
                elif direction == 4:
                    changed = puzzle_game.move_empty_tile("RIGHT")

    def xǁShufflePuzzleLevelCustomizedǁshuffle__mutmut_31 (self, puzzle_game):
        list_directions = [1, 2, 3, 4]
        for number in range(0, self.number_of_shuffles):
            changed = False
            while not changed:
                direction = random.choice(list_directions)
                if direction == 1:
                    changed = puzzle_game.move_empty_tile("UP")
                elif direction == 2:
                    changed = puzzle_game.move_empty_tile("DOWN")
                elif direction == 3:
                    changed = puzzle_game.move_empty_tile(None)
                elif direction == 4:
                    changed = puzzle_game.move_empty_tile("RIGHT")

    def xǁShufflePuzzleLevelCustomizedǁshuffle__mutmut_32 (self, puzzle_game):
        list_directions = [1, 2, 3, 4]
        for number in range(0, self.number_of_shuffles):
            changed = False
            while not changed:
                direction = random.choice(list_directions)
                if direction == 1:
                    changed = puzzle_game.move_empty_tile("UP")
                elif direction == 2:
                    changed = puzzle_game.move_empty_tile("DOWN")
                elif direction == 3:
                    changed = puzzle_game.move_empty_tile("XXLEFTXX")
                elif direction == 4:
                    changed = puzzle_game.move_empty_tile("RIGHT")

    def xǁShufflePuzzleLevelCustomizedǁshuffle__mutmut_33 (self, puzzle_game):
        list_directions = [1, 2, 3, 4]
        for number in range(0, self.number_of_shuffles):
            changed = False
            while not changed:
                direction = random.choice(list_directions)
                if direction == 1:
                    changed = puzzle_game.move_empty_tile("UP")
                elif direction == 2:
                    changed = puzzle_game.move_empty_tile("DOWN")
                elif direction == 3:
                    changed = puzzle_game.move_empty_tile("left")
                elif direction == 4:
                    changed = puzzle_game.move_empty_tile("RIGHT")

    def xǁShufflePuzzleLevelCustomizedǁshuffle__mutmut_34 (self, puzzle_game):
        list_directions = [1, 2, 3, 4]
        for number in range(0, self.number_of_shuffles):
            changed = False
            while not changed:
                direction = random.choice(list_directions)
                if direction == 1:
                    changed = puzzle_game.move_empty_tile("UP")
                elif direction == 2:
                    changed = puzzle_game.move_empty_tile("DOWN")
                elif direction == 3:
                    changed = puzzle_game.move_empty_tile("LEFT")
                elif direction != 4:
                    changed = puzzle_game.move_empty_tile("RIGHT")

    def xǁShufflePuzzleLevelCustomizedǁshuffle__mutmut_35 (self, puzzle_game):
        list_directions = [1, 2, 3, 4]
        for number in range(0, self.number_of_shuffles):
            changed = False
            while not changed:
                direction = random.choice(list_directions)
                if direction == 1:
                    changed = puzzle_game.move_empty_tile("UP")
                elif direction == 2:
                    changed = puzzle_game.move_empty_tile("DOWN")
                elif direction == 3:
                    changed = puzzle_game.move_empty_tile("LEFT")
                elif direction == 5:
                    changed = puzzle_game.move_empty_tile("RIGHT")

    def xǁShufflePuzzleLevelCustomizedǁshuffle__mutmut_36 (self, puzzle_game):
        list_directions = [1, 2, 3, 4]
        for number in range(0, self.number_of_shuffles):
            changed = False
            while not changed:
                direction = random.choice(list_directions)
                if direction == 1:
                    changed = puzzle_game.move_empty_tile("UP")
                elif direction == 2:
                    changed = puzzle_game.move_empty_tile("DOWN")
                elif direction == 3:
                    changed = puzzle_game.move_empty_tile("LEFT")
                elif direction == 4:
                    changed = None

    def xǁShufflePuzzleLevelCustomizedǁshuffle__mutmut_37 (self, puzzle_game):
        list_directions = [1, 2, 3, 4]
        for number in range(0, self.number_of_shuffles):
            changed = False
            while not changed:
                direction = random.choice(list_directions)
                if direction == 1:
                    changed = puzzle_game.move_empty_tile("UP")
                elif direction == 2:
                    changed = puzzle_game.move_empty_tile("DOWN")
                elif direction == 3:
                    changed = puzzle_game.move_empty_tile("LEFT")
                elif direction == 4:
                    changed = puzzle_game.move_empty_tile(None)

    def xǁShufflePuzzleLevelCustomizedǁshuffle__mutmut_38 (self, puzzle_game):
        list_directions = [1, 2, 3, 4]
        for number in range(0, self.number_of_shuffles):
            changed = False
            while not changed:
                direction = random.choice(list_directions)
                if direction == 1:
                    changed = puzzle_game.move_empty_tile("UP")
                elif direction == 2:
                    changed = puzzle_game.move_empty_tile("DOWN")
                elif direction == 3:
                    changed = puzzle_game.move_empty_tile("LEFT")
                elif direction == 4:
                    changed = puzzle_game.move_empty_tile("XXRIGHTXX")

    def xǁShufflePuzzleLevelCustomizedǁshuffle__mutmut_39 (self, puzzle_game):
        list_directions = [1, 2, 3, 4]
        for number in range(0, self.number_of_shuffles):
            changed = False
            while not changed:
                direction = random.choice(list_directions)
                if direction == 1:
                    changed = puzzle_game.move_empty_tile("UP")
                elif direction == 2:
                    changed = puzzle_game.move_empty_tile("DOWN")
                elif direction == 3:
                    changed = puzzle_game.move_empty_tile("LEFT")
                elif direction == 4:
                    changed = puzzle_game.move_empty_tile("right")
    
    xǁShufflePuzzleLevelCustomizedǁshuffle__mutmut_mutants : ClassVar[MutantDict] = {
    'xǁShufflePuzzleLevelCustomizedǁshuffle__mutmut_1': xǁShufflePuzzleLevelCustomizedǁshuffle__mutmut_1, 
        'xǁShufflePuzzleLevelCustomizedǁshuffle__mutmut_2': xǁShufflePuzzleLevelCustomizedǁshuffle__mutmut_2, 
        'xǁShufflePuzzleLevelCustomizedǁshuffle__mutmut_3': xǁShufflePuzzleLevelCustomizedǁshuffle__mutmut_3, 
        'xǁShufflePuzzleLevelCustomizedǁshuffle__mutmut_4': xǁShufflePuzzleLevelCustomizedǁshuffle__mutmut_4, 
        'xǁShufflePuzzleLevelCustomizedǁshuffle__mutmut_5': xǁShufflePuzzleLevelCustomizedǁshuffle__mutmut_5, 
        'xǁShufflePuzzleLevelCustomizedǁshuffle__mutmut_6': xǁShufflePuzzleLevelCustomizedǁshuffle__mutmut_6, 
        'xǁShufflePuzzleLevelCustomizedǁshuffle__mutmut_7': xǁShufflePuzzleLevelCustomizedǁshuffle__mutmut_7, 
        'xǁShufflePuzzleLevelCustomizedǁshuffle__mutmut_8': xǁShufflePuzzleLevelCustomizedǁshuffle__mutmut_8, 
        'xǁShufflePuzzleLevelCustomizedǁshuffle__mutmut_9': xǁShufflePuzzleLevelCustomizedǁshuffle__mutmut_9, 
        'xǁShufflePuzzleLevelCustomizedǁshuffle__mutmut_10': xǁShufflePuzzleLevelCustomizedǁshuffle__mutmut_10, 
        'xǁShufflePuzzleLevelCustomizedǁshuffle__mutmut_11': xǁShufflePuzzleLevelCustomizedǁshuffle__mutmut_11, 
        'xǁShufflePuzzleLevelCustomizedǁshuffle__mutmut_12': xǁShufflePuzzleLevelCustomizedǁshuffle__mutmut_12, 
        'xǁShufflePuzzleLevelCustomizedǁshuffle__mutmut_13': xǁShufflePuzzleLevelCustomizedǁshuffle__mutmut_13, 
        'xǁShufflePuzzleLevelCustomizedǁshuffle__mutmut_14': xǁShufflePuzzleLevelCustomizedǁshuffle__mutmut_14, 
        'xǁShufflePuzzleLevelCustomizedǁshuffle__mutmut_15': xǁShufflePuzzleLevelCustomizedǁshuffle__mutmut_15, 
        'xǁShufflePuzzleLevelCustomizedǁshuffle__mutmut_16': xǁShufflePuzzleLevelCustomizedǁshuffle__mutmut_16, 
        'xǁShufflePuzzleLevelCustomizedǁshuffle__mutmut_17': xǁShufflePuzzleLevelCustomizedǁshuffle__mutmut_17, 
        'xǁShufflePuzzleLevelCustomizedǁshuffle__mutmut_18': xǁShufflePuzzleLevelCustomizedǁshuffle__mutmut_18, 
        'xǁShufflePuzzleLevelCustomizedǁshuffle__mutmut_19': xǁShufflePuzzleLevelCustomizedǁshuffle__mutmut_19, 
        'xǁShufflePuzzleLevelCustomizedǁshuffle__mutmut_20': xǁShufflePuzzleLevelCustomizedǁshuffle__mutmut_20, 
        'xǁShufflePuzzleLevelCustomizedǁshuffle__mutmut_21': xǁShufflePuzzleLevelCustomizedǁshuffle__mutmut_21, 
        'xǁShufflePuzzleLevelCustomizedǁshuffle__mutmut_22': xǁShufflePuzzleLevelCustomizedǁshuffle__mutmut_22, 
        'xǁShufflePuzzleLevelCustomizedǁshuffle__mutmut_23': xǁShufflePuzzleLevelCustomizedǁshuffle__mutmut_23, 
        'xǁShufflePuzzleLevelCustomizedǁshuffle__mutmut_24': xǁShufflePuzzleLevelCustomizedǁshuffle__mutmut_24, 
        'xǁShufflePuzzleLevelCustomizedǁshuffle__mutmut_25': xǁShufflePuzzleLevelCustomizedǁshuffle__mutmut_25, 
        'xǁShufflePuzzleLevelCustomizedǁshuffle__mutmut_26': xǁShufflePuzzleLevelCustomizedǁshuffle__mutmut_26, 
        'xǁShufflePuzzleLevelCustomizedǁshuffle__mutmut_27': xǁShufflePuzzleLevelCustomizedǁshuffle__mutmut_27, 
        'xǁShufflePuzzleLevelCustomizedǁshuffle__mutmut_28': xǁShufflePuzzleLevelCustomizedǁshuffle__mutmut_28, 
        'xǁShufflePuzzleLevelCustomizedǁshuffle__mutmut_29': xǁShufflePuzzleLevelCustomizedǁshuffle__mutmut_29, 
        'xǁShufflePuzzleLevelCustomizedǁshuffle__mutmut_30': xǁShufflePuzzleLevelCustomizedǁshuffle__mutmut_30, 
        'xǁShufflePuzzleLevelCustomizedǁshuffle__mutmut_31': xǁShufflePuzzleLevelCustomizedǁshuffle__mutmut_31, 
        'xǁShufflePuzzleLevelCustomizedǁshuffle__mutmut_32': xǁShufflePuzzleLevelCustomizedǁshuffle__mutmut_32, 
        'xǁShufflePuzzleLevelCustomizedǁshuffle__mutmut_33': xǁShufflePuzzleLevelCustomizedǁshuffle__mutmut_33, 
        'xǁShufflePuzzleLevelCustomizedǁshuffle__mutmut_34': xǁShufflePuzzleLevelCustomizedǁshuffle__mutmut_34, 
        'xǁShufflePuzzleLevelCustomizedǁshuffle__mutmut_35': xǁShufflePuzzleLevelCustomizedǁshuffle__mutmut_35, 
        'xǁShufflePuzzleLevelCustomizedǁshuffle__mutmut_36': xǁShufflePuzzleLevelCustomizedǁshuffle__mutmut_36, 
        'xǁShufflePuzzleLevelCustomizedǁshuffle__mutmut_37': xǁShufflePuzzleLevelCustomizedǁshuffle__mutmut_37, 
        'xǁShufflePuzzleLevelCustomizedǁshuffle__mutmut_38': xǁShufflePuzzleLevelCustomizedǁshuffle__mutmut_38, 
        'xǁShufflePuzzleLevelCustomizedǁshuffle__mutmut_39': xǁShufflePuzzleLevelCustomizedǁshuffle__mutmut_39
    }
    
    def shuffle(self, *args, **kwargs):
        result = _mutmut_trampoline(object.__getattribute__(self, "xǁShufflePuzzleLevelCustomizedǁshuffle__mutmut_orig"), object.__getattribute__(self, "xǁShufflePuzzleLevelCustomizedǁshuffle__mutmut_mutants"), args, kwargs, self)
        return result 
    
    shuffle.__signature__ = _mutmut_signature(xǁShufflePuzzleLevelCustomizedǁshuffle__mutmut_orig)
    xǁShufflePuzzleLevelCustomizedǁshuffle__mutmut_orig.__name__ = 'xǁShufflePuzzleLevelCustomizedǁshuffle'


class ShufflePuzzleLevelEasy:

    def xǁShufflePuzzleLevelEasyǁ__init____mutmut_orig(self):
        self.number_of_shuffles = 4;

    def xǁShufflePuzzleLevelEasyǁ__init____mutmut_1(self):
        self.number_of_shuffles = None;

    def xǁShufflePuzzleLevelEasyǁ__init____mutmut_2(self):
        self.number_of_shuffles = 5;
    
    xǁShufflePuzzleLevelEasyǁ__init____mutmut_mutants : ClassVar[MutantDict] = {
    'xǁShufflePuzzleLevelEasyǁ__init____mutmut_1': xǁShufflePuzzleLevelEasyǁ__init____mutmut_1, 
        'xǁShufflePuzzleLevelEasyǁ__init____mutmut_2': xǁShufflePuzzleLevelEasyǁ__init____mutmut_2
    }
    
    def __init__(self, *args, **kwargs):
        result = _mutmut_trampoline(object.__getattribute__(self, "xǁShufflePuzzleLevelEasyǁ__init____mutmut_orig"), object.__getattribute__(self, "xǁShufflePuzzleLevelEasyǁ__init____mutmut_mutants"), args, kwargs, self)
        return result 
    
    __init__.__signature__ = _mutmut_signature(xǁShufflePuzzleLevelEasyǁ__init____mutmut_orig)
    xǁShufflePuzzleLevelEasyǁ__init____mutmut_orig.__name__ = 'xǁShufflePuzzleLevelEasyǁ__init__'

    def xǁShufflePuzzleLevelEasyǁshuffle__mutmut_orig (self, puzzle_game):
        list_directions = [1, 2, 3, 4]
        for number in range(0, self.number_of_shuffles):
            changed = False
            while not changed:
                direction = random.choice(list_directions)
                if direction == 1:
                    changed = puzzle_game.move_empty_tile("UP")
                elif direction == 2:
                    changed = puzzle_game.move_empty_tile("DOWN")
                elif direction == 3:
                    changed = puzzle_game.move_empty_tile("LEFT")
                elif direction == 4:
                    changed = puzzle_game.move_empty_tile("RIGHT")

    def xǁShufflePuzzleLevelEasyǁshuffle__mutmut_1 (self, puzzle_game):
        list_directions = None
        for number in range(0, self.number_of_shuffles):
            changed = False
            while not changed:
                direction = random.choice(list_directions)
                if direction == 1:
                    changed = puzzle_game.move_empty_tile("UP")
                elif direction == 2:
                    changed = puzzle_game.move_empty_tile("DOWN")
                elif direction == 3:
                    changed = puzzle_game.move_empty_tile("LEFT")
                elif direction == 4:
                    changed = puzzle_game.move_empty_tile("RIGHT")

    def xǁShufflePuzzleLevelEasyǁshuffle__mutmut_2 (self, puzzle_game):
        list_directions = [2, 2, 3, 4]
        for number in range(0, self.number_of_shuffles):
            changed = False
            while not changed:
                direction = random.choice(list_directions)
                if direction == 1:
                    changed = puzzle_game.move_empty_tile("UP")
                elif direction == 2:
                    changed = puzzle_game.move_empty_tile("DOWN")
                elif direction == 3:
                    changed = puzzle_game.move_empty_tile("LEFT")
                elif direction == 4:
                    changed = puzzle_game.move_empty_tile("RIGHT")

    def xǁShufflePuzzleLevelEasyǁshuffle__mutmut_3 (self, puzzle_game):
        list_directions = [1, 3, 3, 4]
        for number in range(0, self.number_of_shuffles):
            changed = False
            while not changed:
                direction = random.choice(list_directions)
                if direction == 1:
                    changed = puzzle_game.move_empty_tile("UP")
                elif direction == 2:
                    changed = puzzle_game.move_empty_tile("DOWN")
                elif direction == 3:
                    changed = puzzle_game.move_empty_tile("LEFT")
                elif direction == 4:
                    changed = puzzle_game.move_empty_tile("RIGHT")

    def xǁShufflePuzzleLevelEasyǁshuffle__mutmut_4 (self, puzzle_game):
        list_directions = [1, 2, 4, 4]
        for number in range(0, self.number_of_shuffles):
            changed = False
            while not changed:
                direction = random.choice(list_directions)
                if direction == 1:
                    changed = puzzle_game.move_empty_tile("UP")
                elif direction == 2:
                    changed = puzzle_game.move_empty_tile("DOWN")
                elif direction == 3:
                    changed = puzzle_game.move_empty_tile("LEFT")
                elif direction == 4:
                    changed = puzzle_game.move_empty_tile("RIGHT")

    def xǁShufflePuzzleLevelEasyǁshuffle__mutmut_5 (self, puzzle_game):
        list_directions = [1, 2, 3, 5]
        for number in range(0, self.number_of_shuffles):
            changed = False
            while not changed:
                direction = random.choice(list_directions)
                if direction == 1:
                    changed = puzzle_game.move_empty_tile("UP")
                elif direction == 2:
                    changed = puzzle_game.move_empty_tile("DOWN")
                elif direction == 3:
                    changed = puzzle_game.move_empty_tile("LEFT")
                elif direction == 4:
                    changed = puzzle_game.move_empty_tile("RIGHT")

    def xǁShufflePuzzleLevelEasyǁshuffle__mutmut_6 (self, puzzle_game):
        list_directions = [1, 2, 3, 4]
        for number in range(None, self.number_of_shuffles):
            changed = False
            while not changed:
                direction = random.choice(list_directions)
                if direction == 1:
                    changed = puzzle_game.move_empty_tile("UP")
                elif direction == 2:
                    changed = puzzle_game.move_empty_tile("DOWN")
                elif direction == 3:
                    changed = puzzle_game.move_empty_tile("LEFT")
                elif direction == 4:
                    changed = puzzle_game.move_empty_tile("RIGHT")

    def xǁShufflePuzzleLevelEasyǁshuffle__mutmut_7 (self, puzzle_game):
        list_directions = [1, 2, 3, 4]
        for number in range(0, None):
            changed = False
            while not changed:
                direction = random.choice(list_directions)
                if direction == 1:
                    changed = puzzle_game.move_empty_tile("UP")
                elif direction == 2:
                    changed = puzzle_game.move_empty_tile("DOWN")
                elif direction == 3:
                    changed = puzzle_game.move_empty_tile("LEFT")
                elif direction == 4:
                    changed = puzzle_game.move_empty_tile("RIGHT")

    def xǁShufflePuzzleLevelEasyǁshuffle__mutmut_8 (self, puzzle_game):
        list_directions = [1, 2, 3, 4]
        for number in range(self.number_of_shuffles):
            changed = False
            while not changed:
                direction = random.choice(list_directions)
                if direction == 1:
                    changed = puzzle_game.move_empty_tile("UP")
                elif direction == 2:
                    changed = puzzle_game.move_empty_tile("DOWN")
                elif direction == 3:
                    changed = puzzle_game.move_empty_tile("LEFT")
                elif direction == 4:
                    changed = puzzle_game.move_empty_tile("RIGHT")

    def xǁShufflePuzzleLevelEasyǁshuffle__mutmut_9 (self, puzzle_game):
        list_directions = [1, 2, 3, 4]
        for number in range(0, ):
            changed = False
            while not changed:
                direction = random.choice(list_directions)
                if direction == 1:
                    changed = puzzle_game.move_empty_tile("UP")
                elif direction == 2:
                    changed = puzzle_game.move_empty_tile("DOWN")
                elif direction == 3:
                    changed = puzzle_game.move_empty_tile("LEFT")
                elif direction == 4:
                    changed = puzzle_game.move_empty_tile("RIGHT")

    def xǁShufflePuzzleLevelEasyǁshuffle__mutmut_10 (self, puzzle_game):
        list_directions = [1, 2, 3, 4]
        for number in range(1, self.number_of_shuffles):
            changed = False
            while not changed:
                direction = random.choice(list_directions)
                if direction == 1:
                    changed = puzzle_game.move_empty_tile("UP")
                elif direction == 2:
                    changed = puzzle_game.move_empty_tile("DOWN")
                elif direction == 3:
                    changed = puzzle_game.move_empty_tile("LEFT")
                elif direction == 4:
                    changed = puzzle_game.move_empty_tile("RIGHT")

    def xǁShufflePuzzleLevelEasyǁshuffle__mutmut_11 (self, puzzle_game):
        list_directions = [1, 2, 3, 4]
        for number in range(0, self.number_of_shuffles):
            changed = None
            while not changed:
                direction = random.choice(list_directions)
                if direction == 1:
                    changed = puzzle_game.move_empty_tile("UP")
                elif direction == 2:
                    changed = puzzle_game.move_empty_tile("DOWN")
                elif direction == 3:
                    changed = puzzle_game.move_empty_tile("LEFT")
                elif direction == 4:
                    changed = puzzle_game.move_empty_tile("RIGHT")

    def xǁShufflePuzzleLevelEasyǁshuffle__mutmut_12 (self, puzzle_game):
        list_directions = [1, 2, 3, 4]
        for number in range(0, self.number_of_shuffles):
            changed = True
            while not changed:
                direction = random.choice(list_directions)
                if direction == 1:
                    changed = puzzle_game.move_empty_tile("UP")
                elif direction == 2:
                    changed = puzzle_game.move_empty_tile("DOWN")
                elif direction == 3:
                    changed = puzzle_game.move_empty_tile("LEFT")
                elif direction == 4:
                    changed = puzzle_game.move_empty_tile("RIGHT")

    def xǁShufflePuzzleLevelEasyǁshuffle__mutmut_13 (self, puzzle_game):
        list_directions = [1, 2, 3, 4]
        for number in range(0, self.number_of_shuffles):
            changed = False
            while changed:
                direction = random.choice(list_directions)
                if direction == 1:
                    changed = puzzle_game.move_empty_tile("UP")
                elif direction == 2:
                    changed = puzzle_game.move_empty_tile("DOWN")
                elif direction == 3:
                    changed = puzzle_game.move_empty_tile("LEFT")
                elif direction == 4:
                    changed = puzzle_game.move_empty_tile("RIGHT")

    def xǁShufflePuzzleLevelEasyǁshuffle__mutmut_14 (self, puzzle_game):
        list_directions = [1, 2, 3, 4]
        for number in range(0, self.number_of_shuffles):
            changed = False
            while not changed:
                direction = None
                if direction == 1:
                    changed = puzzle_game.move_empty_tile("UP")
                elif direction == 2:
                    changed = puzzle_game.move_empty_tile("DOWN")
                elif direction == 3:
                    changed = puzzle_game.move_empty_tile("LEFT")
                elif direction == 4:
                    changed = puzzle_game.move_empty_tile("RIGHT")

    def xǁShufflePuzzleLevelEasyǁshuffle__mutmut_15 (self, puzzle_game):
        list_directions = [1, 2, 3, 4]
        for number in range(0, self.number_of_shuffles):
            changed = False
            while not changed:
                direction = random.choice(None)
                if direction == 1:
                    changed = puzzle_game.move_empty_tile("UP")
                elif direction == 2:
                    changed = puzzle_game.move_empty_tile("DOWN")
                elif direction == 3:
                    changed = puzzle_game.move_empty_tile("LEFT")
                elif direction == 4:
                    changed = puzzle_game.move_empty_tile("RIGHT")

    def xǁShufflePuzzleLevelEasyǁshuffle__mutmut_16 (self, puzzle_game):
        list_directions = [1, 2, 3, 4]
        for number in range(0, self.number_of_shuffles):
            changed = False
            while not changed:
                direction = random.choice(list_directions)
                if direction != 1:
                    changed = puzzle_game.move_empty_tile("UP")
                elif direction == 2:
                    changed = puzzle_game.move_empty_tile("DOWN")
                elif direction == 3:
                    changed = puzzle_game.move_empty_tile("LEFT")
                elif direction == 4:
                    changed = puzzle_game.move_empty_tile("RIGHT")

    def xǁShufflePuzzleLevelEasyǁshuffle__mutmut_17 (self, puzzle_game):
        list_directions = [1, 2, 3, 4]
        for number in range(0, self.number_of_shuffles):
            changed = False
            while not changed:
                direction = random.choice(list_directions)
                if direction == 2:
                    changed = puzzle_game.move_empty_tile("UP")
                elif direction == 2:
                    changed = puzzle_game.move_empty_tile("DOWN")
                elif direction == 3:
                    changed = puzzle_game.move_empty_tile("LEFT")
                elif direction == 4:
                    changed = puzzle_game.move_empty_tile("RIGHT")

    def xǁShufflePuzzleLevelEasyǁshuffle__mutmut_18 (self, puzzle_game):
        list_directions = [1, 2, 3, 4]
        for number in range(0, self.number_of_shuffles):
            changed = False
            while not changed:
                direction = random.choice(list_directions)
                if direction == 1:
                    changed = None
                elif direction == 2:
                    changed = puzzle_game.move_empty_tile("DOWN")
                elif direction == 3:
                    changed = puzzle_game.move_empty_tile("LEFT")
                elif direction == 4:
                    changed = puzzle_game.move_empty_tile("RIGHT")

    def xǁShufflePuzzleLevelEasyǁshuffle__mutmut_19 (self, puzzle_game):
        list_directions = [1, 2, 3, 4]
        for number in range(0, self.number_of_shuffles):
            changed = False
            while not changed:
                direction = random.choice(list_directions)
                if direction == 1:
                    changed = puzzle_game.move_empty_tile(None)
                elif direction == 2:
                    changed = puzzle_game.move_empty_tile("DOWN")
                elif direction == 3:
                    changed = puzzle_game.move_empty_tile("LEFT")
                elif direction == 4:
                    changed = puzzle_game.move_empty_tile("RIGHT")

    def xǁShufflePuzzleLevelEasyǁshuffle__mutmut_20 (self, puzzle_game):
        list_directions = [1, 2, 3, 4]
        for number in range(0, self.number_of_shuffles):
            changed = False
            while not changed:
                direction = random.choice(list_directions)
                if direction == 1:
                    changed = puzzle_game.move_empty_tile("XXUPXX")
                elif direction == 2:
                    changed = puzzle_game.move_empty_tile("DOWN")
                elif direction == 3:
                    changed = puzzle_game.move_empty_tile("LEFT")
                elif direction == 4:
                    changed = puzzle_game.move_empty_tile("RIGHT")

    def xǁShufflePuzzleLevelEasyǁshuffle__mutmut_21 (self, puzzle_game):
        list_directions = [1, 2, 3, 4]
        for number in range(0, self.number_of_shuffles):
            changed = False
            while not changed:
                direction = random.choice(list_directions)
                if direction == 1:
                    changed = puzzle_game.move_empty_tile("up")
                elif direction == 2:
                    changed = puzzle_game.move_empty_tile("DOWN")
                elif direction == 3:
                    changed = puzzle_game.move_empty_tile("LEFT")
                elif direction == 4:
                    changed = puzzle_game.move_empty_tile("RIGHT")

    def xǁShufflePuzzleLevelEasyǁshuffle__mutmut_22 (self, puzzle_game):
        list_directions = [1, 2, 3, 4]
        for number in range(0, self.number_of_shuffles):
            changed = False
            while not changed:
                direction = random.choice(list_directions)
                if direction == 1:
                    changed = puzzle_game.move_empty_tile("UP")
                elif direction != 2:
                    changed = puzzle_game.move_empty_tile("DOWN")
                elif direction == 3:
                    changed = puzzle_game.move_empty_tile("LEFT")
                elif direction == 4:
                    changed = puzzle_game.move_empty_tile("RIGHT")

    def xǁShufflePuzzleLevelEasyǁshuffle__mutmut_23 (self, puzzle_game):
        list_directions = [1, 2, 3, 4]
        for number in range(0, self.number_of_shuffles):
            changed = False
            while not changed:
                direction = random.choice(list_directions)
                if direction == 1:
                    changed = puzzle_game.move_empty_tile("UP")
                elif direction == 3:
                    changed = puzzle_game.move_empty_tile("DOWN")
                elif direction == 3:
                    changed = puzzle_game.move_empty_tile("LEFT")
                elif direction == 4:
                    changed = puzzle_game.move_empty_tile("RIGHT")

    def xǁShufflePuzzleLevelEasyǁshuffle__mutmut_24 (self, puzzle_game):
        list_directions = [1, 2, 3, 4]
        for number in range(0, self.number_of_shuffles):
            changed = False
            while not changed:
                direction = random.choice(list_directions)
                if direction == 1:
                    changed = puzzle_game.move_empty_tile("UP")
                elif direction == 2:
                    changed = None
                elif direction == 3:
                    changed = puzzle_game.move_empty_tile("LEFT")
                elif direction == 4:
                    changed = puzzle_game.move_empty_tile("RIGHT")

    def xǁShufflePuzzleLevelEasyǁshuffle__mutmut_25 (self, puzzle_game):
        list_directions = [1, 2, 3, 4]
        for number in range(0, self.number_of_shuffles):
            changed = False
            while not changed:
                direction = random.choice(list_directions)
                if direction == 1:
                    changed = puzzle_game.move_empty_tile("UP")
                elif direction == 2:
                    changed = puzzle_game.move_empty_tile(None)
                elif direction == 3:
                    changed = puzzle_game.move_empty_tile("LEFT")
                elif direction == 4:
                    changed = puzzle_game.move_empty_tile("RIGHT")

    def xǁShufflePuzzleLevelEasyǁshuffle__mutmut_26 (self, puzzle_game):
        list_directions = [1, 2, 3, 4]
        for number in range(0, self.number_of_shuffles):
            changed = False
            while not changed:
                direction = random.choice(list_directions)
                if direction == 1:
                    changed = puzzle_game.move_empty_tile("UP")
                elif direction == 2:
                    changed = puzzle_game.move_empty_tile("XXDOWNXX")
                elif direction == 3:
                    changed = puzzle_game.move_empty_tile("LEFT")
                elif direction == 4:
                    changed = puzzle_game.move_empty_tile("RIGHT")

    def xǁShufflePuzzleLevelEasyǁshuffle__mutmut_27 (self, puzzle_game):
        list_directions = [1, 2, 3, 4]
        for number in range(0, self.number_of_shuffles):
            changed = False
            while not changed:
                direction = random.choice(list_directions)
                if direction == 1:
                    changed = puzzle_game.move_empty_tile("UP")
                elif direction == 2:
                    changed = puzzle_game.move_empty_tile("down")
                elif direction == 3:
                    changed = puzzle_game.move_empty_tile("LEFT")
                elif direction == 4:
                    changed = puzzle_game.move_empty_tile("RIGHT")

    def xǁShufflePuzzleLevelEasyǁshuffle__mutmut_28 (self, puzzle_game):
        list_directions = [1, 2, 3, 4]
        for number in range(0, self.number_of_shuffles):
            changed = False
            while not changed:
                direction = random.choice(list_directions)
                if direction == 1:
                    changed = puzzle_game.move_empty_tile("UP")
                elif direction == 2:
                    changed = puzzle_game.move_empty_tile("DOWN")
                elif direction != 3:
                    changed = puzzle_game.move_empty_tile("LEFT")
                elif direction == 4:
                    changed = puzzle_game.move_empty_tile("RIGHT")

    def xǁShufflePuzzleLevelEasyǁshuffle__mutmut_29 (self, puzzle_game):
        list_directions = [1, 2, 3, 4]
        for number in range(0, self.number_of_shuffles):
            changed = False
            while not changed:
                direction = random.choice(list_directions)
                if direction == 1:
                    changed = puzzle_game.move_empty_tile("UP")
                elif direction == 2:
                    changed = puzzle_game.move_empty_tile("DOWN")
                elif direction == 4:
                    changed = puzzle_game.move_empty_tile("LEFT")
                elif direction == 4:
                    changed = puzzle_game.move_empty_tile("RIGHT")

    def xǁShufflePuzzleLevelEasyǁshuffle__mutmut_30 (self, puzzle_game):
        list_directions = [1, 2, 3, 4]
        for number in range(0, self.number_of_shuffles):
            changed = False
            while not changed:
                direction = random.choice(list_directions)
                if direction == 1:
                    changed = puzzle_game.move_empty_tile("UP")
                elif direction == 2:
                    changed = puzzle_game.move_empty_tile("DOWN")
                elif direction == 3:
                    changed = None
                elif direction == 4:
                    changed = puzzle_game.move_empty_tile("RIGHT")

    def xǁShufflePuzzleLevelEasyǁshuffle__mutmut_31 (self, puzzle_game):
        list_directions = [1, 2, 3, 4]
        for number in range(0, self.number_of_shuffles):
            changed = False
            while not changed:
                direction = random.choice(list_directions)
                if direction == 1:
                    changed = puzzle_game.move_empty_tile("UP")
                elif direction == 2:
                    changed = puzzle_game.move_empty_tile("DOWN")
                elif direction == 3:
                    changed = puzzle_game.move_empty_tile(None)
                elif direction == 4:
                    changed = puzzle_game.move_empty_tile("RIGHT")

    def xǁShufflePuzzleLevelEasyǁshuffle__mutmut_32 (self, puzzle_game):
        list_directions = [1, 2, 3, 4]
        for number in range(0, self.number_of_shuffles):
            changed = False
            while not changed:
                direction = random.choice(list_directions)
                if direction == 1:
                    changed = puzzle_game.move_empty_tile("UP")
                elif direction == 2:
                    changed = puzzle_game.move_empty_tile("DOWN")
                elif direction == 3:
                    changed = puzzle_game.move_empty_tile("XXLEFTXX")
                elif direction == 4:
                    changed = puzzle_game.move_empty_tile("RIGHT")

    def xǁShufflePuzzleLevelEasyǁshuffle__mutmut_33 (self, puzzle_game):
        list_directions = [1, 2, 3, 4]
        for number in range(0, self.number_of_shuffles):
            changed = False
            while not changed:
                direction = random.choice(list_directions)
                if direction == 1:
                    changed = puzzle_game.move_empty_tile("UP")
                elif direction == 2:
                    changed = puzzle_game.move_empty_tile("DOWN")
                elif direction == 3:
                    changed = puzzle_game.move_empty_tile("left")
                elif direction == 4:
                    changed = puzzle_game.move_empty_tile("RIGHT")

    def xǁShufflePuzzleLevelEasyǁshuffle__mutmut_34 (self, puzzle_game):
        list_directions = [1, 2, 3, 4]
        for number in range(0, self.number_of_shuffles):
            changed = False
            while not changed:
                direction = random.choice(list_directions)
                if direction == 1:
                    changed = puzzle_game.move_empty_tile("UP")
                elif direction == 2:
                    changed = puzzle_game.move_empty_tile("DOWN")
                elif direction == 3:
                    changed = puzzle_game.move_empty_tile("LEFT")
                elif direction != 4:
                    changed = puzzle_game.move_empty_tile("RIGHT")

    def xǁShufflePuzzleLevelEasyǁshuffle__mutmut_35 (self, puzzle_game):
        list_directions = [1, 2, 3, 4]
        for number in range(0, self.number_of_shuffles):
            changed = False
            while not changed:
                direction = random.choice(list_directions)
                if direction == 1:
                    changed = puzzle_game.move_empty_tile("UP")
                elif direction == 2:
                    changed = puzzle_game.move_empty_tile("DOWN")
                elif direction == 3:
                    changed = puzzle_game.move_empty_tile("LEFT")
                elif direction == 5:
                    changed = puzzle_game.move_empty_tile("RIGHT")

    def xǁShufflePuzzleLevelEasyǁshuffle__mutmut_36 (self, puzzle_game):
        list_directions = [1, 2, 3, 4]
        for number in range(0, self.number_of_shuffles):
            changed = False
            while not changed:
                direction = random.choice(list_directions)
                if direction == 1:
                    changed = puzzle_game.move_empty_tile("UP")
                elif direction == 2:
                    changed = puzzle_game.move_empty_tile("DOWN")
                elif direction == 3:
                    changed = puzzle_game.move_empty_tile("LEFT")
                elif direction == 4:
                    changed = None

    def xǁShufflePuzzleLevelEasyǁshuffle__mutmut_37 (self, puzzle_game):
        list_directions = [1, 2, 3, 4]
        for number in range(0, self.number_of_shuffles):
            changed = False
            while not changed:
                direction = random.choice(list_directions)
                if direction == 1:
                    changed = puzzle_game.move_empty_tile("UP")
                elif direction == 2:
                    changed = puzzle_game.move_empty_tile("DOWN")
                elif direction == 3:
                    changed = puzzle_game.move_empty_tile("LEFT")
                elif direction == 4:
                    changed = puzzle_game.move_empty_tile(None)

    def xǁShufflePuzzleLevelEasyǁshuffle__mutmut_38 (self, puzzle_game):
        list_directions = [1, 2, 3, 4]
        for number in range(0, self.number_of_shuffles):
            changed = False
            while not changed:
                direction = random.choice(list_directions)
                if direction == 1:
                    changed = puzzle_game.move_empty_tile("UP")
                elif direction == 2:
                    changed = puzzle_game.move_empty_tile("DOWN")
                elif direction == 3:
                    changed = puzzle_game.move_empty_tile("LEFT")
                elif direction == 4:
                    changed = puzzle_game.move_empty_tile("XXRIGHTXX")

    def xǁShufflePuzzleLevelEasyǁshuffle__mutmut_39 (self, puzzle_game):
        list_directions = [1, 2, 3, 4]
        for number in range(0, self.number_of_shuffles):
            changed = False
            while not changed:
                direction = random.choice(list_directions)
                if direction == 1:
                    changed = puzzle_game.move_empty_tile("UP")
                elif direction == 2:
                    changed = puzzle_game.move_empty_tile("DOWN")
                elif direction == 3:
                    changed = puzzle_game.move_empty_tile("LEFT")
                elif direction == 4:
                    changed = puzzle_game.move_empty_tile("right")
    
    xǁShufflePuzzleLevelEasyǁshuffle__mutmut_mutants : ClassVar[MutantDict] = {
    'xǁShufflePuzzleLevelEasyǁshuffle__mutmut_1': xǁShufflePuzzleLevelEasyǁshuffle__mutmut_1, 
        'xǁShufflePuzzleLevelEasyǁshuffle__mutmut_2': xǁShufflePuzzleLevelEasyǁshuffle__mutmut_2, 
        'xǁShufflePuzzleLevelEasyǁshuffle__mutmut_3': xǁShufflePuzzleLevelEasyǁshuffle__mutmut_3, 
        'xǁShufflePuzzleLevelEasyǁshuffle__mutmut_4': xǁShufflePuzzleLevelEasyǁshuffle__mutmut_4, 
        'xǁShufflePuzzleLevelEasyǁshuffle__mutmut_5': xǁShufflePuzzleLevelEasyǁshuffle__mutmut_5, 
        'xǁShufflePuzzleLevelEasyǁshuffle__mutmut_6': xǁShufflePuzzleLevelEasyǁshuffle__mutmut_6, 
        'xǁShufflePuzzleLevelEasyǁshuffle__mutmut_7': xǁShufflePuzzleLevelEasyǁshuffle__mutmut_7, 
        'xǁShufflePuzzleLevelEasyǁshuffle__mutmut_8': xǁShufflePuzzleLevelEasyǁshuffle__mutmut_8, 
        'xǁShufflePuzzleLevelEasyǁshuffle__mutmut_9': xǁShufflePuzzleLevelEasyǁshuffle__mutmut_9, 
        'xǁShufflePuzzleLevelEasyǁshuffle__mutmut_10': xǁShufflePuzzleLevelEasyǁshuffle__mutmut_10, 
        'xǁShufflePuzzleLevelEasyǁshuffle__mutmut_11': xǁShufflePuzzleLevelEasyǁshuffle__mutmut_11, 
        'xǁShufflePuzzleLevelEasyǁshuffle__mutmut_12': xǁShufflePuzzleLevelEasyǁshuffle__mutmut_12, 
        'xǁShufflePuzzleLevelEasyǁshuffle__mutmut_13': xǁShufflePuzzleLevelEasyǁshuffle__mutmut_13, 
        'xǁShufflePuzzleLevelEasyǁshuffle__mutmut_14': xǁShufflePuzzleLevelEasyǁshuffle__mutmut_14, 
        'xǁShufflePuzzleLevelEasyǁshuffle__mutmut_15': xǁShufflePuzzleLevelEasyǁshuffle__mutmut_15, 
        'xǁShufflePuzzleLevelEasyǁshuffle__mutmut_16': xǁShufflePuzzleLevelEasyǁshuffle__mutmut_16, 
        'xǁShufflePuzzleLevelEasyǁshuffle__mutmut_17': xǁShufflePuzzleLevelEasyǁshuffle__mutmut_17, 
        'xǁShufflePuzzleLevelEasyǁshuffle__mutmut_18': xǁShufflePuzzleLevelEasyǁshuffle__mutmut_18, 
        'xǁShufflePuzzleLevelEasyǁshuffle__mutmut_19': xǁShufflePuzzleLevelEasyǁshuffle__mutmut_19, 
        'xǁShufflePuzzleLevelEasyǁshuffle__mutmut_20': xǁShufflePuzzleLevelEasyǁshuffle__mutmut_20, 
        'xǁShufflePuzzleLevelEasyǁshuffle__mutmut_21': xǁShufflePuzzleLevelEasyǁshuffle__mutmut_21, 
        'xǁShufflePuzzleLevelEasyǁshuffle__mutmut_22': xǁShufflePuzzleLevelEasyǁshuffle__mutmut_22, 
        'xǁShufflePuzzleLevelEasyǁshuffle__mutmut_23': xǁShufflePuzzleLevelEasyǁshuffle__mutmut_23, 
        'xǁShufflePuzzleLevelEasyǁshuffle__mutmut_24': xǁShufflePuzzleLevelEasyǁshuffle__mutmut_24, 
        'xǁShufflePuzzleLevelEasyǁshuffle__mutmut_25': xǁShufflePuzzleLevelEasyǁshuffle__mutmut_25, 
        'xǁShufflePuzzleLevelEasyǁshuffle__mutmut_26': xǁShufflePuzzleLevelEasyǁshuffle__mutmut_26, 
        'xǁShufflePuzzleLevelEasyǁshuffle__mutmut_27': xǁShufflePuzzleLevelEasyǁshuffle__mutmut_27, 
        'xǁShufflePuzzleLevelEasyǁshuffle__mutmut_28': xǁShufflePuzzleLevelEasyǁshuffle__mutmut_28, 
        'xǁShufflePuzzleLevelEasyǁshuffle__mutmut_29': xǁShufflePuzzleLevelEasyǁshuffle__mutmut_29, 
        'xǁShufflePuzzleLevelEasyǁshuffle__mutmut_30': xǁShufflePuzzleLevelEasyǁshuffle__mutmut_30, 
        'xǁShufflePuzzleLevelEasyǁshuffle__mutmut_31': xǁShufflePuzzleLevelEasyǁshuffle__mutmut_31, 
        'xǁShufflePuzzleLevelEasyǁshuffle__mutmut_32': xǁShufflePuzzleLevelEasyǁshuffle__mutmut_32, 
        'xǁShufflePuzzleLevelEasyǁshuffle__mutmut_33': xǁShufflePuzzleLevelEasyǁshuffle__mutmut_33, 
        'xǁShufflePuzzleLevelEasyǁshuffle__mutmut_34': xǁShufflePuzzleLevelEasyǁshuffle__mutmut_34, 
        'xǁShufflePuzzleLevelEasyǁshuffle__mutmut_35': xǁShufflePuzzleLevelEasyǁshuffle__mutmut_35, 
        'xǁShufflePuzzleLevelEasyǁshuffle__mutmut_36': xǁShufflePuzzleLevelEasyǁshuffle__mutmut_36, 
        'xǁShufflePuzzleLevelEasyǁshuffle__mutmut_37': xǁShufflePuzzleLevelEasyǁshuffle__mutmut_37, 
        'xǁShufflePuzzleLevelEasyǁshuffle__mutmut_38': xǁShufflePuzzleLevelEasyǁshuffle__mutmut_38, 
        'xǁShufflePuzzleLevelEasyǁshuffle__mutmut_39': xǁShufflePuzzleLevelEasyǁshuffle__mutmut_39
    }
    
    def shuffle(self, *args, **kwargs):
        result = _mutmut_trampoline(object.__getattribute__(self, "xǁShufflePuzzleLevelEasyǁshuffle__mutmut_orig"), object.__getattribute__(self, "xǁShufflePuzzleLevelEasyǁshuffle__mutmut_mutants"), args, kwargs, self)
        return result 
    
    shuffle.__signature__ = _mutmut_signature(xǁShufflePuzzleLevelEasyǁshuffle__mutmut_orig)
    xǁShufflePuzzleLevelEasyǁshuffle__mutmut_orig.__name__ = 'xǁShufflePuzzleLevelEasyǁshuffle'


class ShufflePuzzleLevelMedium:

    def xǁShufflePuzzleLevelMediumǁ__init____mutmut_orig(self):
        self.number_of_shuffles = 10;

    def xǁShufflePuzzleLevelMediumǁ__init____mutmut_1(self):
        self.number_of_shuffles = None;

    def xǁShufflePuzzleLevelMediumǁ__init____mutmut_2(self):
        self.number_of_shuffles = 11;
    
    xǁShufflePuzzleLevelMediumǁ__init____mutmut_mutants : ClassVar[MutantDict] = {
    'xǁShufflePuzzleLevelMediumǁ__init____mutmut_1': xǁShufflePuzzleLevelMediumǁ__init____mutmut_1, 
        'xǁShufflePuzzleLevelMediumǁ__init____mutmut_2': xǁShufflePuzzleLevelMediumǁ__init____mutmut_2
    }
    
    def __init__(self, *args, **kwargs):
        result = _mutmut_trampoline(object.__getattribute__(self, "xǁShufflePuzzleLevelMediumǁ__init____mutmut_orig"), object.__getattribute__(self, "xǁShufflePuzzleLevelMediumǁ__init____mutmut_mutants"), args, kwargs, self)
        return result 
    
    __init__.__signature__ = _mutmut_signature(xǁShufflePuzzleLevelMediumǁ__init____mutmut_orig)
    xǁShufflePuzzleLevelMediumǁ__init____mutmut_orig.__name__ = 'xǁShufflePuzzleLevelMediumǁ__init__'

    def xǁShufflePuzzleLevelMediumǁshuffle__mutmut_orig (self, puzzle_game):
        list_directions = [1, 2, 3, 4]
        for number in range(0, self.number_of_shuffles):
            changed = False
            while not changed:
                direction = random.choice(list_directions)
                if direction == 1:
                    changed = puzzle_game.move_empty_tile("UP")
                elif direction == 2:
                    changed = puzzle_game.move_empty_tile("DOWN")
                elif direction == 3:
                    changed = puzzle_game.move_empty_tile("LEFT")
                elif direction == 4:
                    changed = puzzle_game.move_empty_tile("RIGHT")

    def xǁShufflePuzzleLevelMediumǁshuffle__mutmut_1 (self, puzzle_game):
        list_directions = None
        for number in range(0, self.number_of_shuffles):
            changed = False
            while not changed:
                direction = random.choice(list_directions)
                if direction == 1:
                    changed = puzzle_game.move_empty_tile("UP")
                elif direction == 2:
                    changed = puzzle_game.move_empty_tile("DOWN")
                elif direction == 3:
                    changed = puzzle_game.move_empty_tile("LEFT")
                elif direction == 4:
                    changed = puzzle_game.move_empty_tile("RIGHT")

    def xǁShufflePuzzleLevelMediumǁshuffle__mutmut_2 (self, puzzle_game):
        list_directions = [2, 2, 3, 4]
        for number in range(0, self.number_of_shuffles):
            changed = False
            while not changed:
                direction = random.choice(list_directions)
                if direction == 1:
                    changed = puzzle_game.move_empty_tile("UP")
                elif direction == 2:
                    changed = puzzle_game.move_empty_tile("DOWN")
                elif direction == 3:
                    changed = puzzle_game.move_empty_tile("LEFT")
                elif direction == 4:
                    changed = puzzle_game.move_empty_tile("RIGHT")

    def xǁShufflePuzzleLevelMediumǁshuffle__mutmut_3 (self, puzzle_game):
        list_directions = [1, 3, 3, 4]
        for number in range(0, self.number_of_shuffles):
            changed = False
            while not changed:
                direction = random.choice(list_directions)
                if direction == 1:
                    changed = puzzle_game.move_empty_tile("UP")
                elif direction == 2:
                    changed = puzzle_game.move_empty_tile("DOWN")
                elif direction == 3:
                    changed = puzzle_game.move_empty_tile("LEFT")
                elif direction == 4:
                    changed = puzzle_game.move_empty_tile("RIGHT")

    def xǁShufflePuzzleLevelMediumǁshuffle__mutmut_4 (self, puzzle_game):
        list_directions = [1, 2, 4, 4]
        for number in range(0, self.number_of_shuffles):
            changed = False
            while not changed:
                direction = random.choice(list_directions)
                if direction == 1:
                    changed = puzzle_game.move_empty_tile("UP")
                elif direction == 2:
                    changed = puzzle_game.move_empty_tile("DOWN")
                elif direction == 3:
                    changed = puzzle_game.move_empty_tile("LEFT")
                elif direction == 4:
                    changed = puzzle_game.move_empty_tile("RIGHT")

    def xǁShufflePuzzleLevelMediumǁshuffle__mutmut_5 (self, puzzle_game):
        list_directions = [1, 2, 3, 5]
        for number in range(0, self.number_of_shuffles):
            changed = False
            while not changed:
                direction = random.choice(list_directions)
                if direction == 1:
                    changed = puzzle_game.move_empty_tile("UP")
                elif direction == 2:
                    changed = puzzle_game.move_empty_tile("DOWN")
                elif direction == 3:
                    changed = puzzle_game.move_empty_tile("LEFT")
                elif direction == 4:
                    changed = puzzle_game.move_empty_tile("RIGHT")

    def xǁShufflePuzzleLevelMediumǁshuffle__mutmut_6 (self, puzzle_game):
        list_directions = [1, 2, 3, 4]
        for number in range(None, self.number_of_shuffles):
            changed = False
            while not changed:
                direction = random.choice(list_directions)
                if direction == 1:
                    changed = puzzle_game.move_empty_tile("UP")
                elif direction == 2:
                    changed = puzzle_game.move_empty_tile("DOWN")
                elif direction == 3:
                    changed = puzzle_game.move_empty_tile("LEFT")
                elif direction == 4:
                    changed = puzzle_game.move_empty_tile("RIGHT")

    def xǁShufflePuzzleLevelMediumǁshuffle__mutmut_7 (self, puzzle_game):
        list_directions = [1, 2, 3, 4]
        for number in range(0, None):
            changed = False
            while not changed:
                direction = random.choice(list_directions)
                if direction == 1:
                    changed = puzzle_game.move_empty_tile("UP")
                elif direction == 2:
                    changed = puzzle_game.move_empty_tile("DOWN")
                elif direction == 3:
                    changed = puzzle_game.move_empty_tile("LEFT")
                elif direction == 4:
                    changed = puzzle_game.move_empty_tile("RIGHT")

    def xǁShufflePuzzleLevelMediumǁshuffle__mutmut_8 (self, puzzle_game):
        list_directions = [1, 2, 3, 4]
        for number in range(self.number_of_shuffles):
            changed = False
            while not changed:
                direction = random.choice(list_directions)
                if direction == 1:
                    changed = puzzle_game.move_empty_tile("UP")
                elif direction == 2:
                    changed = puzzle_game.move_empty_tile("DOWN")
                elif direction == 3:
                    changed = puzzle_game.move_empty_tile("LEFT")
                elif direction == 4:
                    changed = puzzle_game.move_empty_tile("RIGHT")

    def xǁShufflePuzzleLevelMediumǁshuffle__mutmut_9 (self, puzzle_game):
        list_directions = [1, 2, 3, 4]
        for number in range(0, ):
            changed = False
            while not changed:
                direction = random.choice(list_directions)
                if direction == 1:
                    changed = puzzle_game.move_empty_tile("UP")
                elif direction == 2:
                    changed = puzzle_game.move_empty_tile("DOWN")
                elif direction == 3:
                    changed = puzzle_game.move_empty_tile("LEFT")
                elif direction == 4:
                    changed = puzzle_game.move_empty_tile("RIGHT")

    def xǁShufflePuzzleLevelMediumǁshuffle__mutmut_10 (self, puzzle_game):
        list_directions = [1, 2, 3, 4]
        for number in range(1, self.number_of_shuffles):
            changed = False
            while not changed:
                direction = random.choice(list_directions)
                if direction == 1:
                    changed = puzzle_game.move_empty_tile("UP")
                elif direction == 2:
                    changed = puzzle_game.move_empty_tile("DOWN")
                elif direction == 3:
                    changed = puzzle_game.move_empty_tile("LEFT")
                elif direction == 4:
                    changed = puzzle_game.move_empty_tile("RIGHT")

    def xǁShufflePuzzleLevelMediumǁshuffle__mutmut_11 (self, puzzle_game):
        list_directions = [1, 2, 3, 4]
        for number in range(0, self.number_of_shuffles):
            changed = None
            while not changed:
                direction = random.choice(list_directions)
                if direction == 1:
                    changed = puzzle_game.move_empty_tile("UP")
                elif direction == 2:
                    changed = puzzle_game.move_empty_tile("DOWN")
                elif direction == 3:
                    changed = puzzle_game.move_empty_tile("LEFT")
                elif direction == 4:
                    changed = puzzle_game.move_empty_tile("RIGHT")

    def xǁShufflePuzzleLevelMediumǁshuffle__mutmut_12 (self, puzzle_game):
        list_directions = [1, 2, 3, 4]
        for number in range(0, self.number_of_shuffles):
            changed = True
            while not changed:
                direction = random.choice(list_directions)
                if direction == 1:
                    changed = puzzle_game.move_empty_tile("UP")
                elif direction == 2:
                    changed = puzzle_game.move_empty_tile("DOWN")
                elif direction == 3:
                    changed = puzzle_game.move_empty_tile("LEFT")
                elif direction == 4:
                    changed = puzzle_game.move_empty_tile("RIGHT")

    def xǁShufflePuzzleLevelMediumǁshuffle__mutmut_13 (self, puzzle_game):
        list_directions = [1, 2, 3, 4]
        for number in range(0, self.number_of_shuffles):
            changed = False
            while changed:
                direction = random.choice(list_directions)
                if direction == 1:
                    changed = puzzle_game.move_empty_tile("UP")
                elif direction == 2:
                    changed = puzzle_game.move_empty_tile("DOWN")
                elif direction == 3:
                    changed = puzzle_game.move_empty_tile("LEFT")
                elif direction == 4:
                    changed = puzzle_game.move_empty_tile("RIGHT")

    def xǁShufflePuzzleLevelMediumǁshuffle__mutmut_14 (self, puzzle_game):
        list_directions = [1, 2, 3, 4]
        for number in range(0, self.number_of_shuffles):
            changed = False
            while not changed:
                direction = None
                if direction == 1:
                    changed = puzzle_game.move_empty_tile("UP")
                elif direction == 2:
                    changed = puzzle_game.move_empty_tile("DOWN")
                elif direction == 3:
                    changed = puzzle_game.move_empty_tile("LEFT")
                elif direction == 4:
                    changed = puzzle_game.move_empty_tile("RIGHT")

    def xǁShufflePuzzleLevelMediumǁshuffle__mutmut_15 (self, puzzle_game):
        list_directions = [1, 2, 3, 4]
        for number in range(0, self.number_of_shuffles):
            changed = False
            while not changed:
                direction = random.choice(None)
                if direction == 1:
                    changed = puzzle_game.move_empty_tile("UP")
                elif direction == 2:
                    changed = puzzle_game.move_empty_tile("DOWN")
                elif direction == 3:
                    changed = puzzle_game.move_empty_tile("LEFT")
                elif direction == 4:
                    changed = puzzle_game.move_empty_tile("RIGHT")

    def xǁShufflePuzzleLevelMediumǁshuffle__mutmut_16 (self, puzzle_game):
        list_directions = [1, 2, 3, 4]
        for number in range(0, self.number_of_shuffles):
            changed = False
            while not changed:
                direction = random.choice(list_directions)
                if direction != 1:
                    changed = puzzle_game.move_empty_tile("UP")
                elif direction == 2:
                    changed = puzzle_game.move_empty_tile("DOWN")
                elif direction == 3:
                    changed = puzzle_game.move_empty_tile("LEFT")
                elif direction == 4:
                    changed = puzzle_game.move_empty_tile("RIGHT")

    def xǁShufflePuzzleLevelMediumǁshuffle__mutmut_17 (self, puzzle_game):
        list_directions = [1, 2, 3, 4]
        for number in range(0, self.number_of_shuffles):
            changed = False
            while not changed:
                direction = random.choice(list_directions)
                if direction == 2:
                    changed = puzzle_game.move_empty_tile("UP")
                elif direction == 2:
                    changed = puzzle_game.move_empty_tile("DOWN")
                elif direction == 3:
                    changed = puzzle_game.move_empty_tile("LEFT")
                elif direction == 4:
                    changed = puzzle_game.move_empty_tile("RIGHT")

    def xǁShufflePuzzleLevelMediumǁshuffle__mutmut_18 (self, puzzle_game):
        list_directions = [1, 2, 3, 4]
        for number in range(0, self.number_of_shuffles):
            changed = False
            while not changed:
                direction = random.choice(list_directions)
                if direction == 1:
                    changed = None
                elif direction == 2:
                    changed = puzzle_game.move_empty_tile("DOWN")
                elif direction == 3:
                    changed = puzzle_game.move_empty_tile("LEFT")
                elif direction == 4:
                    changed = puzzle_game.move_empty_tile("RIGHT")

    def xǁShufflePuzzleLevelMediumǁshuffle__mutmut_19 (self, puzzle_game):
        list_directions = [1, 2, 3, 4]
        for number in range(0, self.number_of_shuffles):
            changed = False
            while not changed:
                direction = random.choice(list_directions)
                if direction == 1:
                    changed = puzzle_game.move_empty_tile(None)
                elif direction == 2:
                    changed = puzzle_game.move_empty_tile("DOWN")
                elif direction == 3:
                    changed = puzzle_game.move_empty_tile("LEFT")
                elif direction == 4:
                    changed = puzzle_game.move_empty_tile("RIGHT")

    def xǁShufflePuzzleLevelMediumǁshuffle__mutmut_20 (self, puzzle_game):
        list_directions = [1, 2, 3, 4]
        for number in range(0, self.number_of_shuffles):
            changed = False
            while not changed:
                direction = random.choice(list_directions)
                if direction == 1:
                    changed = puzzle_game.move_empty_tile("XXUPXX")
                elif direction == 2:
                    changed = puzzle_game.move_empty_tile("DOWN")
                elif direction == 3:
                    changed = puzzle_game.move_empty_tile("LEFT")
                elif direction == 4:
                    changed = puzzle_game.move_empty_tile("RIGHT")

    def xǁShufflePuzzleLevelMediumǁshuffle__mutmut_21 (self, puzzle_game):
        list_directions = [1, 2, 3, 4]
        for number in range(0, self.number_of_shuffles):
            changed = False
            while not changed:
                direction = random.choice(list_directions)
                if direction == 1:
                    changed = puzzle_game.move_empty_tile("up")
                elif direction == 2:
                    changed = puzzle_game.move_empty_tile("DOWN")
                elif direction == 3:
                    changed = puzzle_game.move_empty_tile("LEFT")
                elif direction == 4:
                    changed = puzzle_game.move_empty_tile("RIGHT")

    def xǁShufflePuzzleLevelMediumǁshuffle__mutmut_22 (self, puzzle_game):
        list_directions = [1, 2, 3, 4]
        for number in range(0, self.number_of_shuffles):
            changed = False
            while not changed:
                direction = random.choice(list_directions)
                if direction == 1:
                    changed = puzzle_game.move_empty_tile("UP")
                elif direction != 2:
                    changed = puzzle_game.move_empty_tile("DOWN")
                elif direction == 3:
                    changed = puzzle_game.move_empty_tile("LEFT")
                elif direction == 4:
                    changed = puzzle_game.move_empty_tile("RIGHT")

    def xǁShufflePuzzleLevelMediumǁshuffle__mutmut_23 (self, puzzle_game):
        list_directions = [1, 2, 3, 4]
        for number in range(0, self.number_of_shuffles):
            changed = False
            while not changed:
                direction = random.choice(list_directions)
                if direction == 1:
                    changed = puzzle_game.move_empty_tile("UP")
                elif direction == 3:
                    changed = puzzle_game.move_empty_tile("DOWN")
                elif direction == 3:
                    changed = puzzle_game.move_empty_tile("LEFT")
                elif direction == 4:
                    changed = puzzle_game.move_empty_tile("RIGHT")

    def xǁShufflePuzzleLevelMediumǁshuffle__mutmut_24 (self, puzzle_game):
        list_directions = [1, 2, 3, 4]
        for number in range(0, self.number_of_shuffles):
            changed = False
            while not changed:
                direction = random.choice(list_directions)
                if direction == 1:
                    changed = puzzle_game.move_empty_tile("UP")
                elif direction == 2:
                    changed = None
                elif direction == 3:
                    changed = puzzle_game.move_empty_tile("LEFT")
                elif direction == 4:
                    changed = puzzle_game.move_empty_tile("RIGHT")

    def xǁShufflePuzzleLevelMediumǁshuffle__mutmut_25 (self, puzzle_game):
        list_directions = [1, 2, 3, 4]
        for number in range(0, self.number_of_shuffles):
            changed = False
            while not changed:
                direction = random.choice(list_directions)
                if direction == 1:
                    changed = puzzle_game.move_empty_tile("UP")
                elif direction == 2:
                    changed = puzzle_game.move_empty_tile(None)
                elif direction == 3:
                    changed = puzzle_game.move_empty_tile("LEFT")
                elif direction == 4:
                    changed = puzzle_game.move_empty_tile("RIGHT")

    def xǁShufflePuzzleLevelMediumǁshuffle__mutmut_26 (self, puzzle_game):
        list_directions = [1, 2, 3, 4]
        for number in range(0, self.number_of_shuffles):
            changed = False
            while not changed:
                direction = random.choice(list_directions)
                if direction == 1:
                    changed = puzzle_game.move_empty_tile("UP")
                elif direction == 2:
                    changed = puzzle_game.move_empty_tile("XXDOWNXX")
                elif direction == 3:
                    changed = puzzle_game.move_empty_tile("LEFT")
                elif direction == 4:
                    changed = puzzle_game.move_empty_tile("RIGHT")

    def xǁShufflePuzzleLevelMediumǁshuffle__mutmut_27 (self, puzzle_game):
        list_directions = [1, 2, 3, 4]
        for number in range(0, self.number_of_shuffles):
            changed = False
            while not changed:
                direction = random.choice(list_directions)
                if direction == 1:
                    changed = puzzle_game.move_empty_tile("UP")
                elif direction == 2:
                    changed = puzzle_game.move_empty_tile("down")
                elif direction == 3:
                    changed = puzzle_game.move_empty_tile("LEFT")
                elif direction == 4:
                    changed = puzzle_game.move_empty_tile("RIGHT")

    def xǁShufflePuzzleLevelMediumǁshuffle__mutmut_28 (self, puzzle_game):
        list_directions = [1, 2, 3, 4]
        for number in range(0, self.number_of_shuffles):
            changed = False
            while not changed:
                direction = random.choice(list_directions)
                if direction == 1:
                    changed = puzzle_game.move_empty_tile("UP")
                elif direction == 2:
                    changed = puzzle_game.move_empty_tile("DOWN")
                elif direction != 3:
                    changed = puzzle_game.move_empty_tile("LEFT")
                elif direction == 4:
                    changed = puzzle_game.move_empty_tile("RIGHT")

    def xǁShufflePuzzleLevelMediumǁshuffle__mutmut_29 (self, puzzle_game):
        list_directions = [1, 2, 3, 4]
        for number in range(0, self.number_of_shuffles):
            changed = False
            while not changed:
                direction = random.choice(list_directions)
                if direction == 1:
                    changed = puzzle_game.move_empty_tile("UP")
                elif direction == 2:
                    changed = puzzle_game.move_empty_tile("DOWN")
                elif direction == 4:
                    changed = puzzle_game.move_empty_tile("LEFT")
                elif direction == 4:
                    changed = puzzle_game.move_empty_tile("RIGHT")

    def xǁShufflePuzzleLevelMediumǁshuffle__mutmut_30 (self, puzzle_game):
        list_directions = [1, 2, 3, 4]
        for number in range(0, self.number_of_shuffles):
            changed = False
            while not changed:
                direction = random.choice(list_directions)
                if direction == 1:
                    changed = puzzle_game.move_empty_tile("UP")
                elif direction == 2:
                    changed = puzzle_game.move_empty_tile("DOWN")
                elif direction == 3:
                    changed = None
                elif direction == 4:
                    changed = puzzle_game.move_empty_tile("RIGHT")

    def xǁShufflePuzzleLevelMediumǁshuffle__mutmut_31 (self, puzzle_game):
        list_directions = [1, 2, 3, 4]
        for number in range(0, self.number_of_shuffles):
            changed = False
            while not changed:
                direction = random.choice(list_directions)
                if direction == 1:
                    changed = puzzle_game.move_empty_tile("UP")
                elif direction == 2:
                    changed = puzzle_game.move_empty_tile("DOWN")
                elif direction == 3:
                    changed = puzzle_game.move_empty_tile(None)
                elif direction == 4:
                    changed = puzzle_game.move_empty_tile("RIGHT")

    def xǁShufflePuzzleLevelMediumǁshuffle__mutmut_32 (self, puzzle_game):
        list_directions = [1, 2, 3, 4]
        for number in range(0, self.number_of_shuffles):
            changed = False
            while not changed:
                direction = random.choice(list_directions)
                if direction == 1:
                    changed = puzzle_game.move_empty_tile("UP")
                elif direction == 2:
                    changed = puzzle_game.move_empty_tile("DOWN")
                elif direction == 3:
                    changed = puzzle_game.move_empty_tile("XXLEFTXX")
                elif direction == 4:
                    changed = puzzle_game.move_empty_tile("RIGHT")

    def xǁShufflePuzzleLevelMediumǁshuffle__mutmut_33 (self, puzzle_game):
        list_directions = [1, 2, 3, 4]
        for number in range(0, self.number_of_shuffles):
            changed = False
            while not changed:
                direction = random.choice(list_directions)
                if direction == 1:
                    changed = puzzle_game.move_empty_tile("UP")
                elif direction == 2:
                    changed = puzzle_game.move_empty_tile("DOWN")
                elif direction == 3:
                    changed = puzzle_game.move_empty_tile("left")
                elif direction == 4:
                    changed = puzzle_game.move_empty_tile("RIGHT")

    def xǁShufflePuzzleLevelMediumǁshuffle__mutmut_34 (self, puzzle_game):
        list_directions = [1, 2, 3, 4]
        for number in range(0, self.number_of_shuffles):
            changed = False
            while not changed:
                direction = random.choice(list_directions)
                if direction == 1:
                    changed = puzzle_game.move_empty_tile("UP")
                elif direction == 2:
                    changed = puzzle_game.move_empty_tile("DOWN")
                elif direction == 3:
                    changed = puzzle_game.move_empty_tile("LEFT")
                elif direction != 4:
                    changed = puzzle_game.move_empty_tile("RIGHT")

    def xǁShufflePuzzleLevelMediumǁshuffle__mutmut_35 (self, puzzle_game):
        list_directions = [1, 2, 3, 4]
        for number in range(0, self.number_of_shuffles):
            changed = False
            while not changed:
                direction = random.choice(list_directions)
                if direction == 1:
                    changed = puzzle_game.move_empty_tile("UP")
                elif direction == 2:
                    changed = puzzle_game.move_empty_tile("DOWN")
                elif direction == 3:
                    changed = puzzle_game.move_empty_tile("LEFT")
                elif direction == 5:
                    changed = puzzle_game.move_empty_tile("RIGHT")

    def xǁShufflePuzzleLevelMediumǁshuffle__mutmut_36 (self, puzzle_game):
        list_directions = [1, 2, 3, 4]
        for number in range(0, self.number_of_shuffles):
            changed = False
            while not changed:
                direction = random.choice(list_directions)
                if direction == 1:
                    changed = puzzle_game.move_empty_tile("UP")
                elif direction == 2:
                    changed = puzzle_game.move_empty_tile("DOWN")
                elif direction == 3:
                    changed = puzzle_game.move_empty_tile("LEFT")
                elif direction == 4:
                    changed = None

    def xǁShufflePuzzleLevelMediumǁshuffle__mutmut_37 (self, puzzle_game):
        list_directions = [1, 2, 3, 4]
        for number in range(0, self.number_of_shuffles):
            changed = False
            while not changed:
                direction = random.choice(list_directions)
                if direction == 1:
                    changed = puzzle_game.move_empty_tile("UP")
                elif direction == 2:
                    changed = puzzle_game.move_empty_tile("DOWN")
                elif direction == 3:
                    changed = puzzle_game.move_empty_tile("LEFT")
                elif direction == 4:
                    changed = puzzle_game.move_empty_tile(None)

    def xǁShufflePuzzleLevelMediumǁshuffle__mutmut_38 (self, puzzle_game):
        list_directions = [1, 2, 3, 4]
        for number in range(0, self.number_of_shuffles):
            changed = False
            while not changed:
                direction = random.choice(list_directions)
                if direction == 1:
                    changed = puzzle_game.move_empty_tile("UP")
                elif direction == 2:
                    changed = puzzle_game.move_empty_tile("DOWN")
                elif direction == 3:
                    changed = puzzle_game.move_empty_tile("LEFT")
                elif direction == 4:
                    changed = puzzle_game.move_empty_tile("XXRIGHTXX")

    def xǁShufflePuzzleLevelMediumǁshuffle__mutmut_39 (self, puzzle_game):
        list_directions = [1, 2, 3, 4]
        for number in range(0, self.number_of_shuffles):
            changed = False
            while not changed:
                direction = random.choice(list_directions)
                if direction == 1:
                    changed = puzzle_game.move_empty_tile("UP")
                elif direction == 2:
                    changed = puzzle_game.move_empty_tile("DOWN")
                elif direction == 3:
                    changed = puzzle_game.move_empty_tile("LEFT")
                elif direction == 4:
                    changed = puzzle_game.move_empty_tile("right")
    
    xǁShufflePuzzleLevelMediumǁshuffle__mutmut_mutants : ClassVar[MutantDict] = {
    'xǁShufflePuzzleLevelMediumǁshuffle__mutmut_1': xǁShufflePuzzleLevelMediumǁshuffle__mutmut_1, 
        'xǁShufflePuzzleLevelMediumǁshuffle__mutmut_2': xǁShufflePuzzleLevelMediumǁshuffle__mutmut_2, 
        'xǁShufflePuzzleLevelMediumǁshuffle__mutmut_3': xǁShufflePuzzleLevelMediumǁshuffle__mutmut_3, 
        'xǁShufflePuzzleLevelMediumǁshuffle__mutmut_4': xǁShufflePuzzleLevelMediumǁshuffle__mutmut_4, 
        'xǁShufflePuzzleLevelMediumǁshuffle__mutmut_5': xǁShufflePuzzleLevelMediumǁshuffle__mutmut_5, 
        'xǁShufflePuzzleLevelMediumǁshuffle__mutmut_6': xǁShufflePuzzleLevelMediumǁshuffle__mutmut_6, 
        'xǁShufflePuzzleLevelMediumǁshuffle__mutmut_7': xǁShufflePuzzleLevelMediumǁshuffle__mutmut_7, 
        'xǁShufflePuzzleLevelMediumǁshuffle__mutmut_8': xǁShufflePuzzleLevelMediumǁshuffle__mutmut_8, 
        'xǁShufflePuzzleLevelMediumǁshuffle__mutmut_9': xǁShufflePuzzleLevelMediumǁshuffle__mutmut_9, 
        'xǁShufflePuzzleLevelMediumǁshuffle__mutmut_10': xǁShufflePuzzleLevelMediumǁshuffle__mutmut_10, 
        'xǁShufflePuzzleLevelMediumǁshuffle__mutmut_11': xǁShufflePuzzleLevelMediumǁshuffle__mutmut_11, 
        'xǁShufflePuzzleLevelMediumǁshuffle__mutmut_12': xǁShufflePuzzleLevelMediumǁshuffle__mutmut_12, 
        'xǁShufflePuzzleLevelMediumǁshuffle__mutmut_13': xǁShufflePuzzleLevelMediumǁshuffle__mutmut_13, 
        'xǁShufflePuzzleLevelMediumǁshuffle__mutmut_14': xǁShufflePuzzleLevelMediumǁshuffle__mutmut_14, 
        'xǁShufflePuzzleLevelMediumǁshuffle__mutmut_15': xǁShufflePuzzleLevelMediumǁshuffle__mutmut_15, 
        'xǁShufflePuzzleLevelMediumǁshuffle__mutmut_16': xǁShufflePuzzleLevelMediumǁshuffle__mutmut_16, 
        'xǁShufflePuzzleLevelMediumǁshuffle__mutmut_17': xǁShufflePuzzleLevelMediumǁshuffle__mutmut_17, 
        'xǁShufflePuzzleLevelMediumǁshuffle__mutmut_18': xǁShufflePuzzleLevelMediumǁshuffle__mutmut_18, 
        'xǁShufflePuzzleLevelMediumǁshuffle__mutmut_19': xǁShufflePuzzleLevelMediumǁshuffle__mutmut_19, 
        'xǁShufflePuzzleLevelMediumǁshuffle__mutmut_20': xǁShufflePuzzleLevelMediumǁshuffle__mutmut_20, 
        'xǁShufflePuzzleLevelMediumǁshuffle__mutmut_21': xǁShufflePuzzleLevelMediumǁshuffle__mutmut_21, 
        'xǁShufflePuzzleLevelMediumǁshuffle__mutmut_22': xǁShufflePuzzleLevelMediumǁshuffle__mutmut_22, 
        'xǁShufflePuzzleLevelMediumǁshuffle__mutmut_23': xǁShufflePuzzleLevelMediumǁshuffle__mutmut_23, 
        'xǁShufflePuzzleLevelMediumǁshuffle__mutmut_24': xǁShufflePuzzleLevelMediumǁshuffle__mutmut_24, 
        'xǁShufflePuzzleLevelMediumǁshuffle__mutmut_25': xǁShufflePuzzleLevelMediumǁshuffle__mutmut_25, 
        'xǁShufflePuzzleLevelMediumǁshuffle__mutmut_26': xǁShufflePuzzleLevelMediumǁshuffle__mutmut_26, 
        'xǁShufflePuzzleLevelMediumǁshuffle__mutmut_27': xǁShufflePuzzleLevelMediumǁshuffle__mutmut_27, 
        'xǁShufflePuzzleLevelMediumǁshuffle__mutmut_28': xǁShufflePuzzleLevelMediumǁshuffle__mutmut_28, 
        'xǁShufflePuzzleLevelMediumǁshuffle__mutmut_29': xǁShufflePuzzleLevelMediumǁshuffle__mutmut_29, 
        'xǁShufflePuzzleLevelMediumǁshuffle__mutmut_30': xǁShufflePuzzleLevelMediumǁshuffle__mutmut_30, 
        'xǁShufflePuzzleLevelMediumǁshuffle__mutmut_31': xǁShufflePuzzleLevelMediumǁshuffle__mutmut_31, 
        'xǁShufflePuzzleLevelMediumǁshuffle__mutmut_32': xǁShufflePuzzleLevelMediumǁshuffle__mutmut_32, 
        'xǁShufflePuzzleLevelMediumǁshuffle__mutmut_33': xǁShufflePuzzleLevelMediumǁshuffle__mutmut_33, 
        'xǁShufflePuzzleLevelMediumǁshuffle__mutmut_34': xǁShufflePuzzleLevelMediumǁshuffle__mutmut_34, 
        'xǁShufflePuzzleLevelMediumǁshuffle__mutmut_35': xǁShufflePuzzleLevelMediumǁshuffle__mutmut_35, 
        'xǁShufflePuzzleLevelMediumǁshuffle__mutmut_36': xǁShufflePuzzleLevelMediumǁshuffle__mutmut_36, 
        'xǁShufflePuzzleLevelMediumǁshuffle__mutmut_37': xǁShufflePuzzleLevelMediumǁshuffle__mutmut_37, 
        'xǁShufflePuzzleLevelMediumǁshuffle__mutmut_38': xǁShufflePuzzleLevelMediumǁshuffle__mutmut_38, 
        'xǁShufflePuzzleLevelMediumǁshuffle__mutmut_39': xǁShufflePuzzleLevelMediumǁshuffle__mutmut_39
    }
    
    def shuffle(self, *args, **kwargs):
        result = _mutmut_trampoline(object.__getattribute__(self, "xǁShufflePuzzleLevelMediumǁshuffle__mutmut_orig"), object.__getattribute__(self, "xǁShufflePuzzleLevelMediumǁshuffle__mutmut_mutants"), args, kwargs, self)
        return result 
    
    shuffle.__signature__ = _mutmut_signature(xǁShufflePuzzleLevelMediumǁshuffle__mutmut_orig)
    xǁShufflePuzzleLevelMediumǁshuffle__mutmut_orig.__name__ = 'xǁShufflePuzzleLevelMediumǁshuffle'


class ShufflePuzzleLevelHard:

    def xǁShufflePuzzleLevelHardǁ__init____mutmut_orig(self):
        self.number_of_shuffles = 30;

    def xǁShufflePuzzleLevelHardǁ__init____mutmut_1(self):
        self.number_of_shuffles = None;

    def xǁShufflePuzzleLevelHardǁ__init____mutmut_2(self):
        self.number_of_shuffles = 31;
    
    xǁShufflePuzzleLevelHardǁ__init____mutmut_mutants : ClassVar[MutantDict] = {
    'xǁShufflePuzzleLevelHardǁ__init____mutmut_1': xǁShufflePuzzleLevelHardǁ__init____mutmut_1, 
        'xǁShufflePuzzleLevelHardǁ__init____mutmut_2': xǁShufflePuzzleLevelHardǁ__init____mutmut_2
    }
    
    def __init__(self, *args, **kwargs):
        result = _mutmut_trampoline(object.__getattribute__(self, "xǁShufflePuzzleLevelHardǁ__init____mutmut_orig"), object.__getattribute__(self, "xǁShufflePuzzleLevelHardǁ__init____mutmut_mutants"), args, kwargs, self)
        return result 
    
    __init__.__signature__ = _mutmut_signature(xǁShufflePuzzleLevelHardǁ__init____mutmut_orig)
    xǁShufflePuzzleLevelHardǁ__init____mutmut_orig.__name__ = 'xǁShufflePuzzleLevelHardǁ__init__'

    def xǁShufflePuzzleLevelHardǁshuffle__mutmut_orig (self, puzzle_game):
        list_directions = [1, 2, 3, 4]
        for number in range(0, self.number_of_shuffles):
            changed = False
            while not changed:
                direction = random.choice(list_directions)
                if direction == 1:
                    changed = puzzle_game.move_empty_tile("UP")
                elif direction == 2:
                    changed = puzzle_game.move_empty_tile("DOWN")
                elif direction == 3:
                    changed = puzzle_game.move_empty_tile("LEFT")
                elif direction == 4:
                    changed = puzzle_game.move_empty_tile("RIGHT")

    def xǁShufflePuzzleLevelHardǁshuffle__mutmut_1 (self, puzzle_game):
        list_directions = None
        for number in range(0, self.number_of_shuffles):
            changed = False
            while not changed:
                direction = random.choice(list_directions)
                if direction == 1:
                    changed = puzzle_game.move_empty_tile("UP")
                elif direction == 2:
                    changed = puzzle_game.move_empty_tile("DOWN")
                elif direction == 3:
                    changed = puzzle_game.move_empty_tile("LEFT")
                elif direction == 4:
                    changed = puzzle_game.move_empty_tile("RIGHT")

    def xǁShufflePuzzleLevelHardǁshuffle__mutmut_2 (self, puzzle_game):
        list_directions = [2, 2, 3, 4]
        for number in range(0, self.number_of_shuffles):
            changed = False
            while not changed:
                direction = random.choice(list_directions)
                if direction == 1:
                    changed = puzzle_game.move_empty_tile("UP")
                elif direction == 2:
                    changed = puzzle_game.move_empty_tile("DOWN")
                elif direction == 3:
                    changed = puzzle_game.move_empty_tile("LEFT")
                elif direction == 4:
                    changed = puzzle_game.move_empty_tile("RIGHT")

    def xǁShufflePuzzleLevelHardǁshuffle__mutmut_3 (self, puzzle_game):
        list_directions = [1, 3, 3, 4]
        for number in range(0, self.number_of_shuffles):
            changed = False
            while not changed:
                direction = random.choice(list_directions)
                if direction == 1:
                    changed = puzzle_game.move_empty_tile("UP")
                elif direction == 2:
                    changed = puzzle_game.move_empty_tile("DOWN")
                elif direction == 3:
                    changed = puzzle_game.move_empty_tile("LEFT")
                elif direction == 4:
                    changed = puzzle_game.move_empty_tile("RIGHT")

    def xǁShufflePuzzleLevelHardǁshuffle__mutmut_4 (self, puzzle_game):
        list_directions = [1, 2, 4, 4]
        for number in range(0, self.number_of_shuffles):
            changed = False
            while not changed:
                direction = random.choice(list_directions)
                if direction == 1:
                    changed = puzzle_game.move_empty_tile("UP")
                elif direction == 2:
                    changed = puzzle_game.move_empty_tile("DOWN")
                elif direction == 3:
                    changed = puzzle_game.move_empty_tile("LEFT")
                elif direction == 4:
                    changed = puzzle_game.move_empty_tile("RIGHT")

    def xǁShufflePuzzleLevelHardǁshuffle__mutmut_5 (self, puzzle_game):
        list_directions = [1, 2, 3, 5]
        for number in range(0, self.number_of_shuffles):
            changed = False
            while not changed:
                direction = random.choice(list_directions)
                if direction == 1:
                    changed = puzzle_game.move_empty_tile("UP")
                elif direction == 2:
                    changed = puzzle_game.move_empty_tile("DOWN")
                elif direction == 3:
                    changed = puzzle_game.move_empty_tile("LEFT")
                elif direction == 4:
                    changed = puzzle_game.move_empty_tile("RIGHT")

    def xǁShufflePuzzleLevelHardǁshuffle__mutmut_6 (self, puzzle_game):
        list_directions = [1, 2, 3, 4]
        for number in range(None, self.number_of_shuffles):
            changed = False
            while not changed:
                direction = random.choice(list_directions)
                if direction == 1:
                    changed = puzzle_game.move_empty_tile("UP")
                elif direction == 2:
                    changed = puzzle_game.move_empty_tile("DOWN")
                elif direction == 3:
                    changed = puzzle_game.move_empty_tile("LEFT")
                elif direction == 4:
                    changed = puzzle_game.move_empty_tile("RIGHT")

    def xǁShufflePuzzleLevelHardǁshuffle__mutmut_7 (self, puzzle_game):
        list_directions = [1, 2, 3, 4]
        for number in range(0, None):
            changed = False
            while not changed:
                direction = random.choice(list_directions)
                if direction == 1:
                    changed = puzzle_game.move_empty_tile("UP")
                elif direction == 2:
                    changed = puzzle_game.move_empty_tile("DOWN")
                elif direction == 3:
                    changed = puzzle_game.move_empty_tile("LEFT")
                elif direction == 4:
                    changed = puzzle_game.move_empty_tile("RIGHT")

    def xǁShufflePuzzleLevelHardǁshuffle__mutmut_8 (self, puzzle_game):
        list_directions = [1, 2, 3, 4]
        for number in range(self.number_of_shuffles):
            changed = False
            while not changed:
                direction = random.choice(list_directions)
                if direction == 1:
                    changed = puzzle_game.move_empty_tile("UP")
                elif direction == 2:
                    changed = puzzle_game.move_empty_tile("DOWN")
                elif direction == 3:
                    changed = puzzle_game.move_empty_tile("LEFT")
                elif direction == 4:
                    changed = puzzle_game.move_empty_tile("RIGHT")

    def xǁShufflePuzzleLevelHardǁshuffle__mutmut_9 (self, puzzle_game):
        list_directions = [1, 2, 3, 4]
        for number in range(0, ):
            changed = False
            while not changed:
                direction = random.choice(list_directions)
                if direction == 1:
                    changed = puzzle_game.move_empty_tile("UP")
                elif direction == 2:
                    changed = puzzle_game.move_empty_tile("DOWN")
                elif direction == 3:
                    changed = puzzle_game.move_empty_tile("LEFT")
                elif direction == 4:
                    changed = puzzle_game.move_empty_tile("RIGHT")

    def xǁShufflePuzzleLevelHardǁshuffle__mutmut_10 (self, puzzle_game):
        list_directions = [1, 2, 3, 4]
        for number in range(1, self.number_of_shuffles):
            changed = False
            while not changed:
                direction = random.choice(list_directions)
                if direction == 1:
                    changed = puzzle_game.move_empty_tile("UP")
                elif direction == 2:
                    changed = puzzle_game.move_empty_tile("DOWN")
                elif direction == 3:
                    changed = puzzle_game.move_empty_tile("LEFT")
                elif direction == 4:
                    changed = puzzle_game.move_empty_tile("RIGHT")

    def xǁShufflePuzzleLevelHardǁshuffle__mutmut_11 (self, puzzle_game):
        list_directions = [1, 2, 3, 4]
        for number in range(0, self.number_of_shuffles):
            changed = None
            while not changed:
                direction = random.choice(list_directions)
                if direction == 1:
                    changed = puzzle_game.move_empty_tile("UP")
                elif direction == 2:
                    changed = puzzle_game.move_empty_tile("DOWN")
                elif direction == 3:
                    changed = puzzle_game.move_empty_tile("LEFT")
                elif direction == 4:
                    changed = puzzle_game.move_empty_tile("RIGHT")

    def xǁShufflePuzzleLevelHardǁshuffle__mutmut_12 (self, puzzle_game):
        list_directions = [1, 2, 3, 4]
        for number in range(0, self.number_of_shuffles):
            changed = True
            while not changed:
                direction = random.choice(list_directions)
                if direction == 1:
                    changed = puzzle_game.move_empty_tile("UP")
                elif direction == 2:
                    changed = puzzle_game.move_empty_tile("DOWN")
                elif direction == 3:
                    changed = puzzle_game.move_empty_tile("LEFT")
                elif direction == 4:
                    changed = puzzle_game.move_empty_tile("RIGHT")

    def xǁShufflePuzzleLevelHardǁshuffle__mutmut_13 (self, puzzle_game):
        list_directions = [1, 2, 3, 4]
        for number in range(0, self.number_of_shuffles):
            changed = False
            while changed:
                direction = random.choice(list_directions)
                if direction == 1:
                    changed = puzzle_game.move_empty_tile("UP")
                elif direction == 2:
                    changed = puzzle_game.move_empty_tile("DOWN")
                elif direction == 3:
                    changed = puzzle_game.move_empty_tile("LEFT")
                elif direction == 4:
                    changed = puzzle_game.move_empty_tile("RIGHT")

    def xǁShufflePuzzleLevelHardǁshuffle__mutmut_14 (self, puzzle_game):
        list_directions = [1, 2, 3, 4]
        for number in range(0, self.number_of_shuffles):
            changed = False
            while not changed:
                direction = None
                if direction == 1:
                    changed = puzzle_game.move_empty_tile("UP")
                elif direction == 2:
                    changed = puzzle_game.move_empty_tile("DOWN")
                elif direction == 3:
                    changed = puzzle_game.move_empty_tile("LEFT")
                elif direction == 4:
                    changed = puzzle_game.move_empty_tile("RIGHT")

    def xǁShufflePuzzleLevelHardǁshuffle__mutmut_15 (self, puzzle_game):
        list_directions = [1, 2, 3, 4]
        for number in range(0, self.number_of_shuffles):
            changed = False
            while not changed:
                direction = random.choice(None)
                if direction == 1:
                    changed = puzzle_game.move_empty_tile("UP")
                elif direction == 2:
                    changed = puzzle_game.move_empty_tile("DOWN")
                elif direction == 3:
                    changed = puzzle_game.move_empty_tile("LEFT")
                elif direction == 4:
                    changed = puzzle_game.move_empty_tile("RIGHT")

    def xǁShufflePuzzleLevelHardǁshuffle__mutmut_16 (self, puzzle_game):
        list_directions = [1, 2, 3, 4]
        for number in range(0, self.number_of_shuffles):
            changed = False
            while not changed:
                direction = random.choice(list_directions)
                if direction != 1:
                    changed = puzzle_game.move_empty_tile("UP")
                elif direction == 2:
                    changed = puzzle_game.move_empty_tile("DOWN")
                elif direction == 3:
                    changed = puzzle_game.move_empty_tile("LEFT")
                elif direction == 4:
                    changed = puzzle_game.move_empty_tile("RIGHT")

    def xǁShufflePuzzleLevelHardǁshuffle__mutmut_17 (self, puzzle_game):
        list_directions = [1, 2, 3, 4]
        for number in range(0, self.number_of_shuffles):
            changed = False
            while not changed:
                direction = random.choice(list_directions)
                if direction == 2:
                    changed = puzzle_game.move_empty_tile("UP")
                elif direction == 2:
                    changed = puzzle_game.move_empty_tile("DOWN")
                elif direction == 3:
                    changed = puzzle_game.move_empty_tile("LEFT")
                elif direction == 4:
                    changed = puzzle_game.move_empty_tile("RIGHT")

    def xǁShufflePuzzleLevelHardǁshuffle__mutmut_18 (self, puzzle_game):
        list_directions = [1, 2, 3, 4]
        for number in range(0, self.number_of_shuffles):
            changed = False
            while not changed:
                direction = random.choice(list_directions)
                if direction == 1:
                    changed = None
                elif direction == 2:
                    changed = puzzle_game.move_empty_tile("DOWN")
                elif direction == 3:
                    changed = puzzle_game.move_empty_tile("LEFT")
                elif direction == 4:
                    changed = puzzle_game.move_empty_tile("RIGHT")

    def xǁShufflePuzzleLevelHardǁshuffle__mutmut_19 (self, puzzle_game):
        list_directions = [1, 2, 3, 4]
        for number in range(0, self.number_of_shuffles):
            changed = False
            while not changed:
                direction = random.choice(list_directions)
                if direction == 1:
                    changed = puzzle_game.move_empty_tile(None)
                elif direction == 2:
                    changed = puzzle_game.move_empty_tile("DOWN")
                elif direction == 3:
                    changed = puzzle_game.move_empty_tile("LEFT")
                elif direction == 4:
                    changed = puzzle_game.move_empty_tile("RIGHT")

    def xǁShufflePuzzleLevelHardǁshuffle__mutmut_20 (self, puzzle_game):
        list_directions = [1, 2, 3, 4]
        for number in range(0, self.number_of_shuffles):
            changed = False
            while not changed:
                direction = random.choice(list_directions)
                if direction == 1:
                    changed = puzzle_game.move_empty_tile("XXUPXX")
                elif direction == 2:
                    changed = puzzle_game.move_empty_tile("DOWN")
                elif direction == 3:
                    changed = puzzle_game.move_empty_tile("LEFT")
                elif direction == 4:
                    changed = puzzle_game.move_empty_tile("RIGHT")

    def xǁShufflePuzzleLevelHardǁshuffle__mutmut_21 (self, puzzle_game):
        list_directions = [1, 2, 3, 4]
        for number in range(0, self.number_of_shuffles):
            changed = False
            while not changed:
                direction = random.choice(list_directions)
                if direction == 1:
                    changed = puzzle_game.move_empty_tile("up")
                elif direction == 2:
                    changed = puzzle_game.move_empty_tile("DOWN")
                elif direction == 3:
                    changed = puzzle_game.move_empty_tile("LEFT")
                elif direction == 4:
                    changed = puzzle_game.move_empty_tile("RIGHT")

    def xǁShufflePuzzleLevelHardǁshuffle__mutmut_22 (self, puzzle_game):
        list_directions = [1, 2, 3, 4]
        for number in range(0, self.number_of_shuffles):
            changed = False
            while not changed:
                direction = random.choice(list_directions)
                if direction == 1:
                    changed = puzzle_game.move_empty_tile("UP")
                elif direction != 2:
                    changed = puzzle_game.move_empty_tile("DOWN")
                elif direction == 3:
                    changed = puzzle_game.move_empty_tile("LEFT")
                elif direction == 4:
                    changed = puzzle_game.move_empty_tile("RIGHT")

    def xǁShufflePuzzleLevelHardǁshuffle__mutmut_23 (self, puzzle_game):
        list_directions = [1, 2, 3, 4]
        for number in range(0, self.number_of_shuffles):
            changed = False
            while not changed:
                direction = random.choice(list_directions)
                if direction == 1:
                    changed = puzzle_game.move_empty_tile("UP")
                elif direction == 3:
                    changed = puzzle_game.move_empty_tile("DOWN")
                elif direction == 3:
                    changed = puzzle_game.move_empty_tile("LEFT")
                elif direction == 4:
                    changed = puzzle_game.move_empty_tile("RIGHT")

    def xǁShufflePuzzleLevelHardǁshuffle__mutmut_24 (self, puzzle_game):
        list_directions = [1, 2, 3, 4]
        for number in range(0, self.number_of_shuffles):
            changed = False
            while not changed:
                direction = random.choice(list_directions)
                if direction == 1:
                    changed = puzzle_game.move_empty_tile("UP")
                elif direction == 2:
                    changed = None
                elif direction == 3:
                    changed = puzzle_game.move_empty_tile("LEFT")
                elif direction == 4:
                    changed = puzzle_game.move_empty_tile("RIGHT")

    def xǁShufflePuzzleLevelHardǁshuffle__mutmut_25 (self, puzzle_game):
        list_directions = [1, 2, 3, 4]
        for number in range(0, self.number_of_shuffles):
            changed = False
            while not changed:
                direction = random.choice(list_directions)
                if direction == 1:
                    changed = puzzle_game.move_empty_tile("UP")
                elif direction == 2:
                    changed = puzzle_game.move_empty_tile(None)
                elif direction == 3:
                    changed = puzzle_game.move_empty_tile("LEFT")
                elif direction == 4:
                    changed = puzzle_game.move_empty_tile("RIGHT")

    def xǁShufflePuzzleLevelHardǁshuffle__mutmut_26 (self, puzzle_game):
        list_directions = [1, 2, 3, 4]
        for number in range(0, self.number_of_shuffles):
            changed = False
            while not changed:
                direction = random.choice(list_directions)
                if direction == 1:
                    changed = puzzle_game.move_empty_tile("UP")
                elif direction == 2:
                    changed = puzzle_game.move_empty_tile("XXDOWNXX")
                elif direction == 3:
                    changed = puzzle_game.move_empty_tile("LEFT")
                elif direction == 4:
                    changed = puzzle_game.move_empty_tile("RIGHT")

    def xǁShufflePuzzleLevelHardǁshuffle__mutmut_27 (self, puzzle_game):
        list_directions = [1, 2, 3, 4]
        for number in range(0, self.number_of_shuffles):
            changed = False
            while not changed:
                direction = random.choice(list_directions)
                if direction == 1:
                    changed = puzzle_game.move_empty_tile("UP")
                elif direction == 2:
                    changed = puzzle_game.move_empty_tile("down")
                elif direction == 3:
                    changed = puzzle_game.move_empty_tile("LEFT")
                elif direction == 4:
                    changed = puzzle_game.move_empty_tile("RIGHT")

    def xǁShufflePuzzleLevelHardǁshuffle__mutmut_28 (self, puzzle_game):
        list_directions = [1, 2, 3, 4]
        for number in range(0, self.number_of_shuffles):
            changed = False
            while not changed:
                direction = random.choice(list_directions)
                if direction == 1:
                    changed = puzzle_game.move_empty_tile("UP")
                elif direction == 2:
                    changed = puzzle_game.move_empty_tile("DOWN")
                elif direction != 3:
                    changed = puzzle_game.move_empty_tile("LEFT")
                elif direction == 4:
                    changed = puzzle_game.move_empty_tile("RIGHT")

    def xǁShufflePuzzleLevelHardǁshuffle__mutmut_29 (self, puzzle_game):
        list_directions = [1, 2, 3, 4]
        for number in range(0, self.number_of_shuffles):
            changed = False
            while not changed:
                direction = random.choice(list_directions)
                if direction == 1:
                    changed = puzzle_game.move_empty_tile("UP")
                elif direction == 2:
                    changed = puzzle_game.move_empty_tile("DOWN")
                elif direction == 4:
                    changed = puzzle_game.move_empty_tile("LEFT")
                elif direction == 4:
                    changed = puzzle_game.move_empty_tile("RIGHT")

    def xǁShufflePuzzleLevelHardǁshuffle__mutmut_30 (self, puzzle_game):
        list_directions = [1, 2, 3, 4]
        for number in range(0, self.number_of_shuffles):
            changed = False
            while not changed:
                direction = random.choice(list_directions)
                if direction == 1:
                    changed = puzzle_game.move_empty_tile("UP")
                elif direction == 2:
                    changed = puzzle_game.move_empty_tile("DOWN")
                elif direction == 3:
                    changed = None
                elif direction == 4:
                    changed = puzzle_game.move_empty_tile("RIGHT")

    def xǁShufflePuzzleLevelHardǁshuffle__mutmut_31 (self, puzzle_game):
        list_directions = [1, 2, 3, 4]
        for number in range(0, self.number_of_shuffles):
            changed = False
            while not changed:
                direction = random.choice(list_directions)
                if direction == 1:
                    changed = puzzle_game.move_empty_tile("UP")
                elif direction == 2:
                    changed = puzzle_game.move_empty_tile("DOWN")
                elif direction == 3:
                    changed = puzzle_game.move_empty_tile(None)
                elif direction == 4:
                    changed = puzzle_game.move_empty_tile("RIGHT")

    def xǁShufflePuzzleLevelHardǁshuffle__mutmut_32 (self, puzzle_game):
        list_directions = [1, 2, 3, 4]
        for number in range(0, self.number_of_shuffles):
            changed = False
            while not changed:
                direction = random.choice(list_directions)
                if direction == 1:
                    changed = puzzle_game.move_empty_tile("UP")
                elif direction == 2:
                    changed = puzzle_game.move_empty_tile("DOWN")
                elif direction == 3:
                    changed = puzzle_game.move_empty_tile("XXLEFTXX")
                elif direction == 4:
                    changed = puzzle_game.move_empty_tile("RIGHT")

    def xǁShufflePuzzleLevelHardǁshuffle__mutmut_33 (self, puzzle_game):
        list_directions = [1, 2, 3, 4]
        for number in range(0, self.number_of_shuffles):
            changed = False
            while not changed:
                direction = random.choice(list_directions)
                if direction == 1:
                    changed = puzzle_game.move_empty_tile("UP")
                elif direction == 2:
                    changed = puzzle_game.move_empty_tile("DOWN")
                elif direction == 3:
                    changed = puzzle_game.move_empty_tile("left")
                elif direction == 4:
                    changed = puzzle_game.move_empty_tile("RIGHT")

    def xǁShufflePuzzleLevelHardǁshuffle__mutmut_34 (self, puzzle_game):
        list_directions = [1, 2, 3, 4]
        for number in range(0, self.number_of_shuffles):
            changed = False
            while not changed:
                direction = random.choice(list_directions)
                if direction == 1:
                    changed = puzzle_game.move_empty_tile("UP")
                elif direction == 2:
                    changed = puzzle_game.move_empty_tile("DOWN")
                elif direction == 3:
                    changed = puzzle_game.move_empty_tile("LEFT")
                elif direction != 4:
                    changed = puzzle_game.move_empty_tile("RIGHT")

    def xǁShufflePuzzleLevelHardǁshuffle__mutmut_35 (self, puzzle_game):
        list_directions = [1, 2, 3, 4]
        for number in range(0, self.number_of_shuffles):
            changed = False
            while not changed:
                direction = random.choice(list_directions)
                if direction == 1:
                    changed = puzzle_game.move_empty_tile("UP")
                elif direction == 2:
                    changed = puzzle_game.move_empty_tile("DOWN")
                elif direction == 3:
                    changed = puzzle_game.move_empty_tile("LEFT")
                elif direction == 5:
                    changed = puzzle_game.move_empty_tile("RIGHT")

    def xǁShufflePuzzleLevelHardǁshuffle__mutmut_36 (self, puzzle_game):
        list_directions = [1, 2, 3, 4]
        for number in range(0, self.number_of_shuffles):
            changed = False
            while not changed:
                direction = random.choice(list_directions)
                if direction == 1:
                    changed = puzzle_game.move_empty_tile("UP")
                elif direction == 2:
                    changed = puzzle_game.move_empty_tile("DOWN")
                elif direction == 3:
                    changed = puzzle_game.move_empty_tile("LEFT")
                elif direction == 4:
                    changed = None

    def xǁShufflePuzzleLevelHardǁshuffle__mutmut_37 (self, puzzle_game):
        list_directions = [1, 2, 3, 4]
        for number in range(0, self.number_of_shuffles):
            changed = False
            while not changed:
                direction = random.choice(list_directions)
                if direction == 1:
                    changed = puzzle_game.move_empty_tile("UP")
                elif direction == 2:
                    changed = puzzle_game.move_empty_tile("DOWN")
                elif direction == 3:
                    changed = puzzle_game.move_empty_tile("LEFT")
                elif direction == 4:
                    changed = puzzle_game.move_empty_tile(None)

    def xǁShufflePuzzleLevelHardǁshuffle__mutmut_38 (self, puzzle_game):
        list_directions = [1, 2, 3, 4]
        for number in range(0, self.number_of_shuffles):
            changed = False
            while not changed:
                direction = random.choice(list_directions)
                if direction == 1:
                    changed = puzzle_game.move_empty_tile("UP")
                elif direction == 2:
                    changed = puzzle_game.move_empty_tile("DOWN")
                elif direction == 3:
                    changed = puzzle_game.move_empty_tile("LEFT")
                elif direction == 4:
                    changed = puzzle_game.move_empty_tile("XXRIGHTXX")

    def xǁShufflePuzzleLevelHardǁshuffle__mutmut_39 (self, puzzle_game):
        list_directions = [1, 2, 3, 4]
        for number in range(0, self.number_of_shuffles):
            changed = False
            while not changed:
                direction = random.choice(list_directions)
                if direction == 1:
                    changed = puzzle_game.move_empty_tile("UP")
                elif direction == 2:
                    changed = puzzle_game.move_empty_tile("DOWN")
                elif direction == 3:
                    changed = puzzle_game.move_empty_tile("LEFT")
                elif direction == 4:
                    changed = puzzle_game.move_empty_tile("right")
    
    xǁShufflePuzzleLevelHardǁshuffle__mutmut_mutants : ClassVar[MutantDict] = {
    'xǁShufflePuzzleLevelHardǁshuffle__mutmut_1': xǁShufflePuzzleLevelHardǁshuffle__mutmut_1, 
        'xǁShufflePuzzleLevelHardǁshuffle__mutmut_2': xǁShufflePuzzleLevelHardǁshuffle__mutmut_2, 
        'xǁShufflePuzzleLevelHardǁshuffle__mutmut_3': xǁShufflePuzzleLevelHardǁshuffle__mutmut_3, 
        'xǁShufflePuzzleLevelHardǁshuffle__mutmut_4': xǁShufflePuzzleLevelHardǁshuffle__mutmut_4, 
        'xǁShufflePuzzleLevelHardǁshuffle__mutmut_5': xǁShufflePuzzleLevelHardǁshuffle__mutmut_5, 
        'xǁShufflePuzzleLevelHardǁshuffle__mutmut_6': xǁShufflePuzzleLevelHardǁshuffle__mutmut_6, 
        'xǁShufflePuzzleLevelHardǁshuffle__mutmut_7': xǁShufflePuzzleLevelHardǁshuffle__mutmut_7, 
        'xǁShufflePuzzleLevelHardǁshuffle__mutmut_8': xǁShufflePuzzleLevelHardǁshuffle__mutmut_8, 
        'xǁShufflePuzzleLevelHardǁshuffle__mutmut_9': xǁShufflePuzzleLevelHardǁshuffle__mutmut_9, 
        'xǁShufflePuzzleLevelHardǁshuffle__mutmut_10': xǁShufflePuzzleLevelHardǁshuffle__mutmut_10, 
        'xǁShufflePuzzleLevelHardǁshuffle__mutmut_11': xǁShufflePuzzleLevelHardǁshuffle__mutmut_11, 
        'xǁShufflePuzzleLevelHardǁshuffle__mutmut_12': xǁShufflePuzzleLevelHardǁshuffle__mutmut_12, 
        'xǁShufflePuzzleLevelHardǁshuffle__mutmut_13': xǁShufflePuzzleLevelHardǁshuffle__mutmut_13, 
        'xǁShufflePuzzleLevelHardǁshuffle__mutmut_14': xǁShufflePuzzleLevelHardǁshuffle__mutmut_14, 
        'xǁShufflePuzzleLevelHardǁshuffle__mutmut_15': xǁShufflePuzzleLevelHardǁshuffle__mutmut_15, 
        'xǁShufflePuzzleLevelHardǁshuffle__mutmut_16': xǁShufflePuzzleLevelHardǁshuffle__mutmut_16, 
        'xǁShufflePuzzleLevelHardǁshuffle__mutmut_17': xǁShufflePuzzleLevelHardǁshuffle__mutmut_17, 
        'xǁShufflePuzzleLevelHardǁshuffle__mutmut_18': xǁShufflePuzzleLevelHardǁshuffle__mutmut_18, 
        'xǁShufflePuzzleLevelHardǁshuffle__mutmut_19': xǁShufflePuzzleLevelHardǁshuffle__mutmut_19, 
        'xǁShufflePuzzleLevelHardǁshuffle__mutmut_20': xǁShufflePuzzleLevelHardǁshuffle__mutmut_20, 
        'xǁShufflePuzzleLevelHardǁshuffle__mutmut_21': xǁShufflePuzzleLevelHardǁshuffle__mutmut_21, 
        'xǁShufflePuzzleLevelHardǁshuffle__mutmut_22': xǁShufflePuzzleLevelHardǁshuffle__mutmut_22, 
        'xǁShufflePuzzleLevelHardǁshuffle__mutmut_23': xǁShufflePuzzleLevelHardǁshuffle__mutmut_23, 
        'xǁShufflePuzzleLevelHardǁshuffle__mutmut_24': xǁShufflePuzzleLevelHardǁshuffle__mutmut_24, 
        'xǁShufflePuzzleLevelHardǁshuffle__mutmut_25': xǁShufflePuzzleLevelHardǁshuffle__mutmut_25, 
        'xǁShufflePuzzleLevelHardǁshuffle__mutmut_26': xǁShufflePuzzleLevelHardǁshuffle__mutmut_26, 
        'xǁShufflePuzzleLevelHardǁshuffle__mutmut_27': xǁShufflePuzzleLevelHardǁshuffle__mutmut_27, 
        'xǁShufflePuzzleLevelHardǁshuffle__mutmut_28': xǁShufflePuzzleLevelHardǁshuffle__mutmut_28, 
        'xǁShufflePuzzleLevelHardǁshuffle__mutmut_29': xǁShufflePuzzleLevelHardǁshuffle__mutmut_29, 
        'xǁShufflePuzzleLevelHardǁshuffle__mutmut_30': xǁShufflePuzzleLevelHardǁshuffle__mutmut_30, 
        'xǁShufflePuzzleLevelHardǁshuffle__mutmut_31': xǁShufflePuzzleLevelHardǁshuffle__mutmut_31, 
        'xǁShufflePuzzleLevelHardǁshuffle__mutmut_32': xǁShufflePuzzleLevelHardǁshuffle__mutmut_32, 
        'xǁShufflePuzzleLevelHardǁshuffle__mutmut_33': xǁShufflePuzzleLevelHardǁshuffle__mutmut_33, 
        'xǁShufflePuzzleLevelHardǁshuffle__mutmut_34': xǁShufflePuzzleLevelHardǁshuffle__mutmut_34, 
        'xǁShufflePuzzleLevelHardǁshuffle__mutmut_35': xǁShufflePuzzleLevelHardǁshuffle__mutmut_35, 
        'xǁShufflePuzzleLevelHardǁshuffle__mutmut_36': xǁShufflePuzzleLevelHardǁshuffle__mutmut_36, 
        'xǁShufflePuzzleLevelHardǁshuffle__mutmut_37': xǁShufflePuzzleLevelHardǁshuffle__mutmut_37, 
        'xǁShufflePuzzleLevelHardǁshuffle__mutmut_38': xǁShufflePuzzleLevelHardǁshuffle__mutmut_38, 
        'xǁShufflePuzzleLevelHardǁshuffle__mutmut_39': xǁShufflePuzzleLevelHardǁshuffle__mutmut_39
    }
    
    def shuffle(self, *args, **kwargs):
        result = _mutmut_trampoline(object.__getattribute__(self, "xǁShufflePuzzleLevelHardǁshuffle__mutmut_orig"), object.__getattribute__(self, "xǁShufflePuzzleLevelHardǁshuffle__mutmut_mutants"), args, kwargs, self)
        return result 
    
    shuffle.__signature__ = _mutmut_signature(xǁShufflePuzzleLevelHardǁshuffle__mutmut_orig)
    xǁShufflePuzzleLevelHardǁshuffle__mutmut_orig.__name__ = 'xǁShufflePuzzleLevelHardǁshuffle'