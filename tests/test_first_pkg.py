"""Tests the mathematical functions defined in first_pkg/trial.py"""

import pytest
import numpy as np

def test_square():
	"tests the squaring function"

	from first_pkg.trial import square

	assert 4 == square(2)

	assert 4 == square(-2)

	assert 12.25 == square(3.5)

	assert 2 == round(square(np.sqrt(2)), 5)

def test_factorial():
	"tests the factorial function"

	from first_pkg.trial import factorial

	assert 24 == factorial(4)

	assert 6 == factorial(3.0)

	assert 1 == factorial(0)

	assert 1 == factorial(-1)

	with pytest.raises(ValueError):
		factorial(3.5)
