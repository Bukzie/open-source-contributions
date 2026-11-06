"""EXPLORATORY out-of-tree probe for hypothesis H1 (not a fix, not a patch to upstream).
Wraps MutmutCallStack.set/reset so the cyclic GC is disabled during the ContextVar call and
restored to its previous state afterwards. Activated only when MUTMUT_596_PROBE=1."""
import gc, os

if os.environ.get("MUTMUT_596_PROBE") == "1":
    from mutmut.core import MutmutCallStack

    def _set(cls, value):
        was = gc.isenabled()
        gc.disable()
        try:
            return cls._ctx.set(value)
        finally:
            if was:
                gc.enable()

    def _reset(cls, token):
        was = gc.isenabled()
        gc.disable()
        try:
            cls._ctx.reset(token)
        finally:
            if was:
                gc.enable()

    MutmutCallStack.set = classmethod(_set)
    MutmutCallStack.reset = classmethod(_reset)
