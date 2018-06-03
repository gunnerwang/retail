import os
import re
def face(file_face):
    # REQUIRE: input file_tone should be format .jpg
    os.system("curl -s -X POST -u \"apikey:iapg7mHwjN23Sl2nrapb2nTqw-USO_9UeA74Uo5qjbfz\" --form \"images_file=@%s\" \
    \"https://gateway.watsonplatform.net/visual-recognition/api/v3/detect_faces?version=2018-03-19\" > face.txt" % file_face)
    file = open("face.txt")
    min = []
    max = []
    for line in file.readlines():
        if (re.match('\"min\":*', line.strip(" "))):
            min.append(line.strip(" ").strip("\n").strip(","))

    file2 = open("face.txt")
    for line in file2.readlines():
        if (re.match('\"max\":*', line.strip(" "))):
            max.append(line.strip(" ").strip("\n"))
    file2.close()

    #----------#
    age = []
    for i in range(len(min)):
        age.append((int(str(min[i]).strip(",").split(":")[1])+int(str(max[i]).strip(",").split(":")[1]))/2)
    num = len(age)
    #----------#

    gender = []
    file3 = open("face.txt")
    for line in file3.readlines():
        if (re.match('\"gender\":*', line.strip(" "))):
            if line.strip(" ").strip("\n").strip(",").split(":")[1]!=" {":
                gender.append(eval(line.strip(" ").strip("\n").strip(",").split(":")[1]))
    file3.close()

    height = []
    file4 = open("face.txt")
    for line in file4.readlines():
        if (re.match('\"height\":*', line.strip(" "))):
            height.append(float(line.strip(" ").strip("\n").strip(",").split(":")[1]))
    file4.close()

    width = []
    file5 = open("face.txt")
    for line in file5.readlines():
        if (re.match('\"width\":*', line.strip(" "))):
            width.append(float(line.strip(" ").strip("\n").strip(",").split(":")[1]))
    file5.close()

    left = []
    file6 = open("face.txt")
    for line in file6.readlines():
        if (re.match('\"left\":*', line.strip(" "))):
            left.append(float(line.strip(" ").strip("\n").strip(",").split(":")[1]))
    file6.close()

    top = []
    file7 = open("face.txt")
    for line in file7.readlines():
        if (re.match('\"top\":*', line.strip(" "))):
            top.append(float(line.strip(" ").strip("\n").strip(",").split(":")[1]))
    file7.close()

    #----------#
    location = []
    for i in range(num):
        location.append((left[i],top[i],width[i],height[i]))
    #----------#

    all_information = []
    for i in range(num):
        all_information.append(dict({"age":age[i],"gender":gender[i],"location":location[i]}))

    return all_information