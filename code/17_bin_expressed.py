### bin_expressed.py
# This script sums all the mapped reads for each bin and saves the result into a text-file.

bin_list = [1, 2, 6, 7, 12, 16, 19, 24, 26]
result_file = 'result_bin_expressed.txt'

with open(result_file, "a") as file:
    file.write('Bin_Site' + ' ' + 'Count' + '\n')

for i in bin_list:
    # Defining the files corresponding to the specific bin
    file = 'bin_' + str(i) + '_count_SiteD3.out'
    file2 = 'bin_' + str(i) + '_count_SiteD1.out'

    # Counting the number of reads from each file
    result = []

    # Opening counting-file from site D3 for a bin and adding all the mapped reads together
    with open(file, "r") as file:
        count_D3 = 0

        for line in file:
            # Looking at features that don't start with _
            if not line.startswith('_'):
                # Splitting line at spacing
                split_line = line.split()

                # Adding number of mapped reads together
                count_D3 = count_D3 + int(split_line[1])

                # Add result to text file
        with open(result_file, "a") as file:
            file.write('bin_' + str(i) + '_D3')
            file.write(' ' + str(count_D3) + '\n')

    # Opening counting-file from site D1 for a bin and adding all the mapped reads together
    with open(file2, "r") as file2:
        count_D1 = 0

        for line in file2:
            # Looking at features that don't start with _
            if not line.startswith('_'):
                # Splitting line at spacing
                split_line = line.split()

                # Adding number of mapped reads together
                count_D1 = count_D1 + int(split_line[1])

                # Add result to text file
        with open(result_file, "a") as file:
            file.write('bin_' + str(i) + '_D1')
            file.write(' ' + str(count_D1) + '\n')