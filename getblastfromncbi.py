# -*- coding: utf-8 -*-
"""
use biopytyon module to get blast results from NCBI blast
"""

from Bio.Blast import NCBIWWW
from Bio import SeqIO
records = list(SeqIO.parse('../cpf1proteins.fasta',format='fasta'))
Cpf1protein = records[0]
result_handle = NCBIWWW.qblast("blastp","nr", Cpf1protein.seq)
with open("Cpf1protein_blast.xml", "w") as out_handle:
    out_handle.write(result_handle.read())
result_handle.close()

