from RestrictedPython import compile_restricted, Eval, Guards, safe_globals, utility_builtins
from RestrictedPython import safe_globals

source_code = """
import os
def example():
    return "Hello World"
"""

loc = {}
byte_code = compile_restricted(source_code, '<inline>', 'exec')
exec(byte_code, safe_globals, loc)

print(loc['example']())
