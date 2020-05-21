#!/usr/bin/env python3
import sys
import numpy as np
import re

#This script calculates the gene lengths and thereafter computes the RPKM for each feature

#Creating result file
with open(result_file, "a") as file:
    file.write('Feature_ID' + ' ' + 'RPKM' + '\n')

# Importing files:
#  1. File with annotation to access gene length
#  2. File with count data for each feature
file_gff = open(sys.argv[1], "r")
file_count = open(sys.argv[2], "r")

# Calculating the gene lengths for mapped features
file_gff_lines = file_gff.readlines()
file_count_lines = file_count.readlines()
for line in file_count_lines:
    # Split at spacing
    split_line_count = line.split()
    feature_name = split_line_count[0]
    feature_count = int(split_line_count[1])

    for line2 in file_gff_lines:
        split_line_gff = line.split()
        if not line2.startswith('##'):
            feature_info = split_line_gff[8]
            feature_info_split = feature_info.split(";")
            feature_id = feature_info.split("=")
            feature_id = feature_id[1]

            # Matching ID in both files
            if feature_id == feature_name:
                gene_length = int(split_line_gff[4]) - int(split_line_gff[3])

                # Running for all data from site D1
                ks = 0.873799
                rpkm = (feature_count/ks)/gene_length
                with open(result_file, "a") as file:
                    file.write(feature_name + ' ' + rpkm)

