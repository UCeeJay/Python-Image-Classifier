dogfile = 'dognames.txt'

'''dognames_dic = dict()

with open(dogfile, "r") as infile:

    line = infile.readlines()
    for i in line:
        i = i.strip()
        if i not in dognames_dic:
            dognames_dic[i] = 1


        #line = infile.readline()

print(dognames_dic)'''

dognames_dic = dict()

with open(dogfile, "r") as infile:

    line = infile.readlines()

    for i in range(len(line)):
        while line[i] != "":
            line[i] = line[i].strip()


        if line[i] not in dognames_dic:
            dognames_dic[line[i]] = 1

        line = infile.readline()

print(dognames_dic)