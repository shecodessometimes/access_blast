from Bio.Blast.NCBIWWW import qblast

fasta_file_names = ["sequence"]

for i in range(len(fasta_file_names)):
    fasta_string = open("fasta_files/"+fasta_file_names[i]+".fasta").read()
    print("File accessed.")
    result_handle = qblast("blastn", "nt", fasta_string)
    print("File blasted.")

    with open("output_files/"+fasta_file_names[i]+"blast.xml", "w") as out_handle:
        out_handle.write(result_handle.read())
        print(f"The {fasta_file_names[i]}.fasta file was blasted.")
    result_handle.close()
