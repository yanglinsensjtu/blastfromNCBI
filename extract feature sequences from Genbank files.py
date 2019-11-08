# -*- coding: utf-8 -*-
"""
Created on Fri Nov  8 15:48:28 2019

@author: yanglinsen
"""
from Bio import SeqIO
from os import walk, listdir, path
import re
filelist = listdir("lbCpf1/")
records = list(SeqIO.parse("../lbCpf1/6His-MBP-TEV-huLbCpf1.gb", "genbank"))
first_record = records[0]
for feature in first_record.features:
    start = feature.location.start.position
    end= feature.location.end.position
    if(end - start > 3600):
        lbCpf1 = feature.extract(first_record)
        lbCpf1.name = re.split('\.',filelist[0])
        
        
    
     
