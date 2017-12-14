
if __name__ == '__main__':

    src1 = open('2016-04-LC.csv')
    src2 = open('LP.csv')
    dest = open('2016-04-LP-top3.csv', 'w')

    global ListingId_set
    ListingId_set = set()

    for line1 in src1:
        temp1 = line1.strip().split(',')
        ListingId_set.add(temp1[0])

    for line2 in src2:
        temp2 = line2.strip().split(',')
        if temp2[0] in ListingId_set and int(temp2[1]) < 4:
            dest.write(line2)

    dest.close()