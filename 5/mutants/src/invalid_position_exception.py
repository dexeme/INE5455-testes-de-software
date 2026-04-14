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
class InvalidPositionException(Exception):

    def xǁInvalidPositionExceptionǁ__init____mutmut_orig(self):
        self.message = 'Posicao invalida.'
        # super().__init__(self.message)

    def xǁInvalidPositionExceptionǁ__init____mutmut_1(self):
        self.message = None
        # super().__init__(self.message)

    def xǁInvalidPositionExceptionǁ__init____mutmut_2(self):
        self.message = 'XXPosicao invalida.XX'
        # super().__init__(self.message)

    def xǁInvalidPositionExceptionǁ__init____mutmut_3(self):
        self.message = 'posicao invalida.'
        # super().__init__(self.message)

    def xǁInvalidPositionExceptionǁ__init____mutmut_4(self):
        self.message = 'POSICAO INVALIDA.'
        # super().__init__(self.message)
    
    xǁInvalidPositionExceptionǁ__init____mutmut_mutants : ClassVar[MutantDict] = {
    'xǁInvalidPositionExceptionǁ__init____mutmut_1': xǁInvalidPositionExceptionǁ__init____mutmut_1, 
        'xǁInvalidPositionExceptionǁ__init____mutmut_2': xǁInvalidPositionExceptionǁ__init____mutmut_2, 
        'xǁInvalidPositionExceptionǁ__init____mutmut_3': xǁInvalidPositionExceptionǁ__init____mutmut_3, 
        'xǁInvalidPositionExceptionǁ__init____mutmut_4': xǁInvalidPositionExceptionǁ__init____mutmut_4
    }
    
    def __init__(self, *args, **kwargs):
        result = _mutmut_trampoline(object.__getattribute__(self, "xǁInvalidPositionExceptionǁ__init____mutmut_orig"), object.__getattribute__(self, "xǁInvalidPositionExceptionǁ__init____mutmut_mutants"), args, kwargs, self)
        return result 
    
    __init__.__signature__ = _mutmut_signature(xǁInvalidPositionExceptionǁ__init____mutmut_orig)
    xǁInvalidPositionExceptionǁ__init____mutmut_orig.__name__ = 'xǁInvalidPositionExceptionǁ__init__'
