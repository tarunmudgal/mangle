import pytest


@pytest.mark.parametrize('func2', ['alpha', 'beta'], indirect=True)
# @pytest.mark.usefixtures('func2')
class TestCases():
	
	def test_1(self, func1, func2, func3, func4):
		print("test_1 called")

	def test_2(self, func1, func2, func3, func4):
		print("test_2 called")

	def test_3(self, func1, func2, func3, func4):
		print("test_3 called")
