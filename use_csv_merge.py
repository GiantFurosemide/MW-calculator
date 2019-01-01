import csv_merge as cs
import csv
import os


# input file path here
file_path = '/Users/wangmu/Desktop/20181222'

# print what we got and number them
di = cs.make_it_dict(file_path)
n = 0
for x, y in di.items():
    if "exit code 1" in y:
        n += 1
        print(x, "exit code 1", n)

    else:
        n += 1
        print(x, len(y), n)

a = cs.show_all(file_path)
print(sorted(a[0]), len(a[0]))

# restructure data for csv
file_name_list, peak_list = list(di.keys()), list(di.values())
construct_name_list = [i.rstrip('.CSV') for i in file_name_list]
rows_data_list = []

for i in range(len(construct_name_list)):
    row_data_list = [construct_name_list[i]]
    row_data_list += list(peak_list[i])
    rows_data_list.append(row_data_list)


# make a csv for all data
def list_to_csv(file_path, input_list):
    save_csv_path = os.path.join(file_path, "all.csv")
    with open(save_csv_path, 'w') as csf:
        csf_writer = csv.writer(csf, dialect='excel')

        for i in input_list:
            csf_writer.writerow(i)


list_to_csv(file_path, rows_data_list)
