from board import Board
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


class PuzzleGame:

    def xǁPuzzleGameǁ__init____mutmut_orig(self, dimension):
        self.__dimension = dimension
        self.__board = Board(self.dimension, self.dimension)
        self.__board_with_final_state = Board(self.dimension, self.dimension)
        self.__dic_positions_of_tiles = {}
        list_tiles = self.__generate_list_of_tiles__()
        self.__put_tiles_in_the_board__(self.board, list_tiles)
        self.__put_tiles_in_the_board__(self.board_with_final_state, list_tiles)
        self.__put_tiles_in_dic_positions__(list_tiles)
        self.line_of_empty_position = self.dimension
        self.column_of_empty_position = self.dimension

    def xǁPuzzleGameǁ__init____mutmut_1(self, dimension):
        self.__dimension = None
        self.__board = Board(self.dimension, self.dimension)
        self.__board_with_final_state = Board(self.dimension, self.dimension)
        self.__dic_positions_of_tiles = {}
        list_tiles = self.__generate_list_of_tiles__()
        self.__put_tiles_in_the_board__(self.board, list_tiles)
        self.__put_tiles_in_the_board__(self.board_with_final_state, list_tiles)
        self.__put_tiles_in_dic_positions__(list_tiles)
        self.line_of_empty_position = self.dimension
        self.column_of_empty_position = self.dimension

    def xǁPuzzleGameǁ__init____mutmut_2(self, dimension):
        self.__dimension = dimension
        self.__board = None
        self.__board_with_final_state = Board(self.dimension, self.dimension)
        self.__dic_positions_of_tiles = {}
        list_tiles = self.__generate_list_of_tiles__()
        self.__put_tiles_in_the_board__(self.board, list_tiles)
        self.__put_tiles_in_the_board__(self.board_with_final_state, list_tiles)
        self.__put_tiles_in_dic_positions__(list_tiles)
        self.line_of_empty_position = self.dimension
        self.column_of_empty_position = self.dimension

    def xǁPuzzleGameǁ__init____mutmut_3(self, dimension):
        self.__dimension = dimension
        self.__board = Board(None, self.dimension)
        self.__board_with_final_state = Board(self.dimension, self.dimension)
        self.__dic_positions_of_tiles = {}
        list_tiles = self.__generate_list_of_tiles__()
        self.__put_tiles_in_the_board__(self.board, list_tiles)
        self.__put_tiles_in_the_board__(self.board_with_final_state, list_tiles)
        self.__put_tiles_in_dic_positions__(list_tiles)
        self.line_of_empty_position = self.dimension
        self.column_of_empty_position = self.dimension

    def xǁPuzzleGameǁ__init____mutmut_4(self, dimension):
        self.__dimension = dimension
        self.__board = Board(self.dimension, None)
        self.__board_with_final_state = Board(self.dimension, self.dimension)
        self.__dic_positions_of_tiles = {}
        list_tiles = self.__generate_list_of_tiles__()
        self.__put_tiles_in_the_board__(self.board, list_tiles)
        self.__put_tiles_in_the_board__(self.board_with_final_state, list_tiles)
        self.__put_tiles_in_dic_positions__(list_tiles)
        self.line_of_empty_position = self.dimension
        self.column_of_empty_position = self.dimension

    def xǁPuzzleGameǁ__init____mutmut_5(self, dimension):
        self.__dimension = dimension
        self.__board = Board(self.dimension)
        self.__board_with_final_state = Board(self.dimension, self.dimension)
        self.__dic_positions_of_tiles = {}
        list_tiles = self.__generate_list_of_tiles__()
        self.__put_tiles_in_the_board__(self.board, list_tiles)
        self.__put_tiles_in_the_board__(self.board_with_final_state, list_tiles)
        self.__put_tiles_in_dic_positions__(list_tiles)
        self.line_of_empty_position = self.dimension
        self.column_of_empty_position = self.dimension

    def xǁPuzzleGameǁ__init____mutmut_6(self, dimension):
        self.__dimension = dimension
        self.__board = Board(self.dimension, )
        self.__board_with_final_state = Board(self.dimension, self.dimension)
        self.__dic_positions_of_tiles = {}
        list_tiles = self.__generate_list_of_tiles__()
        self.__put_tiles_in_the_board__(self.board, list_tiles)
        self.__put_tiles_in_the_board__(self.board_with_final_state, list_tiles)
        self.__put_tiles_in_dic_positions__(list_tiles)
        self.line_of_empty_position = self.dimension
        self.column_of_empty_position = self.dimension

    def xǁPuzzleGameǁ__init____mutmut_7(self, dimension):
        self.__dimension = dimension
        self.__board = Board(self.dimension, self.dimension)
        self.__board_with_final_state = None
        self.__dic_positions_of_tiles = {}
        list_tiles = self.__generate_list_of_tiles__()
        self.__put_tiles_in_the_board__(self.board, list_tiles)
        self.__put_tiles_in_the_board__(self.board_with_final_state, list_tiles)
        self.__put_tiles_in_dic_positions__(list_tiles)
        self.line_of_empty_position = self.dimension
        self.column_of_empty_position = self.dimension

    def xǁPuzzleGameǁ__init____mutmut_8(self, dimension):
        self.__dimension = dimension
        self.__board = Board(self.dimension, self.dimension)
        self.__board_with_final_state = Board(None, self.dimension)
        self.__dic_positions_of_tiles = {}
        list_tiles = self.__generate_list_of_tiles__()
        self.__put_tiles_in_the_board__(self.board, list_tiles)
        self.__put_tiles_in_the_board__(self.board_with_final_state, list_tiles)
        self.__put_tiles_in_dic_positions__(list_tiles)
        self.line_of_empty_position = self.dimension
        self.column_of_empty_position = self.dimension

    def xǁPuzzleGameǁ__init____mutmut_9(self, dimension):
        self.__dimension = dimension
        self.__board = Board(self.dimension, self.dimension)
        self.__board_with_final_state = Board(self.dimension, None)
        self.__dic_positions_of_tiles = {}
        list_tiles = self.__generate_list_of_tiles__()
        self.__put_tiles_in_the_board__(self.board, list_tiles)
        self.__put_tiles_in_the_board__(self.board_with_final_state, list_tiles)
        self.__put_tiles_in_dic_positions__(list_tiles)
        self.line_of_empty_position = self.dimension
        self.column_of_empty_position = self.dimension

    def xǁPuzzleGameǁ__init____mutmut_10(self, dimension):
        self.__dimension = dimension
        self.__board = Board(self.dimension, self.dimension)
        self.__board_with_final_state = Board(self.dimension)
        self.__dic_positions_of_tiles = {}
        list_tiles = self.__generate_list_of_tiles__()
        self.__put_tiles_in_the_board__(self.board, list_tiles)
        self.__put_tiles_in_the_board__(self.board_with_final_state, list_tiles)
        self.__put_tiles_in_dic_positions__(list_tiles)
        self.line_of_empty_position = self.dimension
        self.column_of_empty_position = self.dimension

    def xǁPuzzleGameǁ__init____mutmut_11(self, dimension):
        self.__dimension = dimension
        self.__board = Board(self.dimension, self.dimension)
        self.__board_with_final_state = Board(self.dimension, )
        self.__dic_positions_of_tiles = {}
        list_tiles = self.__generate_list_of_tiles__()
        self.__put_tiles_in_the_board__(self.board, list_tiles)
        self.__put_tiles_in_the_board__(self.board_with_final_state, list_tiles)
        self.__put_tiles_in_dic_positions__(list_tiles)
        self.line_of_empty_position = self.dimension
        self.column_of_empty_position = self.dimension

    def xǁPuzzleGameǁ__init____mutmut_12(self, dimension):
        self.__dimension = dimension
        self.__board = Board(self.dimension, self.dimension)
        self.__board_with_final_state = Board(self.dimension, self.dimension)
        self.__dic_positions_of_tiles = None
        list_tiles = self.__generate_list_of_tiles__()
        self.__put_tiles_in_the_board__(self.board, list_tiles)
        self.__put_tiles_in_the_board__(self.board_with_final_state, list_tiles)
        self.__put_tiles_in_dic_positions__(list_tiles)
        self.line_of_empty_position = self.dimension
        self.column_of_empty_position = self.dimension

    def xǁPuzzleGameǁ__init____mutmut_13(self, dimension):
        self.__dimension = dimension
        self.__board = Board(self.dimension, self.dimension)
        self.__board_with_final_state = Board(self.dimension, self.dimension)
        self.__dic_positions_of_tiles = {}
        list_tiles = None
        self.__put_tiles_in_the_board__(self.board, list_tiles)
        self.__put_tiles_in_the_board__(self.board_with_final_state, list_tiles)
        self.__put_tiles_in_dic_positions__(list_tiles)
        self.line_of_empty_position = self.dimension
        self.column_of_empty_position = self.dimension

    def xǁPuzzleGameǁ__init____mutmut_14(self, dimension):
        self.__dimension = dimension
        self.__board = Board(self.dimension, self.dimension)
        self.__board_with_final_state = Board(self.dimension, self.dimension)
        self.__dic_positions_of_tiles = {}
        list_tiles = self.__generate_list_of_tiles__()
        self.__put_tiles_in_the_board__(None, list_tiles)
        self.__put_tiles_in_the_board__(self.board_with_final_state, list_tiles)
        self.__put_tiles_in_dic_positions__(list_tiles)
        self.line_of_empty_position = self.dimension
        self.column_of_empty_position = self.dimension

    def xǁPuzzleGameǁ__init____mutmut_15(self, dimension):
        self.__dimension = dimension
        self.__board = Board(self.dimension, self.dimension)
        self.__board_with_final_state = Board(self.dimension, self.dimension)
        self.__dic_positions_of_tiles = {}
        list_tiles = self.__generate_list_of_tiles__()
        self.__put_tiles_in_the_board__(self.board, None)
        self.__put_tiles_in_the_board__(self.board_with_final_state, list_tiles)
        self.__put_tiles_in_dic_positions__(list_tiles)
        self.line_of_empty_position = self.dimension
        self.column_of_empty_position = self.dimension

    def xǁPuzzleGameǁ__init____mutmut_16(self, dimension):
        self.__dimension = dimension
        self.__board = Board(self.dimension, self.dimension)
        self.__board_with_final_state = Board(self.dimension, self.dimension)
        self.__dic_positions_of_tiles = {}
        list_tiles = self.__generate_list_of_tiles__()
        self.__put_tiles_in_the_board__(list_tiles)
        self.__put_tiles_in_the_board__(self.board_with_final_state, list_tiles)
        self.__put_tiles_in_dic_positions__(list_tiles)
        self.line_of_empty_position = self.dimension
        self.column_of_empty_position = self.dimension

    def xǁPuzzleGameǁ__init____mutmut_17(self, dimension):
        self.__dimension = dimension
        self.__board = Board(self.dimension, self.dimension)
        self.__board_with_final_state = Board(self.dimension, self.dimension)
        self.__dic_positions_of_tiles = {}
        list_tiles = self.__generate_list_of_tiles__()
        self.__put_tiles_in_the_board__(self.board, )
        self.__put_tiles_in_the_board__(self.board_with_final_state, list_tiles)
        self.__put_tiles_in_dic_positions__(list_tiles)
        self.line_of_empty_position = self.dimension
        self.column_of_empty_position = self.dimension

    def xǁPuzzleGameǁ__init____mutmut_18(self, dimension):
        self.__dimension = dimension
        self.__board = Board(self.dimension, self.dimension)
        self.__board_with_final_state = Board(self.dimension, self.dimension)
        self.__dic_positions_of_tiles = {}
        list_tiles = self.__generate_list_of_tiles__()
        self.__put_tiles_in_the_board__(self.board, list_tiles)
        self.__put_tiles_in_the_board__(None, list_tiles)
        self.__put_tiles_in_dic_positions__(list_tiles)
        self.line_of_empty_position = self.dimension
        self.column_of_empty_position = self.dimension

    def xǁPuzzleGameǁ__init____mutmut_19(self, dimension):
        self.__dimension = dimension
        self.__board = Board(self.dimension, self.dimension)
        self.__board_with_final_state = Board(self.dimension, self.dimension)
        self.__dic_positions_of_tiles = {}
        list_tiles = self.__generate_list_of_tiles__()
        self.__put_tiles_in_the_board__(self.board, list_tiles)
        self.__put_tiles_in_the_board__(self.board_with_final_state, None)
        self.__put_tiles_in_dic_positions__(list_tiles)
        self.line_of_empty_position = self.dimension
        self.column_of_empty_position = self.dimension

    def xǁPuzzleGameǁ__init____mutmut_20(self, dimension):
        self.__dimension = dimension
        self.__board = Board(self.dimension, self.dimension)
        self.__board_with_final_state = Board(self.dimension, self.dimension)
        self.__dic_positions_of_tiles = {}
        list_tiles = self.__generate_list_of_tiles__()
        self.__put_tiles_in_the_board__(self.board, list_tiles)
        self.__put_tiles_in_the_board__(list_tiles)
        self.__put_tiles_in_dic_positions__(list_tiles)
        self.line_of_empty_position = self.dimension
        self.column_of_empty_position = self.dimension

    def xǁPuzzleGameǁ__init____mutmut_21(self, dimension):
        self.__dimension = dimension
        self.__board = Board(self.dimension, self.dimension)
        self.__board_with_final_state = Board(self.dimension, self.dimension)
        self.__dic_positions_of_tiles = {}
        list_tiles = self.__generate_list_of_tiles__()
        self.__put_tiles_in_the_board__(self.board, list_tiles)
        self.__put_tiles_in_the_board__(self.board_with_final_state, )
        self.__put_tiles_in_dic_positions__(list_tiles)
        self.line_of_empty_position = self.dimension
        self.column_of_empty_position = self.dimension

    def xǁPuzzleGameǁ__init____mutmut_22(self, dimension):
        self.__dimension = dimension
        self.__board = Board(self.dimension, self.dimension)
        self.__board_with_final_state = Board(self.dimension, self.dimension)
        self.__dic_positions_of_tiles = {}
        list_tiles = self.__generate_list_of_tiles__()
        self.__put_tiles_in_the_board__(self.board, list_tiles)
        self.__put_tiles_in_the_board__(self.board_with_final_state, list_tiles)
        self.__put_tiles_in_dic_positions__(None)
        self.line_of_empty_position = self.dimension
        self.column_of_empty_position = self.dimension

    def xǁPuzzleGameǁ__init____mutmut_23(self, dimension):
        self.__dimension = dimension
        self.__board = Board(self.dimension, self.dimension)
        self.__board_with_final_state = Board(self.dimension, self.dimension)
        self.__dic_positions_of_tiles = {}
        list_tiles = self.__generate_list_of_tiles__()
        self.__put_tiles_in_the_board__(self.board, list_tiles)
        self.__put_tiles_in_the_board__(self.board_with_final_state, list_tiles)
        self.__put_tiles_in_dic_positions__(list_tiles)
        self.line_of_empty_position = None
        self.column_of_empty_position = self.dimension

    def xǁPuzzleGameǁ__init____mutmut_24(self, dimension):
        self.__dimension = dimension
        self.__board = Board(self.dimension, self.dimension)
        self.__board_with_final_state = Board(self.dimension, self.dimension)
        self.__dic_positions_of_tiles = {}
        list_tiles = self.__generate_list_of_tiles__()
        self.__put_tiles_in_the_board__(self.board, list_tiles)
        self.__put_tiles_in_the_board__(self.board_with_final_state, list_tiles)
        self.__put_tiles_in_dic_positions__(list_tiles)
        self.line_of_empty_position = self.dimension
        self.column_of_empty_position = None
    
    xǁPuzzleGameǁ__init____mutmut_mutants : ClassVar[MutantDict] = {
    'xǁPuzzleGameǁ__init____mutmut_1': xǁPuzzleGameǁ__init____mutmut_1, 
        'xǁPuzzleGameǁ__init____mutmut_2': xǁPuzzleGameǁ__init____mutmut_2, 
        'xǁPuzzleGameǁ__init____mutmut_3': xǁPuzzleGameǁ__init____mutmut_3, 
        'xǁPuzzleGameǁ__init____mutmut_4': xǁPuzzleGameǁ__init____mutmut_4, 
        'xǁPuzzleGameǁ__init____mutmut_5': xǁPuzzleGameǁ__init____mutmut_5, 
        'xǁPuzzleGameǁ__init____mutmut_6': xǁPuzzleGameǁ__init____mutmut_6, 
        'xǁPuzzleGameǁ__init____mutmut_7': xǁPuzzleGameǁ__init____mutmut_7, 
        'xǁPuzzleGameǁ__init____mutmut_8': xǁPuzzleGameǁ__init____mutmut_8, 
        'xǁPuzzleGameǁ__init____mutmut_9': xǁPuzzleGameǁ__init____mutmut_9, 
        'xǁPuzzleGameǁ__init____mutmut_10': xǁPuzzleGameǁ__init____mutmut_10, 
        'xǁPuzzleGameǁ__init____mutmut_11': xǁPuzzleGameǁ__init____mutmut_11, 
        'xǁPuzzleGameǁ__init____mutmut_12': xǁPuzzleGameǁ__init____mutmut_12, 
        'xǁPuzzleGameǁ__init____mutmut_13': xǁPuzzleGameǁ__init____mutmut_13, 
        'xǁPuzzleGameǁ__init____mutmut_14': xǁPuzzleGameǁ__init____mutmut_14, 
        'xǁPuzzleGameǁ__init____mutmut_15': xǁPuzzleGameǁ__init____mutmut_15, 
        'xǁPuzzleGameǁ__init____mutmut_16': xǁPuzzleGameǁ__init____mutmut_16, 
        'xǁPuzzleGameǁ__init____mutmut_17': xǁPuzzleGameǁ__init____mutmut_17, 
        'xǁPuzzleGameǁ__init____mutmut_18': xǁPuzzleGameǁ__init____mutmut_18, 
        'xǁPuzzleGameǁ__init____mutmut_19': xǁPuzzleGameǁ__init____mutmut_19, 
        'xǁPuzzleGameǁ__init____mutmut_20': xǁPuzzleGameǁ__init____mutmut_20, 
        'xǁPuzzleGameǁ__init____mutmut_21': xǁPuzzleGameǁ__init____mutmut_21, 
        'xǁPuzzleGameǁ__init____mutmut_22': xǁPuzzleGameǁ__init____mutmut_22, 
        'xǁPuzzleGameǁ__init____mutmut_23': xǁPuzzleGameǁ__init____mutmut_23, 
        'xǁPuzzleGameǁ__init____mutmut_24': xǁPuzzleGameǁ__init____mutmut_24
    }
    
    def __init__(self, *args, **kwargs):
        result = _mutmut_trampoline(object.__getattribute__(self, "xǁPuzzleGameǁ__init____mutmut_orig"), object.__getattribute__(self, "xǁPuzzleGameǁ__init____mutmut_mutants"), args, kwargs, self)
        return result 
    
    __init__.__signature__ = _mutmut_signature(xǁPuzzleGameǁ__init____mutmut_orig)
    xǁPuzzleGameǁ__init____mutmut_orig.__name__ = 'xǁPuzzleGameǁ__init__'

    @property
    def dimension(self):
        return self.__dimension

    @property
    def board(self):
        return self.__board

    @property
    def board_with_final_state(self):
        return self.__board_with_final_state

    @property
    def dic_positions_of_tiles(self):
        return self.__dic_positions_of_tiles

    def xǁPuzzleGameǁ__generate_list_of_tiles____mutmut_orig(self):
        list_of_tiles = []
        quantity_of_tiles = self.dimension * self.dimension - 1
        for tile in range(1, quantity_of_tiles+1):
            list_of_tiles.append(tile)
        return list_of_tiles

    def xǁPuzzleGameǁ__generate_list_of_tiles____mutmut_1(self):
        list_of_tiles = None
        quantity_of_tiles = self.dimension * self.dimension - 1
        for tile in range(1, quantity_of_tiles+1):
            list_of_tiles.append(tile)
        return list_of_tiles

    def xǁPuzzleGameǁ__generate_list_of_tiles____mutmut_2(self):
        list_of_tiles = []
        quantity_of_tiles = None
        for tile in range(1, quantity_of_tiles+1):
            list_of_tiles.append(tile)
        return list_of_tiles

    def xǁPuzzleGameǁ__generate_list_of_tiles____mutmut_3(self):
        list_of_tiles = []
        quantity_of_tiles = self.dimension * self.dimension + 1
        for tile in range(1, quantity_of_tiles+1):
            list_of_tiles.append(tile)
        return list_of_tiles

    def xǁPuzzleGameǁ__generate_list_of_tiles____mutmut_4(self):
        list_of_tiles = []
        quantity_of_tiles = self.dimension / self.dimension - 1
        for tile in range(1, quantity_of_tiles+1):
            list_of_tiles.append(tile)
        return list_of_tiles

    def xǁPuzzleGameǁ__generate_list_of_tiles____mutmut_5(self):
        list_of_tiles = []
        quantity_of_tiles = self.dimension * self.dimension - 2
        for tile in range(1, quantity_of_tiles+1):
            list_of_tiles.append(tile)
        return list_of_tiles

    def xǁPuzzleGameǁ__generate_list_of_tiles____mutmut_6(self):
        list_of_tiles = []
        quantity_of_tiles = self.dimension * self.dimension - 1
        for tile in range(None, quantity_of_tiles+1):
            list_of_tiles.append(tile)
        return list_of_tiles

    def xǁPuzzleGameǁ__generate_list_of_tiles____mutmut_7(self):
        list_of_tiles = []
        quantity_of_tiles = self.dimension * self.dimension - 1
        for tile in range(1, None):
            list_of_tiles.append(tile)
        return list_of_tiles

    def xǁPuzzleGameǁ__generate_list_of_tiles____mutmut_8(self):
        list_of_tiles = []
        quantity_of_tiles = self.dimension * self.dimension - 1
        for tile in range(quantity_of_tiles+1):
            list_of_tiles.append(tile)
        return list_of_tiles

    def xǁPuzzleGameǁ__generate_list_of_tiles____mutmut_9(self):
        list_of_tiles = []
        quantity_of_tiles = self.dimension * self.dimension - 1
        for tile in range(1, ):
            list_of_tiles.append(tile)
        return list_of_tiles

    def xǁPuzzleGameǁ__generate_list_of_tiles____mutmut_10(self):
        list_of_tiles = []
        quantity_of_tiles = self.dimension * self.dimension - 1
        for tile in range(2, quantity_of_tiles+1):
            list_of_tiles.append(tile)
        return list_of_tiles

    def xǁPuzzleGameǁ__generate_list_of_tiles____mutmut_11(self):
        list_of_tiles = []
        quantity_of_tiles = self.dimension * self.dimension - 1
        for tile in range(1, quantity_of_tiles - 1):
            list_of_tiles.append(tile)
        return list_of_tiles

    def xǁPuzzleGameǁ__generate_list_of_tiles____mutmut_12(self):
        list_of_tiles = []
        quantity_of_tiles = self.dimension * self.dimension - 1
        for tile in range(1, quantity_of_tiles+2):
            list_of_tiles.append(tile)
        return list_of_tiles

    def xǁPuzzleGameǁ__generate_list_of_tiles____mutmut_13(self):
        list_of_tiles = []
        quantity_of_tiles = self.dimension * self.dimension - 1
        for tile in range(1, quantity_of_tiles+1):
            list_of_tiles.append(None)
        return list_of_tiles
    
    xǁPuzzleGameǁ__generate_list_of_tiles____mutmut_mutants : ClassVar[MutantDict] = {
    'xǁPuzzleGameǁ__generate_list_of_tiles____mutmut_1': xǁPuzzleGameǁ__generate_list_of_tiles____mutmut_1, 
        'xǁPuzzleGameǁ__generate_list_of_tiles____mutmut_2': xǁPuzzleGameǁ__generate_list_of_tiles____mutmut_2, 
        'xǁPuzzleGameǁ__generate_list_of_tiles____mutmut_3': xǁPuzzleGameǁ__generate_list_of_tiles____mutmut_3, 
        'xǁPuzzleGameǁ__generate_list_of_tiles____mutmut_4': xǁPuzzleGameǁ__generate_list_of_tiles____mutmut_4, 
        'xǁPuzzleGameǁ__generate_list_of_tiles____mutmut_5': xǁPuzzleGameǁ__generate_list_of_tiles____mutmut_5, 
        'xǁPuzzleGameǁ__generate_list_of_tiles____mutmut_6': xǁPuzzleGameǁ__generate_list_of_tiles____mutmut_6, 
        'xǁPuzzleGameǁ__generate_list_of_tiles____mutmut_7': xǁPuzzleGameǁ__generate_list_of_tiles____mutmut_7, 
        'xǁPuzzleGameǁ__generate_list_of_tiles____mutmut_8': xǁPuzzleGameǁ__generate_list_of_tiles____mutmut_8, 
        'xǁPuzzleGameǁ__generate_list_of_tiles____mutmut_9': xǁPuzzleGameǁ__generate_list_of_tiles____mutmut_9, 
        'xǁPuzzleGameǁ__generate_list_of_tiles____mutmut_10': xǁPuzzleGameǁ__generate_list_of_tiles____mutmut_10, 
        'xǁPuzzleGameǁ__generate_list_of_tiles____mutmut_11': xǁPuzzleGameǁ__generate_list_of_tiles____mutmut_11, 
        'xǁPuzzleGameǁ__generate_list_of_tiles____mutmut_12': xǁPuzzleGameǁ__generate_list_of_tiles____mutmut_12, 
        'xǁPuzzleGameǁ__generate_list_of_tiles____mutmut_13': xǁPuzzleGameǁ__generate_list_of_tiles____mutmut_13
    }
    
    def __generate_list_of_tiles__(self, *args, **kwargs):
        result = _mutmut_trampoline(object.__getattribute__(self, "xǁPuzzleGameǁ__generate_list_of_tiles____mutmut_orig"), object.__getattribute__(self, "xǁPuzzleGameǁ__generate_list_of_tiles____mutmut_mutants"), args, kwargs, self)
        return result 
    
    __generate_list_of_tiles__.__signature__ = _mutmut_signature(xǁPuzzleGameǁ__generate_list_of_tiles____mutmut_orig)
    xǁPuzzleGameǁ__generate_list_of_tiles____mutmut_orig.__name__ = 'xǁPuzzleGameǁ__generate_list_of_tiles__'

    def xǁPuzzleGameǁ__put_tiles_in_the_board____mutmut_orig(self, board, list_tiles):
        iterator_tiles = iter(list_tiles)
        for line in range(1, self.dimension):  # from first line to the line before the last
            for column in range(1, self.dimension + 1):
                board.put_tile(next(iterator_tiles), line, column)
        for column in range(1, self.dimension):  # last line
            board.put_tile(next(iterator_tiles), self.dimension, column)

    def xǁPuzzleGameǁ__put_tiles_in_the_board____mutmut_1(self, board, list_tiles):
        iterator_tiles = None
        for line in range(1, self.dimension):  # from first line to the line before the last
            for column in range(1, self.dimension + 1):
                board.put_tile(next(iterator_tiles), line, column)
        for column in range(1, self.dimension):  # last line
            board.put_tile(next(iterator_tiles), self.dimension, column)

    def xǁPuzzleGameǁ__put_tiles_in_the_board____mutmut_2(self, board, list_tiles):
        iterator_tiles = iter(None)
        for line in range(1, self.dimension):  # from first line to the line before the last
            for column in range(1, self.dimension + 1):
                board.put_tile(next(iterator_tiles), line, column)
        for column in range(1, self.dimension):  # last line
            board.put_tile(next(iterator_tiles), self.dimension, column)

    def xǁPuzzleGameǁ__put_tiles_in_the_board____mutmut_3(self, board, list_tiles):
        iterator_tiles = iter(list_tiles)
        for line in range(None, self.dimension):  # from first line to the line before the last
            for column in range(1, self.dimension + 1):
                board.put_tile(next(iterator_tiles), line, column)
        for column in range(1, self.dimension):  # last line
            board.put_tile(next(iterator_tiles), self.dimension, column)

    def xǁPuzzleGameǁ__put_tiles_in_the_board____mutmut_4(self, board, list_tiles):
        iterator_tiles = iter(list_tiles)
        for line in range(1, None):  # from first line to the line before the last
            for column in range(1, self.dimension + 1):
                board.put_tile(next(iterator_tiles), line, column)
        for column in range(1, self.dimension):  # last line
            board.put_tile(next(iterator_tiles), self.dimension, column)

    def xǁPuzzleGameǁ__put_tiles_in_the_board____mutmut_5(self, board, list_tiles):
        iterator_tiles = iter(list_tiles)
        for line in range(self.dimension):  # from first line to the line before the last
            for column in range(1, self.dimension + 1):
                board.put_tile(next(iterator_tiles), line, column)
        for column in range(1, self.dimension):  # last line
            board.put_tile(next(iterator_tiles), self.dimension, column)

    def xǁPuzzleGameǁ__put_tiles_in_the_board____mutmut_6(self, board, list_tiles):
        iterator_tiles = iter(list_tiles)
        for line in range(1, ):  # from first line to the line before the last
            for column in range(1, self.dimension + 1):
                board.put_tile(next(iterator_tiles), line, column)
        for column in range(1, self.dimension):  # last line
            board.put_tile(next(iterator_tiles), self.dimension, column)

    def xǁPuzzleGameǁ__put_tiles_in_the_board____mutmut_7(self, board, list_tiles):
        iterator_tiles = iter(list_tiles)
        for line in range(2, self.dimension):  # from first line to the line before the last
            for column in range(1, self.dimension + 1):
                board.put_tile(next(iterator_tiles), line, column)
        for column in range(1, self.dimension):  # last line
            board.put_tile(next(iterator_tiles), self.dimension, column)

    def xǁPuzzleGameǁ__put_tiles_in_the_board____mutmut_8(self, board, list_tiles):
        iterator_tiles = iter(list_tiles)
        for line in range(1, self.dimension):  # from first line to the line before the last
            for column in range(None, self.dimension + 1):
                board.put_tile(next(iterator_tiles), line, column)
        for column in range(1, self.dimension):  # last line
            board.put_tile(next(iterator_tiles), self.dimension, column)

    def xǁPuzzleGameǁ__put_tiles_in_the_board____mutmut_9(self, board, list_tiles):
        iterator_tiles = iter(list_tiles)
        for line in range(1, self.dimension):  # from first line to the line before the last
            for column in range(1, None):
                board.put_tile(next(iterator_tiles), line, column)
        for column in range(1, self.dimension):  # last line
            board.put_tile(next(iterator_tiles), self.dimension, column)

    def xǁPuzzleGameǁ__put_tiles_in_the_board____mutmut_10(self, board, list_tiles):
        iterator_tiles = iter(list_tiles)
        for line in range(1, self.dimension):  # from first line to the line before the last
            for column in range(self.dimension + 1):
                board.put_tile(next(iterator_tiles), line, column)
        for column in range(1, self.dimension):  # last line
            board.put_tile(next(iterator_tiles), self.dimension, column)

    def xǁPuzzleGameǁ__put_tiles_in_the_board____mutmut_11(self, board, list_tiles):
        iterator_tiles = iter(list_tiles)
        for line in range(1, self.dimension):  # from first line to the line before the last
            for column in range(1, ):
                board.put_tile(next(iterator_tiles), line, column)
        for column in range(1, self.dimension):  # last line
            board.put_tile(next(iterator_tiles), self.dimension, column)

    def xǁPuzzleGameǁ__put_tiles_in_the_board____mutmut_12(self, board, list_tiles):
        iterator_tiles = iter(list_tiles)
        for line in range(1, self.dimension):  # from first line to the line before the last
            for column in range(2, self.dimension + 1):
                board.put_tile(next(iterator_tiles), line, column)
        for column in range(1, self.dimension):  # last line
            board.put_tile(next(iterator_tiles), self.dimension, column)

    def xǁPuzzleGameǁ__put_tiles_in_the_board____mutmut_13(self, board, list_tiles):
        iterator_tiles = iter(list_tiles)
        for line in range(1, self.dimension):  # from first line to the line before the last
            for column in range(1, self.dimension - 1):
                board.put_tile(next(iterator_tiles), line, column)
        for column in range(1, self.dimension):  # last line
            board.put_tile(next(iterator_tiles), self.dimension, column)

    def xǁPuzzleGameǁ__put_tiles_in_the_board____mutmut_14(self, board, list_tiles):
        iterator_tiles = iter(list_tiles)
        for line in range(1, self.dimension):  # from first line to the line before the last
            for column in range(1, self.dimension + 2):
                board.put_tile(next(iterator_tiles), line, column)
        for column in range(1, self.dimension):  # last line
            board.put_tile(next(iterator_tiles), self.dimension, column)

    def xǁPuzzleGameǁ__put_tiles_in_the_board____mutmut_15(self, board, list_tiles):
        iterator_tiles = iter(list_tiles)
        for line in range(1, self.dimension):  # from first line to the line before the last
            for column in range(1, self.dimension + 1):
                board.put_tile(None, line, column)
        for column in range(1, self.dimension):  # last line
            board.put_tile(next(iterator_tiles), self.dimension, column)

    def xǁPuzzleGameǁ__put_tiles_in_the_board____mutmut_16(self, board, list_tiles):
        iterator_tiles = iter(list_tiles)
        for line in range(1, self.dimension):  # from first line to the line before the last
            for column in range(1, self.dimension + 1):
                board.put_tile(next(iterator_tiles), None, column)
        for column in range(1, self.dimension):  # last line
            board.put_tile(next(iterator_tiles), self.dimension, column)

    def xǁPuzzleGameǁ__put_tiles_in_the_board____mutmut_17(self, board, list_tiles):
        iterator_tiles = iter(list_tiles)
        for line in range(1, self.dimension):  # from first line to the line before the last
            for column in range(1, self.dimension + 1):
                board.put_tile(next(iterator_tiles), line, None)
        for column in range(1, self.dimension):  # last line
            board.put_tile(next(iterator_tiles), self.dimension, column)

    def xǁPuzzleGameǁ__put_tiles_in_the_board____mutmut_18(self, board, list_tiles):
        iterator_tiles = iter(list_tiles)
        for line in range(1, self.dimension):  # from first line to the line before the last
            for column in range(1, self.dimension + 1):
                board.put_tile(line, column)
        for column in range(1, self.dimension):  # last line
            board.put_tile(next(iterator_tiles), self.dimension, column)

    def xǁPuzzleGameǁ__put_tiles_in_the_board____mutmut_19(self, board, list_tiles):
        iterator_tiles = iter(list_tiles)
        for line in range(1, self.dimension):  # from first line to the line before the last
            for column in range(1, self.dimension + 1):
                board.put_tile(next(iterator_tiles), column)
        for column in range(1, self.dimension):  # last line
            board.put_tile(next(iterator_tiles), self.dimension, column)

    def xǁPuzzleGameǁ__put_tiles_in_the_board____mutmut_20(self, board, list_tiles):
        iterator_tiles = iter(list_tiles)
        for line in range(1, self.dimension):  # from first line to the line before the last
            for column in range(1, self.dimension + 1):
                board.put_tile(next(iterator_tiles), line, )
        for column in range(1, self.dimension):  # last line
            board.put_tile(next(iterator_tiles), self.dimension, column)

    def xǁPuzzleGameǁ__put_tiles_in_the_board____mutmut_21(self, board, list_tiles):
        iterator_tiles = iter(list_tiles)
        for line in range(1, self.dimension):  # from first line to the line before the last
            for column in range(1, self.dimension + 1):
                board.put_tile(next(None), line, column)
        for column in range(1, self.dimension):  # last line
            board.put_tile(next(iterator_tiles), self.dimension, column)

    def xǁPuzzleGameǁ__put_tiles_in_the_board____mutmut_22(self, board, list_tiles):
        iterator_tiles = iter(list_tiles)
        for line in range(1, self.dimension):  # from first line to the line before the last
            for column in range(1, self.dimension + 1):
                board.put_tile(next(iterator_tiles), line, column)
        for column in range(None, self.dimension):  # last line
            board.put_tile(next(iterator_tiles), self.dimension, column)

    def xǁPuzzleGameǁ__put_tiles_in_the_board____mutmut_23(self, board, list_tiles):
        iterator_tiles = iter(list_tiles)
        for line in range(1, self.dimension):  # from first line to the line before the last
            for column in range(1, self.dimension + 1):
                board.put_tile(next(iterator_tiles), line, column)
        for column in range(1, None):  # last line
            board.put_tile(next(iterator_tiles), self.dimension, column)

    def xǁPuzzleGameǁ__put_tiles_in_the_board____mutmut_24(self, board, list_tiles):
        iterator_tiles = iter(list_tiles)
        for line in range(1, self.dimension):  # from first line to the line before the last
            for column in range(1, self.dimension + 1):
                board.put_tile(next(iterator_tiles), line, column)
        for column in range(self.dimension):  # last line
            board.put_tile(next(iterator_tiles), self.dimension, column)

    def xǁPuzzleGameǁ__put_tiles_in_the_board____mutmut_25(self, board, list_tiles):
        iterator_tiles = iter(list_tiles)
        for line in range(1, self.dimension):  # from first line to the line before the last
            for column in range(1, self.dimension + 1):
                board.put_tile(next(iterator_tiles), line, column)
        for column in range(1, ):  # last line
            board.put_tile(next(iterator_tiles), self.dimension, column)

    def xǁPuzzleGameǁ__put_tiles_in_the_board____mutmut_26(self, board, list_tiles):
        iterator_tiles = iter(list_tiles)
        for line in range(1, self.dimension):  # from first line to the line before the last
            for column in range(1, self.dimension + 1):
                board.put_tile(next(iterator_tiles), line, column)
        for column in range(2, self.dimension):  # last line
            board.put_tile(next(iterator_tiles), self.dimension, column)

    def xǁPuzzleGameǁ__put_tiles_in_the_board____mutmut_27(self, board, list_tiles):
        iterator_tiles = iter(list_tiles)
        for line in range(1, self.dimension):  # from first line to the line before the last
            for column in range(1, self.dimension + 1):
                board.put_tile(next(iterator_tiles), line, column)
        for column in range(1, self.dimension):  # last line
            board.put_tile(None, self.dimension, column)

    def xǁPuzzleGameǁ__put_tiles_in_the_board____mutmut_28(self, board, list_tiles):
        iterator_tiles = iter(list_tiles)
        for line in range(1, self.dimension):  # from first line to the line before the last
            for column in range(1, self.dimension + 1):
                board.put_tile(next(iterator_tiles), line, column)
        for column in range(1, self.dimension):  # last line
            board.put_tile(next(iterator_tiles), None, column)

    def xǁPuzzleGameǁ__put_tiles_in_the_board____mutmut_29(self, board, list_tiles):
        iterator_tiles = iter(list_tiles)
        for line in range(1, self.dimension):  # from first line to the line before the last
            for column in range(1, self.dimension + 1):
                board.put_tile(next(iterator_tiles), line, column)
        for column in range(1, self.dimension):  # last line
            board.put_tile(next(iterator_tiles), self.dimension, None)

    def xǁPuzzleGameǁ__put_tiles_in_the_board____mutmut_30(self, board, list_tiles):
        iterator_tiles = iter(list_tiles)
        for line in range(1, self.dimension):  # from first line to the line before the last
            for column in range(1, self.dimension + 1):
                board.put_tile(next(iterator_tiles), line, column)
        for column in range(1, self.dimension):  # last line
            board.put_tile(self.dimension, column)

    def xǁPuzzleGameǁ__put_tiles_in_the_board____mutmut_31(self, board, list_tiles):
        iterator_tiles = iter(list_tiles)
        for line in range(1, self.dimension):  # from first line to the line before the last
            for column in range(1, self.dimension + 1):
                board.put_tile(next(iterator_tiles), line, column)
        for column in range(1, self.dimension):  # last line
            board.put_tile(next(iterator_tiles), column)

    def xǁPuzzleGameǁ__put_tiles_in_the_board____mutmut_32(self, board, list_tiles):
        iterator_tiles = iter(list_tiles)
        for line in range(1, self.dimension):  # from first line to the line before the last
            for column in range(1, self.dimension + 1):
                board.put_tile(next(iterator_tiles), line, column)
        for column in range(1, self.dimension):  # last line
            board.put_tile(next(iterator_tiles), self.dimension, )

    def xǁPuzzleGameǁ__put_tiles_in_the_board____mutmut_33(self, board, list_tiles):
        iterator_tiles = iter(list_tiles)
        for line in range(1, self.dimension):  # from first line to the line before the last
            for column in range(1, self.dimension + 1):
                board.put_tile(next(iterator_tiles), line, column)
        for column in range(1, self.dimension):  # last line
            board.put_tile(next(None), self.dimension, column)
    
    xǁPuzzleGameǁ__put_tiles_in_the_board____mutmut_mutants : ClassVar[MutantDict] = {
    'xǁPuzzleGameǁ__put_tiles_in_the_board____mutmut_1': xǁPuzzleGameǁ__put_tiles_in_the_board____mutmut_1, 
        'xǁPuzzleGameǁ__put_tiles_in_the_board____mutmut_2': xǁPuzzleGameǁ__put_tiles_in_the_board____mutmut_2, 
        'xǁPuzzleGameǁ__put_tiles_in_the_board____mutmut_3': xǁPuzzleGameǁ__put_tiles_in_the_board____mutmut_3, 
        'xǁPuzzleGameǁ__put_tiles_in_the_board____mutmut_4': xǁPuzzleGameǁ__put_tiles_in_the_board____mutmut_4, 
        'xǁPuzzleGameǁ__put_tiles_in_the_board____mutmut_5': xǁPuzzleGameǁ__put_tiles_in_the_board____mutmut_5, 
        'xǁPuzzleGameǁ__put_tiles_in_the_board____mutmut_6': xǁPuzzleGameǁ__put_tiles_in_the_board____mutmut_6, 
        'xǁPuzzleGameǁ__put_tiles_in_the_board____mutmut_7': xǁPuzzleGameǁ__put_tiles_in_the_board____mutmut_7, 
        'xǁPuzzleGameǁ__put_tiles_in_the_board____mutmut_8': xǁPuzzleGameǁ__put_tiles_in_the_board____mutmut_8, 
        'xǁPuzzleGameǁ__put_tiles_in_the_board____mutmut_9': xǁPuzzleGameǁ__put_tiles_in_the_board____mutmut_9, 
        'xǁPuzzleGameǁ__put_tiles_in_the_board____mutmut_10': xǁPuzzleGameǁ__put_tiles_in_the_board____mutmut_10, 
        'xǁPuzzleGameǁ__put_tiles_in_the_board____mutmut_11': xǁPuzzleGameǁ__put_tiles_in_the_board____mutmut_11, 
        'xǁPuzzleGameǁ__put_tiles_in_the_board____mutmut_12': xǁPuzzleGameǁ__put_tiles_in_the_board____mutmut_12, 
        'xǁPuzzleGameǁ__put_tiles_in_the_board____mutmut_13': xǁPuzzleGameǁ__put_tiles_in_the_board____mutmut_13, 
        'xǁPuzzleGameǁ__put_tiles_in_the_board____mutmut_14': xǁPuzzleGameǁ__put_tiles_in_the_board____mutmut_14, 
        'xǁPuzzleGameǁ__put_tiles_in_the_board____mutmut_15': xǁPuzzleGameǁ__put_tiles_in_the_board____mutmut_15, 
        'xǁPuzzleGameǁ__put_tiles_in_the_board____mutmut_16': xǁPuzzleGameǁ__put_tiles_in_the_board____mutmut_16, 
        'xǁPuzzleGameǁ__put_tiles_in_the_board____mutmut_17': xǁPuzzleGameǁ__put_tiles_in_the_board____mutmut_17, 
        'xǁPuzzleGameǁ__put_tiles_in_the_board____mutmut_18': xǁPuzzleGameǁ__put_tiles_in_the_board____mutmut_18, 
        'xǁPuzzleGameǁ__put_tiles_in_the_board____mutmut_19': xǁPuzzleGameǁ__put_tiles_in_the_board____mutmut_19, 
        'xǁPuzzleGameǁ__put_tiles_in_the_board____mutmut_20': xǁPuzzleGameǁ__put_tiles_in_the_board____mutmut_20, 
        'xǁPuzzleGameǁ__put_tiles_in_the_board____mutmut_21': xǁPuzzleGameǁ__put_tiles_in_the_board____mutmut_21, 
        'xǁPuzzleGameǁ__put_tiles_in_the_board____mutmut_22': xǁPuzzleGameǁ__put_tiles_in_the_board____mutmut_22, 
        'xǁPuzzleGameǁ__put_tiles_in_the_board____mutmut_23': xǁPuzzleGameǁ__put_tiles_in_the_board____mutmut_23, 
        'xǁPuzzleGameǁ__put_tiles_in_the_board____mutmut_24': xǁPuzzleGameǁ__put_tiles_in_the_board____mutmut_24, 
        'xǁPuzzleGameǁ__put_tiles_in_the_board____mutmut_25': xǁPuzzleGameǁ__put_tiles_in_the_board____mutmut_25, 
        'xǁPuzzleGameǁ__put_tiles_in_the_board____mutmut_26': xǁPuzzleGameǁ__put_tiles_in_the_board____mutmut_26, 
        'xǁPuzzleGameǁ__put_tiles_in_the_board____mutmut_27': xǁPuzzleGameǁ__put_tiles_in_the_board____mutmut_27, 
        'xǁPuzzleGameǁ__put_tiles_in_the_board____mutmut_28': xǁPuzzleGameǁ__put_tiles_in_the_board____mutmut_28, 
        'xǁPuzzleGameǁ__put_tiles_in_the_board____mutmut_29': xǁPuzzleGameǁ__put_tiles_in_the_board____mutmut_29, 
        'xǁPuzzleGameǁ__put_tiles_in_the_board____mutmut_30': xǁPuzzleGameǁ__put_tiles_in_the_board____mutmut_30, 
        'xǁPuzzleGameǁ__put_tiles_in_the_board____mutmut_31': xǁPuzzleGameǁ__put_tiles_in_the_board____mutmut_31, 
        'xǁPuzzleGameǁ__put_tiles_in_the_board____mutmut_32': xǁPuzzleGameǁ__put_tiles_in_the_board____mutmut_32, 
        'xǁPuzzleGameǁ__put_tiles_in_the_board____mutmut_33': xǁPuzzleGameǁ__put_tiles_in_the_board____mutmut_33
    }
    
    def __put_tiles_in_the_board__(self, *args, **kwargs):
        result = _mutmut_trampoline(object.__getattribute__(self, "xǁPuzzleGameǁ__put_tiles_in_the_board____mutmut_orig"), object.__getattribute__(self, "xǁPuzzleGameǁ__put_tiles_in_the_board____mutmut_mutants"), args, kwargs, self)
        return result 
    
    __put_tiles_in_the_board__.__signature__ = _mutmut_signature(xǁPuzzleGameǁ__put_tiles_in_the_board____mutmut_orig)
    xǁPuzzleGameǁ__put_tiles_in_the_board____mutmut_orig.__name__ = 'xǁPuzzleGameǁ__put_tiles_in_the_board__'

    def xǁPuzzleGameǁ__put_tiles_in_dic_positions____mutmut_orig(self, list_tiles):
        iterator_tiles = iter(list_tiles)
        for line in range(1, self.dimension):  # from first line to the line before the last
            for column in range(1, self.dimension + 1):
                self.dic_positions_of_tiles.update({next(iterator_tiles): (line, column)})
        for column in range(1, self.dimension):  # last line
            self.dic_positions_of_tiles.update({next(iterator_tiles): (self.dimension, column)})

    def xǁPuzzleGameǁ__put_tiles_in_dic_positions____mutmut_1(self, list_tiles):
        iterator_tiles = None
        for line in range(1, self.dimension):  # from first line to the line before the last
            for column in range(1, self.dimension + 1):
                self.dic_positions_of_tiles.update({next(iterator_tiles): (line, column)})
        for column in range(1, self.dimension):  # last line
            self.dic_positions_of_tiles.update({next(iterator_tiles): (self.dimension, column)})

    def xǁPuzzleGameǁ__put_tiles_in_dic_positions____mutmut_2(self, list_tiles):
        iterator_tiles = iter(None)
        for line in range(1, self.dimension):  # from first line to the line before the last
            for column in range(1, self.dimension + 1):
                self.dic_positions_of_tiles.update({next(iterator_tiles): (line, column)})
        for column in range(1, self.dimension):  # last line
            self.dic_positions_of_tiles.update({next(iterator_tiles): (self.dimension, column)})

    def xǁPuzzleGameǁ__put_tiles_in_dic_positions____mutmut_3(self, list_tiles):
        iterator_tiles = iter(list_tiles)
        for line in range(None, self.dimension):  # from first line to the line before the last
            for column in range(1, self.dimension + 1):
                self.dic_positions_of_tiles.update({next(iterator_tiles): (line, column)})
        for column in range(1, self.dimension):  # last line
            self.dic_positions_of_tiles.update({next(iterator_tiles): (self.dimension, column)})

    def xǁPuzzleGameǁ__put_tiles_in_dic_positions____mutmut_4(self, list_tiles):
        iterator_tiles = iter(list_tiles)
        for line in range(1, None):  # from first line to the line before the last
            for column in range(1, self.dimension + 1):
                self.dic_positions_of_tiles.update({next(iterator_tiles): (line, column)})
        for column in range(1, self.dimension):  # last line
            self.dic_positions_of_tiles.update({next(iterator_tiles): (self.dimension, column)})

    def xǁPuzzleGameǁ__put_tiles_in_dic_positions____mutmut_5(self, list_tiles):
        iterator_tiles = iter(list_tiles)
        for line in range(self.dimension):  # from first line to the line before the last
            for column in range(1, self.dimension + 1):
                self.dic_positions_of_tiles.update({next(iterator_tiles): (line, column)})
        for column in range(1, self.dimension):  # last line
            self.dic_positions_of_tiles.update({next(iterator_tiles): (self.dimension, column)})

    def xǁPuzzleGameǁ__put_tiles_in_dic_positions____mutmut_6(self, list_tiles):
        iterator_tiles = iter(list_tiles)
        for line in range(1, ):  # from first line to the line before the last
            for column in range(1, self.dimension + 1):
                self.dic_positions_of_tiles.update({next(iterator_tiles): (line, column)})
        for column in range(1, self.dimension):  # last line
            self.dic_positions_of_tiles.update({next(iterator_tiles): (self.dimension, column)})

    def xǁPuzzleGameǁ__put_tiles_in_dic_positions____mutmut_7(self, list_tiles):
        iterator_tiles = iter(list_tiles)
        for line in range(2, self.dimension):  # from first line to the line before the last
            for column in range(1, self.dimension + 1):
                self.dic_positions_of_tiles.update({next(iterator_tiles): (line, column)})
        for column in range(1, self.dimension):  # last line
            self.dic_positions_of_tiles.update({next(iterator_tiles): (self.dimension, column)})

    def xǁPuzzleGameǁ__put_tiles_in_dic_positions____mutmut_8(self, list_tiles):
        iterator_tiles = iter(list_tiles)
        for line in range(1, self.dimension):  # from first line to the line before the last
            for column in range(None, self.dimension + 1):
                self.dic_positions_of_tiles.update({next(iterator_tiles): (line, column)})
        for column in range(1, self.dimension):  # last line
            self.dic_positions_of_tiles.update({next(iterator_tiles): (self.dimension, column)})

    def xǁPuzzleGameǁ__put_tiles_in_dic_positions____mutmut_9(self, list_tiles):
        iterator_tiles = iter(list_tiles)
        for line in range(1, self.dimension):  # from first line to the line before the last
            for column in range(1, None):
                self.dic_positions_of_tiles.update({next(iterator_tiles): (line, column)})
        for column in range(1, self.dimension):  # last line
            self.dic_positions_of_tiles.update({next(iterator_tiles): (self.dimension, column)})

    def xǁPuzzleGameǁ__put_tiles_in_dic_positions____mutmut_10(self, list_tiles):
        iterator_tiles = iter(list_tiles)
        for line in range(1, self.dimension):  # from first line to the line before the last
            for column in range(self.dimension + 1):
                self.dic_positions_of_tiles.update({next(iterator_tiles): (line, column)})
        for column in range(1, self.dimension):  # last line
            self.dic_positions_of_tiles.update({next(iterator_tiles): (self.dimension, column)})

    def xǁPuzzleGameǁ__put_tiles_in_dic_positions____mutmut_11(self, list_tiles):
        iterator_tiles = iter(list_tiles)
        for line in range(1, self.dimension):  # from first line to the line before the last
            for column in range(1, ):
                self.dic_positions_of_tiles.update({next(iterator_tiles): (line, column)})
        for column in range(1, self.dimension):  # last line
            self.dic_positions_of_tiles.update({next(iterator_tiles): (self.dimension, column)})

    def xǁPuzzleGameǁ__put_tiles_in_dic_positions____mutmut_12(self, list_tiles):
        iterator_tiles = iter(list_tiles)
        for line in range(1, self.dimension):  # from first line to the line before the last
            for column in range(2, self.dimension + 1):
                self.dic_positions_of_tiles.update({next(iterator_tiles): (line, column)})
        for column in range(1, self.dimension):  # last line
            self.dic_positions_of_tiles.update({next(iterator_tiles): (self.dimension, column)})

    def xǁPuzzleGameǁ__put_tiles_in_dic_positions____mutmut_13(self, list_tiles):
        iterator_tiles = iter(list_tiles)
        for line in range(1, self.dimension):  # from first line to the line before the last
            for column in range(1, self.dimension - 1):
                self.dic_positions_of_tiles.update({next(iterator_tiles): (line, column)})
        for column in range(1, self.dimension):  # last line
            self.dic_positions_of_tiles.update({next(iterator_tiles): (self.dimension, column)})

    def xǁPuzzleGameǁ__put_tiles_in_dic_positions____mutmut_14(self, list_tiles):
        iterator_tiles = iter(list_tiles)
        for line in range(1, self.dimension):  # from first line to the line before the last
            for column in range(1, self.dimension + 2):
                self.dic_positions_of_tiles.update({next(iterator_tiles): (line, column)})
        for column in range(1, self.dimension):  # last line
            self.dic_positions_of_tiles.update({next(iterator_tiles): (self.dimension, column)})

    def xǁPuzzleGameǁ__put_tiles_in_dic_positions____mutmut_15(self, list_tiles):
        iterator_tiles = iter(list_tiles)
        for line in range(1, self.dimension):  # from first line to the line before the last
            for column in range(1, self.dimension + 1):
                self.dic_positions_of_tiles.update(None)
        for column in range(1, self.dimension):  # last line
            self.dic_positions_of_tiles.update({next(iterator_tiles): (self.dimension, column)})

    def xǁPuzzleGameǁ__put_tiles_in_dic_positions____mutmut_16(self, list_tiles):
        iterator_tiles = iter(list_tiles)
        for line in range(1, self.dimension):  # from first line to the line before the last
            for column in range(1, self.dimension + 1):
                self.dic_positions_of_tiles.update({next(None): (line, column)})
        for column in range(1, self.dimension):  # last line
            self.dic_positions_of_tiles.update({next(iterator_tiles): (self.dimension, column)})

    def xǁPuzzleGameǁ__put_tiles_in_dic_positions____mutmut_17(self, list_tiles):
        iterator_tiles = iter(list_tiles)
        for line in range(1, self.dimension):  # from first line to the line before the last
            for column in range(1, self.dimension + 1):
                self.dic_positions_of_tiles.update({next(iterator_tiles): (line, column)})
        for column in range(None, self.dimension):  # last line
            self.dic_positions_of_tiles.update({next(iterator_tiles): (self.dimension, column)})

    def xǁPuzzleGameǁ__put_tiles_in_dic_positions____mutmut_18(self, list_tiles):
        iterator_tiles = iter(list_tiles)
        for line in range(1, self.dimension):  # from first line to the line before the last
            for column in range(1, self.dimension + 1):
                self.dic_positions_of_tiles.update({next(iterator_tiles): (line, column)})
        for column in range(1, None):  # last line
            self.dic_positions_of_tiles.update({next(iterator_tiles): (self.dimension, column)})

    def xǁPuzzleGameǁ__put_tiles_in_dic_positions____mutmut_19(self, list_tiles):
        iterator_tiles = iter(list_tiles)
        for line in range(1, self.dimension):  # from first line to the line before the last
            for column in range(1, self.dimension + 1):
                self.dic_positions_of_tiles.update({next(iterator_tiles): (line, column)})
        for column in range(self.dimension):  # last line
            self.dic_positions_of_tiles.update({next(iterator_tiles): (self.dimension, column)})

    def xǁPuzzleGameǁ__put_tiles_in_dic_positions____mutmut_20(self, list_tiles):
        iterator_tiles = iter(list_tiles)
        for line in range(1, self.dimension):  # from first line to the line before the last
            for column in range(1, self.dimension + 1):
                self.dic_positions_of_tiles.update({next(iterator_tiles): (line, column)})
        for column in range(1, ):  # last line
            self.dic_positions_of_tiles.update({next(iterator_tiles): (self.dimension, column)})

    def xǁPuzzleGameǁ__put_tiles_in_dic_positions____mutmut_21(self, list_tiles):
        iterator_tiles = iter(list_tiles)
        for line in range(1, self.dimension):  # from first line to the line before the last
            for column in range(1, self.dimension + 1):
                self.dic_positions_of_tiles.update({next(iterator_tiles): (line, column)})
        for column in range(2, self.dimension):  # last line
            self.dic_positions_of_tiles.update({next(iterator_tiles): (self.dimension, column)})

    def xǁPuzzleGameǁ__put_tiles_in_dic_positions____mutmut_22(self, list_tiles):
        iterator_tiles = iter(list_tiles)
        for line in range(1, self.dimension):  # from first line to the line before the last
            for column in range(1, self.dimension + 1):
                self.dic_positions_of_tiles.update({next(iterator_tiles): (line, column)})
        for column in range(1, self.dimension):  # last line
            self.dic_positions_of_tiles.update(None)

    def xǁPuzzleGameǁ__put_tiles_in_dic_positions____mutmut_23(self, list_tiles):
        iterator_tiles = iter(list_tiles)
        for line in range(1, self.dimension):  # from first line to the line before the last
            for column in range(1, self.dimension + 1):
                self.dic_positions_of_tiles.update({next(iterator_tiles): (line, column)})
        for column in range(1, self.dimension):  # last line
            self.dic_positions_of_tiles.update({next(None): (self.dimension, column)})
    
    xǁPuzzleGameǁ__put_tiles_in_dic_positions____mutmut_mutants : ClassVar[MutantDict] = {
    'xǁPuzzleGameǁ__put_tiles_in_dic_positions____mutmut_1': xǁPuzzleGameǁ__put_tiles_in_dic_positions____mutmut_1, 
        'xǁPuzzleGameǁ__put_tiles_in_dic_positions____mutmut_2': xǁPuzzleGameǁ__put_tiles_in_dic_positions____mutmut_2, 
        'xǁPuzzleGameǁ__put_tiles_in_dic_positions____mutmut_3': xǁPuzzleGameǁ__put_tiles_in_dic_positions____mutmut_3, 
        'xǁPuzzleGameǁ__put_tiles_in_dic_positions____mutmut_4': xǁPuzzleGameǁ__put_tiles_in_dic_positions____mutmut_4, 
        'xǁPuzzleGameǁ__put_tiles_in_dic_positions____mutmut_5': xǁPuzzleGameǁ__put_tiles_in_dic_positions____mutmut_5, 
        'xǁPuzzleGameǁ__put_tiles_in_dic_positions____mutmut_6': xǁPuzzleGameǁ__put_tiles_in_dic_positions____mutmut_6, 
        'xǁPuzzleGameǁ__put_tiles_in_dic_positions____mutmut_7': xǁPuzzleGameǁ__put_tiles_in_dic_positions____mutmut_7, 
        'xǁPuzzleGameǁ__put_tiles_in_dic_positions____mutmut_8': xǁPuzzleGameǁ__put_tiles_in_dic_positions____mutmut_8, 
        'xǁPuzzleGameǁ__put_tiles_in_dic_positions____mutmut_9': xǁPuzzleGameǁ__put_tiles_in_dic_positions____mutmut_9, 
        'xǁPuzzleGameǁ__put_tiles_in_dic_positions____mutmut_10': xǁPuzzleGameǁ__put_tiles_in_dic_positions____mutmut_10, 
        'xǁPuzzleGameǁ__put_tiles_in_dic_positions____mutmut_11': xǁPuzzleGameǁ__put_tiles_in_dic_positions____mutmut_11, 
        'xǁPuzzleGameǁ__put_tiles_in_dic_positions____mutmut_12': xǁPuzzleGameǁ__put_tiles_in_dic_positions____mutmut_12, 
        'xǁPuzzleGameǁ__put_tiles_in_dic_positions____mutmut_13': xǁPuzzleGameǁ__put_tiles_in_dic_positions____mutmut_13, 
        'xǁPuzzleGameǁ__put_tiles_in_dic_positions____mutmut_14': xǁPuzzleGameǁ__put_tiles_in_dic_positions____mutmut_14, 
        'xǁPuzzleGameǁ__put_tiles_in_dic_positions____mutmut_15': xǁPuzzleGameǁ__put_tiles_in_dic_positions____mutmut_15, 
        'xǁPuzzleGameǁ__put_tiles_in_dic_positions____mutmut_16': xǁPuzzleGameǁ__put_tiles_in_dic_positions____mutmut_16, 
        'xǁPuzzleGameǁ__put_tiles_in_dic_positions____mutmut_17': xǁPuzzleGameǁ__put_tiles_in_dic_positions____mutmut_17, 
        'xǁPuzzleGameǁ__put_tiles_in_dic_positions____mutmut_18': xǁPuzzleGameǁ__put_tiles_in_dic_positions____mutmut_18, 
        'xǁPuzzleGameǁ__put_tiles_in_dic_positions____mutmut_19': xǁPuzzleGameǁ__put_tiles_in_dic_positions____mutmut_19, 
        'xǁPuzzleGameǁ__put_tiles_in_dic_positions____mutmut_20': xǁPuzzleGameǁ__put_tiles_in_dic_positions____mutmut_20, 
        'xǁPuzzleGameǁ__put_tiles_in_dic_positions____mutmut_21': xǁPuzzleGameǁ__put_tiles_in_dic_positions____mutmut_21, 
        'xǁPuzzleGameǁ__put_tiles_in_dic_positions____mutmut_22': xǁPuzzleGameǁ__put_tiles_in_dic_positions____mutmut_22, 
        'xǁPuzzleGameǁ__put_tiles_in_dic_positions____mutmut_23': xǁPuzzleGameǁ__put_tiles_in_dic_positions____mutmut_23
    }
    
    def __put_tiles_in_dic_positions__(self, *args, **kwargs):
        result = _mutmut_trampoline(object.__getattribute__(self, "xǁPuzzleGameǁ__put_tiles_in_dic_positions____mutmut_orig"), object.__getattribute__(self, "xǁPuzzleGameǁ__put_tiles_in_dic_positions____mutmut_mutants"), args, kwargs, self)
        return result 
    
    __put_tiles_in_dic_positions__.__signature__ = _mutmut_signature(xǁPuzzleGameǁ__put_tiles_in_dic_positions____mutmut_orig)
    xǁPuzzleGameǁ__put_tiles_in_dic_positions____mutmut_orig.__name__ = 'xǁPuzzleGameǁ__put_tiles_in_dic_positions__'

    def xǁPuzzleGameǁshuffle__mutmut_orig(self, shuffler):
        shuffler.shuffle(self)

    def xǁPuzzleGameǁshuffle__mutmut_1(self, shuffler):
        shuffler.shuffle(None)
    
    xǁPuzzleGameǁshuffle__mutmut_mutants : ClassVar[MutantDict] = {
    'xǁPuzzleGameǁshuffle__mutmut_1': xǁPuzzleGameǁshuffle__mutmut_1
    }
    
    def shuffle(self, *args, **kwargs):
        result = _mutmut_trampoline(object.__getattribute__(self, "xǁPuzzleGameǁshuffle__mutmut_orig"), object.__getattribute__(self, "xǁPuzzleGameǁshuffle__mutmut_mutants"), args, kwargs, self)
        return result 
    
    shuffle.__signature__ = _mutmut_signature(xǁPuzzleGameǁshuffle__mutmut_orig)
    xǁPuzzleGameǁshuffle__mutmut_orig.__name__ = 'xǁPuzzleGameǁshuffle'

    def xǁPuzzleGameǁmove_tile_from_a_position_to_the_empty_position__mutmut_orig(self, line, column):
        if self.board.is_inside_the_board(line, column) and self.board.positions_are_adjacent(line, column, self.line_of_empty_position, self.column_of_empty_position):
            tile = self.board.get_tile(line, column)
            self.board.put_tile(tile, self.line_of_empty_position, self.column_of_empty_position)
            self.dic_positions_of_tiles.update({tile: (self.line_of_empty_position, self.column_of_empty_position)})
            self.line_of_empty_position = line
            self.column_of_empty_position = column
            self.board.put_tile(None, self.line_of_empty_position, self.column_of_empty_position)
            return True
        else:
            return False

    def xǁPuzzleGameǁmove_tile_from_a_position_to_the_empty_position__mutmut_1(self, line, column):
        if self.board.is_inside_the_board(line, column) or self.board.positions_are_adjacent(line, column, self.line_of_empty_position, self.column_of_empty_position):
            tile = self.board.get_tile(line, column)
            self.board.put_tile(tile, self.line_of_empty_position, self.column_of_empty_position)
            self.dic_positions_of_tiles.update({tile: (self.line_of_empty_position, self.column_of_empty_position)})
            self.line_of_empty_position = line
            self.column_of_empty_position = column
            self.board.put_tile(None, self.line_of_empty_position, self.column_of_empty_position)
            return True
        else:
            return False

    def xǁPuzzleGameǁmove_tile_from_a_position_to_the_empty_position__mutmut_2(self, line, column):
        if self.board.is_inside_the_board(None, column) and self.board.positions_are_adjacent(line, column, self.line_of_empty_position, self.column_of_empty_position):
            tile = self.board.get_tile(line, column)
            self.board.put_tile(tile, self.line_of_empty_position, self.column_of_empty_position)
            self.dic_positions_of_tiles.update({tile: (self.line_of_empty_position, self.column_of_empty_position)})
            self.line_of_empty_position = line
            self.column_of_empty_position = column
            self.board.put_tile(None, self.line_of_empty_position, self.column_of_empty_position)
            return True
        else:
            return False

    def xǁPuzzleGameǁmove_tile_from_a_position_to_the_empty_position__mutmut_3(self, line, column):
        if self.board.is_inside_the_board(line, None) and self.board.positions_are_adjacent(line, column, self.line_of_empty_position, self.column_of_empty_position):
            tile = self.board.get_tile(line, column)
            self.board.put_tile(tile, self.line_of_empty_position, self.column_of_empty_position)
            self.dic_positions_of_tiles.update({tile: (self.line_of_empty_position, self.column_of_empty_position)})
            self.line_of_empty_position = line
            self.column_of_empty_position = column
            self.board.put_tile(None, self.line_of_empty_position, self.column_of_empty_position)
            return True
        else:
            return False

    def xǁPuzzleGameǁmove_tile_from_a_position_to_the_empty_position__mutmut_4(self, line, column):
        if self.board.is_inside_the_board(column) and self.board.positions_are_adjacent(line, column, self.line_of_empty_position, self.column_of_empty_position):
            tile = self.board.get_tile(line, column)
            self.board.put_tile(tile, self.line_of_empty_position, self.column_of_empty_position)
            self.dic_positions_of_tiles.update({tile: (self.line_of_empty_position, self.column_of_empty_position)})
            self.line_of_empty_position = line
            self.column_of_empty_position = column
            self.board.put_tile(None, self.line_of_empty_position, self.column_of_empty_position)
            return True
        else:
            return False

    def xǁPuzzleGameǁmove_tile_from_a_position_to_the_empty_position__mutmut_5(self, line, column):
        if self.board.is_inside_the_board(line, ) and self.board.positions_are_adjacent(line, column, self.line_of_empty_position, self.column_of_empty_position):
            tile = self.board.get_tile(line, column)
            self.board.put_tile(tile, self.line_of_empty_position, self.column_of_empty_position)
            self.dic_positions_of_tiles.update({tile: (self.line_of_empty_position, self.column_of_empty_position)})
            self.line_of_empty_position = line
            self.column_of_empty_position = column
            self.board.put_tile(None, self.line_of_empty_position, self.column_of_empty_position)
            return True
        else:
            return False

    def xǁPuzzleGameǁmove_tile_from_a_position_to_the_empty_position__mutmut_6(self, line, column):
        if self.board.is_inside_the_board(line, column) and self.board.positions_are_adjacent(None, column, self.line_of_empty_position, self.column_of_empty_position):
            tile = self.board.get_tile(line, column)
            self.board.put_tile(tile, self.line_of_empty_position, self.column_of_empty_position)
            self.dic_positions_of_tiles.update({tile: (self.line_of_empty_position, self.column_of_empty_position)})
            self.line_of_empty_position = line
            self.column_of_empty_position = column
            self.board.put_tile(None, self.line_of_empty_position, self.column_of_empty_position)
            return True
        else:
            return False

    def xǁPuzzleGameǁmove_tile_from_a_position_to_the_empty_position__mutmut_7(self, line, column):
        if self.board.is_inside_the_board(line, column) and self.board.positions_are_adjacent(line, None, self.line_of_empty_position, self.column_of_empty_position):
            tile = self.board.get_tile(line, column)
            self.board.put_tile(tile, self.line_of_empty_position, self.column_of_empty_position)
            self.dic_positions_of_tiles.update({tile: (self.line_of_empty_position, self.column_of_empty_position)})
            self.line_of_empty_position = line
            self.column_of_empty_position = column
            self.board.put_tile(None, self.line_of_empty_position, self.column_of_empty_position)
            return True
        else:
            return False

    def xǁPuzzleGameǁmove_tile_from_a_position_to_the_empty_position__mutmut_8(self, line, column):
        if self.board.is_inside_the_board(line, column) and self.board.positions_are_adjacent(line, column, None, self.column_of_empty_position):
            tile = self.board.get_tile(line, column)
            self.board.put_tile(tile, self.line_of_empty_position, self.column_of_empty_position)
            self.dic_positions_of_tiles.update({tile: (self.line_of_empty_position, self.column_of_empty_position)})
            self.line_of_empty_position = line
            self.column_of_empty_position = column
            self.board.put_tile(None, self.line_of_empty_position, self.column_of_empty_position)
            return True
        else:
            return False

    def xǁPuzzleGameǁmove_tile_from_a_position_to_the_empty_position__mutmut_9(self, line, column):
        if self.board.is_inside_the_board(line, column) and self.board.positions_are_adjacent(line, column, self.line_of_empty_position, None):
            tile = self.board.get_tile(line, column)
            self.board.put_tile(tile, self.line_of_empty_position, self.column_of_empty_position)
            self.dic_positions_of_tiles.update({tile: (self.line_of_empty_position, self.column_of_empty_position)})
            self.line_of_empty_position = line
            self.column_of_empty_position = column
            self.board.put_tile(None, self.line_of_empty_position, self.column_of_empty_position)
            return True
        else:
            return False

    def xǁPuzzleGameǁmove_tile_from_a_position_to_the_empty_position__mutmut_10(self, line, column):
        if self.board.is_inside_the_board(line, column) and self.board.positions_are_adjacent(column, self.line_of_empty_position, self.column_of_empty_position):
            tile = self.board.get_tile(line, column)
            self.board.put_tile(tile, self.line_of_empty_position, self.column_of_empty_position)
            self.dic_positions_of_tiles.update({tile: (self.line_of_empty_position, self.column_of_empty_position)})
            self.line_of_empty_position = line
            self.column_of_empty_position = column
            self.board.put_tile(None, self.line_of_empty_position, self.column_of_empty_position)
            return True
        else:
            return False

    def xǁPuzzleGameǁmove_tile_from_a_position_to_the_empty_position__mutmut_11(self, line, column):
        if self.board.is_inside_the_board(line, column) and self.board.positions_are_adjacent(line, self.line_of_empty_position, self.column_of_empty_position):
            tile = self.board.get_tile(line, column)
            self.board.put_tile(tile, self.line_of_empty_position, self.column_of_empty_position)
            self.dic_positions_of_tiles.update({tile: (self.line_of_empty_position, self.column_of_empty_position)})
            self.line_of_empty_position = line
            self.column_of_empty_position = column
            self.board.put_tile(None, self.line_of_empty_position, self.column_of_empty_position)
            return True
        else:
            return False

    def xǁPuzzleGameǁmove_tile_from_a_position_to_the_empty_position__mutmut_12(self, line, column):
        if self.board.is_inside_the_board(line, column) and self.board.positions_are_adjacent(line, column, self.column_of_empty_position):
            tile = self.board.get_tile(line, column)
            self.board.put_tile(tile, self.line_of_empty_position, self.column_of_empty_position)
            self.dic_positions_of_tiles.update({tile: (self.line_of_empty_position, self.column_of_empty_position)})
            self.line_of_empty_position = line
            self.column_of_empty_position = column
            self.board.put_tile(None, self.line_of_empty_position, self.column_of_empty_position)
            return True
        else:
            return False

    def xǁPuzzleGameǁmove_tile_from_a_position_to_the_empty_position__mutmut_13(self, line, column):
        if self.board.is_inside_the_board(line, column) and self.board.positions_are_adjacent(line, column, self.line_of_empty_position, ):
            tile = self.board.get_tile(line, column)
            self.board.put_tile(tile, self.line_of_empty_position, self.column_of_empty_position)
            self.dic_positions_of_tiles.update({tile: (self.line_of_empty_position, self.column_of_empty_position)})
            self.line_of_empty_position = line
            self.column_of_empty_position = column
            self.board.put_tile(None, self.line_of_empty_position, self.column_of_empty_position)
            return True
        else:
            return False

    def xǁPuzzleGameǁmove_tile_from_a_position_to_the_empty_position__mutmut_14(self, line, column):
        if self.board.is_inside_the_board(line, column) and self.board.positions_are_adjacent(line, column, self.line_of_empty_position, self.column_of_empty_position):
            tile = None
            self.board.put_tile(tile, self.line_of_empty_position, self.column_of_empty_position)
            self.dic_positions_of_tiles.update({tile: (self.line_of_empty_position, self.column_of_empty_position)})
            self.line_of_empty_position = line
            self.column_of_empty_position = column
            self.board.put_tile(None, self.line_of_empty_position, self.column_of_empty_position)
            return True
        else:
            return False

    def xǁPuzzleGameǁmove_tile_from_a_position_to_the_empty_position__mutmut_15(self, line, column):
        if self.board.is_inside_the_board(line, column) and self.board.positions_are_adjacent(line, column, self.line_of_empty_position, self.column_of_empty_position):
            tile = self.board.get_tile(None, column)
            self.board.put_tile(tile, self.line_of_empty_position, self.column_of_empty_position)
            self.dic_positions_of_tiles.update({tile: (self.line_of_empty_position, self.column_of_empty_position)})
            self.line_of_empty_position = line
            self.column_of_empty_position = column
            self.board.put_tile(None, self.line_of_empty_position, self.column_of_empty_position)
            return True
        else:
            return False

    def xǁPuzzleGameǁmove_tile_from_a_position_to_the_empty_position__mutmut_16(self, line, column):
        if self.board.is_inside_the_board(line, column) and self.board.positions_are_adjacent(line, column, self.line_of_empty_position, self.column_of_empty_position):
            tile = self.board.get_tile(line, None)
            self.board.put_tile(tile, self.line_of_empty_position, self.column_of_empty_position)
            self.dic_positions_of_tiles.update({tile: (self.line_of_empty_position, self.column_of_empty_position)})
            self.line_of_empty_position = line
            self.column_of_empty_position = column
            self.board.put_tile(None, self.line_of_empty_position, self.column_of_empty_position)
            return True
        else:
            return False

    def xǁPuzzleGameǁmove_tile_from_a_position_to_the_empty_position__mutmut_17(self, line, column):
        if self.board.is_inside_the_board(line, column) and self.board.positions_are_adjacent(line, column, self.line_of_empty_position, self.column_of_empty_position):
            tile = self.board.get_tile(column)
            self.board.put_tile(tile, self.line_of_empty_position, self.column_of_empty_position)
            self.dic_positions_of_tiles.update({tile: (self.line_of_empty_position, self.column_of_empty_position)})
            self.line_of_empty_position = line
            self.column_of_empty_position = column
            self.board.put_tile(None, self.line_of_empty_position, self.column_of_empty_position)
            return True
        else:
            return False

    def xǁPuzzleGameǁmove_tile_from_a_position_to_the_empty_position__mutmut_18(self, line, column):
        if self.board.is_inside_the_board(line, column) and self.board.positions_are_adjacent(line, column, self.line_of_empty_position, self.column_of_empty_position):
            tile = self.board.get_tile(line, )
            self.board.put_tile(tile, self.line_of_empty_position, self.column_of_empty_position)
            self.dic_positions_of_tiles.update({tile: (self.line_of_empty_position, self.column_of_empty_position)})
            self.line_of_empty_position = line
            self.column_of_empty_position = column
            self.board.put_tile(None, self.line_of_empty_position, self.column_of_empty_position)
            return True
        else:
            return False

    def xǁPuzzleGameǁmove_tile_from_a_position_to_the_empty_position__mutmut_19(self, line, column):
        if self.board.is_inside_the_board(line, column) and self.board.positions_are_adjacent(line, column, self.line_of_empty_position, self.column_of_empty_position):
            tile = self.board.get_tile(line, column)
            self.board.put_tile(None, self.line_of_empty_position, self.column_of_empty_position)
            self.dic_positions_of_tiles.update({tile: (self.line_of_empty_position, self.column_of_empty_position)})
            self.line_of_empty_position = line
            self.column_of_empty_position = column
            self.board.put_tile(None, self.line_of_empty_position, self.column_of_empty_position)
            return True
        else:
            return False

    def xǁPuzzleGameǁmove_tile_from_a_position_to_the_empty_position__mutmut_20(self, line, column):
        if self.board.is_inside_the_board(line, column) and self.board.positions_are_adjacent(line, column, self.line_of_empty_position, self.column_of_empty_position):
            tile = self.board.get_tile(line, column)
            self.board.put_tile(tile, None, self.column_of_empty_position)
            self.dic_positions_of_tiles.update({tile: (self.line_of_empty_position, self.column_of_empty_position)})
            self.line_of_empty_position = line
            self.column_of_empty_position = column
            self.board.put_tile(None, self.line_of_empty_position, self.column_of_empty_position)
            return True
        else:
            return False

    def xǁPuzzleGameǁmove_tile_from_a_position_to_the_empty_position__mutmut_21(self, line, column):
        if self.board.is_inside_the_board(line, column) and self.board.positions_are_adjacent(line, column, self.line_of_empty_position, self.column_of_empty_position):
            tile = self.board.get_tile(line, column)
            self.board.put_tile(tile, self.line_of_empty_position, None)
            self.dic_positions_of_tiles.update({tile: (self.line_of_empty_position, self.column_of_empty_position)})
            self.line_of_empty_position = line
            self.column_of_empty_position = column
            self.board.put_tile(None, self.line_of_empty_position, self.column_of_empty_position)
            return True
        else:
            return False

    def xǁPuzzleGameǁmove_tile_from_a_position_to_the_empty_position__mutmut_22(self, line, column):
        if self.board.is_inside_the_board(line, column) and self.board.positions_are_adjacent(line, column, self.line_of_empty_position, self.column_of_empty_position):
            tile = self.board.get_tile(line, column)
            self.board.put_tile(self.line_of_empty_position, self.column_of_empty_position)
            self.dic_positions_of_tiles.update({tile: (self.line_of_empty_position, self.column_of_empty_position)})
            self.line_of_empty_position = line
            self.column_of_empty_position = column
            self.board.put_tile(None, self.line_of_empty_position, self.column_of_empty_position)
            return True
        else:
            return False

    def xǁPuzzleGameǁmove_tile_from_a_position_to_the_empty_position__mutmut_23(self, line, column):
        if self.board.is_inside_the_board(line, column) and self.board.positions_are_adjacent(line, column, self.line_of_empty_position, self.column_of_empty_position):
            tile = self.board.get_tile(line, column)
            self.board.put_tile(tile, self.column_of_empty_position)
            self.dic_positions_of_tiles.update({tile: (self.line_of_empty_position, self.column_of_empty_position)})
            self.line_of_empty_position = line
            self.column_of_empty_position = column
            self.board.put_tile(None, self.line_of_empty_position, self.column_of_empty_position)
            return True
        else:
            return False

    def xǁPuzzleGameǁmove_tile_from_a_position_to_the_empty_position__mutmut_24(self, line, column):
        if self.board.is_inside_the_board(line, column) and self.board.positions_are_adjacent(line, column, self.line_of_empty_position, self.column_of_empty_position):
            tile = self.board.get_tile(line, column)
            self.board.put_tile(tile, self.line_of_empty_position, )
            self.dic_positions_of_tiles.update({tile: (self.line_of_empty_position, self.column_of_empty_position)})
            self.line_of_empty_position = line
            self.column_of_empty_position = column
            self.board.put_tile(None, self.line_of_empty_position, self.column_of_empty_position)
            return True
        else:
            return False

    def xǁPuzzleGameǁmove_tile_from_a_position_to_the_empty_position__mutmut_25(self, line, column):
        if self.board.is_inside_the_board(line, column) and self.board.positions_are_adjacent(line, column, self.line_of_empty_position, self.column_of_empty_position):
            tile = self.board.get_tile(line, column)
            self.board.put_tile(tile, self.line_of_empty_position, self.column_of_empty_position)
            self.dic_positions_of_tiles.update(None)
            self.line_of_empty_position = line
            self.column_of_empty_position = column
            self.board.put_tile(None, self.line_of_empty_position, self.column_of_empty_position)
            return True
        else:
            return False

    def xǁPuzzleGameǁmove_tile_from_a_position_to_the_empty_position__mutmut_26(self, line, column):
        if self.board.is_inside_the_board(line, column) and self.board.positions_are_adjacent(line, column, self.line_of_empty_position, self.column_of_empty_position):
            tile = self.board.get_tile(line, column)
            self.board.put_tile(tile, self.line_of_empty_position, self.column_of_empty_position)
            self.dic_positions_of_tiles.update({tile: (self.line_of_empty_position, self.column_of_empty_position)})
            self.line_of_empty_position = None
            self.column_of_empty_position = column
            self.board.put_tile(None, self.line_of_empty_position, self.column_of_empty_position)
            return True
        else:
            return False

    def xǁPuzzleGameǁmove_tile_from_a_position_to_the_empty_position__mutmut_27(self, line, column):
        if self.board.is_inside_the_board(line, column) and self.board.positions_are_adjacent(line, column, self.line_of_empty_position, self.column_of_empty_position):
            tile = self.board.get_tile(line, column)
            self.board.put_tile(tile, self.line_of_empty_position, self.column_of_empty_position)
            self.dic_positions_of_tiles.update({tile: (self.line_of_empty_position, self.column_of_empty_position)})
            self.line_of_empty_position = line
            self.column_of_empty_position = None
            self.board.put_tile(None, self.line_of_empty_position, self.column_of_empty_position)
            return True
        else:
            return False

    def xǁPuzzleGameǁmove_tile_from_a_position_to_the_empty_position__mutmut_28(self, line, column):
        if self.board.is_inside_the_board(line, column) and self.board.positions_are_adjacent(line, column, self.line_of_empty_position, self.column_of_empty_position):
            tile = self.board.get_tile(line, column)
            self.board.put_tile(tile, self.line_of_empty_position, self.column_of_empty_position)
            self.dic_positions_of_tiles.update({tile: (self.line_of_empty_position, self.column_of_empty_position)})
            self.line_of_empty_position = line
            self.column_of_empty_position = column
            self.board.put_tile(None, None, self.column_of_empty_position)
            return True
        else:
            return False

    def xǁPuzzleGameǁmove_tile_from_a_position_to_the_empty_position__mutmut_29(self, line, column):
        if self.board.is_inside_the_board(line, column) and self.board.positions_are_adjacent(line, column, self.line_of_empty_position, self.column_of_empty_position):
            tile = self.board.get_tile(line, column)
            self.board.put_tile(tile, self.line_of_empty_position, self.column_of_empty_position)
            self.dic_positions_of_tiles.update({tile: (self.line_of_empty_position, self.column_of_empty_position)})
            self.line_of_empty_position = line
            self.column_of_empty_position = column
            self.board.put_tile(None, self.line_of_empty_position, None)
            return True
        else:
            return False

    def xǁPuzzleGameǁmove_tile_from_a_position_to_the_empty_position__mutmut_30(self, line, column):
        if self.board.is_inside_the_board(line, column) and self.board.positions_are_adjacent(line, column, self.line_of_empty_position, self.column_of_empty_position):
            tile = self.board.get_tile(line, column)
            self.board.put_tile(tile, self.line_of_empty_position, self.column_of_empty_position)
            self.dic_positions_of_tiles.update({tile: (self.line_of_empty_position, self.column_of_empty_position)})
            self.line_of_empty_position = line
            self.column_of_empty_position = column
            self.board.put_tile(self.line_of_empty_position, self.column_of_empty_position)
            return True
        else:
            return False

    def xǁPuzzleGameǁmove_tile_from_a_position_to_the_empty_position__mutmut_31(self, line, column):
        if self.board.is_inside_the_board(line, column) and self.board.positions_are_adjacent(line, column, self.line_of_empty_position, self.column_of_empty_position):
            tile = self.board.get_tile(line, column)
            self.board.put_tile(tile, self.line_of_empty_position, self.column_of_empty_position)
            self.dic_positions_of_tiles.update({tile: (self.line_of_empty_position, self.column_of_empty_position)})
            self.line_of_empty_position = line
            self.column_of_empty_position = column
            self.board.put_tile(None, self.column_of_empty_position)
            return True
        else:
            return False

    def xǁPuzzleGameǁmove_tile_from_a_position_to_the_empty_position__mutmut_32(self, line, column):
        if self.board.is_inside_the_board(line, column) and self.board.positions_are_adjacent(line, column, self.line_of_empty_position, self.column_of_empty_position):
            tile = self.board.get_tile(line, column)
            self.board.put_tile(tile, self.line_of_empty_position, self.column_of_empty_position)
            self.dic_positions_of_tiles.update({tile: (self.line_of_empty_position, self.column_of_empty_position)})
            self.line_of_empty_position = line
            self.column_of_empty_position = column
            self.board.put_tile(None, self.line_of_empty_position, )
            return True
        else:
            return False

    def xǁPuzzleGameǁmove_tile_from_a_position_to_the_empty_position__mutmut_33(self, line, column):
        if self.board.is_inside_the_board(line, column) and self.board.positions_are_adjacent(line, column, self.line_of_empty_position, self.column_of_empty_position):
            tile = self.board.get_tile(line, column)
            self.board.put_tile(tile, self.line_of_empty_position, self.column_of_empty_position)
            self.dic_positions_of_tiles.update({tile: (self.line_of_empty_position, self.column_of_empty_position)})
            self.line_of_empty_position = line
            self.column_of_empty_position = column
            self.board.put_tile(None, self.line_of_empty_position, self.column_of_empty_position)
            return False
        else:
            return False

    def xǁPuzzleGameǁmove_tile_from_a_position_to_the_empty_position__mutmut_34(self, line, column):
        if self.board.is_inside_the_board(line, column) and self.board.positions_are_adjacent(line, column, self.line_of_empty_position, self.column_of_empty_position):
            tile = self.board.get_tile(line, column)
            self.board.put_tile(tile, self.line_of_empty_position, self.column_of_empty_position)
            self.dic_positions_of_tiles.update({tile: (self.line_of_empty_position, self.column_of_empty_position)})
            self.line_of_empty_position = line
            self.column_of_empty_position = column
            self.board.put_tile(None, self.line_of_empty_position, self.column_of_empty_position)
            return True
        else:
            return True
    
    xǁPuzzleGameǁmove_tile_from_a_position_to_the_empty_position__mutmut_mutants : ClassVar[MutantDict] = {
    'xǁPuzzleGameǁmove_tile_from_a_position_to_the_empty_position__mutmut_1': xǁPuzzleGameǁmove_tile_from_a_position_to_the_empty_position__mutmut_1, 
        'xǁPuzzleGameǁmove_tile_from_a_position_to_the_empty_position__mutmut_2': xǁPuzzleGameǁmove_tile_from_a_position_to_the_empty_position__mutmut_2, 
        'xǁPuzzleGameǁmove_tile_from_a_position_to_the_empty_position__mutmut_3': xǁPuzzleGameǁmove_tile_from_a_position_to_the_empty_position__mutmut_3, 
        'xǁPuzzleGameǁmove_tile_from_a_position_to_the_empty_position__mutmut_4': xǁPuzzleGameǁmove_tile_from_a_position_to_the_empty_position__mutmut_4, 
        'xǁPuzzleGameǁmove_tile_from_a_position_to_the_empty_position__mutmut_5': xǁPuzzleGameǁmove_tile_from_a_position_to_the_empty_position__mutmut_5, 
        'xǁPuzzleGameǁmove_tile_from_a_position_to_the_empty_position__mutmut_6': xǁPuzzleGameǁmove_tile_from_a_position_to_the_empty_position__mutmut_6, 
        'xǁPuzzleGameǁmove_tile_from_a_position_to_the_empty_position__mutmut_7': xǁPuzzleGameǁmove_tile_from_a_position_to_the_empty_position__mutmut_7, 
        'xǁPuzzleGameǁmove_tile_from_a_position_to_the_empty_position__mutmut_8': xǁPuzzleGameǁmove_tile_from_a_position_to_the_empty_position__mutmut_8, 
        'xǁPuzzleGameǁmove_tile_from_a_position_to_the_empty_position__mutmut_9': xǁPuzzleGameǁmove_tile_from_a_position_to_the_empty_position__mutmut_9, 
        'xǁPuzzleGameǁmove_tile_from_a_position_to_the_empty_position__mutmut_10': xǁPuzzleGameǁmove_tile_from_a_position_to_the_empty_position__mutmut_10, 
        'xǁPuzzleGameǁmove_tile_from_a_position_to_the_empty_position__mutmut_11': xǁPuzzleGameǁmove_tile_from_a_position_to_the_empty_position__mutmut_11, 
        'xǁPuzzleGameǁmove_tile_from_a_position_to_the_empty_position__mutmut_12': xǁPuzzleGameǁmove_tile_from_a_position_to_the_empty_position__mutmut_12, 
        'xǁPuzzleGameǁmove_tile_from_a_position_to_the_empty_position__mutmut_13': xǁPuzzleGameǁmove_tile_from_a_position_to_the_empty_position__mutmut_13, 
        'xǁPuzzleGameǁmove_tile_from_a_position_to_the_empty_position__mutmut_14': xǁPuzzleGameǁmove_tile_from_a_position_to_the_empty_position__mutmut_14, 
        'xǁPuzzleGameǁmove_tile_from_a_position_to_the_empty_position__mutmut_15': xǁPuzzleGameǁmove_tile_from_a_position_to_the_empty_position__mutmut_15, 
        'xǁPuzzleGameǁmove_tile_from_a_position_to_the_empty_position__mutmut_16': xǁPuzzleGameǁmove_tile_from_a_position_to_the_empty_position__mutmut_16, 
        'xǁPuzzleGameǁmove_tile_from_a_position_to_the_empty_position__mutmut_17': xǁPuzzleGameǁmove_tile_from_a_position_to_the_empty_position__mutmut_17, 
        'xǁPuzzleGameǁmove_tile_from_a_position_to_the_empty_position__mutmut_18': xǁPuzzleGameǁmove_tile_from_a_position_to_the_empty_position__mutmut_18, 
        'xǁPuzzleGameǁmove_tile_from_a_position_to_the_empty_position__mutmut_19': xǁPuzzleGameǁmove_tile_from_a_position_to_the_empty_position__mutmut_19, 
        'xǁPuzzleGameǁmove_tile_from_a_position_to_the_empty_position__mutmut_20': xǁPuzzleGameǁmove_tile_from_a_position_to_the_empty_position__mutmut_20, 
        'xǁPuzzleGameǁmove_tile_from_a_position_to_the_empty_position__mutmut_21': xǁPuzzleGameǁmove_tile_from_a_position_to_the_empty_position__mutmut_21, 
        'xǁPuzzleGameǁmove_tile_from_a_position_to_the_empty_position__mutmut_22': xǁPuzzleGameǁmove_tile_from_a_position_to_the_empty_position__mutmut_22, 
        'xǁPuzzleGameǁmove_tile_from_a_position_to_the_empty_position__mutmut_23': xǁPuzzleGameǁmove_tile_from_a_position_to_the_empty_position__mutmut_23, 
        'xǁPuzzleGameǁmove_tile_from_a_position_to_the_empty_position__mutmut_24': xǁPuzzleGameǁmove_tile_from_a_position_to_the_empty_position__mutmut_24, 
        'xǁPuzzleGameǁmove_tile_from_a_position_to_the_empty_position__mutmut_25': xǁPuzzleGameǁmove_tile_from_a_position_to_the_empty_position__mutmut_25, 
        'xǁPuzzleGameǁmove_tile_from_a_position_to_the_empty_position__mutmut_26': xǁPuzzleGameǁmove_tile_from_a_position_to_the_empty_position__mutmut_26, 
        'xǁPuzzleGameǁmove_tile_from_a_position_to_the_empty_position__mutmut_27': xǁPuzzleGameǁmove_tile_from_a_position_to_the_empty_position__mutmut_27, 
        'xǁPuzzleGameǁmove_tile_from_a_position_to_the_empty_position__mutmut_28': xǁPuzzleGameǁmove_tile_from_a_position_to_the_empty_position__mutmut_28, 
        'xǁPuzzleGameǁmove_tile_from_a_position_to_the_empty_position__mutmut_29': xǁPuzzleGameǁmove_tile_from_a_position_to_the_empty_position__mutmut_29, 
        'xǁPuzzleGameǁmove_tile_from_a_position_to_the_empty_position__mutmut_30': xǁPuzzleGameǁmove_tile_from_a_position_to_the_empty_position__mutmut_30, 
        'xǁPuzzleGameǁmove_tile_from_a_position_to_the_empty_position__mutmut_31': xǁPuzzleGameǁmove_tile_from_a_position_to_the_empty_position__mutmut_31, 
        'xǁPuzzleGameǁmove_tile_from_a_position_to_the_empty_position__mutmut_32': xǁPuzzleGameǁmove_tile_from_a_position_to_the_empty_position__mutmut_32, 
        'xǁPuzzleGameǁmove_tile_from_a_position_to_the_empty_position__mutmut_33': xǁPuzzleGameǁmove_tile_from_a_position_to_the_empty_position__mutmut_33, 
        'xǁPuzzleGameǁmove_tile_from_a_position_to_the_empty_position__mutmut_34': xǁPuzzleGameǁmove_tile_from_a_position_to_the_empty_position__mutmut_34
    }
    
    def move_tile_from_a_position_to_the_empty_position(self, *args, **kwargs):
        result = _mutmut_trampoline(object.__getattribute__(self, "xǁPuzzleGameǁmove_tile_from_a_position_to_the_empty_position__mutmut_orig"), object.__getattribute__(self, "xǁPuzzleGameǁmove_tile_from_a_position_to_the_empty_position__mutmut_mutants"), args, kwargs, self)
        return result 
    
    move_tile_from_a_position_to_the_empty_position.__signature__ = _mutmut_signature(xǁPuzzleGameǁmove_tile_from_a_position_to_the_empty_position__mutmut_orig)
    xǁPuzzleGameǁmove_tile_from_a_position_to_the_empty_position__mutmut_orig.__name__ = 'xǁPuzzleGameǁmove_tile_from_a_position_to_the_empty_position'

    def xǁPuzzleGameǁmove_tile__mutmut_orig(self, tile):
        tile_line = self.dic_positions_of_tiles.get(tile)[0]
        tile_column = self.dic_positions_of_tiles.get(tile)[1]
        if self.board.is_inside_the_board(tile_line, tile_column) and self.board.positions_are_adjacent(tile_line, tile_column, self.line_of_empty_position, self.column_of_empty_position):
            self.board.put_tile(tile, self.line_of_empty_position, self.column_of_empty_position)
            self.dic_positions_of_tiles.update({tile: (self.line_of_empty_position, self.column_of_empty_position)})
            self.line_of_empty_position = tile_line
            self.column_of_empty_position = tile_column
            self.board.put_tile(None, self.line_of_empty_position, self.column_of_empty_position)
            return True
        else:
            return False

    def xǁPuzzleGameǁmove_tile__mutmut_1(self, tile):
        tile_line = None
        tile_column = self.dic_positions_of_tiles.get(tile)[1]
        if self.board.is_inside_the_board(tile_line, tile_column) and self.board.positions_are_adjacent(tile_line, tile_column, self.line_of_empty_position, self.column_of_empty_position):
            self.board.put_tile(tile, self.line_of_empty_position, self.column_of_empty_position)
            self.dic_positions_of_tiles.update({tile: (self.line_of_empty_position, self.column_of_empty_position)})
            self.line_of_empty_position = tile_line
            self.column_of_empty_position = tile_column
            self.board.put_tile(None, self.line_of_empty_position, self.column_of_empty_position)
            return True
        else:
            return False

    def xǁPuzzleGameǁmove_tile__mutmut_2(self, tile):
        tile_line = self.dic_positions_of_tiles.get(None)[0]
        tile_column = self.dic_positions_of_tiles.get(tile)[1]
        if self.board.is_inside_the_board(tile_line, tile_column) and self.board.positions_are_adjacent(tile_line, tile_column, self.line_of_empty_position, self.column_of_empty_position):
            self.board.put_tile(tile, self.line_of_empty_position, self.column_of_empty_position)
            self.dic_positions_of_tiles.update({tile: (self.line_of_empty_position, self.column_of_empty_position)})
            self.line_of_empty_position = tile_line
            self.column_of_empty_position = tile_column
            self.board.put_tile(None, self.line_of_empty_position, self.column_of_empty_position)
            return True
        else:
            return False

    def xǁPuzzleGameǁmove_tile__mutmut_3(self, tile):
        tile_line = self.dic_positions_of_tiles.get(tile)[1]
        tile_column = self.dic_positions_of_tiles.get(tile)[1]
        if self.board.is_inside_the_board(tile_line, tile_column) and self.board.positions_are_adjacent(tile_line, tile_column, self.line_of_empty_position, self.column_of_empty_position):
            self.board.put_tile(tile, self.line_of_empty_position, self.column_of_empty_position)
            self.dic_positions_of_tiles.update({tile: (self.line_of_empty_position, self.column_of_empty_position)})
            self.line_of_empty_position = tile_line
            self.column_of_empty_position = tile_column
            self.board.put_tile(None, self.line_of_empty_position, self.column_of_empty_position)
            return True
        else:
            return False

    def xǁPuzzleGameǁmove_tile__mutmut_4(self, tile):
        tile_line = self.dic_positions_of_tiles.get(tile)[0]
        tile_column = None
        if self.board.is_inside_the_board(tile_line, tile_column) and self.board.positions_are_adjacent(tile_line, tile_column, self.line_of_empty_position, self.column_of_empty_position):
            self.board.put_tile(tile, self.line_of_empty_position, self.column_of_empty_position)
            self.dic_positions_of_tiles.update({tile: (self.line_of_empty_position, self.column_of_empty_position)})
            self.line_of_empty_position = tile_line
            self.column_of_empty_position = tile_column
            self.board.put_tile(None, self.line_of_empty_position, self.column_of_empty_position)
            return True
        else:
            return False

    def xǁPuzzleGameǁmove_tile__mutmut_5(self, tile):
        tile_line = self.dic_positions_of_tiles.get(tile)[0]
        tile_column = self.dic_positions_of_tiles.get(None)[1]
        if self.board.is_inside_the_board(tile_line, tile_column) and self.board.positions_are_adjacent(tile_line, tile_column, self.line_of_empty_position, self.column_of_empty_position):
            self.board.put_tile(tile, self.line_of_empty_position, self.column_of_empty_position)
            self.dic_positions_of_tiles.update({tile: (self.line_of_empty_position, self.column_of_empty_position)})
            self.line_of_empty_position = tile_line
            self.column_of_empty_position = tile_column
            self.board.put_tile(None, self.line_of_empty_position, self.column_of_empty_position)
            return True
        else:
            return False

    def xǁPuzzleGameǁmove_tile__mutmut_6(self, tile):
        tile_line = self.dic_positions_of_tiles.get(tile)[0]
        tile_column = self.dic_positions_of_tiles.get(tile)[2]
        if self.board.is_inside_the_board(tile_line, tile_column) and self.board.positions_are_adjacent(tile_line, tile_column, self.line_of_empty_position, self.column_of_empty_position):
            self.board.put_tile(tile, self.line_of_empty_position, self.column_of_empty_position)
            self.dic_positions_of_tiles.update({tile: (self.line_of_empty_position, self.column_of_empty_position)})
            self.line_of_empty_position = tile_line
            self.column_of_empty_position = tile_column
            self.board.put_tile(None, self.line_of_empty_position, self.column_of_empty_position)
            return True
        else:
            return False

    def xǁPuzzleGameǁmove_tile__mutmut_7(self, tile):
        tile_line = self.dic_positions_of_tiles.get(tile)[0]
        tile_column = self.dic_positions_of_tiles.get(tile)[1]
        if self.board.is_inside_the_board(tile_line, tile_column) or self.board.positions_are_adjacent(tile_line, tile_column, self.line_of_empty_position, self.column_of_empty_position):
            self.board.put_tile(tile, self.line_of_empty_position, self.column_of_empty_position)
            self.dic_positions_of_tiles.update({tile: (self.line_of_empty_position, self.column_of_empty_position)})
            self.line_of_empty_position = tile_line
            self.column_of_empty_position = tile_column
            self.board.put_tile(None, self.line_of_empty_position, self.column_of_empty_position)
            return True
        else:
            return False

    def xǁPuzzleGameǁmove_tile__mutmut_8(self, tile):
        tile_line = self.dic_positions_of_tiles.get(tile)[0]
        tile_column = self.dic_positions_of_tiles.get(tile)[1]
        if self.board.is_inside_the_board(None, tile_column) and self.board.positions_are_adjacent(tile_line, tile_column, self.line_of_empty_position, self.column_of_empty_position):
            self.board.put_tile(tile, self.line_of_empty_position, self.column_of_empty_position)
            self.dic_positions_of_tiles.update({tile: (self.line_of_empty_position, self.column_of_empty_position)})
            self.line_of_empty_position = tile_line
            self.column_of_empty_position = tile_column
            self.board.put_tile(None, self.line_of_empty_position, self.column_of_empty_position)
            return True
        else:
            return False

    def xǁPuzzleGameǁmove_tile__mutmut_9(self, tile):
        tile_line = self.dic_positions_of_tiles.get(tile)[0]
        tile_column = self.dic_positions_of_tiles.get(tile)[1]
        if self.board.is_inside_the_board(tile_line, None) and self.board.positions_are_adjacent(tile_line, tile_column, self.line_of_empty_position, self.column_of_empty_position):
            self.board.put_tile(tile, self.line_of_empty_position, self.column_of_empty_position)
            self.dic_positions_of_tiles.update({tile: (self.line_of_empty_position, self.column_of_empty_position)})
            self.line_of_empty_position = tile_line
            self.column_of_empty_position = tile_column
            self.board.put_tile(None, self.line_of_empty_position, self.column_of_empty_position)
            return True
        else:
            return False

    def xǁPuzzleGameǁmove_tile__mutmut_10(self, tile):
        tile_line = self.dic_positions_of_tiles.get(tile)[0]
        tile_column = self.dic_positions_of_tiles.get(tile)[1]
        if self.board.is_inside_the_board(tile_column) and self.board.positions_are_adjacent(tile_line, tile_column, self.line_of_empty_position, self.column_of_empty_position):
            self.board.put_tile(tile, self.line_of_empty_position, self.column_of_empty_position)
            self.dic_positions_of_tiles.update({tile: (self.line_of_empty_position, self.column_of_empty_position)})
            self.line_of_empty_position = tile_line
            self.column_of_empty_position = tile_column
            self.board.put_tile(None, self.line_of_empty_position, self.column_of_empty_position)
            return True
        else:
            return False

    def xǁPuzzleGameǁmove_tile__mutmut_11(self, tile):
        tile_line = self.dic_positions_of_tiles.get(tile)[0]
        tile_column = self.dic_positions_of_tiles.get(tile)[1]
        if self.board.is_inside_the_board(tile_line, ) and self.board.positions_are_adjacent(tile_line, tile_column, self.line_of_empty_position, self.column_of_empty_position):
            self.board.put_tile(tile, self.line_of_empty_position, self.column_of_empty_position)
            self.dic_positions_of_tiles.update({tile: (self.line_of_empty_position, self.column_of_empty_position)})
            self.line_of_empty_position = tile_line
            self.column_of_empty_position = tile_column
            self.board.put_tile(None, self.line_of_empty_position, self.column_of_empty_position)
            return True
        else:
            return False

    def xǁPuzzleGameǁmove_tile__mutmut_12(self, tile):
        tile_line = self.dic_positions_of_tiles.get(tile)[0]
        tile_column = self.dic_positions_of_tiles.get(tile)[1]
        if self.board.is_inside_the_board(tile_line, tile_column) and self.board.positions_are_adjacent(None, tile_column, self.line_of_empty_position, self.column_of_empty_position):
            self.board.put_tile(tile, self.line_of_empty_position, self.column_of_empty_position)
            self.dic_positions_of_tiles.update({tile: (self.line_of_empty_position, self.column_of_empty_position)})
            self.line_of_empty_position = tile_line
            self.column_of_empty_position = tile_column
            self.board.put_tile(None, self.line_of_empty_position, self.column_of_empty_position)
            return True
        else:
            return False

    def xǁPuzzleGameǁmove_tile__mutmut_13(self, tile):
        tile_line = self.dic_positions_of_tiles.get(tile)[0]
        tile_column = self.dic_positions_of_tiles.get(tile)[1]
        if self.board.is_inside_the_board(tile_line, tile_column) and self.board.positions_are_adjacent(tile_line, None, self.line_of_empty_position, self.column_of_empty_position):
            self.board.put_tile(tile, self.line_of_empty_position, self.column_of_empty_position)
            self.dic_positions_of_tiles.update({tile: (self.line_of_empty_position, self.column_of_empty_position)})
            self.line_of_empty_position = tile_line
            self.column_of_empty_position = tile_column
            self.board.put_tile(None, self.line_of_empty_position, self.column_of_empty_position)
            return True
        else:
            return False

    def xǁPuzzleGameǁmove_tile__mutmut_14(self, tile):
        tile_line = self.dic_positions_of_tiles.get(tile)[0]
        tile_column = self.dic_positions_of_tiles.get(tile)[1]
        if self.board.is_inside_the_board(tile_line, tile_column) and self.board.positions_are_adjacent(tile_line, tile_column, None, self.column_of_empty_position):
            self.board.put_tile(tile, self.line_of_empty_position, self.column_of_empty_position)
            self.dic_positions_of_tiles.update({tile: (self.line_of_empty_position, self.column_of_empty_position)})
            self.line_of_empty_position = tile_line
            self.column_of_empty_position = tile_column
            self.board.put_tile(None, self.line_of_empty_position, self.column_of_empty_position)
            return True
        else:
            return False

    def xǁPuzzleGameǁmove_tile__mutmut_15(self, tile):
        tile_line = self.dic_positions_of_tiles.get(tile)[0]
        tile_column = self.dic_positions_of_tiles.get(tile)[1]
        if self.board.is_inside_the_board(tile_line, tile_column) and self.board.positions_are_adjacent(tile_line, tile_column, self.line_of_empty_position, None):
            self.board.put_tile(tile, self.line_of_empty_position, self.column_of_empty_position)
            self.dic_positions_of_tiles.update({tile: (self.line_of_empty_position, self.column_of_empty_position)})
            self.line_of_empty_position = tile_line
            self.column_of_empty_position = tile_column
            self.board.put_tile(None, self.line_of_empty_position, self.column_of_empty_position)
            return True
        else:
            return False

    def xǁPuzzleGameǁmove_tile__mutmut_16(self, tile):
        tile_line = self.dic_positions_of_tiles.get(tile)[0]
        tile_column = self.dic_positions_of_tiles.get(tile)[1]
        if self.board.is_inside_the_board(tile_line, tile_column) and self.board.positions_are_adjacent(tile_column, self.line_of_empty_position, self.column_of_empty_position):
            self.board.put_tile(tile, self.line_of_empty_position, self.column_of_empty_position)
            self.dic_positions_of_tiles.update({tile: (self.line_of_empty_position, self.column_of_empty_position)})
            self.line_of_empty_position = tile_line
            self.column_of_empty_position = tile_column
            self.board.put_tile(None, self.line_of_empty_position, self.column_of_empty_position)
            return True
        else:
            return False

    def xǁPuzzleGameǁmove_tile__mutmut_17(self, tile):
        tile_line = self.dic_positions_of_tiles.get(tile)[0]
        tile_column = self.dic_positions_of_tiles.get(tile)[1]
        if self.board.is_inside_the_board(tile_line, tile_column) and self.board.positions_are_adjacent(tile_line, self.line_of_empty_position, self.column_of_empty_position):
            self.board.put_tile(tile, self.line_of_empty_position, self.column_of_empty_position)
            self.dic_positions_of_tiles.update({tile: (self.line_of_empty_position, self.column_of_empty_position)})
            self.line_of_empty_position = tile_line
            self.column_of_empty_position = tile_column
            self.board.put_tile(None, self.line_of_empty_position, self.column_of_empty_position)
            return True
        else:
            return False

    def xǁPuzzleGameǁmove_tile__mutmut_18(self, tile):
        tile_line = self.dic_positions_of_tiles.get(tile)[0]
        tile_column = self.dic_positions_of_tiles.get(tile)[1]
        if self.board.is_inside_the_board(tile_line, tile_column) and self.board.positions_are_adjacent(tile_line, tile_column, self.column_of_empty_position):
            self.board.put_tile(tile, self.line_of_empty_position, self.column_of_empty_position)
            self.dic_positions_of_tiles.update({tile: (self.line_of_empty_position, self.column_of_empty_position)})
            self.line_of_empty_position = tile_line
            self.column_of_empty_position = tile_column
            self.board.put_tile(None, self.line_of_empty_position, self.column_of_empty_position)
            return True
        else:
            return False

    def xǁPuzzleGameǁmove_tile__mutmut_19(self, tile):
        tile_line = self.dic_positions_of_tiles.get(tile)[0]
        tile_column = self.dic_positions_of_tiles.get(tile)[1]
        if self.board.is_inside_the_board(tile_line, tile_column) and self.board.positions_are_adjacent(tile_line, tile_column, self.line_of_empty_position, ):
            self.board.put_tile(tile, self.line_of_empty_position, self.column_of_empty_position)
            self.dic_positions_of_tiles.update({tile: (self.line_of_empty_position, self.column_of_empty_position)})
            self.line_of_empty_position = tile_line
            self.column_of_empty_position = tile_column
            self.board.put_tile(None, self.line_of_empty_position, self.column_of_empty_position)
            return True
        else:
            return False

    def xǁPuzzleGameǁmove_tile__mutmut_20(self, tile):
        tile_line = self.dic_positions_of_tiles.get(tile)[0]
        tile_column = self.dic_positions_of_tiles.get(tile)[1]
        if self.board.is_inside_the_board(tile_line, tile_column) and self.board.positions_are_adjacent(tile_line, tile_column, self.line_of_empty_position, self.column_of_empty_position):
            self.board.put_tile(None, self.line_of_empty_position, self.column_of_empty_position)
            self.dic_positions_of_tiles.update({tile: (self.line_of_empty_position, self.column_of_empty_position)})
            self.line_of_empty_position = tile_line
            self.column_of_empty_position = tile_column
            self.board.put_tile(None, self.line_of_empty_position, self.column_of_empty_position)
            return True
        else:
            return False

    def xǁPuzzleGameǁmove_tile__mutmut_21(self, tile):
        tile_line = self.dic_positions_of_tiles.get(tile)[0]
        tile_column = self.dic_positions_of_tiles.get(tile)[1]
        if self.board.is_inside_the_board(tile_line, tile_column) and self.board.positions_are_adjacent(tile_line, tile_column, self.line_of_empty_position, self.column_of_empty_position):
            self.board.put_tile(tile, None, self.column_of_empty_position)
            self.dic_positions_of_tiles.update({tile: (self.line_of_empty_position, self.column_of_empty_position)})
            self.line_of_empty_position = tile_line
            self.column_of_empty_position = tile_column
            self.board.put_tile(None, self.line_of_empty_position, self.column_of_empty_position)
            return True
        else:
            return False

    def xǁPuzzleGameǁmove_tile__mutmut_22(self, tile):
        tile_line = self.dic_positions_of_tiles.get(tile)[0]
        tile_column = self.dic_positions_of_tiles.get(tile)[1]
        if self.board.is_inside_the_board(tile_line, tile_column) and self.board.positions_are_adjacent(tile_line, tile_column, self.line_of_empty_position, self.column_of_empty_position):
            self.board.put_tile(tile, self.line_of_empty_position, None)
            self.dic_positions_of_tiles.update({tile: (self.line_of_empty_position, self.column_of_empty_position)})
            self.line_of_empty_position = tile_line
            self.column_of_empty_position = tile_column
            self.board.put_tile(None, self.line_of_empty_position, self.column_of_empty_position)
            return True
        else:
            return False

    def xǁPuzzleGameǁmove_tile__mutmut_23(self, tile):
        tile_line = self.dic_positions_of_tiles.get(tile)[0]
        tile_column = self.dic_positions_of_tiles.get(tile)[1]
        if self.board.is_inside_the_board(tile_line, tile_column) and self.board.positions_are_adjacent(tile_line, tile_column, self.line_of_empty_position, self.column_of_empty_position):
            self.board.put_tile(self.line_of_empty_position, self.column_of_empty_position)
            self.dic_positions_of_tiles.update({tile: (self.line_of_empty_position, self.column_of_empty_position)})
            self.line_of_empty_position = tile_line
            self.column_of_empty_position = tile_column
            self.board.put_tile(None, self.line_of_empty_position, self.column_of_empty_position)
            return True
        else:
            return False

    def xǁPuzzleGameǁmove_tile__mutmut_24(self, tile):
        tile_line = self.dic_positions_of_tiles.get(tile)[0]
        tile_column = self.dic_positions_of_tiles.get(tile)[1]
        if self.board.is_inside_the_board(tile_line, tile_column) and self.board.positions_are_adjacent(tile_line, tile_column, self.line_of_empty_position, self.column_of_empty_position):
            self.board.put_tile(tile, self.column_of_empty_position)
            self.dic_positions_of_tiles.update({tile: (self.line_of_empty_position, self.column_of_empty_position)})
            self.line_of_empty_position = tile_line
            self.column_of_empty_position = tile_column
            self.board.put_tile(None, self.line_of_empty_position, self.column_of_empty_position)
            return True
        else:
            return False

    def xǁPuzzleGameǁmove_tile__mutmut_25(self, tile):
        tile_line = self.dic_positions_of_tiles.get(tile)[0]
        tile_column = self.dic_positions_of_tiles.get(tile)[1]
        if self.board.is_inside_the_board(tile_line, tile_column) and self.board.positions_are_adjacent(tile_line, tile_column, self.line_of_empty_position, self.column_of_empty_position):
            self.board.put_tile(tile, self.line_of_empty_position, )
            self.dic_positions_of_tiles.update({tile: (self.line_of_empty_position, self.column_of_empty_position)})
            self.line_of_empty_position = tile_line
            self.column_of_empty_position = tile_column
            self.board.put_tile(None, self.line_of_empty_position, self.column_of_empty_position)
            return True
        else:
            return False

    def xǁPuzzleGameǁmove_tile__mutmut_26(self, tile):
        tile_line = self.dic_positions_of_tiles.get(tile)[0]
        tile_column = self.dic_positions_of_tiles.get(tile)[1]
        if self.board.is_inside_the_board(tile_line, tile_column) and self.board.positions_are_adjacent(tile_line, tile_column, self.line_of_empty_position, self.column_of_empty_position):
            self.board.put_tile(tile, self.line_of_empty_position, self.column_of_empty_position)
            self.dic_positions_of_tiles.update(None)
            self.line_of_empty_position = tile_line
            self.column_of_empty_position = tile_column
            self.board.put_tile(None, self.line_of_empty_position, self.column_of_empty_position)
            return True
        else:
            return False

    def xǁPuzzleGameǁmove_tile__mutmut_27(self, tile):
        tile_line = self.dic_positions_of_tiles.get(tile)[0]
        tile_column = self.dic_positions_of_tiles.get(tile)[1]
        if self.board.is_inside_the_board(tile_line, tile_column) and self.board.positions_are_adjacent(tile_line, tile_column, self.line_of_empty_position, self.column_of_empty_position):
            self.board.put_tile(tile, self.line_of_empty_position, self.column_of_empty_position)
            self.dic_positions_of_tiles.update({tile: (self.line_of_empty_position, self.column_of_empty_position)})
            self.line_of_empty_position = None
            self.column_of_empty_position = tile_column
            self.board.put_tile(None, self.line_of_empty_position, self.column_of_empty_position)
            return True
        else:
            return False

    def xǁPuzzleGameǁmove_tile__mutmut_28(self, tile):
        tile_line = self.dic_positions_of_tiles.get(tile)[0]
        tile_column = self.dic_positions_of_tiles.get(tile)[1]
        if self.board.is_inside_the_board(tile_line, tile_column) and self.board.positions_are_adjacent(tile_line, tile_column, self.line_of_empty_position, self.column_of_empty_position):
            self.board.put_tile(tile, self.line_of_empty_position, self.column_of_empty_position)
            self.dic_positions_of_tiles.update({tile: (self.line_of_empty_position, self.column_of_empty_position)})
            self.line_of_empty_position = tile_line
            self.column_of_empty_position = None
            self.board.put_tile(None, self.line_of_empty_position, self.column_of_empty_position)
            return True
        else:
            return False

    def xǁPuzzleGameǁmove_tile__mutmut_29(self, tile):
        tile_line = self.dic_positions_of_tiles.get(tile)[0]
        tile_column = self.dic_positions_of_tiles.get(tile)[1]
        if self.board.is_inside_the_board(tile_line, tile_column) and self.board.positions_are_adjacent(tile_line, tile_column, self.line_of_empty_position, self.column_of_empty_position):
            self.board.put_tile(tile, self.line_of_empty_position, self.column_of_empty_position)
            self.dic_positions_of_tiles.update({tile: (self.line_of_empty_position, self.column_of_empty_position)})
            self.line_of_empty_position = tile_line
            self.column_of_empty_position = tile_column
            self.board.put_tile(None, None, self.column_of_empty_position)
            return True
        else:
            return False

    def xǁPuzzleGameǁmove_tile__mutmut_30(self, tile):
        tile_line = self.dic_positions_of_tiles.get(tile)[0]
        tile_column = self.dic_positions_of_tiles.get(tile)[1]
        if self.board.is_inside_the_board(tile_line, tile_column) and self.board.positions_are_adjacent(tile_line, tile_column, self.line_of_empty_position, self.column_of_empty_position):
            self.board.put_tile(tile, self.line_of_empty_position, self.column_of_empty_position)
            self.dic_positions_of_tiles.update({tile: (self.line_of_empty_position, self.column_of_empty_position)})
            self.line_of_empty_position = tile_line
            self.column_of_empty_position = tile_column
            self.board.put_tile(None, self.line_of_empty_position, None)
            return True
        else:
            return False

    def xǁPuzzleGameǁmove_tile__mutmut_31(self, tile):
        tile_line = self.dic_positions_of_tiles.get(tile)[0]
        tile_column = self.dic_positions_of_tiles.get(tile)[1]
        if self.board.is_inside_the_board(tile_line, tile_column) and self.board.positions_are_adjacent(tile_line, tile_column, self.line_of_empty_position, self.column_of_empty_position):
            self.board.put_tile(tile, self.line_of_empty_position, self.column_of_empty_position)
            self.dic_positions_of_tiles.update({tile: (self.line_of_empty_position, self.column_of_empty_position)})
            self.line_of_empty_position = tile_line
            self.column_of_empty_position = tile_column
            self.board.put_tile(self.line_of_empty_position, self.column_of_empty_position)
            return True
        else:
            return False

    def xǁPuzzleGameǁmove_tile__mutmut_32(self, tile):
        tile_line = self.dic_positions_of_tiles.get(tile)[0]
        tile_column = self.dic_positions_of_tiles.get(tile)[1]
        if self.board.is_inside_the_board(tile_line, tile_column) and self.board.positions_are_adjacent(tile_line, tile_column, self.line_of_empty_position, self.column_of_empty_position):
            self.board.put_tile(tile, self.line_of_empty_position, self.column_of_empty_position)
            self.dic_positions_of_tiles.update({tile: (self.line_of_empty_position, self.column_of_empty_position)})
            self.line_of_empty_position = tile_line
            self.column_of_empty_position = tile_column
            self.board.put_tile(None, self.column_of_empty_position)
            return True
        else:
            return False

    def xǁPuzzleGameǁmove_tile__mutmut_33(self, tile):
        tile_line = self.dic_positions_of_tiles.get(tile)[0]
        tile_column = self.dic_positions_of_tiles.get(tile)[1]
        if self.board.is_inside_the_board(tile_line, tile_column) and self.board.positions_are_adjacent(tile_line, tile_column, self.line_of_empty_position, self.column_of_empty_position):
            self.board.put_tile(tile, self.line_of_empty_position, self.column_of_empty_position)
            self.dic_positions_of_tiles.update({tile: (self.line_of_empty_position, self.column_of_empty_position)})
            self.line_of_empty_position = tile_line
            self.column_of_empty_position = tile_column
            self.board.put_tile(None, self.line_of_empty_position, )
            return True
        else:
            return False

    def xǁPuzzleGameǁmove_tile__mutmut_34(self, tile):
        tile_line = self.dic_positions_of_tiles.get(tile)[0]
        tile_column = self.dic_positions_of_tiles.get(tile)[1]
        if self.board.is_inside_the_board(tile_line, tile_column) and self.board.positions_are_adjacent(tile_line, tile_column, self.line_of_empty_position, self.column_of_empty_position):
            self.board.put_tile(tile, self.line_of_empty_position, self.column_of_empty_position)
            self.dic_positions_of_tiles.update({tile: (self.line_of_empty_position, self.column_of_empty_position)})
            self.line_of_empty_position = tile_line
            self.column_of_empty_position = tile_column
            self.board.put_tile(None, self.line_of_empty_position, self.column_of_empty_position)
            return False
        else:
            return False

    def xǁPuzzleGameǁmove_tile__mutmut_35(self, tile):
        tile_line = self.dic_positions_of_tiles.get(tile)[0]
        tile_column = self.dic_positions_of_tiles.get(tile)[1]
        if self.board.is_inside_the_board(tile_line, tile_column) and self.board.positions_are_adjacent(tile_line, tile_column, self.line_of_empty_position, self.column_of_empty_position):
            self.board.put_tile(tile, self.line_of_empty_position, self.column_of_empty_position)
            self.dic_positions_of_tiles.update({tile: (self.line_of_empty_position, self.column_of_empty_position)})
            self.line_of_empty_position = tile_line
            self.column_of_empty_position = tile_column
            self.board.put_tile(None, self.line_of_empty_position, self.column_of_empty_position)
            return True
        else:
            return True
    
    xǁPuzzleGameǁmove_tile__mutmut_mutants : ClassVar[MutantDict] = {
    'xǁPuzzleGameǁmove_tile__mutmut_1': xǁPuzzleGameǁmove_tile__mutmut_1, 
        'xǁPuzzleGameǁmove_tile__mutmut_2': xǁPuzzleGameǁmove_tile__mutmut_2, 
        'xǁPuzzleGameǁmove_tile__mutmut_3': xǁPuzzleGameǁmove_tile__mutmut_3, 
        'xǁPuzzleGameǁmove_tile__mutmut_4': xǁPuzzleGameǁmove_tile__mutmut_4, 
        'xǁPuzzleGameǁmove_tile__mutmut_5': xǁPuzzleGameǁmove_tile__mutmut_5, 
        'xǁPuzzleGameǁmove_tile__mutmut_6': xǁPuzzleGameǁmove_tile__mutmut_6, 
        'xǁPuzzleGameǁmove_tile__mutmut_7': xǁPuzzleGameǁmove_tile__mutmut_7, 
        'xǁPuzzleGameǁmove_tile__mutmut_8': xǁPuzzleGameǁmove_tile__mutmut_8, 
        'xǁPuzzleGameǁmove_tile__mutmut_9': xǁPuzzleGameǁmove_tile__mutmut_9, 
        'xǁPuzzleGameǁmove_tile__mutmut_10': xǁPuzzleGameǁmove_tile__mutmut_10, 
        'xǁPuzzleGameǁmove_tile__mutmut_11': xǁPuzzleGameǁmove_tile__mutmut_11, 
        'xǁPuzzleGameǁmove_tile__mutmut_12': xǁPuzzleGameǁmove_tile__mutmut_12, 
        'xǁPuzzleGameǁmove_tile__mutmut_13': xǁPuzzleGameǁmove_tile__mutmut_13, 
        'xǁPuzzleGameǁmove_tile__mutmut_14': xǁPuzzleGameǁmove_tile__mutmut_14, 
        'xǁPuzzleGameǁmove_tile__mutmut_15': xǁPuzzleGameǁmove_tile__mutmut_15, 
        'xǁPuzzleGameǁmove_tile__mutmut_16': xǁPuzzleGameǁmove_tile__mutmut_16, 
        'xǁPuzzleGameǁmove_tile__mutmut_17': xǁPuzzleGameǁmove_tile__mutmut_17, 
        'xǁPuzzleGameǁmove_tile__mutmut_18': xǁPuzzleGameǁmove_tile__mutmut_18, 
        'xǁPuzzleGameǁmove_tile__mutmut_19': xǁPuzzleGameǁmove_tile__mutmut_19, 
        'xǁPuzzleGameǁmove_tile__mutmut_20': xǁPuzzleGameǁmove_tile__mutmut_20, 
        'xǁPuzzleGameǁmove_tile__mutmut_21': xǁPuzzleGameǁmove_tile__mutmut_21, 
        'xǁPuzzleGameǁmove_tile__mutmut_22': xǁPuzzleGameǁmove_tile__mutmut_22, 
        'xǁPuzzleGameǁmove_tile__mutmut_23': xǁPuzzleGameǁmove_tile__mutmut_23, 
        'xǁPuzzleGameǁmove_tile__mutmut_24': xǁPuzzleGameǁmove_tile__mutmut_24, 
        'xǁPuzzleGameǁmove_tile__mutmut_25': xǁPuzzleGameǁmove_tile__mutmut_25, 
        'xǁPuzzleGameǁmove_tile__mutmut_26': xǁPuzzleGameǁmove_tile__mutmut_26, 
        'xǁPuzzleGameǁmove_tile__mutmut_27': xǁPuzzleGameǁmove_tile__mutmut_27, 
        'xǁPuzzleGameǁmove_tile__mutmut_28': xǁPuzzleGameǁmove_tile__mutmut_28, 
        'xǁPuzzleGameǁmove_tile__mutmut_29': xǁPuzzleGameǁmove_tile__mutmut_29, 
        'xǁPuzzleGameǁmove_tile__mutmut_30': xǁPuzzleGameǁmove_tile__mutmut_30, 
        'xǁPuzzleGameǁmove_tile__mutmut_31': xǁPuzzleGameǁmove_tile__mutmut_31, 
        'xǁPuzzleGameǁmove_tile__mutmut_32': xǁPuzzleGameǁmove_tile__mutmut_32, 
        'xǁPuzzleGameǁmove_tile__mutmut_33': xǁPuzzleGameǁmove_tile__mutmut_33, 
        'xǁPuzzleGameǁmove_tile__mutmut_34': xǁPuzzleGameǁmove_tile__mutmut_34, 
        'xǁPuzzleGameǁmove_tile__mutmut_35': xǁPuzzleGameǁmove_tile__mutmut_35
    }
    
    def move_tile(self, *args, **kwargs):
        result = _mutmut_trampoline(object.__getattribute__(self, "xǁPuzzleGameǁmove_tile__mutmut_orig"), object.__getattribute__(self, "xǁPuzzleGameǁmove_tile__mutmut_mutants"), args, kwargs, self)
        return result 
    
    move_tile.__signature__ = _mutmut_signature(xǁPuzzleGameǁmove_tile__mutmut_orig)
    xǁPuzzleGameǁmove_tile__mutmut_orig.__name__ = 'xǁPuzzleGameǁmove_tile'

    def xǁPuzzleGameǁ__move_empty_cell_to_down____mutmut_orig (self):
        if self.board.is_in_the_bottom_border(self.line_of_empty_position, self.column_of_empty_position):
            return False
        else:
            new_empty_line = self.line_of_empty_position + 1
            new_empty_column = self.column_of_empty_position
            tile = self.get_tile(new_empty_line, new_empty_column)
            self.board.change_tiles_in_positions(self.line_of_empty_position, self.column_of_empty_position, new_empty_line, new_empty_column)
            self.dic_positions_of_tiles.update({tile: (self.line_of_empty_position, self.column_of_empty_position)})
            self.line_of_empty_position = new_empty_line
            self.column_of_empty_position = new_empty_column
            return True

    def xǁPuzzleGameǁ__move_empty_cell_to_down____mutmut_1 (self):
        if self.board.is_in_the_bottom_border(None, self.column_of_empty_position):
            return False
        else:
            new_empty_line = self.line_of_empty_position + 1
            new_empty_column = self.column_of_empty_position
            tile = self.get_tile(new_empty_line, new_empty_column)
            self.board.change_tiles_in_positions(self.line_of_empty_position, self.column_of_empty_position, new_empty_line, new_empty_column)
            self.dic_positions_of_tiles.update({tile: (self.line_of_empty_position, self.column_of_empty_position)})
            self.line_of_empty_position = new_empty_line
            self.column_of_empty_position = new_empty_column
            return True

    def xǁPuzzleGameǁ__move_empty_cell_to_down____mutmut_2 (self):
        if self.board.is_in_the_bottom_border(self.line_of_empty_position, None):
            return False
        else:
            new_empty_line = self.line_of_empty_position + 1
            new_empty_column = self.column_of_empty_position
            tile = self.get_tile(new_empty_line, new_empty_column)
            self.board.change_tiles_in_positions(self.line_of_empty_position, self.column_of_empty_position, new_empty_line, new_empty_column)
            self.dic_positions_of_tiles.update({tile: (self.line_of_empty_position, self.column_of_empty_position)})
            self.line_of_empty_position = new_empty_line
            self.column_of_empty_position = new_empty_column
            return True

    def xǁPuzzleGameǁ__move_empty_cell_to_down____mutmut_3 (self):
        if self.board.is_in_the_bottom_border(self.column_of_empty_position):
            return False
        else:
            new_empty_line = self.line_of_empty_position + 1
            new_empty_column = self.column_of_empty_position
            tile = self.get_tile(new_empty_line, new_empty_column)
            self.board.change_tiles_in_positions(self.line_of_empty_position, self.column_of_empty_position, new_empty_line, new_empty_column)
            self.dic_positions_of_tiles.update({tile: (self.line_of_empty_position, self.column_of_empty_position)})
            self.line_of_empty_position = new_empty_line
            self.column_of_empty_position = new_empty_column
            return True

    def xǁPuzzleGameǁ__move_empty_cell_to_down____mutmut_4 (self):
        if self.board.is_in_the_bottom_border(self.line_of_empty_position, ):
            return False
        else:
            new_empty_line = self.line_of_empty_position + 1
            new_empty_column = self.column_of_empty_position
            tile = self.get_tile(new_empty_line, new_empty_column)
            self.board.change_tiles_in_positions(self.line_of_empty_position, self.column_of_empty_position, new_empty_line, new_empty_column)
            self.dic_positions_of_tiles.update({tile: (self.line_of_empty_position, self.column_of_empty_position)})
            self.line_of_empty_position = new_empty_line
            self.column_of_empty_position = new_empty_column
            return True

    def xǁPuzzleGameǁ__move_empty_cell_to_down____mutmut_5 (self):
        if self.board.is_in_the_bottom_border(self.line_of_empty_position, self.column_of_empty_position):
            return True
        else:
            new_empty_line = self.line_of_empty_position + 1
            new_empty_column = self.column_of_empty_position
            tile = self.get_tile(new_empty_line, new_empty_column)
            self.board.change_tiles_in_positions(self.line_of_empty_position, self.column_of_empty_position, new_empty_line, new_empty_column)
            self.dic_positions_of_tiles.update({tile: (self.line_of_empty_position, self.column_of_empty_position)})
            self.line_of_empty_position = new_empty_line
            self.column_of_empty_position = new_empty_column
            return True

    def xǁPuzzleGameǁ__move_empty_cell_to_down____mutmut_6 (self):
        if self.board.is_in_the_bottom_border(self.line_of_empty_position, self.column_of_empty_position):
            return False
        else:
            new_empty_line = None
            new_empty_column = self.column_of_empty_position
            tile = self.get_tile(new_empty_line, new_empty_column)
            self.board.change_tiles_in_positions(self.line_of_empty_position, self.column_of_empty_position, new_empty_line, new_empty_column)
            self.dic_positions_of_tiles.update({tile: (self.line_of_empty_position, self.column_of_empty_position)})
            self.line_of_empty_position = new_empty_line
            self.column_of_empty_position = new_empty_column
            return True

    def xǁPuzzleGameǁ__move_empty_cell_to_down____mutmut_7 (self):
        if self.board.is_in_the_bottom_border(self.line_of_empty_position, self.column_of_empty_position):
            return False
        else:
            new_empty_line = self.line_of_empty_position - 1
            new_empty_column = self.column_of_empty_position
            tile = self.get_tile(new_empty_line, new_empty_column)
            self.board.change_tiles_in_positions(self.line_of_empty_position, self.column_of_empty_position, new_empty_line, new_empty_column)
            self.dic_positions_of_tiles.update({tile: (self.line_of_empty_position, self.column_of_empty_position)})
            self.line_of_empty_position = new_empty_line
            self.column_of_empty_position = new_empty_column
            return True

    def xǁPuzzleGameǁ__move_empty_cell_to_down____mutmut_8 (self):
        if self.board.is_in_the_bottom_border(self.line_of_empty_position, self.column_of_empty_position):
            return False
        else:
            new_empty_line = self.line_of_empty_position + 2
            new_empty_column = self.column_of_empty_position
            tile = self.get_tile(new_empty_line, new_empty_column)
            self.board.change_tiles_in_positions(self.line_of_empty_position, self.column_of_empty_position, new_empty_line, new_empty_column)
            self.dic_positions_of_tiles.update({tile: (self.line_of_empty_position, self.column_of_empty_position)})
            self.line_of_empty_position = new_empty_line
            self.column_of_empty_position = new_empty_column
            return True

    def xǁPuzzleGameǁ__move_empty_cell_to_down____mutmut_9 (self):
        if self.board.is_in_the_bottom_border(self.line_of_empty_position, self.column_of_empty_position):
            return False
        else:
            new_empty_line = self.line_of_empty_position + 1
            new_empty_column = None
            tile = self.get_tile(new_empty_line, new_empty_column)
            self.board.change_tiles_in_positions(self.line_of_empty_position, self.column_of_empty_position, new_empty_line, new_empty_column)
            self.dic_positions_of_tiles.update({tile: (self.line_of_empty_position, self.column_of_empty_position)})
            self.line_of_empty_position = new_empty_line
            self.column_of_empty_position = new_empty_column
            return True

    def xǁPuzzleGameǁ__move_empty_cell_to_down____mutmut_10 (self):
        if self.board.is_in_the_bottom_border(self.line_of_empty_position, self.column_of_empty_position):
            return False
        else:
            new_empty_line = self.line_of_empty_position + 1
            new_empty_column = self.column_of_empty_position
            tile = None
            self.board.change_tiles_in_positions(self.line_of_empty_position, self.column_of_empty_position, new_empty_line, new_empty_column)
            self.dic_positions_of_tiles.update({tile: (self.line_of_empty_position, self.column_of_empty_position)})
            self.line_of_empty_position = new_empty_line
            self.column_of_empty_position = new_empty_column
            return True

    def xǁPuzzleGameǁ__move_empty_cell_to_down____mutmut_11 (self):
        if self.board.is_in_the_bottom_border(self.line_of_empty_position, self.column_of_empty_position):
            return False
        else:
            new_empty_line = self.line_of_empty_position + 1
            new_empty_column = self.column_of_empty_position
            tile = self.get_tile(None, new_empty_column)
            self.board.change_tiles_in_positions(self.line_of_empty_position, self.column_of_empty_position, new_empty_line, new_empty_column)
            self.dic_positions_of_tiles.update({tile: (self.line_of_empty_position, self.column_of_empty_position)})
            self.line_of_empty_position = new_empty_line
            self.column_of_empty_position = new_empty_column
            return True

    def xǁPuzzleGameǁ__move_empty_cell_to_down____mutmut_12 (self):
        if self.board.is_in_the_bottom_border(self.line_of_empty_position, self.column_of_empty_position):
            return False
        else:
            new_empty_line = self.line_of_empty_position + 1
            new_empty_column = self.column_of_empty_position
            tile = self.get_tile(new_empty_line, None)
            self.board.change_tiles_in_positions(self.line_of_empty_position, self.column_of_empty_position, new_empty_line, new_empty_column)
            self.dic_positions_of_tiles.update({tile: (self.line_of_empty_position, self.column_of_empty_position)})
            self.line_of_empty_position = new_empty_line
            self.column_of_empty_position = new_empty_column
            return True

    def xǁPuzzleGameǁ__move_empty_cell_to_down____mutmut_13 (self):
        if self.board.is_in_the_bottom_border(self.line_of_empty_position, self.column_of_empty_position):
            return False
        else:
            new_empty_line = self.line_of_empty_position + 1
            new_empty_column = self.column_of_empty_position
            tile = self.get_tile(new_empty_column)
            self.board.change_tiles_in_positions(self.line_of_empty_position, self.column_of_empty_position, new_empty_line, new_empty_column)
            self.dic_positions_of_tiles.update({tile: (self.line_of_empty_position, self.column_of_empty_position)})
            self.line_of_empty_position = new_empty_line
            self.column_of_empty_position = new_empty_column
            return True

    def xǁPuzzleGameǁ__move_empty_cell_to_down____mutmut_14 (self):
        if self.board.is_in_the_bottom_border(self.line_of_empty_position, self.column_of_empty_position):
            return False
        else:
            new_empty_line = self.line_of_empty_position + 1
            new_empty_column = self.column_of_empty_position
            tile = self.get_tile(new_empty_line, )
            self.board.change_tiles_in_positions(self.line_of_empty_position, self.column_of_empty_position, new_empty_line, new_empty_column)
            self.dic_positions_of_tiles.update({tile: (self.line_of_empty_position, self.column_of_empty_position)})
            self.line_of_empty_position = new_empty_line
            self.column_of_empty_position = new_empty_column
            return True

    def xǁPuzzleGameǁ__move_empty_cell_to_down____mutmut_15 (self):
        if self.board.is_in_the_bottom_border(self.line_of_empty_position, self.column_of_empty_position):
            return False
        else:
            new_empty_line = self.line_of_empty_position + 1
            new_empty_column = self.column_of_empty_position
            tile = self.get_tile(new_empty_line, new_empty_column)
            self.board.change_tiles_in_positions(None, self.column_of_empty_position, new_empty_line, new_empty_column)
            self.dic_positions_of_tiles.update({tile: (self.line_of_empty_position, self.column_of_empty_position)})
            self.line_of_empty_position = new_empty_line
            self.column_of_empty_position = new_empty_column
            return True

    def xǁPuzzleGameǁ__move_empty_cell_to_down____mutmut_16 (self):
        if self.board.is_in_the_bottom_border(self.line_of_empty_position, self.column_of_empty_position):
            return False
        else:
            new_empty_line = self.line_of_empty_position + 1
            new_empty_column = self.column_of_empty_position
            tile = self.get_tile(new_empty_line, new_empty_column)
            self.board.change_tiles_in_positions(self.line_of_empty_position, None, new_empty_line, new_empty_column)
            self.dic_positions_of_tiles.update({tile: (self.line_of_empty_position, self.column_of_empty_position)})
            self.line_of_empty_position = new_empty_line
            self.column_of_empty_position = new_empty_column
            return True

    def xǁPuzzleGameǁ__move_empty_cell_to_down____mutmut_17 (self):
        if self.board.is_in_the_bottom_border(self.line_of_empty_position, self.column_of_empty_position):
            return False
        else:
            new_empty_line = self.line_of_empty_position + 1
            new_empty_column = self.column_of_empty_position
            tile = self.get_tile(new_empty_line, new_empty_column)
            self.board.change_tiles_in_positions(self.line_of_empty_position, self.column_of_empty_position, None, new_empty_column)
            self.dic_positions_of_tiles.update({tile: (self.line_of_empty_position, self.column_of_empty_position)})
            self.line_of_empty_position = new_empty_line
            self.column_of_empty_position = new_empty_column
            return True

    def xǁPuzzleGameǁ__move_empty_cell_to_down____mutmut_18 (self):
        if self.board.is_in_the_bottom_border(self.line_of_empty_position, self.column_of_empty_position):
            return False
        else:
            new_empty_line = self.line_of_empty_position + 1
            new_empty_column = self.column_of_empty_position
            tile = self.get_tile(new_empty_line, new_empty_column)
            self.board.change_tiles_in_positions(self.line_of_empty_position, self.column_of_empty_position, new_empty_line, None)
            self.dic_positions_of_tiles.update({tile: (self.line_of_empty_position, self.column_of_empty_position)})
            self.line_of_empty_position = new_empty_line
            self.column_of_empty_position = new_empty_column
            return True

    def xǁPuzzleGameǁ__move_empty_cell_to_down____mutmut_19 (self):
        if self.board.is_in_the_bottom_border(self.line_of_empty_position, self.column_of_empty_position):
            return False
        else:
            new_empty_line = self.line_of_empty_position + 1
            new_empty_column = self.column_of_empty_position
            tile = self.get_tile(new_empty_line, new_empty_column)
            self.board.change_tiles_in_positions(self.column_of_empty_position, new_empty_line, new_empty_column)
            self.dic_positions_of_tiles.update({tile: (self.line_of_empty_position, self.column_of_empty_position)})
            self.line_of_empty_position = new_empty_line
            self.column_of_empty_position = new_empty_column
            return True

    def xǁPuzzleGameǁ__move_empty_cell_to_down____mutmut_20 (self):
        if self.board.is_in_the_bottom_border(self.line_of_empty_position, self.column_of_empty_position):
            return False
        else:
            new_empty_line = self.line_of_empty_position + 1
            new_empty_column = self.column_of_empty_position
            tile = self.get_tile(new_empty_line, new_empty_column)
            self.board.change_tiles_in_positions(self.line_of_empty_position, new_empty_line, new_empty_column)
            self.dic_positions_of_tiles.update({tile: (self.line_of_empty_position, self.column_of_empty_position)})
            self.line_of_empty_position = new_empty_line
            self.column_of_empty_position = new_empty_column
            return True

    def xǁPuzzleGameǁ__move_empty_cell_to_down____mutmut_21 (self):
        if self.board.is_in_the_bottom_border(self.line_of_empty_position, self.column_of_empty_position):
            return False
        else:
            new_empty_line = self.line_of_empty_position + 1
            new_empty_column = self.column_of_empty_position
            tile = self.get_tile(new_empty_line, new_empty_column)
            self.board.change_tiles_in_positions(self.line_of_empty_position, self.column_of_empty_position, new_empty_column)
            self.dic_positions_of_tiles.update({tile: (self.line_of_empty_position, self.column_of_empty_position)})
            self.line_of_empty_position = new_empty_line
            self.column_of_empty_position = new_empty_column
            return True

    def xǁPuzzleGameǁ__move_empty_cell_to_down____mutmut_22 (self):
        if self.board.is_in_the_bottom_border(self.line_of_empty_position, self.column_of_empty_position):
            return False
        else:
            new_empty_line = self.line_of_empty_position + 1
            new_empty_column = self.column_of_empty_position
            tile = self.get_tile(new_empty_line, new_empty_column)
            self.board.change_tiles_in_positions(self.line_of_empty_position, self.column_of_empty_position, new_empty_line, )
            self.dic_positions_of_tiles.update({tile: (self.line_of_empty_position, self.column_of_empty_position)})
            self.line_of_empty_position = new_empty_line
            self.column_of_empty_position = new_empty_column
            return True

    def xǁPuzzleGameǁ__move_empty_cell_to_down____mutmut_23 (self):
        if self.board.is_in_the_bottom_border(self.line_of_empty_position, self.column_of_empty_position):
            return False
        else:
            new_empty_line = self.line_of_empty_position + 1
            new_empty_column = self.column_of_empty_position
            tile = self.get_tile(new_empty_line, new_empty_column)
            self.board.change_tiles_in_positions(self.line_of_empty_position, self.column_of_empty_position, new_empty_line, new_empty_column)
            self.dic_positions_of_tiles.update(None)
            self.line_of_empty_position = new_empty_line
            self.column_of_empty_position = new_empty_column
            return True

    def xǁPuzzleGameǁ__move_empty_cell_to_down____mutmut_24 (self):
        if self.board.is_in_the_bottom_border(self.line_of_empty_position, self.column_of_empty_position):
            return False
        else:
            new_empty_line = self.line_of_empty_position + 1
            new_empty_column = self.column_of_empty_position
            tile = self.get_tile(new_empty_line, new_empty_column)
            self.board.change_tiles_in_positions(self.line_of_empty_position, self.column_of_empty_position, new_empty_line, new_empty_column)
            self.dic_positions_of_tiles.update({tile: (self.line_of_empty_position, self.column_of_empty_position)})
            self.line_of_empty_position = None
            self.column_of_empty_position = new_empty_column
            return True

    def xǁPuzzleGameǁ__move_empty_cell_to_down____mutmut_25 (self):
        if self.board.is_in_the_bottom_border(self.line_of_empty_position, self.column_of_empty_position):
            return False
        else:
            new_empty_line = self.line_of_empty_position + 1
            new_empty_column = self.column_of_empty_position
            tile = self.get_tile(new_empty_line, new_empty_column)
            self.board.change_tiles_in_positions(self.line_of_empty_position, self.column_of_empty_position, new_empty_line, new_empty_column)
            self.dic_positions_of_tiles.update({tile: (self.line_of_empty_position, self.column_of_empty_position)})
            self.line_of_empty_position = new_empty_line
            self.column_of_empty_position = None
            return True

    def xǁPuzzleGameǁ__move_empty_cell_to_down____mutmut_26 (self):
        if self.board.is_in_the_bottom_border(self.line_of_empty_position, self.column_of_empty_position):
            return False
        else:
            new_empty_line = self.line_of_empty_position + 1
            new_empty_column = self.column_of_empty_position
            tile = self.get_tile(new_empty_line, new_empty_column)
            self.board.change_tiles_in_positions(self.line_of_empty_position, self.column_of_empty_position, new_empty_line, new_empty_column)
            self.dic_positions_of_tiles.update({tile: (self.line_of_empty_position, self.column_of_empty_position)})
            self.line_of_empty_position = new_empty_line
            self.column_of_empty_position = new_empty_column
            return False
    
    xǁPuzzleGameǁ__move_empty_cell_to_down____mutmut_mutants : ClassVar[MutantDict] = {
    'xǁPuzzleGameǁ__move_empty_cell_to_down____mutmut_1': xǁPuzzleGameǁ__move_empty_cell_to_down____mutmut_1, 
        'xǁPuzzleGameǁ__move_empty_cell_to_down____mutmut_2': xǁPuzzleGameǁ__move_empty_cell_to_down____mutmut_2, 
        'xǁPuzzleGameǁ__move_empty_cell_to_down____mutmut_3': xǁPuzzleGameǁ__move_empty_cell_to_down____mutmut_3, 
        'xǁPuzzleGameǁ__move_empty_cell_to_down____mutmut_4': xǁPuzzleGameǁ__move_empty_cell_to_down____mutmut_4, 
        'xǁPuzzleGameǁ__move_empty_cell_to_down____mutmut_5': xǁPuzzleGameǁ__move_empty_cell_to_down____mutmut_5, 
        'xǁPuzzleGameǁ__move_empty_cell_to_down____mutmut_6': xǁPuzzleGameǁ__move_empty_cell_to_down____mutmut_6, 
        'xǁPuzzleGameǁ__move_empty_cell_to_down____mutmut_7': xǁPuzzleGameǁ__move_empty_cell_to_down____mutmut_7, 
        'xǁPuzzleGameǁ__move_empty_cell_to_down____mutmut_8': xǁPuzzleGameǁ__move_empty_cell_to_down____mutmut_8, 
        'xǁPuzzleGameǁ__move_empty_cell_to_down____mutmut_9': xǁPuzzleGameǁ__move_empty_cell_to_down____mutmut_9, 
        'xǁPuzzleGameǁ__move_empty_cell_to_down____mutmut_10': xǁPuzzleGameǁ__move_empty_cell_to_down____mutmut_10, 
        'xǁPuzzleGameǁ__move_empty_cell_to_down____mutmut_11': xǁPuzzleGameǁ__move_empty_cell_to_down____mutmut_11, 
        'xǁPuzzleGameǁ__move_empty_cell_to_down____mutmut_12': xǁPuzzleGameǁ__move_empty_cell_to_down____mutmut_12, 
        'xǁPuzzleGameǁ__move_empty_cell_to_down____mutmut_13': xǁPuzzleGameǁ__move_empty_cell_to_down____mutmut_13, 
        'xǁPuzzleGameǁ__move_empty_cell_to_down____mutmut_14': xǁPuzzleGameǁ__move_empty_cell_to_down____mutmut_14, 
        'xǁPuzzleGameǁ__move_empty_cell_to_down____mutmut_15': xǁPuzzleGameǁ__move_empty_cell_to_down____mutmut_15, 
        'xǁPuzzleGameǁ__move_empty_cell_to_down____mutmut_16': xǁPuzzleGameǁ__move_empty_cell_to_down____mutmut_16, 
        'xǁPuzzleGameǁ__move_empty_cell_to_down____mutmut_17': xǁPuzzleGameǁ__move_empty_cell_to_down____mutmut_17, 
        'xǁPuzzleGameǁ__move_empty_cell_to_down____mutmut_18': xǁPuzzleGameǁ__move_empty_cell_to_down____mutmut_18, 
        'xǁPuzzleGameǁ__move_empty_cell_to_down____mutmut_19': xǁPuzzleGameǁ__move_empty_cell_to_down____mutmut_19, 
        'xǁPuzzleGameǁ__move_empty_cell_to_down____mutmut_20': xǁPuzzleGameǁ__move_empty_cell_to_down____mutmut_20, 
        'xǁPuzzleGameǁ__move_empty_cell_to_down____mutmut_21': xǁPuzzleGameǁ__move_empty_cell_to_down____mutmut_21, 
        'xǁPuzzleGameǁ__move_empty_cell_to_down____mutmut_22': xǁPuzzleGameǁ__move_empty_cell_to_down____mutmut_22, 
        'xǁPuzzleGameǁ__move_empty_cell_to_down____mutmut_23': xǁPuzzleGameǁ__move_empty_cell_to_down____mutmut_23, 
        'xǁPuzzleGameǁ__move_empty_cell_to_down____mutmut_24': xǁPuzzleGameǁ__move_empty_cell_to_down____mutmut_24, 
        'xǁPuzzleGameǁ__move_empty_cell_to_down____mutmut_25': xǁPuzzleGameǁ__move_empty_cell_to_down____mutmut_25, 
        'xǁPuzzleGameǁ__move_empty_cell_to_down____mutmut_26': xǁPuzzleGameǁ__move_empty_cell_to_down____mutmut_26
    }
    
    def __move_empty_cell_to_down__(self, *args, **kwargs):
        result = _mutmut_trampoline(object.__getattribute__(self, "xǁPuzzleGameǁ__move_empty_cell_to_down____mutmut_orig"), object.__getattribute__(self, "xǁPuzzleGameǁ__move_empty_cell_to_down____mutmut_mutants"), args, kwargs, self)
        return result 
    
    __move_empty_cell_to_down__.__signature__ = _mutmut_signature(xǁPuzzleGameǁ__move_empty_cell_to_down____mutmut_orig)
    xǁPuzzleGameǁ__move_empty_cell_to_down____mutmut_orig.__name__ = 'xǁPuzzleGameǁ__move_empty_cell_to_down__'

    def xǁPuzzleGameǁ__move_empty_cell_to_up____mutmut_orig (self):
        if self.board.is_in_the_superior_border(self.line_of_empty_position, self.column_of_empty_position):
            return False
        else:
            new_empty_line = self.line_of_empty_position - 1
            new_empty_column = self.column_of_empty_position
            tile = self.get_tile(new_empty_line, new_empty_column)
            self.board.change_tiles_in_positions(self.line_of_empty_position, self.column_of_empty_position, new_empty_line, new_empty_column)
            self.dic_positions_of_tiles.update({tile: (self.line_of_empty_position, self.column_of_empty_position)})
            self.line_of_empty_position = new_empty_line
            self.column_of_empty_position = new_empty_column
            return True

    def xǁPuzzleGameǁ__move_empty_cell_to_up____mutmut_1 (self):
        if self.board.is_in_the_superior_border(None, self.column_of_empty_position):
            return False
        else:
            new_empty_line = self.line_of_empty_position - 1
            new_empty_column = self.column_of_empty_position
            tile = self.get_tile(new_empty_line, new_empty_column)
            self.board.change_tiles_in_positions(self.line_of_empty_position, self.column_of_empty_position, new_empty_line, new_empty_column)
            self.dic_positions_of_tiles.update({tile: (self.line_of_empty_position, self.column_of_empty_position)})
            self.line_of_empty_position = new_empty_line
            self.column_of_empty_position = new_empty_column
            return True

    def xǁPuzzleGameǁ__move_empty_cell_to_up____mutmut_2 (self):
        if self.board.is_in_the_superior_border(self.line_of_empty_position, None):
            return False
        else:
            new_empty_line = self.line_of_empty_position - 1
            new_empty_column = self.column_of_empty_position
            tile = self.get_tile(new_empty_line, new_empty_column)
            self.board.change_tiles_in_positions(self.line_of_empty_position, self.column_of_empty_position, new_empty_line, new_empty_column)
            self.dic_positions_of_tiles.update({tile: (self.line_of_empty_position, self.column_of_empty_position)})
            self.line_of_empty_position = new_empty_line
            self.column_of_empty_position = new_empty_column
            return True

    def xǁPuzzleGameǁ__move_empty_cell_to_up____mutmut_3 (self):
        if self.board.is_in_the_superior_border(self.column_of_empty_position):
            return False
        else:
            new_empty_line = self.line_of_empty_position - 1
            new_empty_column = self.column_of_empty_position
            tile = self.get_tile(new_empty_line, new_empty_column)
            self.board.change_tiles_in_positions(self.line_of_empty_position, self.column_of_empty_position, new_empty_line, new_empty_column)
            self.dic_positions_of_tiles.update({tile: (self.line_of_empty_position, self.column_of_empty_position)})
            self.line_of_empty_position = new_empty_line
            self.column_of_empty_position = new_empty_column
            return True

    def xǁPuzzleGameǁ__move_empty_cell_to_up____mutmut_4 (self):
        if self.board.is_in_the_superior_border(self.line_of_empty_position, ):
            return False
        else:
            new_empty_line = self.line_of_empty_position - 1
            new_empty_column = self.column_of_empty_position
            tile = self.get_tile(new_empty_line, new_empty_column)
            self.board.change_tiles_in_positions(self.line_of_empty_position, self.column_of_empty_position, new_empty_line, new_empty_column)
            self.dic_positions_of_tiles.update({tile: (self.line_of_empty_position, self.column_of_empty_position)})
            self.line_of_empty_position = new_empty_line
            self.column_of_empty_position = new_empty_column
            return True

    def xǁPuzzleGameǁ__move_empty_cell_to_up____mutmut_5 (self):
        if self.board.is_in_the_superior_border(self.line_of_empty_position, self.column_of_empty_position):
            return True
        else:
            new_empty_line = self.line_of_empty_position - 1
            new_empty_column = self.column_of_empty_position
            tile = self.get_tile(new_empty_line, new_empty_column)
            self.board.change_tiles_in_positions(self.line_of_empty_position, self.column_of_empty_position, new_empty_line, new_empty_column)
            self.dic_positions_of_tiles.update({tile: (self.line_of_empty_position, self.column_of_empty_position)})
            self.line_of_empty_position = new_empty_line
            self.column_of_empty_position = new_empty_column
            return True

    def xǁPuzzleGameǁ__move_empty_cell_to_up____mutmut_6 (self):
        if self.board.is_in_the_superior_border(self.line_of_empty_position, self.column_of_empty_position):
            return False
        else:
            new_empty_line = None
            new_empty_column = self.column_of_empty_position
            tile = self.get_tile(new_empty_line, new_empty_column)
            self.board.change_tiles_in_positions(self.line_of_empty_position, self.column_of_empty_position, new_empty_line, new_empty_column)
            self.dic_positions_of_tiles.update({tile: (self.line_of_empty_position, self.column_of_empty_position)})
            self.line_of_empty_position = new_empty_line
            self.column_of_empty_position = new_empty_column
            return True

    def xǁPuzzleGameǁ__move_empty_cell_to_up____mutmut_7 (self):
        if self.board.is_in_the_superior_border(self.line_of_empty_position, self.column_of_empty_position):
            return False
        else:
            new_empty_line = self.line_of_empty_position + 1
            new_empty_column = self.column_of_empty_position
            tile = self.get_tile(new_empty_line, new_empty_column)
            self.board.change_tiles_in_positions(self.line_of_empty_position, self.column_of_empty_position, new_empty_line, new_empty_column)
            self.dic_positions_of_tiles.update({tile: (self.line_of_empty_position, self.column_of_empty_position)})
            self.line_of_empty_position = new_empty_line
            self.column_of_empty_position = new_empty_column
            return True

    def xǁPuzzleGameǁ__move_empty_cell_to_up____mutmut_8 (self):
        if self.board.is_in_the_superior_border(self.line_of_empty_position, self.column_of_empty_position):
            return False
        else:
            new_empty_line = self.line_of_empty_position - 2
            new_empty_column = self.column_of_empty_position
            tile = self.get_tile(new_empty_line, new_empty_column)
            self.board.change_tiles_in_positions(self.line_of_empty_position, self.column_of_empty_position, new_empty_line, new_empty_column)
            self.dic_positions_of_tiles.update({tile: (self.line_of_empty_position, self.column_of_empty_position)})
            self.line_of_empty_position = new_empty_line
            self.column_of_empty_position = new_empty_column
            return True

    def xǁPuzzleGameǁ__move_empty_cell_to_up____mutmut_9 (self):
        if self.board.is_in_the_superior_border(self.line_of_empty_position, self.column_of_empty_position):
            return False
        else:
            new_empty_line = self.line_of_empty_position - 1
            new_empty_column = None
            tile = self.get_tile(new_empty_line, new_empty_column)
            self.board.change_tiles_in_positions(self.line_of_empty_position, self.column_of_empty_position, new_empty_line, new_empty_column)
            self.dic_positions_of_tiles.update({tile: (self.line_of_empty_position, self.column_of_empty_position)})
            self.line_of_empty_position = new_empty_line
            self.column_of_empty_position = new_empty_column
            return True

    def xǁPuzzleGameǁ__move_empty_cell_to_up____mutmut_10 (self):
        if self.board.is_in_the_superior_border(self.line_of_empty_position, self.column_of_empty_position):
            return False
        else:
            new_empty_line = self.line_of_empty_position - 1
            new_empty_column = self.column_of_empty_position
            tile = None
            self.board.change_tiles_in_positions(self.line_of_empty_position, self.column_of_empty_position, new_empty_line, new_empty_column)
            self.dic_positions_of_tiles.update({tile: (self.line_of_empty_position, self.column_of_empty_position)})
            self.line_of_empty_position = new_empty_line
            self.column_of_empty_position = new_empty_column
            return True

    def xǁPuzzleGameǁ__move_empty_cell_to_up____mutmut_11 (self):
        if self.board.is_in_the_superior_border(self.line_of_empty_position, self.column_of_empty_position):
            return False
        else:
            new_empty_line = self.line_of_empty_position - 1
            new_empty_column = self.column_of_empty_position
            tile = self.get_tile(None, new_empty_column)
            self.board.change_tiles_in_positions(self.line_of_empty_position, self.column_of_empty_position, new_empty_line, new_empty_column)
            self.dic_positions_of_tiles.update({tile: (self.line_of_empty_position, self.column_of_empty_position)})
            self.line_of_empty_position = new_empty_line
            self.column_of_empty_position = new_empty_column
            return True

    def xǁPuzzleGameǁ__move_empty_cell_to_up____mutmut_12 (self):
        if self.board.is_in_the_superior_border(self.line_of_empty_position, self.column_of_empty_position):
            return False
        else:
            new_empty_line = self.line_of_empty_position - 1
            new_empty_column = self.column_of_empty_position
            tile = self.get_tile(new_empty_line, None)
            self.board.change_tiles_in_positions(self.line_of_empty_position, self.column_of_empty_position, new_empty_line, new_empty_column)
            self.dic_positions_of_tiles.update({tile: (self.line_of_empty_position, self.column_of_empty_position)})
            self.line_of_empty_position = new_empty_line
            self.column_of_empty_position = new_empty_column
            return True

    def xǁPuzzleGameǁ__move_empty_cell_to_up____mutmut_13 (self):
        if self.board.is_in_the_superior_border(self.line_of_empty_position, self.column_of_empty_position):
            return False
        else:
            new_empty_line = self.line_of_empty_position - 1
            new_empty_column = self.column_of_empty_position
            tile = self.get_tile(new_empty_column)
            self.board.change_tiles_in_positions(self.line_of_empty_position, self.column_of_empty_position, new_empty_line, new_empty_column)
            self.dic_positions_of_tiles.update({tile: (self.line_of_empty_position, self.column_of_empty_position)})
            self.line_of_empty_position = new_empty_line
            self.column_of_empty_position = new_empty_column
            return True

    def xǁPuzzleGameǁ__move_empty_cell_to_up____mutmut_14 (self):
        if self.board.is_in_the_superior_border(self.line_of_empty_position, self.column_of_empty_position):
            return False
        else:
            new_empty_line = self.line_of_empty_position - 1
            new_empty_column = self.column_of_empty_position
            tile = self.get_tile(new_empty_line, )
            self.board.change_tiles_in_positions(self.line_of_empty_position, self.column_of_empty_position, new_empty_line, new_empty_column)
            self.dic_positions_of_tiles.update({tile: (self.line_of_empty_position, self.column_of_empty_position)})
            self.line_of_empty_position = new_empty_line
            self.column_of_empty_position = new_empty_column
            return True

    def xǁPuzzleGameǁ__move_empty_cell_to_up____mutmut_15 (self):
        if self.board.is_in_the_superior_border(self.line_of_empty_position, self.column_of_empty_position):
            return False
        else:
            new_empty_line = self.line_of_empty_position - 1
            new_empty_column = self.column_of_empty_position
            tile = self.get_tile(new_empty_line, new_empty_column)
            self.board.change_tiles_in_positions(None, self.column_of_empty_position, new_empty_line, new_empty_column)
            self.dic_positions_of_tiles.update({tile: (self.line_of_empty_position, self.column_of_empty_position)})
            self.line_of_empty_position = new_empty_line
            self.column_of_empty_position = new_empty_column
            return True

    def xǁPuzzleGameǁ__move_empty_cell_to_up____mutmut_16 (self):
        if self.board.is_in_the_superior_border(self.line_of_empty_position, self.column_of_empty_position):
            return False
        else:
            new_empty_line = self.line_of_empty_position - 1
            new_empty_column = self.column_of_empty_position
            tile = self.get_tile(new_empty_line, new_empty_column)
            self.board.change_tiles_in_positions(self.line_of_empty_position, None, new_empty_line, new_empty_column)
            self.dic_positions_of_tiles.update({tile: (self.line_of_empty_position, self.column_of_empty_position)})
            self.line_of_empty_position = new_empty_line
            self.column_of_empty_position = new_empty_column
            return True

    def xǁPuzzleGameǁ__move_empty_cell_to_up____mutmut_17 (self):
        if self.board.is_in_the_superior_border(self.line_of_empty_position, self.column_of_empty_position):
            return False
        else:
            new_empty_line = self.line_of_empty_position - 1
            new_empty_column = self.column_of_empty_position
            tile = self.get_tile(new_empty_line, new_empty_column)
            self.board.change_tiles_in_positions(self.line_of_empty_position, self.column_of_empty_position, None, new_empty_column)
            self.dic_positions_of_tiles.update({tile: (self.line_of_empty_position, self.column_of_empty_position)})
            self.line_of_empty_position = new_empty_line
            self.column_of_empty_position = new_empty_column
            return True

    def xǁPuzzleGameǁ__move_empty_cell_to_up____mutmut_18 (self):
        if self.board.is_in_the_superior_border(self.line_of_empty_position, self.column_of_empty_position):
            return False
        else:
            new_empty_line = self.line_of_empty_position - 1
            new_empty_column = self.column_of_empty_position
            tile = self.get_tile(new_empty_line, new_empty_column)
            self.board.change_tiles_in_positions(self.line_of_empty_position, self.column_of_empty_position, new_empty_line, None)
            self.dic_positions_of_tiles.update({tile: (self.line_of_empty_position, self.column_of_empty_position)})
            self.line_of_empty_position = new_empty_line
            self.column_of_empty_position = new_empty_column
            return True

    def xǁPuzzleGameǁ__move_empty_cell_to_up____mutmut_19 (self):
        if self.board.is_in_the_superior_border(self.line_of_empty_position, self.column_of_empty_position):
            return False
        else:
            new_empty_line = self.line_of_empty_position - 1
            new_empty_column = self.column_of_empty_position
            tile = self.get_tile(new_empty_line, new_empty_column)
            self.board.change_tiles_in_positions(self.column_of_empty_position, new_empty_line, new_empty_column)
            self.dic_positions_of_tiles.update({tile: (self.line_of_empty_position, self.column_of_empty_position)})
            self.line_of_empty_position = new_empty_line
            self.column_of_empty_position = new_empty_column
            return True

    def xǁPuzzleGameǁ__move_empty_cell_to_up____mutmut_20 (self):
        if self.board.is_in_the_superior_border(self.line_of_empty_position, self.column_of_empty_position):
            return False
        else:
            new_empty_line = self.line_of_empty_position - 1
            new_empty_column = self.column_of_empty_position
            tile = self.get_tile(new_empty_line, new_empty_column)
            self.board.change_tiles_in_positions(self.line_of_empty_position, new_empty_line, new_empty_column)
            self.dic_positions_of_tiles.update({tile: (self.line_of_empty_position, self.column_of_empty_position)})
            self.line_of_empty_position = new_empty_line
            self.column_of_empty_position = new_empty_column
            return True

    def xǁPuzzleGameǁ__move_empty_cell_to_up____mutmut_21 (self):
        if self.board.is_in_the_superior_border(self.line_of_empty_position, self.column_of_empty_position):
            return False
        else:
            new_empty_line = self.line_of_empty_position - 1
            new_empty_column = self.column_of_empty_position
            tile = self.get_tile(new_empty_line, new_empty_column)
            self.board.change_tiles_in_positions(self.line_of_empty_position, self.column_of_empty_position, new_empty_column)
            self.dic_positions_of_tiles.update({tile: (self.line_of_empty_position, self.column_of_empty_position)})
            self.line_of_empty_position = new_empty_line
            self.column_of_empty_position = new_empty_column
            return True

    def xǁPuzzleGameǁ__move_empty_cell_to_up____mutmut_22 (self):
        if self.board.is_in_the_superior_border(self.line_of_empty_position, self.column_of_empty_position):
            return False
        else:
            new_empty_line = self.line_of_empty_position - 1
            new_empty_column = self.column_of_empty_position
            tile = self.get_tile(new_empty_line, new_empty_column)
            self.board.change_tiles_in_positions(self.line_of_empty_position, self.column_of_empty_position, new_empty_line, )
            self.dic_positions_of_tiles.update({tile: (self.line_of_empty_position, self.column_of_empty_position)})
            self.line_of_empty_position = new_empty_line
            self.column_of_empty_position = new_empty_column
            return True

    def xǁPuzzleGameǁ__move_empty_cell_to_up____mutmut_23 (self):
        if self.board.is_in_the_superior_border(self.line_of_empty_position, self.column_of_empty_position):
            return False
        else:
            new_empty_line = self.line_of_empty_position - 1
            new_empty_column = self.column_of_empty_position
            tile = self.get_tile(new_empty_line, new_empty_column)
            self.board.change_tiles_in_positions(self.line_of_empty_position, self.column_of_empty_position, new_empty_line, new_empty_column)
            self.dic_positions_of_tiles.update(None)
            self.line_of_empty_position = new_empty_line
            self.column_of_empty_position = new_empty_column
            return True

    def xǁPuzzleGameǁ__move_empty_cell_to_up____mutmut_24 (self):
        if self.board.is_in_the_superior_border(self.line_of_empty_position, self.column_of_empty_position):
            return False
        else:
            new_empty_line = self.line_of_empty_position - 1
            new_empty_column = self.column_of_empty_position
            tile = self.get_tile(new_empty_line, new_empty_column)
            self.board.change_tiles_in_positions(self.line_of_empty_position, self.column_of_empty_position, new_empty_line, new_empty_column)
            self.dic_positions_of_tiles.update({tile: (self.line_of_empty_position, self.column_of_empty_position)})
            self.line_of_empty_position = None
            self.column_of_empty_position = new_empty_column
            return True

    def xǁPuzzleGameǁ__move_empty_cell_to_up____mutmut_25 (self):
        if self.board.is_in_the_superior_border(self.line_of_empty_position, self.column_of_empty_position):
            return False
        else:
            new_empty_line = self.line_of_empty_position - 1
            new_empty_column = self.column_of_empty_position
            tile = self.get_tile(new_empty_line, new_empty_column)
            self.board.change_tiles_in_positions(self.line_of_empty_position, self.column_of_empty_position, new_empty_line, new_empty_column)
            self.dic_positions_of_tiles.update({tile: (self.line_of_empty_position, self.column_of_empty_position)})
            self.line_of_empty_position = new_empty_line
            self.column_of_empty_position = None
            return True

    def xǁPuzzleGameǁ__move_empty_cell_to_up____mutmut_26 (self):
        if self.board.is_in_the_superior_border(self.line_of_empty_position, self.column_of_empty_position):
            return False
        else:
            new_empty_line = self.line_of_empty_position - 1
            new_empty_column = self.column_of_empty_position
            tile = self.get_tile(new_empty_line, new_empty_column)
            self.board.change_tiles_in_positions(self.line_of_empty_position, self.column_of_empty_position, new_empty_line, new_empty_column)
            self.dic_positions_of_tiles.update({tile: (self.line_of_empty_position, self.column_of_empty_position)})
            self.line_of_empty_position = new_empty_line
            self.column_of_empty_position = new_empty_column
            return False
    
    xǁPuzzleGameǁ__move_empty_cell_to_up____mutmut_mutants : ClassVar[MutantDict] = {
    'xǁPuzzleGameǁ__move_empty_cell_to_up____mutmut_1': xǁPuzzleGameǁ__move_empty_cell_to_up____mutmut_1, 
        'xǁPuzzleGameǁ__move_empty_cell_to_up____mutmut_2': xǁPuzzleGameǁ__move_empty_cell_to_up____mutmut_2, 
        'xǁPuzzleGameǁ__move_empty_cell_to_up____mutmut_3': xǁPuzzleGameǁ__move_empty_cell_to_up____mutmut_3, 
        'xǁPuzzleGameǁ__move_empty_cell_to_up____mutmut_4': xǁPuzzleGameǁ__move_empty_cell_to_up____mutmut_4, 
        'xǁPuzzleGameǁ__move_empty_cell_to_up____mutmut_5': xǁPuzzleGameǁ__move_empty_cell_to_up____mutmut_5, 
        'xǁPuzzleGameǁ__move_empty_cell_to_up____mutmut_6': xǁPuzzleGameǁ__move_empty_cell_to_up____mutmut_6, 
        'xǁPuzzleGameǁ__move_empty_cell_to_up____mutmut_7': xǁPuzzleGameǁ__move_empty_cell_to_up____mutmut_7, 
        'xǁPuzzleGameǁ__move_empty_cell_to_up____mutmut_8': xǁPuzzleGameǁ__move_empty_cell_to_up____mutmut_8, 
        'xǁPuzzleGameǁ__move_empty_cell_to_up____mutmut_9': xǁPuzzleGameǁ__move_empty_cell_to_up____mutmut_9, 
        'xǁPuzzleGameǁ__move_empty_cell_to_up____mutmut_10': xǁPuzzleGameǁ__move_empty_cell_to_up____mutmut_10, 
        'xǁPuzzleGameǁ__move_empty_cell_to_up____mutmut_11': xǁPuzzleGameǁ__move_empty_cell_to_up____mutmut_11, 
        'xǁPuzzleGameǁ__move_empty_cell_to_up____mutmut_12': xǁPuzzleGameǁ__move_empty_cell_to_up____mutmut_12, 
        'xǁPuzzleGameǁ__move_empty_cell_to_up____mutmut_13': xǁPuzzleGameǁ__move_empty_cell_to_up____mutmut_13, 
        'xǁPuzzleGameǁ__move_empty_cell_to_up____mutmut_14': xǁPuzzleGameǁ__move_empty_cell_to_up____mutmut_14, 
        'xǁPuzzleGameǁ__move_empty_cell_to_up____mutmut_15': xǁPuzzleGameǁ__move_empty_cell_to_up____mutmut_15, 
        'xǁPuzzleGameǁ__move_empty_cell_to_up____mutmut_16': xǁPuzzleGameǁ__move_empty_cell_to_up____mutmut_16, 
        'xǁPuzzleGameǁ__move_empty_cell_to_up____mutmut_17': xǁPuzzleGameǁ__move_empty_cell_to_up____mutmut_17, 
        'xǁPuzzleGameǁ__move_empty_cell_to_up____mutmut_18': xǁPuzzleGameǁ__move_empty_cell_to_up____mutmut_18, 
        'xǁPuzzleGameǁ__move_empty_cell_to_up____mutmut_19': xǁPuzzleGameǁ__move_empty_cell_to_up____mutmut_19, 
        'xǁPuzzleGameǁ__move_empty_cell_to_up____mutmut_20': xǁPuzzleGameǁ__move_empty_cell_to_up____mutmut_20, 
        'xǁPuzzleGameǁ__move_empty_cell_to_up____mutmut_21': xǁPuzzleGameǁ__move_empty_cell_to_up____mutmut_21, 
        'xǁPuzzleGameǁ__move_empty_cell_to_up____mutmut_22': xǁPuzzleGameǁ__move_empty_cell_to_up____mutmut_22, 
        'xǁPuzzleGameǁ__move_empty_cell_to_up____mutmut_23': xǁPuzzleGameǁ__move_empty_cell_to_up____mutmut_23, 
        'xǁPuzzleGameǁ__move_empty_cell_to_up____mutmut_24': xǁPuzzleGameǁ__move_empty_cell_to_up____mutmut_24, 
        'xǁPuzzleGameǁ__move_empty_cell_to_up____mutmut_25': xǁPuzzleGameǁ__move_empty_cell_to_up____mutmut_25, 
        'xǁPuzzleGameǁ__move_empty_cell_to_up____mutmut_26': xǁPuzzleGameǁ__move_empty_cell_to_up____mutmut_26
    }
    
    def __move_empty_cell_to_up__(self, *args, **kwargs):
        result = _mutmut_trampoline(object.__getattribute__(self, "xǁPuzzleGameǁ__move_empty_cell_to_up____mutmut_orig"), object.__getattribute__(self, "xǁPuzzleGameǁ__move_empty_cell_to_up____mutmut_mutants"), args, kwargs, self)
        return result 
    
    __move_empty_cell_to_up__.__signature__ = _mutmut_signature(xǁPuzzleGameǁ__move_empty_cell_to_up____mutmut_orig)
    xǁPuzzleGameǁ__move_empty_cell_to_up____mutmut_orig.__name__ = 'xǁPuzzleGameǁ__move_empty_cell_to_up__'

    def xǁPuzzleGameǁ__move_empty_cell_to_right____mutmut_orig (self):
        if self.board.is_in_the_right_border(self.line_of_empty_position, self.column_of_empty_position):
            return False
        else:
            new_empty_line = self.line_of_empty_position
            new_empty_column = self.column_of_empty_position + 1
            tile = self.get_tile(new_empty_line, new_empty_column)
            self.board.change_tiles_in_positions(self.line_of_empty_position, self.column_of_empty_position, new_empty_line, new_empty_column)
            self.dic_positions_of_tiles.update({tile: (self.line_of_empty_position, self.column_of_empty_position)})
            self.line_of_empty_position = new_empty_line
            self.column_of_empty_position = new_empty_column
            return True

    def xǁPuzzleGameǁ__move_empty_cell_to_right____mutmut_1 (self):
        if self.board.is_in_the_right_border(None, self.column_of_empty_position):
            return False
        else:
            new_empty_line = self.line_of_empty_position
            new_empty_column = self.column_of_empty_position + 1
            tile = self.get_tile(new_empty_line, new_empty_column)
            self.board.change_tiles_in_positions(self.line_of_empty_position, self.column_of_empty_position, new_empty_line, new_empty_column)
            self.dic_positions_of_tiles.update({tile: (self.line_of_empty_position, self.column_of_empty_position)})
            self.line_of_empty_position = new_empty_line
            self.column_of_empty_position = new_empty_column
            return True

    def xǁPuzzleGameǁ__move_empty_cell_to_right____mutmut_2 (self):
        if self.board.is_in_the_right_border(self.line_of_empty_position, None):
            return False
        else:
            new_empty_line = self.line_of_empty_position
            new_empty_column = self.column_of_empty_position + 1
            tile = self.get_tile(new_empty_line, new_empty_column)
            self.board.change_tiles_in_positions(self.line_of_empty_position, self.column_of_empty_position, new_empty_line, new_empty_column)
            self.dic_positions_of_tiles.update({tile: (self.line_of_empty_position, self.column_of_empty_position)})
            self.line_of_empty_position = new_empty_line
            self.column_of_empty_position = new_empty_column
            return True

    def xǁPuzzleGameǁ__move_empty_cell_to_right____mutmut_3 (self):
        if self.board.is_in_the_right_border(self.column_of_empty_position):
            return False
        else:
            new_empty_line = self.line_of_empty_position
            new_empty_column = self.column_of_empty_position + 1
            tile = self.get_tile(new_empty_line, new_empty_column)
            self.board.change_tiles_in_positions(self.line_of_empty_position, self.column_of_empty_position, new_empty_line, new_empty_column)
            self.dic_positions_of_tiles.update({tile: (self.line_of_empty_position, self.column_of_empty_position)})
            self.line_of_empty_position = new_empty_line
            self.column_of_empty_position = new_empty_column
            return True

    def xǁPuzzleGameǁ__move_empty_cell_to_right____mutmut_4 (self):
        if self.board.is_in_the_right_border(self.line_of_empty_position, ):
            return False
        else:
            new_empty_line = self.line_of_empty_position
            new_empty_column = self.column_of_empty_position + 1
            tile = self.get_tile(new_empty_line, new_empty_column)
            self.board.change_tiles_in_positions(self.line_of_empty_position, self.column_of_empty_position, new_empty_line, new_empty_column)
            self.dic_positions_of_tiles.update({tile: (self.line_of_empty_position, self.column_of_empty_position)})
            self.line_of_empty_position = new_empty_line
            self.column_of_empty_position = new_empty_column
            return True

    def xǁPuzzleGameǁ__move_empty_cell_to_right____mutmut_5 (self):
        if self.board.is_in_the_right_border(self.line_of_empty_position, self.column_of_empty_position):
            return True
        else:
            new_empty_line = self.line_of_empty_position
            new_empty_column = self.column_of_empty_position + 1
            tile = self.get_tile(new_empty_line, new_empty_column)
            self.board.change_tiles_in_positions(self.line_of_empty_position, self.column_of_empty_position, new_empty_line, new_empty_column)
            self.dic_positions_of_tiles.update({tile: (self.line_of_empty_position, self.column_of_empty_position)})
            self.line_of_empty_position = new_empty_line
            self.column_of_empty_position = new_empty_column
            return True

    def xǁPuzzleGameǁ__move_empty_cell_to_right____mutmut_6 (self):
        if self.board.is_in_the_right_border(self.line_of_empty_position, self.column_of_empty_position):
            return False
        else:
            new_empty_line = None
            new_empty_column = self.column_of_empty_position + 1
            tile = self.get_tile(new_empty_line, new_empty_column)
            self.board.change_tiles_in_positions(self.line_of_empty_position, self.column_of_empty_position, new_empty_line, new_empty_column)
            self.dic_positions_of_tiles.update({tile: (self.line_of_empty_position, self.column_of_empty_position)})
            self.line_of_empty_position = new_empty_line
            self.column_of_empty_position = new_empty_column
            return True

    def xǁPuzzleGameǁ__move_empty_cell_to_right____mutmut_7 (self):
        if self.board.is_in_the_right_border(self.line_of_empty_position, self.column_of_empty_position):
            return False
        else:
            new_empty_line = self.line_of_empty_position
            new_empty_column = None
            tile = self.get_tile(new_empty_line, new_empty_column)
            self.board.change_tiles_in_positions(self.line_of_empty_position, self.column_of_empty_position, new_empty_line, new_empty_column)
            self.dic_positions_of_tiles.update({tile: (self.line_of_empty_position, self.column_of_empty_position)})
            self.line_of_empty_position = new_empty_line
            self.column_of_empty_position = new_empty_column
            return True

    def xǁPuzzleGameǁ__move_empty_cell_to_right____mutmut_8 (self):
        if self.board.is_in_the_right_border(self.line_of_empty_position, self.column_of_empty_position):
            return False
        else:
            new_empty_line = self.line_of_empty_position
            new_empty_column = self.column_of_empty_position - 1
            tile = self.get_tile(new_empty_line, new_empty_column)
            self.board.change_tiles_in_positions(self.line_of_empty_position, self.column_of_empty_position, new_empty_line, new_empty_column)
            self.dic_positions_of_tiles.update({tile: (self.line_of_empty_position, self.column_of_empty_position)})
            self.line_of_empty_position = new_empty_line
            self.column_of_empty_position = new_empty_column
            return True

    def xǁPuzzleGameǁ__move_empty_cell_to_right____mutmut_9 (self):
        if self.board.is_in_the_right_border(self.line_of_empty_position, self.column_of_empty_position):
            return False
        else:
            new_empty_line = self.line_of_empty_position
            new_empty_column = self.column_of_empty_position + 2
            tile = self.get_tile(new_empty_line, new_empty_column)
            self.board.change_tiles_in_positions(self.line_of_empty_position, self.column_of_empty_position, new_empty_line, new_empty_column)
            self.dic_positions_of_tiles.update({tile: (self.line_of_empty_position, self.column_of_empty_position)})
            self.line_of_empty_position = new_empty_line
            self.column_of_empty_position = new_empty_column
            return True

    def xǁPuzzleGameǁ__move_empty_cell_to_right____mutmut_10 (self):
        if self.board.is_in_the_right_border(self.line_of_empty_position, self.column_of_empty_position):
            return False
        else:
            new_empty_line = self.line_of_empty_position
            new_empty_column = self.column_of_empty_position + 1
            tile = None
            self.board.change_tiles_in_positions(self.line_of_empty_position, self.column_of_empty_position, new_empty_line, new_empty_column)
            self.dic_positions_of_tiles.update({tile: (self.line_of_empty_position, self.column_of_empty_position)})
            self.line_of_empty_position = new_empty_line
            self.column_of_empty_position = new_empty_column
            return True

    def xǁPuzzleGameǁ__move_empty_cell_to_right____mutmut_11 (self):
        if self.board.is_in_the_right_border(self.line_of_empty_position, self.column_of_empty_position):
            return False
        else:
            new_empty_line = self.line_of_empty_position
            new_empty_column = self.column_of_empty_position + 1
            tile = self.get_tile(None, new_empty_column)
            self.board.change_tiles_in_positions(self.line_of_empty_position, self.column_of_empty_position, new_empty_line, new_empty_column)
            self.dic_positions_of_tiles.update({tile: (self.line_of_empty_position, self.column_of_empty_position)})
            self.line_of_empty_position = new_empty_line
            self.column_of_empty_position = new_empty_column
            return True

    def xǁPuzzleGameǁ__move_empty_cell_to_right____mutmut_12 (self):
        if self.board.is_in_the_right_border(self.line_of_empty_position, self.column_of_empty_position):
            return False
        else:
            new_empty_line = self.line_of_empty_position
            new_empty_column = self.column_of_empty_position + 1
            tile = self.get_tile(new_empty_line, None)
            self.board.change_tiles_in_positions(self.line_of_empty_position, self.column_of_empty_position, new_empty_line, new_empty_column)
            self.dic_positions_of_tiles.update({tile: (self.line_of_empty_position, self.column_of_empty_position)})
            self.line_of_empty_position = new_empty_line
            self.column_of_empty_position = new_empty_column
            return True

    def xǁPuzzleGameǁ__move_empty_cell_to_right____mutmut_13 (self):
        if self.board.is_in_the_right_border(self.line_of_empty_position, self.column_of_empty_position):
            return False
        else:
            new_empty_line = self.line_of_empty_position
            new_empty_column = self.column_of_empty_position + 1
            tile = self.get_tile(new_empty_column)
            self.board.change_tiles_in_positions(self.line_of_empty_position, self.column_of_empty_position, new_empty_line, new_empty_column)
            self.dic_positions_of_tiles.update({tile: (self.line_of_empty_position, self.column_of_empty_position)})
            self.line_of_empty_position = new_empty_line
            self.column_of_empty_position = new_empty_column
            return True

    def xǁPuzzleGameǁ__move_empty_cell_to_right____mutmut_14 (self):
        if self.board.is_in_the_right_border(self.line_of_empty_position, self.column_of_empty_position):
            return False
        else:
            new_empty_line = self.line_of_empty_position
            new_empty_column = self.column_of_empty_position + 1
            tile = self.get_tile(new_empty_line, )
            self.board.change_tiles_in_positions(self.line_of_empty_position, self.column_of_empty_position, new_empty_line, new_empty_column)
            self.dic_positions_of_tiles.update({tile: (self.line_of_empty_position, self.column_of_empty_position)})
            self.line_of_empty_position = new_empty_line
            self.column_of_empty_position = new_empty_column
            return True

    def xǁPuzzleGameǁ__move_empty_cell_to_right____mutmut_15 (self):
        if self.board.is_in_the_right_border(self.line_of_empty_position, self.column_of_empty_position):
            return False
        else:
            new_empty_line = self.line_of_empty_position
            new_empty_column = self.column_of_empty_position + 1
            tile = self.get_tile(new_empty_line, new_empty_column)
            self.board.change_tiles_in_positions(None, self.column_of_empty_position, new_empty_line, new_empty_column)
            self.dic_positions_of_tiles.update({tile: (self.line_of_empty_position, self.column_of_empty_position)})
            self.line_of_empty_position = new_empty_line
            self.column_of_empty_position = new_empty_column
            return True

    def xǁPuzzleGameǁ__move_empty_cell_to_right____mutmut_16 (self):
        if self.board.is_in_the_right_border(self.line_of_empty_position, self.column_of_empty_position):
            return False
        else:
            new_empty_line = self.line_of_empty_position
            new_empty_column = self.column_of_empty_position + 1
            tile = self.get_tile(new_empty_line, new_empty_column)
            self.board.change_tiles_in_positions(self.line_of_empty_position, None, new_empty_line, new_empty_column)
            self.dic_positions_of_tiles.update({tile: (self.line_of_empty_position, self.column_of_empty_position)})
            self.line_of_empty_position = new_empty_line
            self.column_of_empty_position = new_empty_column
            return True

    def xǁPuzzleGameǁ__move_empty_cell_to_right____mutmut_17 (self):
        if self.board.is_in_the_right_border(self.line_of_empty_position, self.column_of_empty_position):
            return False
        else:
            new_empty_line = self.line_of_empty_position
            new_empty_column = self.column_of_empty_position + 1
            tile = self.get_tile(new_empty_line, new_empty_column)
            self.board.change_tiles_in_positions(self.line_of_empty_position, self.column_of_empty_position, None, new_empty_column)
            self.dic_positions_of_tiles.update({tile: (self.line_of_empty_position, self.column_of_empty_position)})
            self.line_of_empty_position = new_empty_line
            self.column_of_empty_position = new_empty_column
            return True

    def xǁPuzzleGameǁ__move_empty_cell_to_right____mutmut_18 (self):
        if self.board.is_in_the_right_border(self.line_of_empty_position, self.column_of_empty_position):
            return False
        else:
            new_empty_line = self.line_of_empty_position
            new_empty_column = self.column_of_empty_position + 1
            tile = self.get_tile(new_empty_line, new_empty_column)
            self.board.change_tiles_in_positions(self.line_of_empty_position, self.column_of_empty_position, new_empty_line, None)
            self.dic_positions_of_tiles.update({tile: (self.line_of_empty_position, self.column_of_empty_position)})
            self.line_of_empty_position = new_empty_line
            self.column_of_empty_position = new_empty_column
            return True

    def xǁPuzzleGameǁ__move_empty_cell_to_right____mutmut_19 (self):
        if self.board.is_in_the_right_border(self.line_of_empty_position, self.column_of_empty_position):
            return False
        else:
            new_empty_line = self.line_of_empty_position
            new_empty_column = self.column_of_empty_position + 1
            tile = self.get_tile(new_empty_line, new_empty_column)
            self.board.change_tiles_in_positions(self.column_of_empty_position, new_empty_line, new_empty_column)
            self.dic_positions_of_tiles.update({tile: (self.line_of_empty_position, self.column_of_empty_position)})
            self.line_of_empty_position = new_empty_line
            self.column_of_empty_position = new_empty_column
            return True

    def xǁPuzzleGameǁ__move_empty_cell_to_right____mutmut_20 (self):
        if self.board.is_in_the_right_border(self.line_of_empty_position, self.column_of_empty_position):
            return False
        else:
            new_empty_line = self.line_of_empty_position
            new_empty_column = self.column_of_empty_position + 1
            tile = self.get_tile(new_empty_line, new_empty_column)
            self.board.change_tiles_in_positions(self.line_of_empty_position, new_empty_line, new_empty_column)
            self.dic_positions_of_tiles.update({tile: (self.line_of_empty_position, self.column_of_empty_position)})
            self.line_of_empty_position = new_empty_line
            self.column_of_empty_position = new_empty_column
            return True

    def xǁPuzzleGameǁ__move_empty_cell_to_right____mutmut_21 (self):
        if self.board.is_in_the_right_border(self.line_of_empty_position, self.column_of_empty_position):
            return False
        else:
            new_empty_line = self.line_of_empty_position
            new_empty_column = self.column_of_empty_position + 1
            tile = self.get_tile(new_empty_line, new_empty_column)
            self.board.change_tiles_in_positions(self.line_of_empty_position, self.column_of_empty_position, new_empty_column)
            self.dic_positions_of_tiles.update({tile: (self.line_of_empty_position, self.column_of_empty_position)})
            self.line_of_empty_position = new_empty_line
            self.column_of_empty_position = new_empty_column
            return True

    def xǁPuzzleGameǁ__move_empty_cell_to_right____mutmut_22 (self):
        if self.board.is_in_the_right_border(self.line_of_empty_position, self.column_of_empty_position):
            return False
        else:
            new_empty_line = self.line_of_empty_position
            new_empty_column = self.column_of_empty_position + 1
            tile = self.get_tile(new_empty_line, new_empty_column)
            self.board.change_tiles_in_positions(self.line_of_empty_position, self.column_of_empty_position, new_empty_line, )
            self.dic_positions_of_tiles.update({tile: (self.line_of_empty_position, self.column_of_empty_position)})
            self.line_of_empty_position = new_empty_line
            self.column_of_empty_position = new_empty_column
            return True

    def xǁPuzzleGameǁ__move_empty_cell_to_right____mutmut_23 (self):
        if self.board.is_in_the_right_border(self.line_of_empty_position, self.column_of_empty_position):
            return False
        else:
            new_empty_line = self.line_of_empty_position
            new_empty_column = self.column_of_empty_position + 1
            tile = self.get_tile(new_empty_line, new_empty_column)
            self.board.change_tiles_in_positions(self.line_of_empty_position, self.column_of_empty_position, new_empty_line, new_empty_column)
            self.dic_positions_of_tiles.update(None)
            self.line_of_empty_position = new_empty_line
            self.column_of_empty_position = new_empty_column
            return True

    def xǁPuzzleGameǁ__move_empty_cell_to_right____mutmut_24 (self):
        if self.board.is_in_the_right_border(self.line_of_empty_position, self.column_of_empty_position):
            return False
        else:
            new_empty_line = self.line_of_empty_position
            new_empty_column = self.column_of_empty_position + 1
            tile = self.get_tile(new_empty_line, new_empty_column)
            self.board.change_tiles_in_positions(self.line_of_empty_position, self.column_of_empty_position, new_empty_line, new_empty_column)
            self.dic_positions_of_tiles.update({tile: (self.line_of_empty_position, self.column_of_empty_position)})
            self.line_of_empty_position = None
            self.column_of_empty_position = new_empty_column
            return True

    def xǁPuzzleGameǁ__move_empty_cell_to_right____mutmut_25 (self):
        if self.board.is_in_the_right_border(self.line_of_empty_position, self.column_of_empty_position):
            return False
        else:
            new_empty_line = self.line_of_empty_position
            new_empty_column = self.column_of_empty_position + 1
            tile = self.get_tile(new_empty_line, new_empty_column)
            self.board.change_tiles_in_positions(self.line_of_empty_position, self.column_of_empty_position, new_empty_line, new_empty_column)
            self.dic_positions_of_tiles.update({tile: (self.line_of_empty_position, self.column_of_empty_position)})
            self.line_of_empty_position = new_empty_line
            self.column_of_empty_position = None
            return True

    def xǁPuzzleGameǁ__move_empty_cell_to_right____mutmut_26 (self):
        if self.board.is_in_the_right_border(self.line_of_empty_position, self.column_of_empty_position):
            return False
        else:
            new_empty_line = self.line_of_empty_position
            new_empty_column = self.column_of_empty_position + 1
            tile = self.get_tile(new_empty_line, new_empty_column)
            self.board.change_tiles_in_positions(self.line_of_empty_position, self.column_of_empty_position, new_empty_line, new_empty_column)
            self.dic_positions_of_tiles.update({tile: (self.line_of_empty_position, self.column_of_empty_position)})
            self.line_of_empty_position = new_empty_line
            self.column_of_empty_position = new_empty_column
            return False
    
    xǁPuzzleGameǁ__move_empty_cell_to_right____mutmut_mutants : ClassVar[MutantDict] = {
    'xǁPuzzleGameǁ__move_empty_cell_to_right____mutmut_1': xǁPuzzleGameǁ__move_empty_cell_to_right____mutmut_1, 
        'xǁPuzzleGameǁ__move_empty_cell_to_right____mutmut_2': xǁPuzzleGameǁ__move_empty_cell_to_right____mutmut_2, 
        'xǁPuzzleGameǁ__move_empty_cell_to_right____mutmut_3': xǁPuzzleGameǁ__move_empty_cell_to_right____mutmut_3, 
        'xǁPuzzleGameǁ__move_empty_cell_to_right____mutmut_4': xǁPuzzleGameǁ__move_empty_cell_to_right____mutmut_4, 
        'xǁPuzzleGameǁ__move_empty_cell_to_right____mutmut_5': xǁPuzzleGameǁ__move_empty_cell_to_right____mutmut_5, 
        'xǁPuzzleGameǁ__move_empty_cell_to_right____mutmut_6': xǁPuzzleGameǁ__move_empty_cell_to_right____mutmut_6, 
        'xǁPuzzleGameǁ__move_empty_cell_to_right____mutmut_7': xǁPuzzleGameǁ__move_empty_cell_to_right____mutmut_7, 
        'xǁPuzzleGameǁ__move_empty_cell_to_right____mutmut_8': xǁPuzzleGameǁ__move_empty_cell_to_right____mutmut_8, 
        'xǁPuzzleGameǁ__move_empty_cell_to_right____mutmut_9': xǁPuzzleGameǁ__move_empty_cell_to_right____mutmut_9, 
        'xǁPuzzleGameǁ__move_empty_cell_to_right____mutmut_10': xǁPuzzleGameǁ__move_empty_cell_to_right____mutmut_10, 
        'xǁPuzzleGameǁ__move_empty_cell_to_right____mutmut_11': xǁPuzzleGameǁ__move_empty_cell_to_right____mutmut_11, 
        'xǁPuzzleGameǁ__move_empty_cell_to_right____mutmut_12': xǁPuzzleGameǁ__move_empty_cell_to_right____mutmut_12, 
        'xǁPuzzleGameǁ__move_empty_cell_to_right____mutmut_13': xǁPuzzleGameǁ__move_empty_cell_to_right____mutmut_13, 
        'xǁPuzzleGameǁ__move_empty_cell_to_right____mutmut_14': xǁPuzzleGameǁ__move_empty_cell_to_right____mutmut_14, 
        'xǁPuzzleGameǁ__move_empty_cell_to_right____mutmut_15': xǁPuzzleGameǁ__move_empty_cell_to_right____mutmut_15, 
        'xǁPuzzleGameǁ__move_empty_cell_to_right____mutmut_16': xǁPuzzleGameǁ__move_empty_cell_to_right____mutmut_16, 
        'xǁPuzzleGameǁ__move_empty_cell_to_right____mutmut_17': xǁPuzzleGameǁ__move_empty_cell_to_right____mutmut_17, 
        'xǁPuzzleGameǁ__move_empty_cell_to_right____mutmut_18': xǁPuzzleGameǁ__move_empty_cell_to_right____mutmut_18, 
        'xǁPuzzleGameǁ__move_empty_cell_to_right____mutmut_19': xǁPuzzleGameǁ__move_empty_cell_to_right____mutmut_19, 
        'xǁPuzzleGameǁ__move_empty_cell_to_right____mutmut_20': xǁPuzzleGameǁ__move_empty_cell_to_right____mutmut_20, 
        'xǁPuzzleGameǁ__move_empty_cell_to_right____mutmut_21': xǁPuzzleGameǁ__move_empty_cell_to_right____mutmut_21, 
        'xǁPuzzleGameǁ__move_empty_cell_to_right____mutmut_22': xǁPuzzleGameǁ__move_empty_cell_to_right____mutmut_22, 
        'xǁPuzzleGameǁ__move_empty_cell_to_right____mutmut_23': xǁPuzzleGameǁ__move_empty_cell_to_right____mutmut_23, 
        'xǁPuzzleGameǁ__move_empty_cell_to_right____mutmut_24': xǁPuzzleGameǁ__move_empty_cell_to_right____mutmut_24, 
        'xǁPuzzleGameǁ__move_empty_cell_to_right____mutmut_25': xǁPuzzleGameǁ__move_empty_cell_to_right____mutmut_25, 
        'xǁPuzzleGameǁ__move_empty_cell_to_right____mutmut_26': xǁPuzzleGameǁ__move_empty_cell_to_right____mutmut_26
    }
    
    def __move_empty_cell_to_right__(self, *args, **kwargs):
        result = _mutmut_trampoline(object.__getattribute__(self, "xǁPuzzleGameǁ__move_empty_cell_to_right____mutmut_orig"), object.__getattribute__(self, "xǁPuzzleGameǁ__move_empty_cell_to_right____mutmut_mutants"), args, kwargs, self)
        return result 
    
    __move_empty_cell_to_right__.__signature__ = _mutmut_signature(xǁPuzzleGameǁ__move_empty_cell_to_right____mutmut_orig)
    xǁPuzzleGameǁ__move_empty_cell_to_right____mutmut_orig.__name__ = 'xǁPuzzleGameǁ__move_empty_cell_to_right__'

    def xǁPuzzleGameǁ__move_empty_cell_to_left____mutmut_orig (self):
        if self.board.is_in_the_left_border(self.line_of_empty_position, self.column_of_empty_position):
            return False
        else:
            new_empty_line = self.line_of_empty_position
            new_empty_column = self.column_of_empty_position - 1
            tile = self.get_tile(new_empty_line, new_empty_column)
            self.board.change_tiles_in_positions(self.line_of_empty_position, self.column_of_empty_position, new_empty_line, new_empty_column)
            self.dic_positions_of_tiles.update({tile: (self.line_of_empty_position, self.column_of_empty_position)})
            self.line_of_empty_position = new_empty_line
            self.column_of_empty_position = new_empty_column
            return True

    def xǁPuzzleGameǁ__move_empty_cell_to_left____mutmut_1 (self):
        if self.board.is_in_the_left_border(None, self.column_of_empty_position):
            return False
        else:
            new_empty_line = self.line_of_empty_position
            new_empty_column = self.column_of_empty_position - 1
            tile = self.get_tile(new_empty_line, new_empty_column)
            self.board.change_tiles_in_positions(self.line_of_empty_position, self.column_of_empty_position, new_empty_line, new_empty_column)
            self.dic_positions_of_tiles.update({tile: (self.line_of_empty_position, self.column_of_empty_position)})
            self.line_of_empty_position = new_empty_line
            self.column_of_empty_position = new_empty_column
            return True

    def xǁPuzzleGameǁ__move_empty_cell_to_left____mutmut_2 (self):
        if self.board.is_in_the_left_border(self.line_of_empty_position, None):
            return False
        else:
            new_empty_line = self.line_of_empty_position
            new_empty_column = self.column_of_empty_position - 1
            tile = self.get_tile(new_empty_line, new_empty_column)
            self.board.change_tiles_in_positions(self.line_of_empty_position, self.column_of_empty_position, new_empty_line, new_empty_column)
            self.dic_positions_of_tiles.update({tile: (self.line_of_empty_position, self.column_of_empty_position)})
            self.line_of_empty_position = new_empty_line
            self.column_of_empty_position = new_empty_column
            return True

    def xǁPuzzleGameǁ__move_empty_cell_to_left____mutmut_3 (self):
        if self.board.is_in_the_left_border(self.column_of_empty_position):
            return False
        else:
            new_empty_line = self.line_of_empty_position
            new_empty_column = self.column_of_empty_position - 1
            tile = self.get_tile(new_empty_line, new_empty_column)
            self.board.change_tiles_in_positions(self.line_of_empty_position, self.column_of_empty_position, new_empty_line, new_empty_column)
            self.dic_positions_of_tiles.update({tile: (self.line_of_empty_position, self.column_of_empty_position)})
            self.line_of_empty_position = new_empty_line
            self.column_of_empty_position = new_empty_column
            return True

    def xǁPuzzleGameǁ__move_empty_cell_to_left____mutmut_4 (self):
        if self.board.is_in_the_left_border(self.line_of_empty_position, ):
            return False
        else:
            new_empty_line = self.line_of_empty_position
            new_empty_column = self.column_of_empty_position - 1
            tile = self.get_tile(new_empty_line, new_empty_column)
            self.board.change_tiles_in_positions(self.line_of_empty_position, self.column_of_empty_position, new_empty_line, new_empty_column)
            self.dic_positions_of_tiles.update({tile: (self.line_of_empty_position, self.column_of_empty_position)})
            self.line_of_empty_position = new_empty_line
            self.column_of_empty_position = new_empty_column
            return True

    def xǁPuzzleGameǁ__move_empty_cell_to_left____mutmut_5 (self):
        if self.board.is_in_the_left_border(self.line_of_empty_position, self.column_of_empty_position):
            return True
        else:
            new_empty_line = self.line_of_empty_position
            new_empty_column = self.column_of_empty_position - 1
            tile = self.get_tile(new_empty_line, new_empty_column)
            self.board.change_tiles_in_positions(self.line_of_empty_position, self.column_of_empty_position, new_empty_line, new_empty_column)
            self.dic_positions_of_tiles.update({tile: (self.line_of_empty_position, self.column_of_empty_position)})
            self.line_of_empty_position = new_empty_line
            self.column_of_empty_position = new_empty_column
            return True

    def xǁPuzzleGameǁ__move_empty_cell_to_left____mutmut_6 (self):
        if self.board.is_in_the_left_border(self.line_of_empty_position, self.column_of_empty_position):
            return False
        else:
            new_empty_line = None
            new_empty_column = self.column_of_empty_position - 1
            tile = self.get_tile(new_empty_line, new_empty_column)
            self.board.change_tiles_in_positions(self.line_of_empty_position, self.column_of_empty_position, new_empty_line, new_empty_column)
            self.dic_positions_of_tiles.update({tile: (self.line_of_empty_position, self.column_of_empty_position)})
            self.line_of_empty_position = new_empty_line
            self.column_of_empty_position = new_empty_column
            return True

    def xǁPuzzleGameǁ__move_empty_cell_to_left____mutmut_7 (self):
        if self.board.is_in_the_left_border(self.line_of_empty_position, self.column_of_empty_position):
            return False
        else:
            new_empty_line = self.line_of_empty_position
            new_empty_column = None
            tile = self.get_tile(new_empty_line, new_empty_column)
            self.board.change_tiles_in_positions(self.line_of_empty_position, self.column_of_empty_position, new_empty_line, new_empty_column)
            self.dic_positions_of_tiles.update({tile: (self.line_of_empty_position, self.column_of_empty_position)})
            self.line_of_empty_position = new_empty_line
            self.column_of_empty_position = new_empty_column
            return True

    def xǁPuzzleGameǁ__move_empty_cell_to_left____mutmut_8 (self):
        if self.board.is_in_the_left_border(self.line_of_empty_position, self.column_of_empty_position):
            return False
        else:
            new_empty_line = self.line_of_empty_position
            new_empty_column = self.column_of_empty_position + 1
            tile = self.get_tile(new_empty_line, new_empty_column)
            self.board.change_tiles_in_positions(self.line_of_empty_position, self.column_of_empty_position, new_empty_line, new_empty_column)
            self.dic_positions_of_tiles.update({tile: (self.line_of_empty_position, self.column_of_empty_position)})
            self.line_of_empty_position = new_empty_line
            self.column_of_empty_position = new_empty_column
            return True

    def xǁPuzzleGameǁ__move_empty_cell_to_left____mutmut_9 (self):
        if self.board.is_in_the_left_border(self.line_of_empty_position, self.column_of_empty_position):
            return False
        else:
            new_empty_line = self.line_of_empty_position
            new_empty_column = self.column_of_empty_position - 2
            tile = self.get_tile(new_empty_line, new_empty_column)
            self.board.change_tiles_in_positions(self.line_of_empty_position, self.column_of_empty_position, new_empty_line, new_empty_column)
            self.dic_positions_of_tiles.update({tile: (self.line_of_empty_position, self.column_of_empty_position)})
            self.line_of_empty_position = new_empty_line
            self.column_of_empty_position = new_empty_column
            return True

    def xǁPuzzleGameǁ__move_empty_cell_to_left____mutmut_10 (self):
        if self.board.is_in_the_left_border(self.line_of_empty_position, self.column_of_empty_position):
            return False
        else:
            new_empty_line = self.line_of_empty_position
            new_empty_column = self.column_of_empty_position - 1
            tile = None
            self.board.change_tiles_in_positions(self.line_of_empty_position, self.column_of_empty_position, new_empty_line, new_empty_column)
            self.dic_positions_of_tiles.update({tile: (self.line_of_empty_position, self.column_of_empty_position)})
            self.line_of_empty_position = new_empty_line
            self.column_of_empty_position = new_empty_column
            return True

    def xǁPuzzleGameǁ__move_empty_cell_to_left____mutmut_11 (self):
        if self.board.is_in_the_left_border(self.line_of_empty_position, self.column_of_empty_position):
            return False
        else:
            new_empty_line = self.line_of_empty_position
            new_empty_column = self.column_of_empty_position - 1
            tile = self.get_tile(None, new_empty_column)
            self.board.change_tiles_in_positions(self.line_of_empty_position, self.column_of_empty_position, new_empty_line, new_empty_column)
            self.dic_positions_of_tiles.update({tile: (self.line_of_empty_position, self.column_of_empty_position)})
            self.line_of_empty_position = new_empty_line
            self.column_of_empty_position = new_empty_column
            return True

    def xǁPuzzleGameǁ__move_empty_cell_to_left____mutmut_12 (self):
        if self.board.is_in_the_left_border(self.line_of_empty_position, self.column_of_empty_position):
            return False
        else:
            new_empty_line = self.line_of_empty_position
            new_empty_column = self.column_of_empty_position - 1
            tile = self.get_tile(new_empty_line, None)
            self.board.change_tiles_in_positions(self.line_of_empty_position, self.column_of_empty_position, new_empty_line, new_empty_column)
            self.dic_positions_of_tiles.update({tile: (self.line_of_empty_position, self.column_of_empty_position)})
            self.line_of_empty_position = new_empty_line
            self.column_of_empty_position = new_empty_column
            return True

    def xǁPuzzleGameǁ__move_empty_cell_to_left____mutmut_13 (self):
        if self.board.is_in_the_left_border(self.line_of_empty_position, self.column_of_empty_position):
            return False
        else:
            new_empty_line = self.line_of_empty_position
            new_empty_column = self.column_of_empty_position - 1
            tile = self.get_tile(new_empty_column)
            self.board.change_tiles_in_positions(self.line_of_empty_position, self.column_of_empty_position, new_empty_line, new_empty_column)
            self.dic_positions_of_tiles.update({tile: (self.line_of_empty_position, self.column_of_empty_position)})
            self.line_of_empty_position = new_empty_line
            self.column_of_empty_position = new_empty_column
            return True

    def xǁPuzzleGameǁ__move_empty_cell_to_left____mutmut_14 (self):
        if self.board.is_in_the_left_border(self.line_of_empty_position, self.column_of_empty_position):
            return False
        else:
            new_empty_line = self.line_of_empty_position
            new_empty_column = self.column_of_empty_position - 1
            tile = self.get_tile(new_empty_line, )
            self.board.change_tiles_in_positions(self.line_of_empty_position, self.column_of_empty_position, new_empty_line, new_empty_column)
            self.dic_positions_of_tiles.update({tile: (self.line_of_empty_position, self.column_of_empty_position)})
            self.line_of_empty_position = new_empty_line
            self.column_of_empty_position = new_empty_column
            return True

    def xǁPuzzleGameǁ__move_empty_cell_to_left____mutmut_15 (self):
        if self.board.is_in_the_left_border(self.line_of_empty_position, self.column_of_empty_position):
            return False
        else:
            new_empty_line = self.line_of_empty_position
            new_empty_column = self.column_of_empty_position - 1
            tile = self.get_tile(new_empty_line, new_empty_column)
            self.board.change_tiles_in_positions(None, self.column_of_empty_position, new_empty_line, new_empty_column)
            self.dic_positions_of_tiles.update({tile: (self.line_of_empty_position, self.column_of_empty_position)})
            self.line_of_empty_position = new_empty_line
            self.column_of_empty_position = new_empty_column
            return True

    def xǁPuzzleGameǁ__move_empty_cell_to_left____mutmut_16 (self):
        if self.board.is_in_the_left_border(self.line_of_empty_position, self.column_of_empty_position):
            return False
        else:
            new_empty_line = self.line_of_empty_position
            new_empty_column = self.column_of_empty_position - 1
            tile = self.get_tile(new_empty_line, new_empty_column)
            self.board.change_tiles_in_positions(self.line_of_empty_position, None, new_empty_line, new_empty_column)
            self.dic_positions_of_tiles.update({tile: (self.line_of_empty_position, self.column_of_empty_position)})
            self.line_of_empty_position = new_empty_line
            self.column_of_empty_position = new_empty_column
            return True

    def xǁPuzzleGameǁ__move_empty_cell_to_left____mutmut_17 (self):
        if self.board.is_in_the_left_border(self.line_of_empty_position, self.column_of_empty_position):
            return False
        else:
            new_empty_line = self.line_of_empty_position
            new_empty_column = self.column_of_empty_position - 1
            tile = self.get_tile(new_empty_line, new_empty_column)
            self.board.change_tiles_in_positions(self.line_of_empty_position, self.column_of_empty_position, None, new_empty_column)
            self.dic_positions_of_tiles.update({tile: (self.line_of_empty_position, self.column_of_empty_position)})
            self.line_of_empty_position = new_empty_line
            self.column_of_empty_position = new_empty_column
            return True

    def xǁPuzzleGameǁ__move_empty_cell_to_left____mutmut_18 (self):
        if self.board.is_in_the_left_border(self.line_of_empty_position, self.column_of_empty_position):
            return False
        else:
            new_empty_line = self.line_of_empty_position
            new_empty_column = self.column_of_empty_position - 1
            tile = self.get_tile(new_empty_line, new_empty_column)
            self.board.change_tiles_in_positions(self.line_of_empty_position, self.column_of_empty_position, new_empty_line, None)
            self.dic_positions_of_tiles.update({tile: (self.line_of_empty_position, self.column_of_empty_position)})
            self.line_of_empty_position = new_empty_line
            self.column_of_empty_position = new_empty_column
            return True

    def xǁPuzzleGameǁ__move_empty_cell_to_left____mutmut_19 (self):
        if self.board.is_in_the_left_border(self.line_of_empty_position, self.column_of_empty_position):
            return False
        else:
            new_empty_line = self.line_of_empty_position
            new_empty_column = self.column_of_empty_position - 1
            tile = self.get_tile(new_empty_line, new_empty_column)
            self.board.change_tiles_in_positions(self.column_of_empty_position, new_empty_line, new_empty_column)
            self.dic_positions_of_tiles.update({tile: (self.line_of_empty_position, self.column_of_empty_position)})
            self.line_of_empty_position = new_empty_line
            self.column_of_empty_position = new_empty_column
            return True

    def xǁPuzzleGameǁ__move_empty_cell_to_left____mutmut_20 (self):
        if self.board.is_in_the_left_border(self.line_of_empty_position, self.column_of_empty_position):
            return False
        else:
            new_empty_line = self.line_of_empty_position
            new_empty_column = self.column_of_empty_position - 1
            tile = self.get_tile(new_empty_line, new_empty_column)
            self.board.change_tiles_in_positions(self.line_of_empty_position, new_empty_line, new_empty_column)
            self.dic_positions_of_tiles.update({tile: (self.line_of_empty_position, self.column_of_empty_position)})
            self.line_of_empty_position = new_empty_line
            self.column_of_empty_position = new_empty_column
            return True

    def xǁPuzzleGameǁ__move_empty_cell_to_left____mutmut_21 (self):
        if self.board.is_in_the_left_border(self.line_of_empty_position, self.column_of_empty_position):
            return False
        else:
            new_empty_line = self.line_of_empty_position
            new_empty_column = self.column_of_empty_position - 1
            tile = self.get_tile(new_empty_line, new_empty_column)
            self.board.change_tiles_in_positions(self.line_of_empty_position, self.column_of_empty_position, new_empty_column)
            self.dic_positions_of_tiles.update({tile: (self.line_of_empty_position, self.column_of_empty_position)})
            self.line_of_empty_position = new_empty_line
            self.column_of_empty_position = new_empty_column
            return True

    def xǁPuzzleGameǁ__move_empty_cell_to_left____mutmut_22 (self):
        if self.board.is_in_the_left_border(self.line_of_empty_position, self.column_of_empty_position):
            return False
        else:
            new_empty_line = self.line_of_empty_position
            new_empty_column = self.column_of_empty_position - 1
            tile = self.get_tile(new_empty_line, new_empty_column)
            self.board.change_tiles_in_positions(self.line_of_empty_position, self.column_of_empty_position, new_empty_line, )
            self.dic_positions_of_tiles.update({tile: (self.line_of_empty_position, self.column_of_empty_position)})
            self.line_of_empty_position = new_empty_line
            self.column_of_empty_position = new_empty_column
            return True

    def xǁPuzzleGameǁ__move_empty_cell_to_left____mutmut_23 (self):
        if self.board.is_in_the_left_border(self.line_of_empty_position, self.column_of_empty_position):
            return False
        else:
            new_empty_line = self.line_of_empty_position
            new_empty_column = self.column_of_empty_position - 1
            tile = self.get_tile(new_empty_line, new_empty_column)
            self.board.change_tiles_in_positions(self.line_of_empty_position, self.column_of_empty_position, new_empty_line, new_empty_column)
            self.dic_positions_of_tiles.update(None)
            self.line_of_empty_position = new_empty_line
            self.column_of_empty_position = new_empty_column
            return True

    def xǁPuzzleGameǁ__move_empty_cell_to_left____mutmut_24 (self):
        if self.board.is_in_the_left_border(self.line_of_empty_position, self.column_of_empty_position):
            return False
        else:
            new_empty_line = self.line_of_empty_position
            new_empty_column = self.column_of_empty_position - 1
            tile = self.get_tile(new_empty_line, new_empty_column)
            self.board.change_tiles_in_positions(self.line_of_empty_position, self.column_of_empty_position, new_empty_line, new_empty_column)
            self.dic_positions_of_tiles.update({tile: (self.line_of_empty_position, self.column_of_empty_position)})
            self.line_of_empty_position = None
            self.column_of_empty_position = new_empty_column
            return True

    def xǁPuzzleGameǁ__move_empty_cell_to_left____mutmut_25 (self):
        if self.board.is_in_the_left_border(self.line_of_empty_position, self.column_of_empty_position):
            return False
        else:
            new_empty_line = self.line_of_empty_position
            new_empty_column = self.column_of_empty_position - 1
            tile = self.get_tile(new_empty_line, new_empty_column)
            self.board.change_tiles_in_positions(self.line_of_empty_position, self.column_of_empty_position, new_empty_line, new_empty_column)
            self.dic_positions_of_tiles.update({tile: (self.line_of_empty_position, self.column_of_empty_position)})
            self.line_of_empty_position = new_empty_line
            self.column_of_empty_position = None
            return True

    def xǁPuzzleGameǁ__move_empty_cell_to_left____mutmut_26 (self):
        if self.board.is_in_the_left_border(self.line_of_empty_position, self.column_of_empty_position):
            return False
        else:
            new_empty_line = self.line_of_empty_position
            new_empty_column = self.column_of_empty_position - 1
            tile = self.get_tile(new_empty_line, new_empty_column)
            self.board.change_tiles_in_positions(self.line_of_empty_position, self.column_of_empty_position, new_empty_line, new_empty_column)
            self.dic_positions_of_tiles.update({tile: (self.line_of_empty_position, self.column_of_empty_position)})
            self.line_of_empty_position = new_empty_line
            self.column_of_empty_position = new_empty_column
            return False
    
    xǁPuzzleGameǁ__move_empty_cell_to_left____mutmut_mutants : ClassVar[MutantDict] = {
    'xǁPuzzleGameǁ__move_empty_cell_to_left____mutmut_1': xǁPuzzleGameǁ__move_empty_cell_to_left____mutmut_1, 
        'xǁPuzzleGameǁ__move_empty_cell_to_left____mutmut_2': xǁPuzzleGameǁ__move_empty_cell_to_left____mutmut_2, 
        'xǁPuzzleGameǁ__move_empty_cell_to_left____mutmut_3': xǁPuzzleGameǁ__move_empty_cell_to_left____mutmut_3, 
        'xǁPuzzleGameǁ__move_empty_cell_to_left____mutmut_4': xǁPuzzleGameǁ__move_empty_cell_to_left____mutmut_4, 
        'xǁPuzzleGameǁ__move_empty_cell_to_left____mutmut_5': xǁPuzzleGameǁ__move_empty_cell_to_left____mutmut_5, 
        'xǁPuzzleGameǁ__move_empty_cell_to_left____mutmut_6': xǁPuzzleGameǁ__move_empty_cell_to_left____mutmut_6, 
        'xǁPuzzleGameǁ__move_empty_cell_to_left____mutmut_7': xǁPuzzleGameǁ__move_empty_cell_to_left____mutmut_7, 
        'xǁPuzzleGameǁ__move_empty_cell_to_left____mutmut_8': xǁPuzzleGameǁ__move_empty_cell_to_left____mutmut_8, 
        'xǁPuzzleGameǁ__move_empty_cell_to_left____mutmut_9': xǁPuzzleGameǁ__move_empty_cell_to_left____mutmut_9, 
        'xǁPuzzleGameǁ__move_empty_cell_to_left____mutmut_10': xǁPuzzleGameǁ__move_empty_cell_to_left____mutmut_10, 
        'xǁPuzzleGameǁ__move_empty_cell_to_left____mutmut_11': xǁPuzzleGameǁ__move_empty_cell_to_left____mutmut_11, 
        'xǁPuzzleGameǁ__move_empty_cell_to_left____mutmut_12': xǁPuzzleGameǁ__move_empty_cell_to_left____mutmut_12, 
        'xǁPuzzleGameǁ__move_empty_cell_to_left____mutmut_13': xǁPuzzleGameǁ__move_empty_cell_to_left____mutmut_13, 
        'xǁPuzzleGameǁ__move_empty_cell_to_left____mutmut_14': xǁPuzzleGameǁ__move_empty_cell_to_left____mutmut_14, 
        'xǁPuzzleGameǁ__move_empty_cell_to_left____mutmut_15': xǁPuzzleGameǁ__move_empty_cell_to_left____mutmut_15, 
        'xǁPuzzleGameǁ__move_empty_cell_to_left____mutmut_16': xǁPuzzleGameǁ__move_empty_cell_to_left____mutmut_16, 
        'xǁPuzzleGameǁ__move_empty_cell_to_left____mutmut_17': xǁPuzzleGameǁ__move_empty_cell_to_left____mutmut_17, 
        'xǁPuzzleGameǁ__move_empty_cell_to_left____mutmut_18': xǁPuzzleGameǁ__move_empty_cell_to_left____mutmut_18, 
        'xǁPuzzleGameǁ__move_empty_cell_to_left____mutmut_19': xǁPuzzleGameǁ__move_empty_cell_to_left____mutmut_19, 
        'xǁPuzzleGameǁ__move_empty_cell_to_left____mutmut_20': xǁPuzzleGameǁ__move_empty_cell_to_left____mutmut_20, 
        'xǁPuzzleGameǁ__move_empty_cell_to_left____mutmut_21': xǁPuzzleGameǁ__move_empty_cell_to_left____mutmut_21, 
        'xǁPuzzleGameǁ__move_empty_cell_to_left____mutmut_22': xǁPuzzleGameǁ__move_empty_cell_to_left____mutmut_22, 
        'xǁPuzzleGameǁ__move_empty_cell_to_left____mutmut_23': xǁPuzzleGameǁ__move_empty_cell_to_left____mutmut_23, 
        'xǁPuzzleGameǁ__move_empty_cell_to_left____mutmut_24': xǁPuzzleGameǁ__move_empty_cell_to_left____mutmut_24, 
        'xǁPuzzleGameǁ__move_empty_cell_to_left____mutmut_25': xǁPuzzleGameǁ__move_empty_cell_to_left____mutmut_25, 
        'xǁPuzzleGameǁ__move_empty_cell_to_left____mutmut_26': xǁPuzzleGameǁ__move_empty_cell_to_left____mutmut_26
    }
    
    def __move_empty_cell_to_left__(self, *args, **kwargs):
        result = _mutmut_trampoline(object.__getattribute__(self, "xǁPuzzleGameǁ__move_empty_cell_to_left____mutmut_orig"), object.__getattribute__(self, "xǁPuzzleGameǁ__move_empty_cell_to_left____mutmut_mutants"), args, kwargs, self)
        return result 
    
    __move_empty_cell_to_left__.__signature__ = _mutmut_signature(xǁPuzzleGameǁ__move_empty_cell_to_left____mutmut_orig)
    xǁPuzzleGameǁ__move_empty_cell_to_left____mutmut_orig.__name__ = 'xǁPuzzleGameǁ__move_empty_cell_to_left__'

    def xǁPuzzleGameǁmove_empty_tile__mutmut_orig(self, direction):
        if direction.upper() == "DOWN":
            return self.__move_empty_cell_to_down__()
        elif direction.upper() == "UP":
            return self.__move_empty_cell_to_up__()
        elif direction.upper() == "RIGHT":
            return self.__move_empty_cell_to_right__()
        elif direction.upper() == "LEFT":
            return self.__move_empty_cell_to_left__()

    def xǁPuzzleGameǁmove_empty_tile__mutmut_1(self, direction):
        if direction.lower() == "DOWN":
            return self.__move_empty_cell_to_down__()
        elif direction.upper() == "UP":
            return self.__move_empty_cell_to_up__()
        elif direction.upper() == "RIGHT":
            return self.__move_empty_cell_to_right__()
        elif direction.upper() == "LEFT":
            return self.__move_empty_cell_to_left__()

    def xǁPuzzleGameǁmove_empty_tile__mutmut_2(self, direction):
        if direction.upper() != "DOWN":
            return self.__move_empty_cell_to_down__()
        elif direction.upper() == "UP":
            return self.__move_empty_cell_to_up__()
        elif direction.upper() == "RIGHT":
            return self.__move_empty_cell_to_right__()
        elif direction.upper() == "LEFT":
            return self.__move_empty_cell_to_left__()

    def xǁPuzzleGameǁmove_empty_tile__mutmut_3(self, direction):
        if direction.upper() == "XXDOWNXX":
            return self.__move_empty_cell_to_down__()
        elif direction.upper() == "UP":
            return self.__move_empty_cell_to_up__()
        elif direction.upper() == "RIGHT":
            return self.__move_empty_cell_to_right__()
        elif direction.upper() == "LEFT":
            return self.__move_empty_cell_to_left__()

    def xǁPuzzleGameǁmove_empty_tile__mutmut_4(self, direction):
        if direction.upper() == "down":
            return self.__move_empty_cell_to_down__()
        elif direction.upper() == "UP":
            return self.__move_empty_cell_to_up__()
        elif direction.upper() == "RIGHT":
            return self.__move_empty_cell_to_right__()
        elif direction.upper() == "LEFT":
            return self.__move_empty_cell_to_left__()

    def xǁPuzzleGameǁmove_empty_tile__mutmut_5(self, direction):
        if direction.upper() == "DOWN":
            return self.__move_empty_cell_to_down__()
        elif direction.lower() == "UP":
            return self.__move_empty_cell_to_up__()
        elif direction.upper() == "RIGHT":
            return self.__move_empty_cell_to_right__()
        elif direction.upper() == "LEFT":
            return self.__move_empty_cell_to_left__()

    def xǁPuzzleGameǁmove_empty_tile__mutmut_6(self, direction):
        if direction.upper() == "DOWN":
            return self.__move_empty_cell_to_down__()
        elif direction.upper() != "UP":
            return self.__move_empty_cell_to_up__()
        elif direction.upper() == "RIGHT":
            return self.__move_empty_cell_to_right__()
        elif direction.upper() == "LEFT":
            return self.__move_empty_cell_to_left__()

    def xǁPuzzleGameǁmove_empty_tile__mutmut_7(self, direction):
        if direction.upper() == "DOWN":
            return self.__move_empty_cell_to_down__()
        elif direction.upper() == "XXUPXX":
            return self.__move_empty_cell_to_up__()
        elif direction.upper() == "RIGHT":
            return self.__move_empty_cell_to_right__()
        elif direction.upper() == "LEFT":
            return self.__move_empty_cell_to_left__()

    def xǁPuzzleGameǁmove_empty_tile__mutmut_8(self, direction):
        if direction.upper() == "DOWN":
            return self.__move_empty_cell_to_down__()
        elif direction.upper() == "up":
            return self.__move_empty_cell_to_up__()
        elif direction.upper() == "RIGHT":
            return self.__move_empty_cell_to_right__()
        elif direction.upper() == "LEFT":
            return self.__move_empty_cell_to_left__()

    def xǁPuzzleGameǁmove_empty_tile__mutmut_9(self, direction):
        if direction.upper() == "DOWN":
            return self.__move_empty_cell_to_down__()
        elif direction.upper() == "UP":
            return self.__move_empty_cell_to_up__()
        elif direction.lower() == "RIGHT":
            return self.__move_empty_cell_to_right__()
        elif direction.upper() == "LEFT":
            return self.__move_empty_cell_to_left__()

    def xǁPuzzleGameǁmove_empty_tile__mutmut_10(self, direction):
        if direction.upper() == "DOWN":
            return self.__move_empty_cell_to_down__()
        elif direction.upper() == "UP":
            return self.__move_empty_cell_to_up__()
        elif direction.upper() != "RIGHT":
            return self.__move_empty_cell_to_right__()
        elif direction.upper() == "LEFT":
            return self.__move_empty_cell_to_left__()

    def xǁPuzzleGameǁmove_empty_tile__mutmut_11(self, direction):
        if direction.upper() == "DOWN":
            return self.__move_empty_cell_to_down__()
        elif direction.upper() == "UP":
            return self.__move_empty_cell_to_up__()
        elif direction.upper() == "XXRIGHTXX":
            return self.__move_empty_cell_to_right__()
        elif direction.upper() == "LEFT":
            return self.__move_empty_cell_to_left__()

    def xǁPuzzleGameǁmove_empty_tile__mutmut_12(self, direction):
        if direction.upper() == "DOWN":
            return self.__move_empty_cell_to_down__()
        elif direction.upper() == "UP":
            return self.__move_empty_cell_to_up__()
        elif direction.upper() == "right":
            return self.__move_empty_cell_to_right__()
        elif direction.upper() == "LEFT":
            return self.__move_empty_cell_to_left__()

    def xǁPuzzleGameǁmove_empty_tile__mutmut_13(self, direction):
        if direction.upper() == "DOWN":
            return self.__move_empty_cell_to_down__()
        elif direction.upper() == "UP":
            return self.__move_empty_cell_to_up__()
        elif direction.upper() == "RIGHT":
            return self.__move_empty_cell_to_right__()
        elif direction.lower() == "LEFT":
            return self.__move_empty_cell_to_left__()

    def xǁPuzzleGameǁmove_empty_tile__mutmut_14(self, direction):
        if direction.upper() == "DOWN":
            return self.__move_empty_cell_to_down__()
        elif direction.upper() == "UP":
            return self.__move_empty_cell_to_up__()
        elif direction.upper() == "RIGHT":
            return self.__move_empty_cell_to_right__()
        elif direction.upper() != "LEFT":
            return self.__move_empty_cell_to_left__()

    def xǁPuzzleGameǁmove_empty_tile__mutmut_15(self, direction):
        if direction.upper() == "DOWN":
            return self.__move_empty_cell_to_down__()
        elif direction.upper() == "UP":
            return self.__move_empty_cell_to_up__()
        elif direction.upper() == "RIGHT":
            return self.__move_empty_cell_to_right__()
        elif direction.upper() == "XXLEFTXX":
            return self.__move_empty_cell_to_left__()

    def xǁPuzzleGameǁmove_empty_tile__mutmut_16(self, direction):
        if direction.upper() == "DOWN":
            return self.__move_empty_cell_to_down__()
        elif direction.upper() == "UP":
            return self.__move_empty_cell_to_up__()
        elif direction.upper() == "RIGHT":
            return self.__move_empty_cell_to_right__()
        elif direction.upper() == "left":
            return self.__move_empty_cell_to_left__()
    
    xǁPuzzleGameǁmove_empty_tile__mutmut_mutants : ClassVar[MutantDict] = {
    'xǁPuzzleGameǁmove_empty_tile__mutmut_1': xǁPuzzleGameǁmove_empty_tile__mutmut_1, 
        'xǁPuzzleGameǁmove_empty_tile__mutmut_2': xǁPuzzleGameǁmove_empty_tile__mutmut_2, 
        'xǁPuzzleGameǁmove_empty_tile__mutmut_3': xǁPuzzleGameǁmove_empty_tile__mutmut_3, 
        'xǁPuzzleGameǁmove_empty_tile__mutmut_4': xǁPuzzleGameǁmove_empty_tile__mutmut_4, 
        'xǁPuzzleGameǁmove_empty_tile__mutmut_5': xǁPuzzleGameǁmove_empty_tile__mutmut_5, 
        'xǁPuzzleGameǁmove_empty_tile__mutmut_6': xǁPuzzleGameǁmove_empty_tile__mutmut_6, 
        'xǁPuzzleGameǁmove_empty_tile__mutmut_7': xǁPuzzleGameǁmove_empty_tile__mutmut_7, 
        'xǁPuzzleGameǁmove_empty_tile__mutmut_8': xǁPuzzleGameǁmove_empty_tile__mutmut_8, 
        'xǁPuzzleGameǁmove_empty_tile__mutmut_9': xǁPuzzleGameǁmove_empty_tile__mutmut_9, 
        'xǁPuzzleGameǁmove_empty_tile__mutmut_10': xǁPuzzleGameǁmove_empty_tile__mutmut_10, 
        'xǁPuzzleGameǁmove_empty_tile__mutmut_11': xǁPuzzleGameǁmove_empty_tile__mutmut_11, 
        'xǁPuzzleGameǁmove_empty_tile__mutmut_12': xǁPuzzleGameǁmove_empty_tile__mutmut_12, 
        'xǁPuzzleGameǁmove_empty_tile__mutmut_13': xǁPuzzleGameǁmove_empty_tile__mutmut_13, 
        'xǁPuzzleGameǁmove_empty_tile__mutmut_14': xǁPuzzleGameǁmove_empty_tile__mutmut_14, 
        'xǁPuzzleGameǁmove_empty_tile__mutmut_15': xǁPuzzleGameǁmove_empty_tile__mutmut_15, 
        'xǁPuzzleGameǁmove_empty_tile__mutmut_16': xǁPuzzleGameǁmove_empty_tile__mutmut_16
    }
    
    def move_empty_tile(self, *args, **kwargs):
        result = _mutmut_trampoline(object.__getattribute__(self, "xǁPuzzleGameǁmove_empty_tile__mutmut_orig"), object.__getattribute__(self, "xǁPuzzleGameǁmove_empty_tile__mutmut_mutants"), args, kwargs, self)
        return result 
    
    move_empty_tile.__signature__ = _mutmut_signature(xǁPuzzleGameǁmove_empty_tile__mutmut_orig)
    xǁPuzzleGameǁmove_empty_tile__mutmut_orig.__name__ = 'xǁPuzzleGameǁmove_empty_tile'

    def xǁPuzzleGameǁ__print_board_of_puzzle_game____mutmut_orig(self):
        for line in range(0, self.board.number_of_lines):
            for column in range(0, self.board.number_of_columns):
                if self.board.grid[line][column] == None:
                    print(f"- ", end='')
                else:
                    print (f"{self.board.grid[line][column]} ", end='')
            print()

    def xǁPuzzleGameǁ__print_board_of_puzzle_game____mutmut_1(self):
        for line in range(None, self.board.number_of_lines):
            for column in range(0, self.board.number_of_columns):
                if self.board.grid[line][column] == None:
                    print(f"- ", end='')
                else:
                    print (f"{self.board.grid[line][column]} ", end='')
            print()

    def xǁPuzzleGameǁ__print_board_of_puzzle_game____mutmut_2(self):
        for line in range(0, None):
            for column in range(0, self.board.number_of_columns):
                if self.board.grid[line][column] == None:
                    print(f"- ", end='')
                else:
                    print (f"{self.board.grid[line][column]} ", end='')
            print()

    def xǁPuzzleGameǁ__print_board_of_puzzle_game____mutmut_3(self):
        for line in range(self.board.number_of_lines):
            for column in range(0, self.board.number_of_columns):
                if self.board.grid[line][column] == None:
                    print(f"- ", end='')
                else:
                    print (f"{self.board.grid[line][column]} ", end='')
            print()

    def xǁPuzzleGameǁ__print_board_of_puzzle_game____mutmut_4(self):
        for line in range(0, ):
            for column in range(0, self.board.number_of_columns):
                if self.board.grid[line][column] == None:
                    print(f"- ", end='')
                else:
                    print (f"{self.board.grid[line][column]} ", end='')
            print()

    def xǁPuzzleGameǁ__print_board_of_puzzle_game____mutmut_5(self):
        for line in range(1, self.board.number_of_lines):
            for column in range(0, self.board.number_of_columns):
                if self.board.grid[line][column] == None:
                    print(f"- ", end='')
                else:
                    print (f"{self.board.grid[line][column]} ", end='')
            print()

    def xǁPuzzleGameǁ__print_board_of_puzzle_game____mutmut_6(self):
        for line in range(0, self.board.number_of_lines):
            for column in range(None, self.board.number_of_columns):
                if self.board.grid[line][column] == None:
                    print(f"- ", end='')
                else:
                    print (f"{self.board.grid[line][column]} ", end='')
            print()

    def xǁPuzzleGameǁ__print_board_of_puzzle_game____mutmut_7(self):
        for line in range(0, self.board.number_of_lines):
            for column in range(0, None):
                if self.board.grid[line][column] == None:
                    print(f"- ", end='')
                else:
                    print (f"{self.board.grid[line][column]} ", end='')
            print()

    def xǁPuzzleGameǁ__print_board_of_puzzle_game____mutmut_8(self):
        for line in range(0, self.board.number_of_lines):
            for column in range(self.board.number_of_columns):
                if self.board.grid[line][column] == None:
                    print(f"- ", end='')
                else:
                    print (f"{self.board.grid[line][column]} ", end='')
            print()

    def xǁPuzzleGameǁ__print_board_of_puzzle_game____mutmut_9(self):
        for line in range(0, self.board.number_of_lines):
            for column in range(0, ):
                if self.board.grid[line][column] == None:
                    print(f"- ", end='')
                else:
                    print (f"{self.board.grid[line][column]} ", end='')
            print()

    def xǁPuzzleGameǁ__print_board_of_puzzle_game____mutmut_10(self):
        for line in range(0, self.board.number_of_lines):
            for column in range(1, self.board.number_of_columns):
                if self.board.grid[line][column] == None:
                    print(f"- ", end='')
                else:
                    print (f"{self.board.grid[line][column]} ", end='')
            print()

    def xǁPuzzleGameǁ__print_board_of_puzzle_game____mutmut_11(self):
        for line in range(0, self.board.number_of_lines):
            for column in range(0, self.board.number_of_columns):
                if self.board.grid[line][column] != None:
                    print(f"- ", end='')
                else:
                    print (f"{self.board.grid[line][column]} ", end='')
            print()

    def xǁPuzzleGameǁ__print_board_of_puzzle_game____mutmut_12(self):
        for line in range(0, self.board.number_of_lines):
            for column in range(0, self.board.number_of_columns):
                if self.board.grid[line][column] == None:
                    print(None, end='')
                else:
                    print (f"{self.board.grid[line][column]} ", end='')
            print()

    def xǁPuzzleGameǁ__print_board_of_puzzle_game____mutmut_13(self):
        for line in range(0, self.board.number_of_lines):
            for column in range(0, self.board.number_of_columns):
                if self.board.grid[line][column] == None:
                    print(f"- ", end=None)
                else:
                    print (f"{self.board.grid[line][column]} ", end='')
            print()

    def xǁPuzzleGameǁ__print_board_of_puzzle_game____mutmut_14(self):
        for line in range(0, self.board.number_of_lines):
            for column in range(0, self.board.number_of_columns):
                if self.board.grid[line][column] == None:
                    print(end='')
                else:
                    print (f"{self.board.grid[line][column]} ", end='')
            print()

    def xǁPuzzleGameǁ__print_board_of_puzzle_game____mutmut_15(self):
        for line in range(0, self.board.number_of_lines):
            for column in range(0, self.board.number_of_columns):
                if self.board.grid[line][column] == None:
                    print(f"- ", )
                else:
                    print (f"{self.board.grid[line][column]} ", end='')
            print()

    def xǁPuzzleGameǁ__print_board_of_puzzle_game____mutmut_16(self):
        for line in range(0, self.board.number_of_lines):
            for column in range(0, self.board.number_of_columns):
                if self.board.grid[line][column] == None:
                    print(f"- ", end='XXXX')
                else:
                    print (f"{self.board.grid[line][column]} ", end='')
            print()

    def xǁPuzzleGameǁ__print_board_of_puzzle_game____mutmut_17(self):
        for line in range(0, self.board.number_of_lines):
            for column in range(0, self.board.number_of_columns):
                if self.board.grid[line][column] == None:
                    print(f"- ", end='')
                else:
                    print (None, end='')
            print()

    def xǁPuzzleGameǁ__print_board_of_puzzle_game____mutmut_18(self):
        for line in range(0, self.board.number_of_lines):
            for column in range(0, self.board.number_of_columns):
                if self.board.grid[line][column] == None:
                    print(f"- ", end='')
                else:
                    print (f"{self.board.grid[line][column]} ", end=None)
            print()

    def xǁPuzzleGameǁ__print_board_of_puzzle_game____mutmut_19(self):
        for line in range(0, self.board.number_of_lines):
            for column in range(0, self.board.number_of_columns):
                if self.board.grid[line][column] == None:
                    print(f"- ", end='')
                else:
                    print (end='')
            print()

    def xǁPuzzleGameǁ__print_board_of_puzzle_game____mutmut_20(self):
        for line in range(0, self.board.number_of_lines):
            for column in range(0, self.board.number_of_columns):
                if self.board.grid[line][column] == None:
                    print(f"- ", end='')
                else:
                    print (f"{self.board.grid[line][column]} ", )
            print()

    def xǁPuzzleGameǁ__print_board_of_puzzle_game____mutmut_21(self):
        for line in range(0, self.board.number_of_lines):
            for column in range(0, self.board.number_of_columns):
                if self.board.grid[line][column] == None:
                    print(f"- ", end='')
                else:
                    print (f"{self.board.grid[line][column]} ", end='XXXX')
            print()
    
    xǁPuzzleGameǁ__print_board_of_puzzle_game____mutmut_mutants : ClassVar[MutantDict] = {
    'xǁPuzzleGameǁ__print_board_of_puzzle_game____mutmut_1': xǁPuzzleGameǁ__print_board_of_puzzle_game____mutmut_1, 
        'xǁPuzzleGameǁ__print_board_of_puzzle_game____mutmut_2': xǁPuzzleGameǁ__print_board_of_puzzle_game____mutmut_2, 
        'xǁPuzzleGameǁ__print_board_of_puzzle_game____mutmut_3': xǁPuzzleGameǁ__print_board_of_puzzle_game____mutmut_3, 
        'xǁPuzzleGameǁ__print_board_of_puzzle_game____mutmut_4': xǁPuzzleGameǁ__print_board_of_puzzle_game____mutmut_4, 
        'xǁPuzzleGameǁ__print_board_of_puzzle_game____mutmut_5': xǁPuzzleGameǁ__print_board_of_puzzle_game____mutmut_5, 
        'xǁPuzzleGameǁ__print_board_of_puzzle_game____mutmut_6': xǁPuzzleGameǁ__print_board_of_puzzle_game____mutmut_6, 
        'xǁPuzzleGameǁ__print_board_of_puzzle_game____mutmut_7': xǁPuzzleGameǁ__print_board_of_puzzle_game____mutmut_7, 
        'xǁPuzzleGameǁ__print_board_of_puzzle_game____mutmut_8': xǁPuzzleGameǁ__print_board_of_puzzle_game____mutmut_8, 
        'xǁPuzzleGameǁ__print_board_of_puzzle_game____mutmut_9': xǁPuzzleGameǁ__print_board_of_puzzle_game____mutmut_9, 
        'xǁPuzzleGameǁ__print_board_of_puzzle_game____mutmut_10': xǁPuzzleGameǁ__print_board_of_puzzle_game____mutmut_10, 
        'xǁPuzzleGameǁ__print_board_of_puzzle_game____mutmut_11': xǁPuzzleGameǁ__print_board_of_puzzle_game____mutmut_11, 
        'xǁPuzzleGameǁ__print_board_of_puzzle_game____mutmut_12': xǁPuzzleGameǁ__print_board_of_puzzle_game____mutmut_12, 
        'xǁPuzzleGameǁ__print_board_of_puzzle_game____mutmut_13': xǁPuzzleGameǁ__print_board_of_puzzle_game____mutmut_13, 
        'xǁPuzzleGameǁ__print_board_of_puzzle_game____mutmut_14': xǁPuzzleGameǁ__print_board_of_puzzle_game____mutmut_14, 
        'xǁPuzzleGameǁ__print_board_of_puzzle_game____mutmut_15': xǁPuzzleGameǁ__print_board_of_puzzle_game____mutmut_15, 
        'xǁPuzzleGameǁ__print_board_of_puzzle_game____mutmut_16': xǁPuzzleGameǁ__print_board_of_puzzle_game____mutmut_16, 
        'xǁPuzzleGameǁ__print_board_of_puzzle_game____mutmut_17': xǁPuzzleGameǁ__print_board_of_puzzle_game____mutmut_17, 
        'xǁPuzzleGameǁ__print_board_of_puzzle_game____mutmut_18': xǁPuzzleGameǁ__print_board_of_puzzle_game____mutmut_18, 
        'xǁPuzzleGameǁ__print_board_of_puzzle_game____mutmut_19': xǁPuzzleGameǁ__print_board_of_puzzle_game____mutmut_19, 
        'xǁPuzzleGameǁ__print_board_of_puzzle_game____mutmut_20': xǁPuzzleGameǁ__print_board_of_puzzle_game____mutmut_20, 
        'xǁPuzzleGameǁ__print_board_of_puzzle_game____mutmut_21': xǁPuzzleGameǁ__print_board_of_puzzle_game____mutmut_21
    }
    
    def __print_board_of_puzzle_game__(self, *args, **kwargs):
        result = _mutmut_trampoline(object.__getattribute__(self, "xǁPuzzleGameǁ__print_board_of_puzzle_game____mutmut_orig"), object.__getattribute__(self, "xǁPuzzleGameǁ__print_board_of_puzzle_game____mutmut_mutants"), args, kwargs, self)
        return result 
    
    __print_board_of_puzzle_game__.__signature__ = _mutmut_signature(xǁPuzzleGameǁ__print_board_of_puzzle_game____mutmut_orig)
    xǁPuzzleGameǁ__print_board_of_puzzle_game____mutmut_orig.__name__ = 'xǁPuzzleGameǁ__print_board_of_puzzle_game__'

    def xǁPuzzleGameǁend_of_the_game__mutmut_orig(self):
        return self.board.__eq__(self.board_with_final_state)

    def xǁPuzzleGameǁend_of_the_game__mutmut_1(self):
        return self.board.__eq__(None)
    
    xǁPuzzleGameǁend_of_the_game__mutmut_mutants : ClassVar[MutantDict] = {
    'xǁPuzzleGameǁend_of_the_game__mutmut_1': xǁPuzzleGameǁend_of_the_game__mutmut_1
    }
    
    def end_of_the_game(self, *args, **kwargs):
        result = _mutmut_trampoline(object.__getattribute__(self, "xǁPuzzleGameǁend_of_the_game__mutmut_orig"), object.__getattribute__(self, "xǁPuzzleGameǁend_of_the_game__mutmut_mutants"), args, kwargs, self)
        return result 
    
    end_of_the_game.__signature__ = _mutmut_signature(xǁPuzzleGameǁend_of_the_game__mutmut_orig)
    xǁPuzzleGameǁend_of_the_game__mutmut_orig.__name__ = 'xǁPuzzleGameǁend_of_the_game'

    def xǁPuzzleGameǁget_tile__mutmut_orig(self, line, column):
        if line > 0 and line <= self.board.number_of_lines and \
                column > 0 and column <= self.board.number_of_columns:
            if line == self.line_of_empty_position and \
                column == self.column_of_empty_position:
                return (" ")
            else:
                return self.board.get_tile(line, column)
        else:
            raise InvalidPositionException()

    def xǁPuzzleGameǁget_tile__mutmut_1(self, line, column):
        if line > 0 and line <= self.board.number_of_lines and \
                column > 0 or column <= self.board.number_of_columns:
            if line == self.line_of_empty_position and \
                column == self.column_of_empty_position:
                return (" ")
            else:
                return self.board.get_tile(line, column)
        else:
            raise InvalidPositionException()

    def xǁPuzzleGameǁget_tile__mutmut_2(self, line, column):
        if line > 0 and line <= self.board.number_of_lines or column > 0 and column <= self.board.number_of_columns:
            if line == self.line_of_empty_position and \
                column == self.column_of_empty_position:
                return (" ")
            else:
                return self.board.get_tile(line, column)
        else:
            raise InvalidPositionException()

    def xǁPuzzleGameǁget_tile__mutmut_3(self, line, column):
        if line > 0 or line <= self.board.number_of_lines and \
                column > 0 and column <= self.board.number_of_columns:
            if line == self.line_of_empty_position and \
                column == self.column_of_empty_position:
                return (" ")
            else:
                return self.board.get_tile(line, column)
        else:
            raise InvalidPositionException()

    def xǁPuzzleGameǁget_tile__mutmut_4(self, line, column):
        if line >= 0 and line <= self.board.number_of_lines and \
                column > 0 and column <= self.board.number_of_columns:
            if line == self.line_of_empty_position and \
                column == self.column_of_empty_position:
                return (" ")
            else:
                return self.board.get_tile(line, column)
        else:
            raise InvalidPositionException()

    def xǁPuzzleGameǁget_tile__mutmut_5(self, line, column):
        if line > 1 and line <= self.board.number_of_lines and \
                column > 0 and column <= self.board.number_of_columns:
            if line == self.line_of_empty_position and \
                column == self.column_of_empty_position:
                return (" ")
            else:
                return self.board.get_tile(line, column)
        else:
            raise InvalidPositionException()

    def xǁPuzzleGameǁget_tile__mutmut_6(self, line, column):
        if line > 0 and line < self.board.number_of_lines and \
                column > 0 and column <= self.board.number_of_columns:
            if line == self.line_of_empty_position and \
                column == self.column_of_empty_position:
                return (" ")
            else:
                return self.board.get_tile(line, column)
        else:
            raise InvalidPositionException()

    def xǁPuzzleGameǁget_tile__mutmut_7(self, line, column):
        if line > 0 and line <= self.board.number_of_lines and \
                column >= 0 and column <= self.board.number_of_columns:
            if line == self.line_of_empty_position and \
                column == self.column_of_empty_position:
                return (" ")
            else:
                return self.board.get_tile(line, column)
        else:
            raise InvalidPositionException()

    def xǁPuzzleGameǁget_tile__mutmut_8(self, line, column):
        if line > 0 and line <= self.board.number_of_lines and \
                column > 1 and column <= self.board.number_of_columns:
            if line == self.line_of_empty_position and \
                column == self.column_of_empty_position:
                return (" ")
            else:
                return self.board.get_tile(line, column)
        else:
            raise InvalidPositionException()

    def xǁPuzzleGameǁget_tile__mutmut_9(self, line, column):
        if line > 0 and line <= self.board.number_of_lines and \
                column > 0 and column < self.board.number_of_columns:
            if line == self.line_of_empty_position and \
                column == self.column_of_empty_position:
                return (" ")
            else:
                return self.board.get_tile(line, column)
        else:
            raise InvalidPositionException()

    def xǁPuzzleGameǁget_tile__mutmut_10(self, line, column):
        if line > 0 and line <= self.board.number_of_lines and \
                column > 0 and column <= self.board.number_of_columns:
            if line == self.line_of_empty_position or column == self.column_of_empty_position:
                return (" ")
            else:
                return self.board.get_tile(line, column)
        else:
            raise InvalidPositionException()

    def xǁPuzzleGameǁget_tile__mutmut_11(self, line, column):
        if line > 0 and line <= self.board.number_of_lines and \
                column > 0 and column <= self.board.number_of_columns:
            if line != self.line_of_empty_position and \
                column == self.column_of_empty_position:
                return (" ")
            else:
                return self.board.get_tile(line, column)
        else:
            raise InvalidPositionException()

    def xǁPuzzleGameǁget_tile__mutmut_12(self, line, column):
        if line > 0 and line <= self.board.number_of_lines and \
                column > 0 and column <= self.board.number_of_columns:
            if line == self.line_of_empty_position and \
                column != self.column_of_empty_position:
                return (" ")
            else:
                return self.board.get_tile(line, column)
        else:
            raise InvalidPositionException()

    def xǁPuzzleGameǁget_tile__mutmut_13(self, line, column):
        if line > 0 and line <= self.board.number_of_lines and \
                column > 0 and column <= self.board.number_of_columns:
            if line == self.line_of_empty_position and \
                column == self.column_of_empty_position:
                return ("XX XX")
            else:
                return self.board.get_tile(line, column)
        else:
            raise InvalidPositionException()

    def xǁPuzzleGameǁget_tile__mutmut_14(self, line, column):
        if line > 0 and line <= self.board.number_of_lines and \
                column > 0 and column <= self.board.number_of_columns:
            if line == self.line_of_empty_position and \
                column == self.column_of_empty_position:
                return (" ")
            else:
                return self.board.get_tile(None, column)
        else:
            raise InvalidPositionException()

    def xǁPuzzleGameǁget_tile__mutmut_15(self, line, column):
        if line > 0 and line <= self.board.number_of_lines and \
                column > 0 and column <= self.board.number_of_columns:
            if line == self.line_of_empty_position and \
                column == self.column_of_empty_position:
                return (" ")
            else:
                return self.board.get_tile(line, None)
        else:
            raise InvalidPositionException()

    def xǁPuzzleGameǁget_tile__mutmut_16(self, line, column):
        if line > 0 and line <= self.board.number_of_lines and \
                column > 0 and column <= self.board.number_of_columns:
            if line == self.line_of_empty_position and \
                column == self.column_of_empty_position:
                return (" ")
            else:
                return self.board.get_tile(column)
        else:
            raise InvalidPositionException()

    def xǁPuzzleGameǁget_tile__mutmut_17(self, line, column):
        if line > 0 and line <= self.board.number_of_lines and \
                column > 0 and column <= self.board.number_of_columns:
            if line == self.line_of_empty_position and \
                column == self.column_of_empty_position:
                return (" ")
            else:
                return self.board.get_tile(line, )
        else:
            raise InvalidPositionException()
    
    xǁPuzzleGameǁget_tile__mutmut_mutants : ClassVar[MutantDict] = {
    'xǁPuzzleGameǁget_tile__mutmut_1': xǁPuzzleGameǁget_tile__mutmut_1, 
        'xǁPuzzleGameǁget_tile__mutmut_2': xǁPuzzleGameǁget_tile__mutmut_2, 
        'xǁPuzzleGameǁget_tile__mutmut_3': xǁPuzzleGameǁget_tile__mutmut_3, 
        'xǁPuzzleGameǁget_tile__mutmut_4': xǁPuzzleGameǁget_tile__mutmut_4, 
        'xǁPuzzleGameǁget_tile__mutmut_5': xǁPuzzleGameǁget_tile__mutmut_5, 
        'xǁPuzzleGameǁget_tile__mutmut_6': xǁPuzzleGameǁget_tile__mutmut_6, 
        'xǁPuzzleGameǁget_tile__mutmut_7': xǁPuzzleGameǁget_tile__mutmut_7, 
        'xǁPuzzleGameǁget_tile__mutmut_8': xǁPuzzleGameǁget_tile__mutmut_8, 
        'xǁPuzzleGameǁget_tile__mutmut_9': xǁPuzzleGameǁget_tile__mutmut_9, 
        'xǁPuzzleGameǁget_tile__mutmut_10': xǁPuzzleGameǁget_tile__mutmut_10, 
        'xǁPuzzleGameǁget_tile__mutmut_11': xǁPuzzleGameǁget_tile__mutmut_11, 
        'xǁPuzzleGameǁget_tile__mutmut_12': xǁPuzzleGameǁget_tile__mutmut_12, 
        'xǁPuzzleGameǁget_tile__mutmut_13': xǁPuzzleGameǁget_tile__mutmut_13, 
        'xǁPuzzleGameǁget_tile__mutmut_14': xǁPuzzleGameǁget_tile__mutmut_14, 
        'xǁPuzzleGameǁget_tile__mutmut_15': xǁPuzzleGameǁget_tile__mutmut_15, 
        'xǁPuzzleGameǁget_tile__mutmut_16': xǁPuzzleGameǁget_tile__mutmut_16, 
        'xǁPuzzleGameǁget_tile__mutmut_17': xǁPuzzleGameǁget_tile__mutmut_17
    }
    
    def get_tile(self, *args, **kwargs):
        result = _mutmut_trampoline(object.__getattribute__(self, "xǁPuzzleGameǁget_tile__mutmut_orig"), object.__getattribute__(self, "xǁPuzzleGameǁget_tile__mutmut_mutants"), args, kwargs, self)
        return result 
    
    get_tile.__signature__ = _mutmut_signature(xǁPuzzleGameǁget_tile__mutmut_orig)
    xǁPuzzleGameǁget_tile__mutmut_orig.__name__ = 'xǁPuzzleGameǁget_tile'

    def __str__(self):
        return self.board.__str__()
