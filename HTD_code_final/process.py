question_file = open("question_words.txt", 'r')
question_words = question_file.readline().split('|')
num = {}
for item in question_words:
    num[item] = 0
data = open("data/weibo_pair_train_Q_after.response")
for line in data:
    sen = line.strip().split()
    for word in sen:
        if num.has_key(word):
            num[word] = num[word] + 1

for item in question_words:
    print item, num[item]
