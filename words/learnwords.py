import random
import sys

def loadWords(fileName):
    f = open(fileName)
    dic = []
    for line in f.readlines():
        if line:
            line = line.split('\n')[0]
            meaning, word = line.split('\t')[-1].strip(), line.split('\t')[0].strip().split("/")
            print "{}   :   {}".format(word, meaning)
            dic.append([meaning, word])
    f.close()
    return dic

def performTest(dic):
    print "\n" * 24
    print "+" * 60
    print "\n" * 24

    passed = []
    failed = []
    while len(dic) > 0:
        index = random.randint(0, len(dic)-1)
        pair = dic[index]
        print "\n" + pair[0] + " : ",
        answer = raw_input()
        for word in pair[1]:
            if cmp(answer, word) == 0:
                passed.append(pair)
                print " correct "
                break
        else:
            failed.append(pair)
            print " wrong, should be " + str(pair[1])
        dic.remove(pair)
    return passed, failed

def handleFailure(failed):
    print "\n" * 4
    print "+" * 60
    print "\n" * 4
    print "{} words failed:".format(len(failed))
    for word in failed:
        print "  {} : {}".format(word[0], word[1])
    print "\nWould you like to test the failed words again? (y/n)"
    answer = raw_input()
    if cmp(answer, 'n') == 0 or cmp(answer, 'no') == 0 or cmp(answer, 'N') == 0:
        return False
    else:
        passed, failed = performTest(failed)
        if len(failed) > 0:
            return handleFailure(failed)
        else:
            return True


def learnWords(fileName):
    dic = loadWords(fileName)

    passed = []
    failed = []

    passed, failed = performTest(dic)

    success = True
    if len(failed) > 0:
        success = handleFailure(failed)
    else:
        success = True

    if success:
        print "All correct!"


learnWords(sys.argv[1])
