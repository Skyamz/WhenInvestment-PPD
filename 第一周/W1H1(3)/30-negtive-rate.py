# -*- coding: utf-8 -*-
__author__ = 'Administrator'

from collections import defaultdict
biaodi_num = 10


def get_pwd(str_list, num):
    if num == 1:
        for x in str_list:
            yield x
    else:
        for x in str_list:
            str_list.remove(x)
            for y in get_pwd(str_list, num-1):
                yield x + '-' + y


if __name__ == '__main__':

    src1 = open('overdate-LP.csv')
    src2 = open('2016-04-LC.csv')
    src3 = open('non-overdate-LP.csv')

    global ListingId_set
    ListingId_set = set()

    global ListingId_all_money_dic
    ListingId_all_money_dic = defaultdict(int)

    global ListingId_all_have_paid_money_dic
    ListingId_all_have_paid_money_dic = defaultdict(float)

    overdate_biao_num = 0

    for line2 in src2:
        temp2 = line2.strip().split(',')
        ListingId_all_money_dic[temp2[0]] = temp2[1]    # Id-借款金额

    for line3 in src3:
        temp3 = line3.strip().split(',')
        ListingId_all_have_paid_money_dic[temp3[0]] += float(temp3[3])   # 已还本金

    for line1 in src1:
        temp1 = line1.strip().split(',')
        ListingId_set.add(temp1[0])

    # overdate_biao_num = len(ListingId_set)
    # print overdate_biao_num
    ListingId_list = list(ListingId_set)

    Max_rate = 0.0
    Min_rate = 1.0

    for each in get_pwd(ListingId_list, biaodi_num):
        temp = each.split('-')
        all_money = 0.0
        all_have_paid_money = 0.0
        for each_id in temp:
            all_money += float(ListingId_all_money_dic[each_id])   # 所有标的本金之和
            all_have_paid_money += float(ListingId_all_have_paid_money_dic[each_id])    # 所有标的已还本金之和

        rate_30 = (all_money - all_have_paid_money)/all_money
        if rate_30 > Max_rate:
            Max_rate = rate_30
        if rate_30 < Min_rate:
            Min_rate = rate_30

    print Max_rate, Min_rate