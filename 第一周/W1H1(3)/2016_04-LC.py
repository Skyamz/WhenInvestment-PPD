
if __name__ == '__main__':

    src = open('LC.csv')
    dest = open('2016-04-LC.csv', 'w')
    for line in src:
        temp = line.strip().split(',')
        date = temp[4]
        if '2016-04' in date:
            dest.write(line)

    dest.close()