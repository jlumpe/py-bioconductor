"""Generic tools for supplementing rpy2."""

import rpy2.rinterface as ri


class S4Wrapper:
	"""Wrapper around rpy2's wrapper around an R S4 class instance.

	:param robj: The R object to wrap.
	:type robj: rpy2.rinterface.SexpS4
	"""

	def __init__(self, robj):
		if not isinstance(robj, ri.SexpS4):
			raise TypeError('Must pass instance of rpy2.rinterface.SexpS4')

		object.__setattr__(self, 'robj_', robj)
		object.__setattr__(self, 'slots_', tuple(robj.list_attrs()))

	def get_(self, slot):
		return self.robj_.do_slot(slot)

	def set_(self, slot, value):
		raise self.robj_.do_slot_assign(slot, value)

	def __getattr__(self, name):
		if name in self.slots_:
			return self.get_(name)
		else:
			raise AttributeError('S4 object has no slot named {!r}'.format(name))

	def __setattr__(self, name, value):
		if name in self.slots_:
			return self.set_(name, value)
		else:
			raise AttributeError('S4 object has no slot named {!r}'.format(name))

	@property
	def rclass_(self):
		return self.robj_.rclass[0]

	def __dir__(self):
		return [*type(self).__dict__, *self.__dict__, *self.slots_]

	def __repr__(self):
		return '<{} {}>'.format(type(self).__name__, self.robj_.r_repr())
