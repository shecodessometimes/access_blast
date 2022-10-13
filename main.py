from Bio.Blast.NCBIWWW import qblast
import os

#identify the folder to look for .fasta files in
foldername = "fasta_files"
folder = os.fsencode(foldername)

#blast all the .fasta files within the folder
for file in os.listdir(folder):
    #get the file name for a given file
    filename = os.fsdecode(file)

    #check if it's a .fasta file
    if filename.endswith(".fasta"):
        fasta_string = open(foldername + "/" + filename).read()
        print(f"{filename} was accessed.")

        #blast the file and put result in result_handle
        result_handle = qblast("blastn", "nt", fasta_string)
        print(f"{filename} was blasted.")

        #write the result into a new .xml file
        with open(f"output_files/{filename[:-6]}_blast.xml", "w") as out_handle:
            out_handle.write(result_handle.read())
            print(f"The blasted {filename} file was written to{filename[:-6]}_blast.xml")

        #exit the program
        result_handle.close()
