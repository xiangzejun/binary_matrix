from binmatrix import BinMatrix

if __name__ == "__main__":

	m = [[1,1,0],[0,0,1],[1,0,1]]
	try:
		matrix = BinMatrix(m)
		print "matrix = %s" % str(matrix.m)
		print "rank = %d" % matrix.rank()
		print "det = %d" % matrix.det()
		print "inv = %s" % str(matrix.inv())
	except FormatError as e1:
		e1.printError()
	except DataError as e2:
		e2.printError()
	except RankError as e3:
		e3.printError()