from file_funcs import *
from constants import *
from logic import *

def main():
	debug = input('Debug? ')
	if not debug:
		path = PATH_TO_DATA
	else:
		path = PATH_TO_DATA_TEST
	data = open_file(path)
	data_list = organize_data(data)
	print(data_list)
	plot_histogram(data_list)
	#plot_curve(data_list)


if __name__ == '__main__':
	main()