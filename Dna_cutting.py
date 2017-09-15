#**************************************************************
#                   Project #2 Restriction Enzymes
#                    Name: Valliyil Saikiran
#                    BioInformatics Date: 09/02/2017
#***************************************************************
#      This program takes strands as input from the user and then
#      returns a list of sub-strings by cutting the input strand 
#      DNA into pieces. It also  prints out the substrands together 
#      with their associated complementary strands.
#***************************************************************      
#                    Way to Execute Program:
#  In this project, we Input a specific DNA Strand which is a string
#          "ACGAACATCTTTGGCCAACTAGACCTGGCCAACCTAGCGG"
#  The HaeIII method takes input Strand and returns a list of substrings 
#     by cutting at every GGCC that occurs in the input dna strand.
#   In this program, it prints out the substrands together with their 
#                associated complementary strands
#
#*****************************************************************

#*******************************************************************
#                      ObjectName::HaeIII()
#                       Parameters: strand
#                       Complexity: O(N)    
#********************************************************************
# I have written the entire programas turned in and have not copied this code,
# or parts of this code from the internet or another student.
#
#						                        Signature:______________



import string

#Takes input strand and returns a list of substrings
def HaeIII(strand):
    strand_list = []
    while len(strand)!=0:
        position = strand.find("GGCC")
        if position != -1:
            #Slicing the strand
            substring = strand[:position+2]
            strand_list.append(substring)
            strand = strand[position+2:]
        else:
            strand_list.append(strand)
            strand = ""
    return strand_list

if __name__ == '__main__':
    sub_str = []
    str1 = "ATCG"
    str2 = "TAGC"
    strand = input("Input a Strand\n")
    sub_str = HaeIII(strand)

    print("\nSubstrands and their complements are:")
    #To print the substrands and their complements
    for i in sub_str:
        trans = i.maketrans(str1,str2)
        print(i)
        print(i.translate(trans),"\n")