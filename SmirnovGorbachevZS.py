import os
import re
import codecs

def files():
    i = input('Введите название команды:')
    ZS = []
    TP = 0
    FNpre = 0
    long1 = 0
    long2 = 0

    for (dirpath, dirnames, filenames) in os.walk('./ZS/Razmetka'):
        ZS.extend(filenames)
    f0 = open('results_'+i+'.csv','w', encoding='utf-8-sig')
    f0.write('Полнота;Точность;F-мера')

    for file_name in ZS:
        text1 = []
        text2 = []



        if os.path.exists(file_name[0:-7]+'.txt'):
            f1 = codecs.open("./ZS/Razmetka/"+file_name, 'r', encoding='utf-8-sig')

            f2 = codecs.open(file_name[0:-7]+'.txt', 'r', encoding='utf-8-sig')

            for line1 in f1:
                long1 += 1
                item1 = []
                r = re.findall('[а-яё]+',line1.lower())
                for word1 in r:
                    item1.append(word1)
                text1.append(item1)

            for line2 in f2:
                long2 += 1
                item2 = []
                r2 = re.findall('[а-яё]+',line2.lower())
                for word2 in r2:
                    item2.append(word2)
                text2.append(item2)

            for i in text1:
                for ii in text2:

                    if jaccard_similarity(i, ii) >= 0.7:
                        TP += 1
                        long1 -= 1
                        long2 -= 1

                    if jaccard_similarity(i, ii) > 0.1 and jaccard_similarity(i, ii) < 0.6:
                        FNpre += 1
                        long1 -= 1

            f1.close()
            f2.close()



        else:
            f1 = codecs.open("./ZS/Razmetka/"+file_name, 'rb')
            for line1 in f1:
                long1 += 1
                print(long1)




    FN = long1
    FP = long2
    if (TP + FN) == 0:
        R = 0
    else:
        R = float(TP / (TP + FN))
    if (TP + FP) == 0:
        P = 0
    else:
        P = float(TP / (TP + FP))
    if (P + R) == 0:
        F = 0
    else:
        F = (2*P*R) / (P + R)
    f0.write('\r'+str(R)+';' + str(P)+';' + str(F))


def jaccard_similarity(a, b):
    set_a = set(a)
    set_b = set(b)
    return float(len(set_a.intersection(set_b))) / float(len(set_a.union(set_b)))

files()