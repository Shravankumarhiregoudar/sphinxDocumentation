
import numpy as np
from scipy import interpolate
from scipy.interpolate import interp1d


def cubicInterpolationSpectra(x,y,start,stop,totalPointsDesired):
	"""
		:cubicInterpolationSpectra: Interpolate original data with cubic spline
		:param x: original data array.
		:type x: array

		:param y: original data array
		:type y: array

		:param start: desired range start position
		:type start: int

		:param stop: desired range stop position
		:type stop: int
		
		:param totalPointsDesired: the total number of points which defines the point spacing
		:type totalPointsDesired: int

		:returns: newX, New point spacing and newY, New interpolated data
	"""
	#interpolate original data with cubic spline
	f = interpolate.interp1d(x,y, kind = 'cubic')

	#sample from the desired range
	newX = np.linspace(start,stop,totalPointsDesired)
	newY = f(newX)
	return newX, newY