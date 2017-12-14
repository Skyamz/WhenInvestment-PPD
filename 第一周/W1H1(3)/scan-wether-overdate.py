__author__ = 'Administrator'

if __name__ == '__main__':

    src = open('2016-04-LP-top3.csv')
    dest1 = open('overdate-LP.csv', 'w')
    dest2 = open('non-overdate-LP.csv', 'w')

    for line in src:
        temp = line.strip().split(',')

        date1 = ''.join(temp[7].split('-'))
        date2 = ''.join(temp[8].split('-'))
        if temp[8] != '\N':
            # if float(date1) < 20160702 and float(date2) - float(date1) > 99:
            if float(date1) < 20160702 and float(date2) > 20160731:
                dest1.write(line)
            else:
                dest2.write(line)
        elif float(date1) < 20160702:
            dest1.write(line)
        else:
            dest2.write(line)

    dest1.close()
