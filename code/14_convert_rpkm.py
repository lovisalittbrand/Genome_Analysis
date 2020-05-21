#!/usr/bin/env python3
import sys

#This script calculates the gene lengths and thereafter computes the RPKM for each feature

#Creating result file
result_file = sys.argv[3]

# Importing files:
#  1. File with annotation to access gene length
#  2. File with count data for each feature
file_gff = open(sys.argv[1], "r")
file_count = open(sys.argv[2], "r")

# Calculating the gene lengths for mapped features
file_gff_lines = file_gff.readlines()
file_count_lines = file_count.readlines()

for line in file_count_lines:
 if line.startswith('_'):
  continue
 else:
  # Split at spacing
  split_line_count = line.split()
  feature_name = split_line_count[0]
  feature_count = split_line_count[1]

  for line2 in file_gff_lines:
   if line2.startswith('k'):
    split_line_gff = line2.split('\t')
    feature_info = split_line_gff[8]
    feature_id = feature_info.split("ID=")
    if (len(feature_id) > 1):
     #with open(result_file, "a") as file:
      #file.write(feature_id[1])
    
     # Matching ID in both files
     if feature_id[1].startswith(feature_name):
      gene_length = float(split_line_gff[4]) - float(split_line_gff[3])
     

      # Running for all data from site D1
      ks = 0.873799
      rpkm = (float(feature_count)/ks)
      rpkm2 = rpkm/gene_length
      with open(result_file, "a") as file:
       file.write(feature_name + ' ' + str(rpkm2) + '\n')

