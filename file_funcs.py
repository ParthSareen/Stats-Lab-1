import os

def open_file(path):
        data = []
        with open(path) as fp:
                for data_line in fp:
                        #print("Line {}: {}".format(cnt, line))
                        data.append(data_line)
                fp.close()
        return data
