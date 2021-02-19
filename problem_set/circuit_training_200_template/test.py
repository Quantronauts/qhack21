NODES = 6
max_ind_set = []
data = 7
print("Data : ", data)

binary = '{0:06b}'.format(data)
binary_str = str(binary)

print("Binaire : ", binary_str)

compteur = NODES - 1
for i in range(NODES):
    if binary_str[i] == "1":
        max_ind_set.append(compteur)
    compteur -= 1

max_ind_set = list(dict.fromkeys(max_ind_set))
max_ind_set.reverse()

print("Finish :", max_ind_set)
