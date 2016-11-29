# For feedback or questions, pleast contact at xiangzejun@iie.ac.cn

# Implemented by Xiang Zejun, State Key Laboratory of Information Security, 
# Institute Of Information Engineering, CAS

class DataError(Exception):
	"""
	Define my data exception.
	Check whether the elements of the matrxi are binaries.
	"""
	def __init__(self, x, y):
		"""
		store the coordinate of the entry which is not binary.
		"""
		self.x = x
		self.y = y

	def printError(self):
		print "The element at [{0}][{1}] is NOT binary!".format(self.x, self.y)

class FormatError(Exception):
	"""
	Define my format exception.
	Check whether input is a matrix or a square matrix.
	"""
	def __init__(self, s):
		self.error = "The input is " + s
	def printError(self):
		print self.error

class RankError(Exception):
	"""
	Define my rank exception.
	Check whether the square matrix is full rank when calculating its inverse. 
	"""
	def __init__(self, r):
		self.r = r
	def printError(self):
		print "The matrix is NOT full rank. (rank = {0})".format(self.r)

class BinMatrix:
	def __init__(self, m = [[1]]):
		"""
		Initilize a matrix.
		"""
		self.m = m
		self.r_len = len(self.m) # row number
		self.c_len = len(self.m[0]) # column number
		# self.length = len(self.m)

	def __convertMatrixToInt(self):
		"""
		Convert each row of the binary matrix to an integer.
		"""
		return [int(reduce(lambda x , y: x + y, map(str, self.m[i])), 2) for i in range(self.r_len)]

	def __appendUnitMatrix(self):
		"""
		Append a unit matrix to m_int.
		"""
		m_int = self.__convertMatrixToInt()
		return [(1 << (self.r_len + self.c_len - 1 - i)) ^ m_int[i] for i in range(self.r_len)]

	def __chooseElement(self, r, c, m_int):
		"""
		Choose a none-zero row started from position [r][c].
		"""
		assert r <= c, "The row index can not exceed the column index in row-reduced echelon matrix."

		if c == self.c_len:
			return None
		else:
			mask = (1 << (self.c_len - 1 - c))
			temp = [(m_int[i] & mask) for i in range(r, self.r_len)]
			if mask not in temp:
				return self.__chooseElement(r, c + 1, m_int)
			else:
				return (temp.index(mask) + r, c)

	@staticmethod
	def __switchRows(r1, r2, m_int):
		"""
		Switch r1-th and r2-th rows of m_int.
		"""
		temp = m_int[r1]
		m_int[r1] = m_int[r2]
		m_int[r2] = temp

	def __addRows(self, r, c, m_int):
		"""
		Add the r-th row to all the other rows if the c-th element of 
		the corresponding rows are nonzero.
		"""
		mask = (1 << (self.c_len - 1 - c))
		it = range(self.r_len)
		it.remove(r)
		for i in it:
			if m_int[i] & mask != 0:
				m_int[i] ^= m_int[r]

	
	def __isMatrix(self):
		"""
		Check whether the input is a matrix.
		"""
		if [len(l) for l in self.m].count(self.c_len) != self.r_len:
			raise FormatError("NOT a matrix!")
		else:
			pass

	def __isSquareMatrix(self):
		"""
		Check whether the input is a square matrix.
		"""
		if [len(l) for l in self.m].count(self.r_len) != self.r_len:
			raise FormatError("NOT a Square matrix!")
		else:
			pass

	def __isBinary(self):
		"""
		Check whether the entrys in the input are binaries.
		"""
		for i in range(len(self.m)):
			for j in range(len(self.m[i])):
				if self.m[i][j] not in [0,1]:
					raise DataError(i, j)
				else:
					pass

	def rank(self):
		"""
		Calculate the Rank of the matrix.
		"""
		self.__isMatrix()
		self.__isBinary()
		m_int = self.__convertMatrixToInt()
		r = 0
		c = 0
		for i in range(self.r_len):
			arg = self.__chooseElement(r, c, m_int)
			if arg != None:
				r_temp = arg[0]
				c = arg[1]
				self.__switchRows(r, r_temp, m_int)
				self.__addRows(r, c, m_int)
				r += 1
				c += 1  
			else:
				return r
		return self.r_len

	def det(self):
		"""
		Calculate the Det of the matrix.
		"""
		self.__isSquareMatrix()
		self.__isBinary()
		if self.rank() == self.r_len:
			return 1
		else:
			return 0

	def inv(self):
		"""
		Calculate the inverse of the matrix.
		"""
		self.__isSquareMatrix()
		self.__isBinary()
		m_adj = self.__appendUnitMatrix()
		r = 0
		c = 0
		for i in range(self.r_len):
			arg = self.__chooseElement(r, c, m_adj)
			if arg != None:
				r_temp = arg[0]
				c = arg[1]
				self.__switchRows(r, r_temp, m_adj)
				self.__addRows(r, c, m_adj)
				r += 1
				c += 1
			else:
				raise RankError(r)
		return [map(int, list(format((m_adj[i] >> self.c_len), "0" + str(self.r_len) + "b"))) for i in range(self.r_len)]
