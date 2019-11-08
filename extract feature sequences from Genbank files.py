# -*- coding: utf-8 -*-
"""
Created on Fri Nov  8 15:48:28 2019

@author: yanglinsen
"""
from Bio import SeqIO
records = list(SeqIO.parse("../lbCpf1/addgene-plasmid-102566-sequence-198456.gbk", "genbank"))
first_record = records[0]
lbCpf1 = first_record.features[9].extract(first_record)
print(lbCpf1)
