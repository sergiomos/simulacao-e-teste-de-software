from typing import Annotated
from typing import Callable
from typing import ClassVar

MutantDict = Annotated[dict[str, Callable], "Mutant"] # type: ignore


def _mutmut_trampoline(orig, mutants, call_args, call_kwargs, self_arg = None): # type: ignore
    """Forward call to original or mutated function, depending on the environment"""
    import os # type: ignore
    mutant_under_test = os.environ['MUTANT_UNDER_TEST'] # type: ignore
    if mutant_under_test == 'fail': # type: ignore
        from mutmut.__main__ import MutmutProgrammaticFailException # type: ignore
        raise MutmutProgrammaticFailException('Failed programmatically')       # type: ignore
    elif mutant_under_test == 'stats': # type: ignore
        from mutmut.__main__ import record_trampoline_hit # type: ignore
        record_trampoline_hit(orig.__module__ + '.' + orig.__name__) # type: ignore
        # (for class methods, orig is bound and thus does not need the explicit self argument)
        result = orig(*call_args, **call_kwargs) # type: ignore
        return result # type: ignore
    prefix = orig.__module__ + '.' + orig.__name__ + '__mutmut_' # type: ignore
    if not mutant_under_test.startswith(prefix): # type: ignore
        result = orig(*call_args, **call_kwargs) # type: ignore
        return result # type: ignore
    mutant_name = mutant_under_test.rpartition('.')[-1] # type: ignore
    if self_arg is not None: # type: ignore
        # call to a class method where self is not bound
        result = mutants[mutant_name](self_arg, *call_args, **call_kwargs) # type: ignore
    else:
        result = mutants[mutant_name](*call_args, **call_kwargs) # type: ignore
    return result # type: ignore
def somar(a, b):
    args = [a, b]# type: ignore
    kwargs = {}# type: ignore
    return _mutmut_trampoline(x_somar__mutmut_orig, x_somar__mutmut_mutants, args, kwargs, None)
def x_somar__mutmut_orig(a, b):
    return a + b
def x_somar__mutmut_1(a, b):
    return a - b

x_somar__mutmut_mutants : ClassVar[MutantDict] = { # type: ignore
'x_somar__mutmut_1': x_somar__mutmut_1
}
x_somar__mutmut_orig.__name__ = 'x_somar'


def subtrair(a, b):
    args = [a, b]# type: ignore
    kwargs = {}# type: ignore
    return _mutmut_trampoline(x_subtrair__mutmut_orig, x_subtrair__mutmut_mutants, args, kwargs, None)


def x_subtrair__mutmut_orig(a, b):
    return a - b


def x_subtrair__mutmut_1(a, b):
    return a + b

x_subtrair__mutmut_mutants : ClassVar[MutantDict] = { # type: ignore
'x_subtrair__mutmut_1': x_subtrair__mutmut_1
}
x_subtrair__mutmut_orig.__name__ = 'x_subtrair'


def multiplicar(a, b):
    args = [a, b]# type: ignore
    kwargs = {}# type: ignore
    return _mutmut_trampoline(x_multiplicar__mutmut_orig, x_multiplicar__mutmut_mutants, args, kwargs, None)


def x_multiplicar__mutmut_orig(a, b):
    return a * b


def x_multiplicar__mutmut_1(a, b):
    return a / b

x_multiplicar__mutmut_mutants : ClassVar[MutantDict] = { # type: ignore
'x_multiplicar__mutmut_1': x_multiplicar__mutmut_1
}
x_multiplicar__mutmut_orig.__name__ = 'x_multiplicar'


def dividir(a, b):
    args = [a, b]# type: ignore
    kwargs = {}# type: ignore
    return _mutmut_trampoline(x_dividir__mutmut_orig, x_dividir__mutmut_mutants, args, kwargs, None)


def x_dividir__mutmut_orig(a, b):
    if b == 0:
        raise ValueError("divisao por zero")
    return a / b


def x_dividir__mutmut_1(a, b):
    if b != 0:
        raise ValueError("divisao por zero")
    return a / b


def x_dividir__mutmut_2(a, b):
    if b == 1:
        raise ValueError("divisao por zero")
    return a / b


def x_dividir__mutmut_3(a, b):
    if b == 0:
        raise ValueError(None)
    return a / b


def x_dividir__mutmut_4(a, b):
    if b == 0:
        raise ValueError("XXdivisao por zeroXX")
    return a / b


def x_dividir__mutmut_5(a, b):
    if b == 0:
        raise ValueError("DIVISAO POR ZERO")
    return a / b


def x_dividir__mutmut_6(a, b):
    if b == 0:
        raise ValueError("divisao por zero")
    return a * b

x_dividir__mutmut_mutants : ClassVar[MutantDict] = { # type: ignore
'x_dividir__mutmut_1': x_dividir__mutmut_1, 
    'x_dividir__mutmut_2': x_dividir__mutmut_2, 
    'x_dividir__mutmut_3': x_dividir__mutmut_3, 
    'x_dividir__mutmut_4': x_dividir__mutmut_4, 
    'x_dividir__mutmut_5': x_dividir__mutmut_5, 
    'x_dividir__mutmut_6': x_dividir__mutmut_6
}
x_dividir__mutmut_orig.__name__ = 'x_dividir'


def eh_par(n):
    args = [n]# type: ignore
    kwargs = {}# type: ignore
    return _mutmut_trampoline(x_eh_par__mutmut_orig, x_eh_par__mutmut_mutants, args, kwargs, None)


def x_eh_par__mutmut_orig(n):
    return n % 2 == 0


def x_eh_par__mutmut_1(n):
    return n / 2 == 0


def x_eh_par__mutmut_2(n):
    return n % 3 == 0


def x_eh_par__mutmut_3(n):
    return n % 2 != 0


def x_eh_par__mutmut_4(n):
    return n % 2 == 1

x_eh_par__mutmut_mutants : ClassVar[MutantDict] = { # type: ignore
'x_eh_par__mutmut_1': x_eh_par__mutmut_1, 
    'x_eh_par__mutmut_2': x_eh_par__mutmut_2, 
    'x_eh_par__mutmut_3': x_eh_par__mutmut_3, 
    'x_eh_par__mutmut_4': x_eh_par__mutmut_4
}
x_eh_par__mutmut_orig.__name__ = 'x_eh_par'
