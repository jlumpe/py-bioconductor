"""Convert S4Vectors objects to and from their Python representations.

Bioconductor package: `S4Vectors <http://bioconductor.org/packages/S4Vectors/>`_

::

	Pagès H, Lawrence M and Aboyoun P (2017). S4Vectors: S4 implementation of
	vectors and lists. R package version 0.14.6.
"""

import numpy as np
from rpy2.robjects.packages import importr


def dataframe_to_pandas(dataframe):
	"""Convert an S4Vector DataFrame to a Pandas DataFrame.

	Requires the pandas package be installed, obviously.

	:param dataframe: rpy2 S4 object corresponding to an S4VectorS DataFrame.
	:type dataframe: rpy2.robjects.methods.RS4
	:rtype: pandas.DataFrame
	"""
	import pandas as pd

	rbase = importr('base')

	colnames = list(rbase.colnames(dataframe))
	data = list(map(np.array, dataframe.do_slot('listData')))

	df = pd.DataFrame.from_items(list(zip(colnames, data)))
	df.index = dataframe.do_slot('rownames')

	return df
