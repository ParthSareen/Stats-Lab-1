from file_funcs import *
from constants import *
from logic import *

def main():
	data = open_file(PATH_TO_DATA)
	data_list = organize_data(data)
	print(data_list)
	plot_histogram(data_list)
	#plot_curve(data_list)


if __name__ == '__main__':
	main()