from invalid_position_exception import InvalidPositionException
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

class Board:  # Board comeca com a linha 1 e com a coluna 1

    def xǁBoardǁ__init____mutmut_orig(self, number_of_lines, number_of_columns):
        self.__number_of_lines = number_of_lines
        self.__number_of_columns = number_of_columns
        self.grid = []
        for line in range(0, number_of_lines):
            self.grid.append([None] * number_of_columns)

    def xǁBoardǁ__init____mutmut_1(self, number_of_lines, number_of_columns):
        self.__number_of_lines = None
        self.__number_of_columns = number_of_columns
        self.grid = []
        for line in range(0, number_of_lines):
            self.grid.append([None] * number_of_columns)

    def xǁBoardǁ__init____mutmut_2(self, number_of_lines, number_of_columns):
        self.__number_of_lines = number_of_lines
        self.__number_of_columns = None
        self.grid = []
        for line in range(0, number_of_lines):
            self.grid.append([None] * number_of_columns)

    def xǁBoardǁ__init____mutmut_3(self, number_of_lines, number_of_columns):
        self.__number_of_lines = number_of_lines
        self.__number_of_columns = number_of_columns
        self.grid = None
        for line in range(0, number_of_lines):
            self.grid.append([None] * number_of_columns)

    def xǁBoardǁ__init____mutmut_4(self, number_of_lines, number_of_columns):
        self.__number_of_lines = number_of_lines
        self.__number_of_columns = number_of_columns
        self.grid = []
        for line in range(None, number_of_lines):
            self.grid.append([None] * number_of_columns)

    def xǁBoardǁ__init____mutmut_5(self, number_of_lines, number_of_columns):
        self.__number_of_lines = number_of_lines
        self.__number_of_columns = number_of_columns
        self.grid = []
        for line in range(0, None):
            self.grid.append([None] * number_of_columns)

    def xǁBoardǁ__init____mutmut_6(self, number_of_lines, number_of_columns):
        self.__number_of_lines = number_of_lines
        self.__number_of_columns = number_of_columns
        self.grid = []
        for line in range(number_of_lines):
            self.grid.append([None] * number_of_columns)

    def xǁBoardǁ__init____mutmut_7(self, number_of_lines, number_of_columns):
        self.__number_of_lines = number_of_lines
        self.__number_of_columns = number_of_columns
        self.grid = []
        for line in range(0, ):
            self.grid.append([None] * number_of_columns)

    def xǁBoardǁ__init____mutmut_8(self, number_of_lines, number_of_columns):
        self.__number_of_lines = number_of_lines
        self.__number_of_columns = number_of_columns
        self.grid = []
        for line in range(1, number_of_lines):
            self.grid.append([None] * number_of_columns)

    def xǁBoardǁ__init____mutmut_9(self, number_of_lines, number_of_columns):
        self.__number_of_lines = number_of_lines
        self.__number_of_columns = number_of_columns
        self.grid = []
        for line in range(0, number_of_lines):
            self.grid.append(None)

    def xǁBoardǁ__init____mutmut_10(self, number_of_lines, number_of_columns):
        self.__number_of_lines = number_of_lines
        self.__number_of_columns = number_of_columns
        self.grid = []
        for line in range(0, number_of_lines):
            self.grid.append([None] / number_of_columns)
    
    xǁBoardǁ__init____mutmut_mutants : ClassVar[MutantDict] = {
    'xǁBoardǁ__init____mutmut_1': xǁBoardǁ__init____mutmut_1, 
        'xǁBoardǁ__init____mutmut_2': xǁBoardǁ__init____mutmut_2, 
        'xǁBoardǁ__init____mutmut_3': xǁBoardǁ__init____mutmut_3, 
        'xǁBoardǁ__init____mutmut_4': xǁBoardǁ__init____mutmut_4, 
        'xǁBoardǁ__init____mutmut_5': xǁBoardǁ__init____mutmut_5, 
        'xǁBoardǁ__init____mutmut_6': xǁBoardǁ__init____mutmut_6, 
        'xǁBoardǁ__init____mutmut_7': xǁBoardǁ__init____mutmut_7, 
        'xǁBoardǁ__init____mutmut_8': xǁBoardǁ__init____mutmut_8, 
        'xǁBoardǁ__init____mutmut_9': xǁBoardǁ__init____mutmut_9, 
        'xǁBoardǁ__init____mutmut_10': xǁBoardǁ__init____mutmut_10
    }
    
    def __init__(self, *args, **kwargs):
        result = _mutmut_trampoline(object.__getattribute__(self, "xǁBoardǁ__init____mutmut_orig"), object.__getattribute__(self, "xǁBoardǁ__init____mutmut_mutants"), args, kwargs, self)
        return result 
    
    __init__.__signature__ = _mutmut_signature(xǁBoardǁ__init____mutmut_orig)
    xǁBoardǁ__init____mutmut_orig.__name__ = 'xǁBoardǁ__init__'

    @property
    def number_of_lines(self):
        return self.__number_of_lines

    @property
    def number_of_columns(self):
        return self.__number_of_columns

    def xǁBoardǁput_tile__mutmut_orig(self, tile, line, column):
        if self.is_inside_the_board(line, column):
            self.grid[line-1][column-1] = tile

    def xǁBoardǁput_tile__mutmut_1(self, tile, line, column):
        if self.is_inside_the_board(None, column):
            self.grid[line-1][column-1] = tile

    def xǁBoardǁput_tile__mutmut_2(self, tile, line, column):
        if self.is_inside_the_board(line, None):
            self.grid[line-1][column-1] = tile

    def xǁBoardǁput_tile__mutmut_3(self, tile, line, column):
        if self.is_inside_the_board(column):
            self.grid[line-1][column-1] = tile

    def xǁBoardǁput_tile__mutmut_4(self, tile, line, column):
        if self.is_inside_the_board(line, ):
            self.grid[line-1][column-1] = tile

    def xǁBoardǁput_tile__mutmut_5(self, tile, line, column):
        if self.is_inside_the_board(line, column):
            self.grid[line-1][column-1] = None

    def xǁBoardǁput_tile__mutmut_6(self, tile, line, column):
        if self.is_inside_the_board(line, column):
            self.grid[line + 1][column-1] = tile

    def xǁBoardǁput_tile__mutmut_7(self, tile, line, column):
        if self.is_inside_the_board(line, column):
            self.grid[line-2][column-1] = tile

    def xǁBoardǁput_tile__mutmut_8(self, tile, line, column):
        if self.is_inside_the_board(line, column):
            self.grid[line-1][column + 1] = tile

    def xǁBoardǁput_tile__mutmut_9(self, tile, line, column):
        if self.is_inside_the_board(line, column):
            self.grid[line-1][column-2] = tile
    
    xǁBoardǁput_tile__mutmut_mutants : ClassVar[MutantDict] = {
    'xǁBoardǁput_tile__mutmut_1': xǁBoardǁput_tile__mutmut_1, 
        'xǁBoardǁput_tile__mutmut_2': xǁBoardǁput_tile__mutmut_2, 
        'xǁBoardǁput_tile__mutmut_3': xǁBoardǁput_tile__mutmut_3, 
        'xǁBoardǁput_tile__mutmut_4': xǁBoardǁput_tile__mutmut_4, 
        'xǁBoardǁput_tile__mutmut_5': xǁBoardǁput_tile__mutmut_5, 
        'xǁBoardǁput_tile__mutmut_6': xǁBoardǁput_tile__mutmut_6, 
        'xǁBoardǁput_tile__mutmut_7': xǁBoardǁput_tile__mutmut_7, 
        'xǁBoardǁput_tile__mutmut_8': xǁBoardǁput_tile__mutmut_8, 
        'xǁBoardǁput_tile__mutmut_9': xǁBoardǁput_tile__mutmut_9
    }
    
    def put_tile(self, *args, **kwargs):
        result = _mutmut_trampoline(object.__getattribute__(self, "xǁBoardǁput_tile__mutmut_orig"), object.__getattribute__(self, "xǁBoardǁput_tile__mutmut_mutants"), args, kwargs, self)
        return result 
    
    put_tile.__signature__ = _mutmut_signature(xǁBoardǁput_tile__mutmut_orig)
    xǁBoardǁput_tile__mutmut_orig.__name__ = 'xǁBoardǁput_tile'

    def xǁBoardǁget_tile__mutmut_orig(self, line, column):
        if self.is_inside_the_board(line, column):
            return self.grid[line-1][column-1]
        return None

    def xǁBoardǁget_tile__mutmut_1(self, line, column):
        if self.is_inside_the_board(None, column):
            return self.grid[line-1][column-1]
        return None

    def xǁBoardǁget_tile__mutmut_2(self, line, column):
        if self.is_inside_the_board(line, None):
            return self.grid[line-1][column-1]
        return None

    def xǁBoardǁget_tile__mutmut_3(self, line, column):
        if self.is_inside_the_board(column):
            return self.grid[line-1][column-1]
        return None

    def xǁBoardǁget_tile__mutmut_4(self, line, column):
        if self.is_inside_the_board(line, ):
            return self.grid[line-1][column-1]
        return None

    def xǁBoardǁget_tile__mutmut_5(self, line, column):
        if self.is_inside_the_board(line, column):
            return self.grid[line + 1][column-1]
        return None

    def xǁBoardǁget_tile__mutmut_6(self, line, column):
        if self.is_inside_the_board(line, column):
            return self.grid[line-2][column-1]
        return None

    def xǁBoardǁget_tile__mutmut_7(self, line, column):
        if self.is_inside_the_board(line, column):
            return self.grid[line-1][column + 1]
        return None

    def xǁBoardǁget_tile__mutmut_8(self, line, column):
        if self.is_inside_the_board(line, column):
            return self.grid[line-1][column-2]
        return None
    
    xǁBoardǁget_tile__mutmut_mutants : ClassVar[MutantDict] = {
    'xǁBoardǁget_tile__mutmut_1': xǁBoardǁget_tile__mutmut_1, 
        'xǁBoardǁget_tile__mutmut_2': xǁBoardǁget_tile__mutmut_2, 
        'xǁBoardǁget_tile__mutmut_3': xǁBoardǁget_tile__mutmut_3, 
        'xǁBoardǁget_tile__mutmut_4': xǁBoardǁget_tile__mutmut_4, 
        'xǁBoardǁget_tile__mutmut_5': xǁBoardǁget_tile__mutmut_5, 
        'xǁBoardǁget_tile__mutmut_6': xǁBoardǁget_tile__mutmut_6, 
        'xǁBoardǁget_tile__mutmut_7': xǁBoardǁget_tile__mutmut_7, 
        'xǁBoardǁget_tile__mutmut_8': xǁBoardǁget_tile__mutmut_8
    }
    
    def get_tile(self, *args, **kwargs):
        result = _mutmut_trampoline(object.__getattribute__(self, "xǁBoardǁget_tile__mutmut_orig"), object.__getattribute__(self, "xǁBoardǁget_tile__mutmut_mutants"), args, kwargs, self)
        return result 
    
    get_tile.__signature__ = _mutmut_signature(xǁBoardǁget_tile__mutmut_orig)
    xǁBoardǁget_tile__mutmut_orig.__name__ = 'xǁBoardǁget_tile'

    def xǁBoardǁis_inside_the_board__mutmut_orig(self, line, column):
        return line > 0 and line <= self.__number_of_lines and column > 0 and column <= self.number_of_columns

    def xǁBoardǁis_inside_the_board__mutmut_1(self, line, column):
        return line > 0 and line <= self.__number_of_lines and column > 0 or column <= self.number_of_columns

    def xǁBoardǁis_inside_the_board__mutmut_2(self, line, column):
        return line > 0 and line <= self.__number_of_lines or column > 0 and column <= self.number_of_columns

    def xǁBoardǁis_inside_the_board__mutmut_3(self, line, column):
        return line > 0 or line <= self.__number_of_lines and column > 0 and column <= self.number_of_columns

    def xǁBoardǁis_inside_the_board__mutmut_4(self, line, column):
        return line >= 0 and line <= self.__number_of_lines and column > 0 and column <= self.number_of_columns

    def xǁBoardǁis_inside_the_board__mutmut_5(self, line, column):
        return line > 1 and line <= self.__number_of_lines and column > 0 and column <= self.number_of_columns

    def xǁBoardǁis_inside_the_board__mutmut_6(self, line, column):
        return line > 0 and line < self.__number_of_lines and column > 0 and column <= self.number_of_columns

    def xǁBoardǁis_inside_the_board__mutmut_7(self, line, column):
        return line > 0 and line <= self.__number_of_lines and column >= 0 and column <= self.number_of_columns

    def xǁBoardǁis_inside_the_board__mutmut_8(self, line, column):
        return line > 0 and line <= self.__number_of_lines and column > 1 and column <= self.number_of_columns

    def xǁBoardǁis_inside_the_board__mutmut_9(self, line, column):
        return line > 0 and line <= self.__number_of_lines and column > 0 and column < self.number_of_columns
    
    xǁBoardǁis_inside_the_board__mutmut_mutants : ClassVar[MutantDict] = {
    'xǁBoardǁis_inside_the_board__mutmut_1': xǁBoardǁis_inside_the_board__mutmut_1, 
        'xǁBoardǁis_inside_the_board__mutmut_2': xǁBoardǁis_inside_the_board__mutmut_2, 
        'xǁBoardǁis_inside_the_board__mutmut_3': xǁBoardǁis_inside_the_board__mutmut_3, 
        'xǁBoardǁis_inside_the_board__mutmut_4': xǁBoardǁis_inside_the_board__mutmut_4, 
        'xǁBoardǁis_inside_the_board__mutmut_5': xǁBoardǁis_inside_the_board__mutmut_5, 
        'xǁBoardǁis_inside_the_board__mutmut_6': xǁBoardǁis_inside_the_board__mutmut_6, 
        'xǁBoardǁis_inside_the_board__mutmut_7': xǁBoardǁis_inside_the_board__mutmut_7, 
        'xǁBoardǁis_inside_the_board__mutmut_8': xǁBoardǁis_inside_the_board__mutmut_8, 
        'xǁBoardǁis_inside_the_board__mutmut_9': xǁBoardǁis_inside_the_board__mutmut_9
    }
    
    def is_inside_the_board(self, *args, **kwargs):
        result = _mutmut_trampoline(object.__getattribute__(self, "xǁBoardǁis_inside_the_board__mutmut_orig"), object.__getattribute__(self, "xǁBoardǁis_inside_the_board__mutmut_mutants"), args, kwargs, self)
        return result 
    
    is_inside_the_board.__signature__ = _mutmut_signature(xǁBoardǁis_inside_the_board__mutmut_orig)
    xǁBoardǁis_inside_the_board__mutmut_orig.__name__ = 'xǁBoardǁis_inside_the_board'

    def xǁBoardǁchange_tiles_in_positions__mutmut_orig(self, line1, column1, line2, column2):
        if self.is_inside_the_board(line1, column1) and self.is_inside_the_board(line2, column2):
            tile1 = self.get_tile(line1, column1)
            tile2 = self.get_tile(line2, column2)
            self.put_tile(tile2, line1, column1)
            self.put_tile(tile1, line2, column2)
        else:
            raise InvalidPositionException()

    def xǁBoardǁchange_tiles_in_positions__mutmut_1(self, line1, column1, line2, column2):
        if self.is_inside_the_board(line1, column1) or self.is_inside_the_board(line2, column2):
            tile1 = self.get_tile(line1, column1)
            tile2 = self.get_tile(line2, column2)
            self.put_tile(tile2, line1, column1)
            self.put_tile(tile1, line2, column2)
        else:
            raise InvalidPositionException()

    def xǁBoardǁchange_tiles_in_positions__mutmut_2(self, line1, column1, line2, column2):
        if self.is_inside_the_board(None, column1) and self.is_inside_the_board(line2, column2):
            tile1 = self.get_tile(line1, column1)
            tile2 = self.get_tile(line2, column2)
            self.put_tile(tile2, line1, column1)
            self.put_tile(tile1, line2, column2)
        else:
            raise InvalidPositionException()

    def xǁBoardǁchange_tiles_in_positions__mutmut_3(self, line1, column1, line2, column2):
        if self.is_inside_the_board(line1, None) and self.is_inside_the_board(line2, column2):
            tile1 = self.get_tile(line1, column1)
            tile2 = self.get_tile(line2, column2)
            self.put_tile(tile2, line1, column1)
            self.put_tile(tile1, line2, column2)
        else:
            raise InvalidPositionException()

    def xǁBoardǁchange_tiles_in_positions__mutmut_4(self, line1, column1, line2, column2):
        if self.is_inside_the_board(column1) and self.is_inside_the_board(line2, column2):
            tile1 = self.get_tile(line1, column1)
            tile2 = self.get_tile(line2, column2)
            self.put_tile(tile2, line1, column1)
            self.put_tile(tile1, line2, column2)
        else:
            raise InvalidPositionException()

    def xǁBoardǁchange_tiles_in_positions__mutmut_5(self, line1, column1, line2, column2):
        if self.is_inside_the_board(line1, ) and self.is_inside_the_board(line2, column2):
            tile1 = self.get_tile(line1, column1)
            tile2 = self.get_tile(line2, column2)
            self.put_tile(tile2, line1, column1)
            self.put_tile(tile1, line2, column2)
        else:
            raise InvalidPositionException()

    def xǁBoardǁchange_tiles_in_positions__mutmut_6(self, line1, column1, line2, column2):
        if self.is_inside_the_board(line1, column1) and self.is_inside_the_board(None, column2):
            tile1 = self.get_tile(line1, column1)
            tile2 = self.get_tile(line2, column2)
            self.put_tile(tile2, line1, column1)
            self.put_tile(tile1, line2, column2)
        else:
            raise InvalidPositionException()

    def xǁBoardǁchange_tiles_in_positions__mutmut_7(self, line1, column1, line2, column2):
        if self.is_inside_the_board(line1, column1) and self.is_inside_the_board(line2, None):
            tile1 = self.get_tile(line1, column1)
            tile2 = self.get_tile(line2, column2)
            self.put_tile(tile2, line1, column1)
            self.put_tile(tile1, line2, column2)
        else:
            raise InvalidPositionException()

    def xǁBoardǁchange_tiles_in_positions__mutmut_8(self, line1, column1, line2, column2):
        if self.is_inside_the_board(line1, column1) and self.is_inside_the_board(column2):
            tile1 = self.get_tile(line1, column1)
            tile2 = self.get_tile(line2, column2)
            self.put_tile(tile2, line1, column1)
            self.put_tile(tile1, line2, column2)
        else:
            raise InvalidPositionException()

    def xǁBoardǁchange_tiles_in_positions__mutmut_9(self, line1, column1, line2, column2):
        if self.is_inside_the_board(line1, column1) and self.is_inside_the_board(line2, ):
            tile1 = self.get_tile(line1, column1)
            tile2 = self.get_tile(line2, column2)
            self.put_tile(tile2, line1, column1)
            self.put_tile(tile1, line2, column2)
        else:
            raise InvalidPositionException()

    def xǁBoardǁchange_tiles_in_positions__mutmut_10(self, line1, column1, line2, column2):
        if self.is_inside_the_board(line1, column1) and self.is_inside_the_board(line2, column2):
            tile1 = None
            tile2 = self.get_tile(line2, column2)
            self.put_tile(tile2, line1, column1)
            self.put_tile(tile1, line2, column2)
        else:
            raise InvalidPositionException()

    def xǁBoardǁchange_tiles_in_positions__mutmut_11(self, line1, column1, line2, column2):
        if self.is_inside_the_board(line1, column1) and self.is_inside_the_board(line2, column2):
            tile1 = self.get_tile(None, column1)
            tile2 = self.get_tile(line2, column2)
            self.put_tile(tile2, line1, column1)
            self.put_tile(tile1, line2, column2)
        else:
            raise InvalidPositionException()

    def xǁBoardǁchange_tiles_in_positions__mutmut_12(self, line1, column1, line2, column2):
        if self.is_inside_the_board(line1, column1) and self.is_inside_the_board(line2, column2):
            tile1 = self.get_tile(line1, None)
            tile2 = self.get_tile(line2, column2)
            self.put_tile(tile2, line1, column1)
            self.put_tile(tile1, line2, column2)
        else:
            raise InvalidPositionException()

    def xǁBoardǁchange_tiles_in_positions__mutmut_13(self, line1, column1, line2, column2):
        if self.is_inside_the_board(line1, column1) and self.is_inside_the_board(line2, column2):
            tile1 = self.get_tile(column1)
            tile2 = self.get_tile(line2, column2)
            self.put_tile(tile2, line1, column1)
            self.put_tile(tile1, line2, column2)
        else:
            raise InvalidPositionException()

    def xǁBoardǁchange_tiles_in_positions__mutmut_14(self, line1, column1, line2, column2):
        if self.is_inside_the_board(line1, column1) and self.is_inside_the_board(line2, column2):
            tile1 = self.get_tile(line1, )
            tile2 = self.get_tile(line2, column2)
            self.put_tile(tile2, line1, column1)
            self.put_tile(tile1, line2, column2)
        else:
            raise InvalidPositionException()

    def xǁBoardǁchange_tiles_in_positions__mutmut_15(self, line1, column1, line2, column2):
        if self.is_inside_the_board(line1, column1) and self.is_inside_the_board(line2, column2):
            tile1 = self.get_tile(line1, column1)
            tile2 = None
            self.put_tile(tile2, line1, column1)
            self.put_tile(tile1, line2, column2)
        else:
            raise InvalidPositionException()

    def xǁBoardǁchange_tiles_in_positions__mutmut_16(self, line1, column1, line2, column2):
        if self.is_inside_the_board(line1, column1) and self.is_inside_the_board(line2, column2):
            tile1 = self.get_tile(line1, column1)
            tile2 = self.get_tile(None, column2)
            self.put_tile(tile2, line1, column1)
            self.put_tile(tile1, line2, column2)
        else:
            raise InvalidPositionException()

    def xǁBoardǁchange_tiles_in_positions__mutmut_17(self, line1, column1, line2, column2):
        if self.is_inside_the_board(line1, column1) and self.is_inside_the_board(line2, column2):
            tile1 = self.get_tile(line1, column1)
            tile2 = self.get_tile(line2, None)
            self.put_tile(tile2, line1, column1)
            self.put_tile(tile1, line2, column2)
        else:
            raise InvalidPositionException()

    def xǁBoardǁchange_tiles_in_positions__mutmut_18(self, line1, column1, line2, column2):
        if self.is_inside_the_board(line1, column1) and self.is_inside_the_board(line2, column2):
            tile1 = self.get_tile(line1, column1)
            tile2 = self.get_tile(column2)
            self.put_tile(tile2, line1, column1)
            self.put_tile(tile1, line2, column2)
        else:
            raise InvalidPositionException()

    def xǁBoardǁchange_tiles_in_positions__mutmut_19(self, line1, column1, line2, column2):
        if self.is_inside_the_board(line1, column1) and self.is_inside_the_board(line2, column2):
            tile1 = self.get_tile(line1, column1)
            tile2 = self.get_tile(line2, )
            self.put_tile(tile2, line1, column1)
            self.put_tile(tile1, line2, column2)
        else:
            raise InvalidPositionException()

    def xǁBoardǁchange_tiles_in_positions__mutmut_20(self, line1, column1, line2, column2):
        if self.is_inside_the_board(line1, column1) and self.is_inside_the_board(line2, column2):
            tile1 = self.get_tile(line1, column1)
            tile2 = self.get_tile(line2, column2)
            self.put_tile(None, line1, column1)
            self.put_tile(tile1, line2, column2)
        else:
            raise InvalidPositionException()

    def xǁBoardǁchange_tiles_in_positions__mutmut_21(self, line1, column1, line2, column2):
        if self.is_inside_the_board(line1, column1) and self.is_inside_the_board(line2, column2):
            tile1 = self.get_tile(line1, column1)
            tile2 = self.get_tile(line2, column2)
            self.put_tile(tile2, None, column1)
            self.put_tile(tile1, line2, column2)
        else:
            raise InvalidPositionException()

    def xǁBoardǁchange_tiles_in_positions__mutmut_22(self, line1, column1, line2, column2):
        if self.is_inside_the_board(line1, column1) and self.is_inside_the_board(line2, column2):
            tile1 = self.get_tile(line1, column1)
            tile2 = self.get_tile(line2, column2)
            self.put_tile(tile2, line1, None)
            self.put_tile(tile1, line2, column2)
        else:
            raise InvalidPositionException()

    def xǁBoardǁchange_tiles_in_positions__mutmut_23(self, line1, column1, line2, column2):
        if self.is_inside_the_board(line1, column1) and self.is_inside_the_board(line2, column2):
            tile1 = self.get_tile(line1, column1)
            tile2 = self.get_tile(line2, column2)
            self.put_tile(line1, column1)
            self.put_tile(tile1, line2, column2)
        else:
            raise InvalidPositionException()

    def xǁBoardǁchange_tiles_in_positions__mutmut_24(self, line1, column1, line2, column2):
        if self.is_inside_the_board(line1, column1) and self.is_inside_the_board(line2, column2):
            tile1 = self.get_tile(line1, column1)
            tile2 = self.get_tile(line2, column2)
            self.put_tile(tile2, column1)
            self.put_tile(tile1, line2, column2)
        else:
            raise InvalidPositionException()

    def xǁBoardǁchange_tiles_in_positions__mutmut_25(self, line1, column1, line2, column2):
        if self.is_inside_the_board(line1, column1) and self.is_inside_the_board(line2, column2):
            tile1 = self.get_tile(line1, column1)
            tile2 = self.get_tile(line2, column2)
            self.put_tile(tile2, line1, )
            self.put_tile(tile1, line2, column2)
        else:
            raise InvalidPositionException()

    def xǁBoardǁchange_tiles_in_positions__mutmut_26(self, line1, column1, line2, column2):
        if self.is_inside_the_board(line1, column1) and self.is_inside_the_board(line2, column2):
            tile1 = self.get_tile(line1, column1)
            tile2 = self.get_tile(line2, column2)
            self.put_tile(tile2, line1, column1)
            self.put_tile(None, line2, column2)
        else:
            raise InvalidPositionException()

    def xǁBoardǁchange_tiles_in_positions__mutmut_27(self, line1, column1, line2, column2):
        if self.is_inside_the_board(line1, column1) and self.is_inside_the_board(line2, column2):
            tile1 = self.get_tile(line1, column1)
            tile2 = self.get_tile(line2, column2)
            self.put_tile(tile2, line1, column1)
            self.put_tile(tile1, None, column2)
        else:
            raise InvalidPositionException()

    def xǁBoardǁchange_tiles_in_positions__mutmut_28(self, line1, column1, line2, column2):
        if self.is_inside_the_board(line1, column1) and self.is_inside_the_board(line2, column2):
            tile1 = self.get_tile(line1, column1)
            tile2 = self.get_tile(line2, column2)
            self.put_tile(tile2, line1, column1)
            self.put_tile(tile1, line2, None)
        else:
            raise InvalidPositionException()

    def xǁBoardǁchange_tiles_in_positions__mutmut_29(self, line1, column1, line2, column2):
        if self.is_inside_the_board(line1, column1) and self.is_inside_the_board(line2, column2):
            tile1 = self.get_tile(line1, column1)
            tile2 = self.get_tile(line2, column2)
            self.put_tile(tile2, line1, column1)
            self.put_tile(line2, column2)
        else:
            raise InvalidPositionException()

    def xǁBoardǁchange_tiles_in_positions__mutmut_30(self, line1, column1, line2, column2):
        if self.is_inside_the_board(line1, column1) and self.is_inside_the_board(line2, column2):
            tile1 = self.get_tile(line1, column1)
            tile2 = self.get_tile(line2, column2)
            self.put_tile(tile2, line1, column1)
            self.put_tile(tile1, column2)
        else:
            raise InvalidPositionException()

    def xǁBoardǁchange_tiles_in_positions__mutmut_31(self, line1, column1, line2, column2):
        if self.is_inside_the_board(line1, column1) and self.is_inside_the_board(line2, column2):
            tile1 = self.get_tile(line1, column1)
            tile2 = self.get_tile(line2, column2)
            self.put_tile(tile2, line1, column1)
            self.put_tile(tile1, line2, )
        else:
            raise InvalidPositionException()
    
    xǁBoardǁchange_tiles_in_positions__mutmut_mutants : ClassVar[MutantDict] = {
    'xǁBoardǁchange_tiles_in_positions__mutmut_1': xǁBoardǁchange_tiles_in_positions__mutmut_1, 
        'xǁBoardǁchange_tiles_in_positions__mutmut_2': xǁBoardǁchange_tiles_in_positions__mutmut_2, 
        'xǁBoardǁchange_tiles_in_positions__mutmut_3': xǁBoardǁchange_tiles_in_positions__mutmut_3, 
        'xǁBoardǁchange_tiles_in_positions__mutmut_4': xǁBoardǁchange_tiles_in_positions__mutmut_4, 
        'xǁBoardǁchange_tiles_in_positions__mutmut_5': xǁBoardǁchange_tiles_in_positions__mutmut_5, 
        'xǁBoardǁchange_tiles_in_positions__mutmut_6': xǁBoardǁchange_tiles_in_positions__mutmut_6, 
        'xǁBoardǁchange_tiles_in_positions__mutmut_7': xǁBoardǁchange_tiles_in_positions__mutmut_7, 
        'xǁBoardǁchange_tiles_in_positions__mutmut_8': xǁBoardǁchange_tiles_in_positions__mutmut_8, 
        'xǁBoardǁchange_tiles_in_positions__mutmut_9': xǁBoardǁchange_tiles_in_positions__mutmut_9, 
        'xǁBoardǁchange_tiles_in_positions__mutmut_10': xǁBoardǁchange_tiles_in_positions__mutmut_10, 
        'xǁBoardǁchange_tiles_in_positions__mutmut_11': xǁBoardǁchange_tiles_in_positions__mutmut_11, 
        'xǁBoardǁchange_tiles_in_positions__mutmut_12': xǁBoardǁchange_tiles_in_positions__mutmut_12, 
        'xǁBoardǁchange_tiles_in_positions__mutmut_13': xǁBoardǁchange_tiles_in_positions__mutmut_13, 
        'xǁBoardǁchange_tiles_in_positions__mutmut_14': xǁBoardǁchange_tiles_in_positions__mutmut_14, 
        'xǁBoardǁchange_tiles_in_positions__mutmut_15': xǁBoardǁchange_tiles_in_positions__mutmut_15, 
        'xǁBoardǁchange_tiles_in_positions__mutmut_16': xǁBoardǁchange_tiles_in_positions__mutmut_16, 
        'xǁBoardǁchange_tiles_in_positions__mutmut_17': xǁBoardǁchange_tiles_in_positions__mutmut_17, 
        'xǁBoardǁchange_tiles_in_positions__mutmut_18': xǁBoardǁchange_tiles_in_positions__mutmut_18, 
        'xǁBoardǁchange_tiles_in_positions__mutmut_19': xǁBoardǁchange_tiles_in_positions__mutmut_19, 
        'xǁBoardǁchange_tiles_in_positions__mutmut_20': xǁBoardǁchange_tiles_in_positions__mutmut_20, 
        'xǁBoardǁchange_tiles_in_positions__mutmut_21': xǁBoardǁchange_tiles_in_positions__mutmut_21, 
        'xǁBoardǁchange_tiles_in_positions__mutmut_22': xǁBoardǁchange_tiles_in_positions__mutmut_22, 
        'xǁBoardǁchange_tiles_in_positions__mutmut_23': xǁBoardǁchange_tiles_in_positions__mutmut_23, 
        'xǁBoardǁchange_tiles_in_positions__mutmut_24': xǁBoardǁchange_tiles_in_positions__mutmut_24, 
        'xǁBoardǁchange_tiles_in_positions__mutmut_25': xǁBoardǁchange_tiles_in_positions__mutmut_25, 
        'xǁBoardǁchange_tiles_in_positions__mutmut_26': xǁBoardǁchange_tiles_in_positions__mutmut_26, 
        'xǁBoardǁchange_tiles_in_positions__mutmut_27': xǁBoardǁchange_tiles_in_positions__mutmut_27, 
        'xǁBoardǁchange_tiles_in_positions__mutmut_28': xǁBoardǁchange_tiles_in_positions__mutmut_28, 
        'xǁBoardǁchange_tiles_in_positions__mutmut_29': xǁBoardǁchange_tiles_in_positions__mutmut_29, 
        'xǁBoardǁchange_tiles_in_positions__mutmut_30': xǁBoardǁchange_tiles_in_positions__mutmut_30, 
        'xǁBoardǁchange_tiles_in_positions__mutmut_31': xǁBoardǁchange_tiles_in_positions__mutmut_31
    }
    
    def change_tiles_in_positions(self, *args, **kwargs):
        result = _mutmut_trampoline(object.__getattribute__(self, "xǁBoardǁchange_tiles_in_positions__mutmut_orig"), object.__getattribute__(self, "xǁBoardǁchange_tiles_in_positions__mutmut_mutants"), args, kwargs, self)
        return result 
    
    change_tiles_in_positions.__signature__ = _mutmut_signature(xǁBoardǁchange_tiles_in_positions__mutmut_orig)
    xǁBoardǁchange_tiles_in_positions__mutmut_orig.__name__ = 'xǁBoardǁchange_tiles_in_positions'

    def xǁBoardǁpositions_are_adjacent__mutmut_orig(self, line1, column1, line2, column2):
        return self.is_inside_the_board(line1, column1) and self.is_inside_the_board(line2, column2) and ((line1 == line2 and abs(column1-column2) == 1) or (column1 == column2 and abs(line1-line2) == 1))

    def xǁBoardǁpositions_are_adjacent__mutmut_1(self, line1, column1, line2, column2):
        return self.is_inside_the_board(line1, column1) and self.is_inside_the_board(line2, column2) or ((line1 == line2 and abs(column1-column2) == 1) or (column1 == column2 and abs(line1-line2) == 1))

    def xǁBoardǁpositions_are_adjacent__mutmut_2(self, line1, column1, line2, column2):
        return self.is_inside_the_board(line1, column1) or self.is_inside_the_board(line2, column2) and ((line1 == line2 and abs(column1-column2) == 1) or (column1 == column2 and abs(line1-line2) == 1))

    def xǁBoardǁpositions_are_adjacent__mutmut_3(self, line1, column1, line2, column2):
        return self.is_inside_the_board(None, column1) and self.is_inside_the_board(line2, column2) and ((line1 == line2 and abs(column1-column2) == 1) or (column1 == column2 and abs(line1-line2) == 1))

    def xǁBoardǁpositions_are_adjacent__mutmut_4(self, line1, column1, line2, column2):
        return self.is_inside_the_board(line1, None) and self.is_inside_the_board(line2, column2) and ((line1 == line2 and abs(column1-column2) == 1) or (column1 == column2 and abs(line1-line2) == 1))

    def xǁBoardǁpositions_are_adjacent__mutmut_5(self, line1, column1, line2, column2):
        return self.is_inside_the_board(column1) and self.is_inside_the_board(line2, column2) and ((line1 == line2 and abs(column1-column2) == 1) or (column1 == column2 and abs(line1-line2) == 1))

    def xǁBoardǁpositions_are_adjacent__mutmut_6(self, line1, column1, line2, column2):
        return self.is_inside_the_board(line1, ) and self.is_inside_the_board(line2, column2) and ((line1 == line2 and abs(column1-column2) == 1) or (column1 == column2 and abs(line1-line2) == 1))

    def xǁBoardǁpositions_are_adjacent__mutmut_7(self, line1, column1, line2, column2):
        return self.is_inside_the_board(line1, column1) and self.is_inside_the_board(None, column2) and ((line1 == line2 and abs(column1-column2) == 1) or (column1 == column2 and abs(line1-line2) == 1))

    def xǁBoardǁpositions_are_adjacent__mutmut_8(self, line1, column1, line2, column2):
        return self.is_inside_the_board(line1, column1) and self.is_inside_the_board(line2, None) and ((line1 == line2 and abs(column1-column2) == 1) or (column1 == column2 and abs(line1-line2) == 1))

    def xǁBoardǁpositions_are_adjacent__mutmut_9(self, line1, column1, line2, column2):
        return self.is_inside_the_board(line1, column1) and self.is_inside_the_board(column2) and ((line1 == line2 and abs(column1-column2) == 1) or (column1 == column2 and abs(line1-line2) == 1))

    def xǁBoardǁpositions_are_adjacent__mutmut_10(self, line1, column1, line2, column2):
        return self.is_inside_the_board(line1, column1) and self.is_inside_the_board(line2, ) and ((line1 == line2 and abs(column1-column2) == 1) or (column1 == column2 and abs(line1-line2) == 1))

    def xǁBoardǁpositions_are_adjacent__mutmut_11(self, line1, column1, line2, column2):
        return self.is_inside_the_board(line1, column1) and self.is_inside_the_board(line2, column2) and ((line1 == line2 and abs(column1-column2) == 1) and (column1 == column2 and abs(line1-line2) == 1))

    def xǁBoardǁpositions_are_adjacent__mutmut_12(self, line1, column1, line2, column2):
        return self.is_inside_the_board(line1, column1) and self.is_inside_the_board(line2, column2) and ((line1 == line2 or abs(column1-column2) == 1) or (column1 == column2 and abs(line1-line2) == 1))

    def xǁBoardǁpositions_are_adjacent__mutmut_13(self, line1, column1, line2, column2):
        return self.is_inside_the_board(line1, column1) and self.is_inside_the_board(line2, column2) and ((line1 != line2 and abs(column1-column2) == 1) or (column1 == column2 and abs(line1-line2) == 1))

    def xǁBoardǁpositions_are_adjacent__mutmut_14(self, line1, column1, line2, column2):
        return self.is_inside_the_board(line1, column1) and self.is_inside_the_board(line2, column2) and ((line1 == line2 and abs(None) == 1) or (column1 == column2 and abs(line1-line2) == 1))

    def xǁBoardǁpositions_are_adjacent__mutmut_15(self, line1, column1, line2, column2):
        return self.is_inside_the_board(line1, column1) and self.is_inside_the_board(line2, column2) and ((line1 == line2 and abs(column1 + column2) == 1) or (column1 == column2 and abs(line1-line2) == 1))

    def xǁBoardǁpositions_are_adjacent__mutmut_16(self, line1, column1, line2, column2):
        return self.is_inside_the_board(line1, column1) and self.is_inside_the_board(line2, column2) and ((line1 == line2 and abs(column1-column2) != 1) or (column1 == column2 and abs(line1-line2) == 1))

    def xǁBoardǁpositions_are_adjacent__mutmut_17(self, line1, column1, line2, column2):
        return self.is_inside_the_board(line1, column1) and self.is_inside_the_board(line2, column2) and ((line1 == line2 and abs(column1-column2) == 2) or (column1 == column2 and abs(line1-line2) == 1))

    def xǁBoardǁpositions_are_adjacent__mutmut_18(self, line1, column1, line2, column2):
        return self.is_inside_the_board(line1, column1) and self.is_inside_the_board(line2, column2) and ((line1 == line2 and abs(column1-column2) == 1) or (column1 == column2 or abs(line1-line2) == 1))

    def xǁBoardǁpositions_are_adjacent__mutmut_19(self, line1, column1, line2, column2):
        return self.is_inside_the_board(line1, column1) and self.is_inside_the_board(line2, column2) and ((line1 == line2 and abs(column1-column2) == 1) or (column1 != column2 and abs(line1-line2) == 1))

    def xǁBoardǁpositions_are_adjacent__mutmut_20(self, line1, column1, line2, column2):
        return self.is_inside_the_board(line1, column1) and self.is_inside_the_board(line2, column2) and ((line1 == line2 and abs(column1-column2) == 1) or (column1 == column2 and abs(None) == 1))

    def xǁBoardǁpositions_are_adjacent__mutmut_21(self, line1, column1, line2, column2):
        return self.is_inside_the_board(line1, column1) and self.is_inside_the_board(line2, column2) and ((line1 == line2 and abs(column1-column2) == 1) or (column1 == column2 and abs(line1 + line2) == 1))

    def xǁBoardǁpositions_are_adjacent__mutmut_22(self, line1, column1, line2, column2):
        return self.is_inside_the_board(line1, column1) and self.is_inside_the_board(line2, column2) and ((line1 == line2 and abs(column1-column2) == 1) or (column1 == column2 and abs(line1-line2) != 1))

    def xǁBoardǁpositions_are_adjacent__mutmut_23(self, line1, column1, line2, column2):
        return self.is_inside_the_board(line1, column1) and self.is_inside_the_board(line2, column2) and ((line1 == line2 and abs(column1-column2) == 1) or (column1 == column2 and abs(line1-line2) == 2))
    
    xǁBoardǁpositions_are_adjacent__mutmut_mutants : ClassVar[MutantDict] = {
    'xǁBoardǁpositions_are_adjacent__mutmut_1': xǁBoardǁpositions_are_adjacent__mutmut_1, 
        'xǁBoardǁpositions_are_adjacent__mutmut_2': xǁBoardǁpositions_are_adjacent__mutmut_2, 
        'xǁBoardǁpositions_are_adjacent__mutmut_3': xǁBoardǁpositions_are_adjacent__mutmut_3, 
        'xǁBoardǁpositions_are_adjacent__mutmut_4': xǁBoardǁpositions_are_adjacent__mutmut_4, 
        'xǁBoardǁpositions_are_adjacent__mutmut_5': xǁBoardǁpositions_are_adjacent__mutmut_5, 
        'xǁBoardǁpositions_are_adjacent__mutmut_6': xǁBoardǁpositions_are_adjacent__mutmut_6, 
        'xǁBoardǁpositions_are_adjacent__mutmut_7': xǁBoardǁpositions_are_adjacent__mutmut_7, 
        'xǁBoardǁpositions_are_adjacent__mutmut_8': xǁBoardǁpositions_are_adjacent__mutmut_8, 
        'xǁBoardǁpositions_are_adjacent__mutmut_9': xǁBoardǁpositions_are_adjacent__mutmut_9, 
        'xǁBoardǁpositions_are_adjacent__mutmut_10': xǁBoardǁpositions_are_adjacent__mutmut_10, 
        'xǁBoardǁpositions_are_adjacent__mutmut_11': xǁBoardǁpositions_are_adjacent__mutmut_11, 
        'xǁBoardǁpositions_are_adjacent__mutmut_12': xǁBoardǁpositions_are_adjacent__mutmut_12, 
        'xǁBoardǁpositions_are_adjacent__mutmut_13': xǁBoardǁpositions_are_adjacent__mutmut_13, 
        'xǁBoardǁpositions_are_adjacent__mutmut_14': xǁBoardǁpositions_are_adjacent__mutmut_14, 
        'xǁBoardǁpositions_are_adjacent__mutmut_15': xǁBoardǁpositions_are_adjacent__mutmut_15, 
        'xǁBoardǁpositions_are_adjacent__mutmut_16': xǁBoardǁpositions_are_adjacent__mutmut_16, 
        'xǁBoardǁpositions_are_adjacent__mutmut_17': xǁBoardǁpositions_are_adjacent__mutmut_17, 
        'xǁBoardǁpositions_are_adjacent__mutmut_18': xǁBoardǁpositions_are_adjacent__mutmut_18, 
        'xǁBoardǁpositions_are_adjacent__mutmut_19': xǁBoardǁpositions_are_adjacent__mutmut_19, 
        'xǁBoardǁpositions_are_adjacent__mutmut_20': xǁBoardǁpositions_are_adjacent__mutmut_20, 
        'xǁBoardǁpositions_are_adjacent__mutmut_21': xǁBoardǁpositions_are_adjacent__mutmut_21, 
        'xǁBoardǁpositions_are_adjacent__mutmut_22': xǁBoardǁpositions_are_adjacent__mutmut_22, 
        'xǁBoardǁpositions_are_adjacent__mutmut_23': xǁBoardǁpositions_are_adjacent__mutmut_23
    }
    
    def positions_are_adjacent(self, *args, **kwargs):
        result = _mutmut_trampoline(object.__getattribute__(self, "xǁBoardǁpositions_are_adjacent__mutmut_orig"), object.__getattribute__(self, "xǁBoardǁpositions_are_adjacent__mutmut_mutants"), args, kwargs, self)
        return result 
    
    positions_are_adjacent.__signature__ = _mutmut_signature(xǁBoardǁpositions_are_adjacent__mutmut_orig)
    xǁBoardǁpositions_are_adjacent__mutmut_orig.__name__ = 'xǁBoardǁpositions_are_adjacent'

    def xǁBoardǁis_in_the_superior_border__mutmut_orig(self, line, column):
        return self.is_inside_the_board(line, column) and line == 1

    def xǁBoardǁis_in_the_superior_border__mutmut_1(self, line, column):
        return self.is_inside_the_board(line, column) or line == 1

    def xǁBoardǁis_in_the_superior_border__mutmut_2(self, line, column):
        return self.is_inside_the_board(None, column) and line == 1

    def xǁBoardǁis_in_the_superior_border__mutmut_3(self, line, column):
        return self.is_inside_the_board(line, None) and line == 1

    def xǁBoardǁis_in_the_superior_border__mutmut_4(self, line, column):
        return self.is_inside_the_board(column) and line == 1

    def xǁBoardǁis_in_the_superior_border__mutmut_5(self, line, column):
        return self.is_inside_the_board(line, ) and line == 1

    def xǁBoardǁis_in_the_superior_border__mutmut_6(self, line, column):
        return self.is_inside_the_board(line, column) and line != 1

    def xǁBoardǁis_in_the_superior_border__mutmut_7(self, line, column):
        return self.is_inside_the_board(line, column) and line == 2
    
    xǁBoardǁis_in_the_superior_border__mutmut_mutants : ClassVar[MutantDict] = {
    'xǁBoardǁis_in_the_superior_border__mutmut_1': xǁBoardǁis_in_the_superior_border__mutmut_1, 
        'xǁBoardǁis_in_the_superior_border__mutmut_2': xǁBoardǁis_in_the_superior_border__mutmut_2, 
        'xǁBoardǁis_in_the_superior_border__mutmut_3': xǁBoardǁis_in_the_superior_border__mutmut_3, 
        'xǁBoardǁis_in_the_superior_border__mutmut_4': xǁBoardǁis_in_the_superior_border__mutmut_4, 
        'xǁBoardǁis_in_the_superior_border__mutmut_5': xǁBoardǁis_in_the_superior_border__mutmut_5, 
        'xǁBoardǁis_in_the_superior_border__mutmut_6': xǁBoardǁis_in_the_superior_border__mutmut_6, 
        'xǁBoardǁis_in_the_superior_border__mutmut_7': xǁBoardǁis_in_the_superior_border__mutmut_7
    }
    
    def is_in_the_superior_border(self, *args, **kwargs):
        result = _mutmut_trampoline(object.__getattribute__(self, "xǁBoardǁis_in_the_superior_border__mutmut_orig"), object.__getattribute__(self, "xǁBoardǁis_in_the_superior_border__mutmut_mutants"), args, kwargs, self)
        return result 
    
    is_in_the_superior_border.__signature__ = _mutmut_signature(xǁBoardǁis_in_the_superior_border__mutmut_orig)
    xǁBoardǁis_in_the_superior_border__mutmut_orig.__name__ = 'xǁBoardǁis_in_the_superior_border'

    def xǁBoardǁis_in_the_bottom_border__mutmut_orig(self, line, column):
        return self.is_inside_the_board(line, column) and line == self.__number_of_lines

    def xǁBoardǁis_in_the_bottom_border__mutmut_1(self, line, column):
        return self.is_inside_the_board(line, column) or line == self.__number_of_lines

    def xǁBoardǁis_in_the_bottom_border__mutmut_2(self, line, column):
        return self.is_inside_the_board(None, column) and line == self.__number_of_lines

    def xǁBoardǁis_in_the_bottom_border__mutmut_3(self, line, column):
        return self.is_inside_the_board(line, None) and line == self.__number_of_lines

    def xǁBoardǁis_in_the_bottom_border__mutmut_4(self, line, column):
        return self.is_inside_the_board(column) and line == self.__number_of_lines

    def xǁBoardǁis_in_the_bottom_border__mutmut_5(self, line, column):
        return self.is_inside_the_board(line, ) and line == self.__number_of_lines

    def xǁBoardǁis_in_the_bottom_border__mutmut_6(self, line, column):
        return self.is_inside_the_board(line, column) and line != self.__number_of_lines
    
    xǁBoardǁis_in_the_bottom_border__mutmut_mutants : ClassVar[MutantDict] = {
    'xǁBoardǁis_in_the_bottom_border__mutmut_1': xǁBoardǁis_in_the_bottom_border__mutmut_1, 
        'xǁBoardǁis_in_the_bottom_border__mutmut_2': xǁBoardǁis_in_the_bottom_border__mutmut_2, 
        'xǁBoardǁis_in_the_bottom_border__mutmut_3': xǁBoardǁis_in_the_bottom_border__mutmut_3, 
        'xǁBoardǁis_in_the_bottom_border__mutmut_4': xǁBoardǁis_in_the_bottom_border__mutmut_4, 
        'xǁBoardǁis_in_the_bottom_border__mutmut_5': xǁBoardǁis_in_the_bottom_border__mutmut_5, 
        'xǁBoardǁis_in_the_bottom_border__mutmut_6': xǁBoardǁis_in_the_bottom_border__mutmut_6
    }
    
    def is_in_the_bottom_border(self, *args, **kwargs):
        result = _mutmut_trampoline(object.__getattribute__(self, "xǁBoardǁis_in_the_bottom_border__mutmut_orig"), object.__getattribute__(self, "xǁBoardǁis_in_the_bottom_border__mutmut_mutants"), args, kwargs, self)
        return result 
    
    is_in_the_bottom_border.__signature__ = _mutmut_signature(xǁBoardǁis_in_the_bottom_border__mutmut_orig)
    xǁBoardǁis_in_the_bottom_border__mutmut_orig.__name__ = 'xǁBoardǁis_in_the_bottom_border'

    def xǁBoardǁis_in_the_left_border__mutmut_orig(self, line, column):
        return self.is_inside_the_board(line, column) and column == 1

    def xǁBoardǁis_in_the_left_border__mutmut_1(self, line, column):
        return self.is_inside_the_board(line, column) or column == 1

    def xǁBoardǁis_in_the_left_border__mutmut_2(self, line, column):
        return self.is_inside_the_board(None, column) and column == 1

    def xǁBoardǁis_in_the_left_border__mutmut_3(self, line, column):
        return self.is_inside_the_board(line, None) and column == 1

    def xǁBoardǁis_in_the_left_border__mutmut_4(self, line, column):
        return self.is_inside_the_board(column) and column == 1

    def xǁBoardǁis_in_the_left_border__mutmut_5(self, line, column):
        return self.is_inside_the_board(line, ) and column == 1

    def xǁBoardǁis_in_the_left_border__mutmut_6(self, line, column):
        return self.is_inside_the_board(line, column) and column != 1

    def xǁBoardǁis_in_the_left_border__mutmut_7(self, line, column):
        return self.is_inside_the_board(line, column) and column == 2
    
    xǁBoardǁis_in_the_left_border__mutmut_mutants : ClassVar[MutantDict] = {
    'xǁBoardǁis_in_the_left_border__mutmut_1': xǁBoardǁis_in_the_left_border__mutmut_1, 
        'xǁBoardǁis_in_the_left_border__mutmut_2': xǁBoardǁis_in_the_left_border__mutmut_2, 
        'xǁBoardǁis_in_the_left_border__mutmut_3': xǁBoardǁis_in_the_left_border__mutmut_3, 
        'xǁBoardǁis_in_the_left_border__mutmut_4': xǁBoardǁis_in_the_left_border__mutmut_4, 
        'xǁBoardǁis_in_the_left_border__mutmut_5': xǁBoardǁis_in_the_left_border__mutmut_5, 
        'xǁBoardǁis_in_the_left_border__mutmut_6': xǁBoardǁis_in_the_left_border__mutmut_6, 
        'xǁBoardǁis_in_the_left_border__mutmut_7': xǁBoardǁis_in_the_left_border__mutmut_7
    }
    
    def is_in_the_left_border(self, *args, **kwargs):
        result = _mutmut_trampoline(object.__getattribute__(self, "xǁBoardǁis_in_the_left_border__mutmut_orig"), object.__getattribute__(self, "xǁBoardǁis_in_the_left_border__mutmut_mutants"), args, kwargs, self)
        return result 
    
    is_in_the_left_border.__signature__ = _mutmut_signature(xǁBoardǁis_in_the_left_border__mutmut_orig)
    xǁBoardǁis_in_the_left_border__mutmut_orig.__name__ = 'xǁBoardǁis_in_the_left_border'

    def xǁBoardǁis_in_the_right_border__mutmut_orig(self, line, column):
        return self.is_inside_the_board(line, column) and column == self.number_of_columns

    def xǁBoardǁis_in_the_right_border__mutmut_1(self, line, column):
        return self.is_inside_the_board(line, column) or column == self.number_of_columns

    def xǁBoardǁis_in_the_right_border__mutmut_2(self, line, column):
        return self.is_inside_the_board(None, column) and column == self.number_of_columns

    def xǁBoardǁis_in_the_right_border__mutmut_3(self, line, column):
        return self.is_inside_the_board(line, None) and column == self.number_of_columns

    def xǁBoardǁis_in_the_right_border__mutmut_4(self, line, column):
        return self.is_inside_the_board(column) and column == self.number_of_columns

    def xǁBoardǁis_in_the_right_border__mutmut_5(self, line, column):
        return self.is_inside_the_board(line, ) and column == self.number_of_columns

    def xǁBoardǁis_in_the_right_border__mutmut_6(self, line, column):
        return self.is_inside_the_board(line, column) and column != self.number_of_columns
    
    xǁBoardǁis_in_the_right_border__mutmut_mutants : ClassVar[MutantDict] = {
    'xǁBoardǁis_in_the_right_border__mutmut_1': xǁBoardǁis_in_the_right_border__mutmut_1, 
        'xǁBoardǁis_in_the_right_border__mutmut_2': xǁBoardǁis_in_the_right_border__mutmut_2, 
        'xǁBoardǁis_in_the_right_border__mutmut_3': xǁBoardǁis_in_the_right_border__mutmut_3, 
        'xǁBoardǁis_in_the_right_border__mutmut_4': xǁBoardǁis_in_the_right_border__mutmut_4, 
        'xǁBoardǁis_in_the_right_border__mutmut_5': xǁBoardǁis_in_the_right_border__mutmut_5, 
        'xǁBoardǁis_in_the_right_border__mutmut_6': xǁBoardǁis_in_the_right_border__mutmut_6
    }
    
    def is_in_the_right_border(self, *args, **kwargs):
        result = _mutmut_trampoline(object.__getattribute__(self, "xǁBoardǁis_in_the_right_border__mutmut_orig"), object.__getattribute__(self, "xǁBoardǁis_in_the_right_border__mutmut_mutants"), args, kwargs, self)
        return result 
    
    is_in_the_right_border.__signature__ = _mutmut_signature(xǁBoardǁis_in_the_right_border__mutmut_orig)
    xǁBoardǁis_in_the_right_border__mutmut_orig.__name__ = 'xǁBoardǁis_in_the_right_border'

    def xǁBoardǁ__eq____mutmut_orig(self, other):
        if (self.__number_of_lines != other.__number_of_lines) or (self.number_of_columns != other.number_of_columns):
            return False
        for line in range(0, self.__number_of_lines):
            for column in range(0, self.number_of_columns):
                if not(self.grid[line][column] == other.grid[line][column]):
                    return False
        return True

    def xǁBoardǁ__eq____mutmut_1(self, other):
        if (self.__number_of_lines != other.__number_of_lines) and (self.number_of_columns != other.number_of_columns):
            return False
        for line in range(0, self.__number_of_lines):
            for column in range(0, self.number_of_columns):
                if not(self.grid[line][column] == other.grid[line][column]):
                    return False
        return True

    def xǁBoardǁ__eq____mutmut_2(self, other):
        if (self.__number_of_lines == other.__number_of_lines) or (self.number_of_columns != other.number_of_columns):
            return False
        for line in range(0, self.__number_of_lines):
            for column in range(0, self.number_of_columns):
                if not(self.grid[line][column] == other.grid[line][column]):
                    return False
        return True

    def xǁBoardǁ__eq____mutmut_3(self, other):
        if (self.__number_of_lines != other.__number_of_lines) or (self.number_of_columns == other.number_of_columns):
            return False
        for line in range(0, self.__number_of_lines):
            for column in range(0, self.number_of_columns):
                if not(self.grid[line][column] == other.grid[line][column]):
                    return False
        return True

    def xǁBoardǁ__eq____mutmut_4(self, other):
        if (self.__number_of_lines != other.__number_of_lines) or (self.number_of_columns != other.number_of_columns):
            return True
        for line in range(0, self.__number_of_lines):
            for column in range(0, self.number_of_columns):
                if not(self.grid[line][column] == other.grid[line][column]):
                    return False
        return True

    def xǁBoardǁ__eq____mutmut_5(self, other):
        if (self.__number_of_lines != other.__number_of_lines) or (self.number_of_columns != other.number_of_columns):
            return False
        for line in range(None, self.__number_of_lines):
            for column in range(0, self.number_of_columns):
                if not(self.grid[line][column] == other.grid[line][column]):
                    return False
        return True

    def xǁBoardǁ__eq____mutmut_6(self, other):
        if (self.__number_of_lines != other.__number_of_lines) or (self.number_of_columns != other.number_of_columns):
            return False
        for line in range(0, None):
            for column in range(0, self.number_of_columns):
                if not(self.grid[line][column] == other.grid[line][column]):
                    return False
        return True

    def xǁBoardǁ__eq____mutmut_7(self, other):
        if (self.__number_of_lines != other.__number_of_lines) or (self.number_of_columns != other.number_of_columns):
            return False
        for line in range(self.__number_of_lines):
            for column in range(0, self.number_of_columns):
                if not(self.grid[line][column] == other.grid[line][column]):
                    return False
        return True

    def xǁBoardǁ__eq____mutmut_8(self, other):
        if (self.__number_of_lines != other.__number_of_lines) or (self.number_of_columns != other.number_of_columns):
            return False
        for line in range(0, ):
            for column in range(0, self.number_of_columns):
                if not(self.grid[line][column] == other.grid[line][column]):
                    return False
        return True

    def xǁBoardǁ__eq____mutmut_9(self, other):
        if (self.__number_of_lines != other.__number_of_lines) or (self.number_of_columns != other.number_of_columns):
            return False
        for line in range(1, self.__number_of_lines):
            for column in range(0, self.number_of_columns):
                if not(self.grid[line][column] == other.grid[line][column]):
                    return False
        return True

    def xǁBoardǁ__eq____mutmut_10(self, other):
        if (self.__number_of_lines != other.__number_of_lines) or (self.number_of_columns != other.number_of_columns):
            return False
        for line in range(0, self.__number_of_lines):
            for column in range(None, self.number_of_columns):
                if not(self.grid[line][column] == other.grid[line][column]):
                    return False
        return True

    def xǁBoardǁ__eq____mutmut_11(self, other):
        if (self.__number_of_lines != other.__number_of_lines) or (self.number_of_columns != other.number_of_columns):
            return False
        for line in range(0, self.__number_of_lines):
            for column in range(0, None):
                if not(self.grid[line][column] == other.grid[line][column]):
                    return False
        return True

    def xǁBoardǁ__eq____mutmut_12(self, other):
        if (self.__number_of_lines != other.__number_of_lines) or (self.number_of_columns != other.number_of_columns):
            return False
        for line in range(0, self.__number_of_lines):
            for column in range(self.number_of_columns):
                if not(self.grid[line][column] == other.grid[line][column]):
                    return False
        return True

    def xǁBoardǁ__eq____mutmut_13(self, other):
        if (self.__number_of_lines != other.__number_of_lines) or (self.number_of_columns != other.number_of_columns):
            return False
        for line in range(0, self.__number_of_lines):
            for column in range(0, ):
                if not(self.grid[line][column] == other.grid[line][column]):
                    return False
        return True

    def xǁBoardǁ__eq____mutmut_14(self, other):
        if (self.__number_of_lines != other.__number_of_lines) or (self.number_of_columns != other.number_of_columns):
            return False
        for line in range(0, self.__number_of_lines):
            for column in range(1, self.number_of_columns):
                if not(self.grid[line][column] == other.grid[line][column]):
                    return False
        return True

    def xǁBoardǁ__eq____mutmut_15(self, other):
        if (self.__number_of_lines != other.__number_of_lines) or (self.number_of_columns != other.number_of_columns):
            return False
        for line in range(0, self.__number_of_lines):
            for column in range(0, self.number_of_columns):
                if (self.grid[line][column] == other.grid[line][column]):
                    return False
        return True

    def xǁBoardǁ__eq____mutmut_16(self, other):
        if (self.__number_of_lines != other.__number_of_lines) or (self.number_of_columns != other.number_of_columns):
            return False
        for line in range(0, self.__number_of_lines):
            for column in range(0, self.number_of_columns):
                if not(self.grid[line][column] != other.grid[line][column]):
                    return False
        return True

    def xǁBoardǁ__eq____mutmut_17(self, other):
        if (self.__number_of_lines != other.__number_of_lines) or (self.number_of_columns != other.number_of_columns):
            return False
        for line in range(0, self.__number_of_lines):
            for column in range(0, self.number_of_columns):
                if not(self.grid[line][column] == other.grid[line][column]):
                    return True
        return True

    def xǁBoardǁ__eq____mutmut_18(self, other):
        if (self.__number_of_lines != other.__number_of_lines) or (self.number_of_columns != other.number_of_columns):
            return False
        for line in range(0, self.__number_of_lines):
            for column in range(0, self.number_of_columns):
                if not(self.grid[line][column] == other.grid[line][column]):
                    return False
        return False
    
    xǁBoardǁ__eq____mutmut_mutants : ClassVar[MutantDict] = {
    'xǁBoardǁ__eq____mutmut_1': xǁBoardǁ__eq____mutmut_1, 
        'xǁBoardǁ__eq____mutmut_2': xǁBoardǁ__eq____mutmut_2, 
        'xǁBoardǁ__eq____mutmut_3': xǁBoardǁ__eq____mutmut_3, 
        'xǁBoardǁ__eq____mutmut_4': xǁBoardǁ__eq____mutmut_4, 
        'xǁBoardǁ__eq____mutmut_5': xǁBoardǁ__eq____mutmut_5, 
        'xǁBoardǁ__eq____mutmut_6': xǁBoardǁ__eq____mutmut_6, 
        'xǁBoardǁ__eq____mutmut_7': xǁBoardǁ__eq____mutmut_7, 
        'xǁBoardǁ__eq____mutmut_8': xǁBoardǁ__eq____mutmut_8, 
        'xǁBoardǁ__eq____mutmut_9': xǁBoardǁ__eq____mutmut_9, 
        'xǁBoardǁ__eq____mutmut_10': xǁBoardǁ__eq____mutmut_10, 
        'xǁBoardǁ__eq____mutmut_11': xǁBoardǁ__eq____mutmut_11, 
        'xǁBoardǁ__eq____mutmut_12': xǁBoardǁ__eq____mutmut_12, 
        'xǁBoardǁ__eq____mutmut_13': xǁBoardǁ__eq____mutmut_13, 
        'xǁBoardǁ__eq____mutmut_14': xǁBoardǁ__eq____mutmut_14, 
        'xǁBoardǁ__eq____mutmut_15': xǁBoardǁ__eq____mutmut_15, 
        'xǁBoardǁ__eq____mutmut_16': xǁBoardǁ__eq____mutmut_16, 
        'xǁBoardǁ__eq____mutmut_17': xǁBoardǁ__eq____mutmut_17, 
        'xǁBoardǁ__eq____mutmut_18': xǁBoardǁ__eq____mutmut_18
    }
    
    def __eq__(self, *args, **kwargs):
        result = _mutmut_trampoline(object.__getattribute__(self, "xǁBoardǁ__eq____mutmut_orig"), object.__getattribute__(self, "xǁBoardǁ__eq____mutmut_mutants"), args, kwargs, self)
        return result 
    
    __eq__.__signature__ = _mutmut_signature(xǁBoardǁ__eq____mutmut_orig)
    xǁBoardǁ__eq____mutmut_orig.__name__ = 'xǁBoardǁ__eq__'

    def xǁBoardǁ__str____mutmut_orig(self):
        result = ""
        for line in range(0, self.__number_of_lines):
            for column in range(0, self.number_of_columns):
                value = self.grid[line][column]
                result += f"({line+1},{column+1}):{value}   "
            result += "\n"
        return result

    def xǁBoardǁ__str____mutmut_1(self):
        result = None
        for line in range(0, self.__number_of_lines):
            for column in range(0, self.number_of_columns):
                value = self.grid[line][column]
                result += f"({line+1},{column+1}):{value}   "
            result += "\n"
        return result

    def xǁBoardǁ__str____mutmut_2(self):
        result = "XXXX"
        for line in range(0, self.__number_of_lines):
            for column in range(0, self.number_of_columns):
                value = self.grid[line][column]
                result += f"({line+1},{column+1}):{value}   "
            result += "\n"
        return result

    def xǁBoardǁ__str____mutmut_3(self):
        result = ""
        for line in range(None, self.__number_of_lines):
            for column in range(0, self.number_of_columns):
                value = self.grid[line][column]
                result += f"({line+1},{column+1}):{value}   "
            result += "\n"
        return result

    def xǁBoardǁ__str____mutmut_4(self):
        result = ""
        for line in range(0, None):
            for column in range(0, self.number_of_columns):
                value = self.grid[line][column]
                result += f"({line+1},{column+1}):{value}   "
            result += "\n"
        return result

    def xǁBoardǁ__str____mutmut_5(self):
        result = ""
        for line in range(self.__number_of_lines):
            for column in range(0, self.number_of_columns):
                value = self.grid[line][column]
                result += f"({line+1},{column+1}):{value}   "
            result += "\n"
        return result

    def xǁBoardǁ__str____mutmut_6(self):
        result = ""
        for line in range(0, ):
            for column in range(0, self.number_of_columns):
                value = self.grid[line][column]
                result += f"({line+1},{column+1}):{value}   "
            result += "\n"
        return result

    def xǁBoardǁ__str____mutmut_7(self):
        result = ""
        for line in range(1, self.__number_of_lines):
            for column in range(0, self.number_of_columns):
                value = self.grid[line][column]
                result += f"({line+1},{column+1}):{value}   "
            result += "\n"
        return result

    def xǁBoardǁ__str____mutmut_8(self):
        result = ""
        for line in range(0, self.__number_of_lines):
            for column in range(None, self.number_of_columns):
                value = self.grid[line][column]
                result += f"({line+1},{column+1}):{value}   "
            result += "\n"
        return result

    def xǁBoardǁ__str____mutmut_9(self):
        result = ""
        for line in range(0, self.__number_of_lines):
            for column in range(0, None):
                value = self.grid[line][column]
                result += f"({line+1},{column+1}):{value}   "
            result += "\n"
        return result

    def xǁBoardǁ__str____mutmut_10(self):
        result = ""
        for line in range(0, self.__number_of_lines):
            for column in range(self.number_of_columns):
                value = self.grid[line][column]
                result += f"({line+1},{column+1}):{value}   "
            result += "\n"
        return result

    def xǁBoardǁ__str____mutmut_11(self):
        result = ""
        for line in range(0, self.__number_of_lines):
            for column in range(0, ):
                value = self.grid[line][column]
                result += f"({line+1},{column+1}):{value}   "
            result += "\n"
        return result

    def xǁBoardǁ__str____mutmut_12(self):
        result = ""
        for line in range(0, self.__number_of_lines):
            for column in range(1, self.number_of_columns):
                value = self.grid[line][column]
                result += f"({line+1},{column+1}):{value}   "
            result += "\n"
        return result

    def xǁBoardǁ__str____mutmut_13(self):
        result = ""
        for line in range(0, self.__number_of_lines):
            for column in range(0, self.number_of_columns):
                value = None
                result += f"({line+1},{column+1}):{value}   "
            result += "\n"
        return result

    def xǁBoardǁ__str____mutmut_14(self):
        result = ""
        for line in range(0, self.__number_of_lines):
            for column in range(0, self.number_of_columns):
                value = self.grid[line][column]
                result = f"({line+1},{column+1}):{value}   "
            result += "\n"
        return result

    def xǁBoardǁ__str____mutmut_15(self):
        result = ""
        for line in range(0, self.__number_of_lines):
            for column in range(0, self.number_of_columns):
                value = self.grid[line][column]
                result -= f"({line+1},{column+1}):{value}   "
            result += "\n"
        return result

    def xǁBoardǁ__str____mutmut_16(self):
        result = ""
        for line in range(0, self.__number_of_lines):
            for column in range(0, self.number_of_columns):
                value = self.grid[line][column]
                result += f"({line - 1},{column+1}):{value}   "
            result += "\n"
        return result

    def xǁBoardǁ__str____mutmut_17(self):
        result = ""
        for line in range(0, self.__number_of_lines):
            for column in range(0, self.number_of_columns):
                value = self.grid[line][column]
                result += f"({line+2},{column+1}):{value}   "
            result += "\n"
        return result

    def xǁBoardǁ__str____mutmut_18(self):
        result = ""
        for line in range(0, self.__number_of_lines):
            for column in range(0, self.number_of_columns):
                value = self.grid[line][column]
                result += f"({line+1},{column - 1}):{value}   "
            result += "\n"
        return result

    def xǁBoardǁ__str____mutmut_19(self):
        result = ""
        for line in range(0, self.__number_of_lines):
            for column in range(0, self.number_of_columns):
                value = self.grid[line][column]
                result += f"({line+1},{column+2}):{value}   "
            result += "\n"
        return result

    def xǁBoardǁ__str____mutmut_20(self):
        result = ""
        for line in range(0, self.__number_of_lines):
            for column in range(0, self.number_of_columns):
                value = self.grid[line][column]
                result += f"({line+1},{column+1}):{value}   "
            result = "\n"
        return result

    def xǁBoardǁ__str____mutmut_21(self):
        result = ""
        for line in range(0, self.__number_of_lines):
            for column in range(0, self.number_of_columns):
                value = self.grid[line][column]
                result += f"({line+1},{column+1}):{value}   "
            result -= "\n"
        return result

    def xǁBoardǁ__str____mutmut_22(self):
        result = ""
        for line in range(0, self.__number_of_lines):
            for column in range(0, self.number_of_columns):
                value = self.grid[line][column]
                result += f"({line+1},{column+1}):{value}   "
            result += "XX\nXX"
        return result
    
    xǁBoardǁ__str____mutmut_mutants : ClassVar[MutantDict] = {
    'xǁBoardǁ__str____mutmut_1': xǁBoardǁ__str____mutmut_1, 
        'xǁBoardǁ__str____mutmut_2': xǁBoardǁ__str____mutmut_2, 
        'xǁBoardǁ__str____mutmut_3': xǁBoardǁ__str____mutmut_3, 
        'xǁBoardǁ__str____mutmut_4': xǁBoardǁ__str____mutmut_4, 
        'xǁBoardǁ__str____mutmut_5': xǁBoardǁ__str____mutmut_5, 
        'xǁBoardǁ__str____mutmut_6': xǁBoardǁ__str____mutmut_6, 
        'xǁBoardǁ__str____mutmut_7': xǁBoardǁ__str____mutmut_7, 
        'xǁBoardǁ__str____mutmut_8': xǁBoardǁ__str____mutmut_8, 
        'xǁBoardǁ__str____mutmut_9': xǁBoardǁ__str____mutmut_9, 
        'xǁBoardǁ__str____mutmut_10': xǁBoardǁ__str____mutmut_10, 
        'xǁBoardǁ__str____mutmut_11': xǁBoardǁ__str____mutmut_11, 
        'xǁBoardǁ__str____mutmut_12': xǁBoardǁ__str____mutmut_12, 
        'xǁBoardǁ__str____mutmut_13': xǁBoardǁ__str____mutmut_13, 
        'xǁBoardǁ__str____mutmut_14': xǁBoardǁ__str____mutmut_14, 
        'xǁBoardǁ__str____mutmut_15': xǁBoardǁ__str____mutmut_15, 
        'xǁBoardǁ__str____mutmut_16': xǁBoardǁ__str____mutmut_16, 
        'xǁBoardǁ__str____mutmut_17': xǁBoardǁ__str____mutmut_17, 
        'xǁBoardǁ__str____mutmut_18': xǁBoardǁ__str____mutmut_18, 
        'xǁBoardǁ__str____mutmut_19': xǁBoardǁ__str____mutmut_19, 
        'xǁBoardǁ__str____mutmut_20': xǁBoardǁ__str____mutmut_20, 
        'xǁBoardǁ__str____mutmut_21': xǁBoardǁ__str____mutmut_21, 
        'xǁBoardǁ__str____mutmut_22': xǁBoardǁ__str____mutmut_22
    }
    
    def __str__(self, *args, **kwargs):
        result = _mutmut_trampoline(object.__getattribute__(self, "xǁBoardǁ__str____mutmut_orig"), object.__getattribute__(self, "xǁBoardǁ__str____mutmut_mutants"), args, kwargs, self)
        return result 
    
    __str__.__signature__ = _mutmut_signature(xǁBoardǁ__str____mutmut_orig)
    xǁBoardǁ__str____mutmut_orig.__name__ = 'xǁBoardǁ__str__'

