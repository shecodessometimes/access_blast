from Bio.Blast.NCBIWWW import qblast

fasta_file_names = ["sequence", "sequence (2)"]

for i in range(len(fasta_file_names)):
    fasta_string = open("fasta_files/"+fasta_file_names[i]+".fasta").read()
    print(f"{fasta_file_names[i]}.fasta was accessed.")
    result_handle = qblast("blastn", "nt", fasta_string)
    print(f"{fasta_file_names[i]}.fasta was blasted.")

    with open("output_files/"+fasta_file_names[i]+"_blast.xml", "w") as out_handle:
        out_handle.write(result_handle.read())
        print(f"The blasted {fasta_file_names[i]}.fasta file was written to {fasta_file_names[i]}_blast.xml.")
    result_handle.close()
