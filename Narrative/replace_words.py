import fileinput

text = "samplefile.txt"
fields = {"Marvin": "Kweyu", "Melvin": "Emmanuel"}
file = open('samplefile2.txt','a')

print("start")
print("replacing words...")
for line in fileinput.input(text, inplace=False):
    line = line.rstrip()
    if not line:
        continue
    for key in fields.keys():
        if key in line:
            line = line.replace(key, fields[key])
    file.write(line+"\n")
file.close()
print("Done")

#example2 ..bad idea

# fields = {"Marvin": "Kweyu", "Melvin": "Emmanuel"}
#
# # with open('samplefile.txt', 'w+') as f:
# f = open('2Story.txt', 'w+')
# s = f.read()
#
# for key in fields:
#     r = s.replace(key, fields[key])
#     f.write(r)
#
# print("Closing file...")
# f.close()
# print("Done replacing")

#example3


# import fileinput
#
# text = "samplefile.txt"
# # fields = {"pattern 1": "replacement text 1", "pattern 2": "replacement text 2"}
# fields = {"Marvin": "Kweyu", "Melvin": "Emmanuel"}
#
# for line in fileinput.input(text, inplace=True):
#     line = line.rstrip()
#     for field in fields:
#         if field in line:
#             line = line.replace(field, fields[field])
#
#     print line
