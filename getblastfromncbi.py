# -*- coding: utf-8 -*-
"""
Created on Fri Nov  8 12:07:04 2019

@author: yanglinsen

use biopytyon module to get blast results from NCBI blast
"""

from Bio.Blast import NCBIWWW
from Bio import SeqIO
records = list(SeqIO.parse('../cpf1proteins.fasta',format='fasta'))
Cpf1protein = records[0]
result_handle = NCBIWWW.qblast("blastp","nr", Cpf1protein.format("fasta"))
with open("Cpf1protein_blastp.xml", "w") as out_handle:
    out_handle.write(result_handle.read())
result_handle.close()

#using tblastn
result_handle2 = NCBIWWW.qblast("tblastn","nt", Cpf1protein.format("fasta"))
with open("Cpf1protein_tblastn.xml", "w") as out_handle:
    out_handle.write(result_handle2.read())
result_handle2.close()


