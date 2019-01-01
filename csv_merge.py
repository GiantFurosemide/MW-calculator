import csv
import os


'''
give a directory of csv files, then return a dictionary of file_name:[[time],[peak height]].
you should use a directory path and give it to def make_it_dict(file_path) then return a dictionary
'''


def show_all(file_path):
    files_name_list = os.listdir(file_path)  # list all file/directory below this path
    file_path_list = []  # make a list to save all files we got beneath

    for fi in files_name_list:
        full_path = os.path.join(file_path, fi)
        file_path_list.append(full_path)
    return files_name_list, file_path_list


def return_peak(file_name):
    # input a csv file and return two list of time and peak height in float
    with open(file_name, encoding="UTF-16") as f:  # by "UTF-16"
        reader = csv.reader(f)
        # header_row = next(reader)
        # save time and peak height as a list
        row_split_list = []
        peak_height_list = []
        try:
            a = next(reader)
        except UnicodeError:
            peak_height_list.append('exit code 1')
        else:
            for rows in reader:
                row_split_list.append(rows[0].split('\t'))

            for i in row_split_list:
                peak_height_list.append(float(i[1]))

    return peak_height_list


def make_it_dict(dir_path):
    files_name_list, file_path_list = show_all(dir_path)
    peak_list = []
    for files_path in file_path_list:
        peak = return_peak(files_path)
        peak_list.append(peak)
        di = dict(sorted(zip(files_name_list, peak_list), key=lambda x: x[0]))  # sort dict after a sorted tuple
    return di


if __name__ == '__main__':
    file_path = '/Users/wangmu/Desktop/20181222'
    file_name = '/Users/wangmu/Desktop/20181222/10115.CSV'

    b = return_peak(file_name)

    c = make_it_dict(file_path)

    print(b)
