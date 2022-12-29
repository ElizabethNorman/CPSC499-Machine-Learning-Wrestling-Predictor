import csv

f = open("AEWSinglesEdited2.txt")

data_header = ['wrestler 1', 'wrestler 2', 'winner', 'location', 'time', 'show', 'champion match', 'title', 'champion at start', 'title change', 'champion at end', 'date']

f2 = open('aew_match_data2.csv', 'w')

writer = csv.writer(f2)
writer.writerow(data_header)


def skip(m):
    if "aping" in m:
        return True
    if "Dark Match" in m:
        return True
    if "Fan Fest" in m:
        return True
    if "Cruise" in m:
        return True
    return False


data_line = []
champ_bool = False
title_change = False
title = "none"
champion_before = "none"
champion_after = "none"

for i in range(1000):
    date = f.readline()
    match = f.readline()

    if skip(match):
        continue

    print("match is ", match)

    if "(c)" in match:
        match = match.replace("(c)", "{c}")
        champ_bool = True

    wrestlers_split = match.split(" defeats ")

    wrestler1 = wrestlers_split[0].split(":")

    print("wrestler one", wrestler1[len(wrestler1) - 1])


    if len(wrestler1) > 1 and champ_bool is True:
        title = wrestler1[0]
        title = title.strip()

    wrestler2 = wrestlers_split[1].split("(")
    print("wrestler two", wrestler2[0])

    wrestler1name = wrestler1[len(wrestler1) - 1]
    wrestler1name = wrestler1name.strip()
    wrestler2name = wrestler2[0]
    wrestler2name = wrestler2name.strip()

    if "{c}" in wrestler1name:
        w1split = wrestler1name.split("{")
        wrestler1name = w1split[0]
        champion_before = wrestler1name.strip()

    if "{c}" in wrestler2name:
        w2split = wrestler2name.split("{")
        wrestler2name = w2split[0]
        champion_before = wrestler2name.strip()
        title_change = True

    if wrestler1name == "Jungle Boy":
        wrestler1name = "Jack Perry"

    if wrestler2name == "Jungle Boy":
        wrestler2name = "Jack Perry"

    if wrestler1name == "Will Hobbs":
        wrestler1name = "Powerhouse Hobbs"

    if wrestler2name == "Will Hobbs":
        wrestler2name = "Powerhouse Hobbs"

    data_line.append(wrestler1name)
    data_line.append(wrestler2name)

    print("winner is", wrestler1name)
    data_line.append(wrestler1name)

    if champ_bool is True:
        champion_after = wrestler1name

    time = wrestler2[1].split(")")
    print("time is ", time[0])

    show = time[1].split("@")
    show_type = show[0].split("#")
    show_title = show_type[0].split("!!!")
    show_type = show_title[len(show_title) - 1]

    print("show type is:", show_type)

    location_split = match.split(" in ")
    location = location_split[1]

    print("location is ", location)
    print("date is", date)

    data_line.append(location.strip())
    data_line.append(time[0].strip())
    data_line.append(show_type.strip())
    data_line.append(champ_bool)
    data_line.append(title.strip())
    data_line.append(champion_before)
    data_line.append(title_change)
    data_line.append(champion_after)
    data_line.append(date)

    writer.writerow(data_line)

    data_line = []
    champ_bool = False
    title = "none"
    champion_before = "none"
    title_change = False
    champion_after = "none"

    print("**Starting new match**")

f.close()
