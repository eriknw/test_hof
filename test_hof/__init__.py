from .firstorder import one, two, three, inc, double, triple, identity
from .higherorder import incremented, doubled, tripled, identified

__author__ = 'Erik Welch'
__email__ = 'erik.n.welch@gmail.com'
__version__ = '0.1.0'

__all__ = list(name for name in locals()
               if not name.startswith('_'))

from ._homaker import create_higher_order_module as _make_hof

_reverse = False
_composition = True
if _composition:
    _fofs = [one, two, three, identity]
    _hofs = [inc, double, triple]
    _make_hof(__package__, 'hofs', _fofs, _hofs, composition=True,
              reverse=_reverse)
else:
    _fofs = [one, two, three, identity, inc, double, triple]
    _hofs = [incremented, doubled, tripled, identified]
    _make_hof(__package__, 'hofs', _fofs, _hofs, reverse=_reverse)
