### count_analyze.py
# 1. This script finds the 3 top genetic features with the maximum number of reads mapped to it in sample D3
# 2. It thereafter finds the corresponding count for the genetic feature in sample D1
# 3. Lastly, it normalizes the count by the number of reads per sample

bin_list = [1, 2, 6, 7, 12, 16, 19, 24, 26]
result_file = 'result_count_D3_max.txt'

with open(result_file, "a") as file:
    file.write('Bin' + ' ' + 'Feature_name' + ' ' + 'Count_D1' + ' ' + 'Count_D3' + '\n')

for i in bin_list:
    # Defining the files corresponding to the specific bin
    file = 'bin_' + str(i) + '_count_SiteD3.out'
    file2 = 'bin_' + str(i) + '_count_SiteD1.out'

    # Counting the number of reads from each file
    result = []

    # Opening counting-file from site D3 for a bin
    with open(file, "r") as file:
        count_1 = 0
        count_2 = 0
        count_3 = 0

        for line in file:
            # Looking at features that
            if not line.startswith('_'):
                # Splitting line at spacing
                split_line = line.split()

                # Second argument corresponds to number of reads mapped to a feature
                if int(split_line[1]) > count_1:
                    count_1 = int(split_line[1])
                    name_feature_1 = split_line[0]
                elif int(split_line[1]) > count_2:
                    count_2 = int(split_line[1])
                    name_feature_2 = split_line[0]
                elif int(split_line[1]) > count_3:
                    count_3 = int(split_line[1])
                    name_feature_3 = split_line[0]


    # Opening counting-file from site D1 for a bin and finding corresponding count for top features
    with open(file2, "r") as file2:
        for line in file2:
            split_line = line.split()
            if split_line[0] == name_feature_1:
                count_opposite_1 = int(split_line[1])
            elif split_line[0] == name_feature_2:
                count_opposite_2 = int(split_line[1])
            elif split_line[0] == name_feature_3:
                count_opposite_3 = int(split_line[1])

    # Writing result to file
    with open(result_file, "a") as file:
        file.write('bin_' + str(i) + ' ')
        file.write(name_feature_1 + ' ')
        file.write(str(count_1) + ' ')
        file.write(str(count_opposite_1) + '\n')
        file.write('bin_' + str(i) + ' ')
        file.write(name_feature_2 + ' ')
        file.write(str(count_2) + ' ')
        file.write(str(count_opposite_2) + '\n')
        file.write('bin_' + str(i) + ' ')
        file.write(name_feature_3 + ' ')
        file.write(str(count_3) + ' ')
        file.write(str(count_opposite_3) + '\n')
