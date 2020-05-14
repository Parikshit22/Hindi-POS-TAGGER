import pickle
import os
curr_dir = os.path.dirname(os.path.realpath(__file__))
with open(curr_dir+'/crf_model.pkl', 'rb') as f:
    model = pickle.load(f)
import re
import re
def features(sentence,index):
    ### sentence is of the form [w1,w2,w3,..], index is the position of the word in the sentence
    return {
        'is_first_word': int(index==0),
        'is_last_word':int(index==len(sentence)-1),
        'prev_word':'' if index==0 else sentence[index-1],
        'next_word':'' if index==len(sentence)-1 else sentence[index+1],
        'is_numeric':int(sentence[index].isdigit()),
        'prefix_1':sentence[index][0],
        'prefix_2': sentence[index][:2],
        'prefix_3':sentence[index][:3],
        'prefix_4':sentence[index][:4],
        'suffix_1':sentence[index][-1],
        'suffix_2':sentence[index][-2:],
        'suffix_3':sentence[index][-3:],
        'suffix_4':sentence[index][-4:],
        'word_has_hyphen': 1 if '-' in sentence[index] else 0  
         }

def Testing(sentences):
    X=[]
    for sentence in sentences:
        X.append([features(sentence, index) for index in range(len(sentence.split()))])
    return X

def merge(list1,list2):
    merge_list = []
    for i in range(len(list1)):
        list1[i] = list1[i].split()
        merge_list.append(list(zip(list1[i], list2[i])))
    return merge_list
def prediction(sentences):
    sentences = re.split('\||\n|\u0964',sentences)
    raw_sentence = sentences
    sentences = Testing(sentences)
    pred = model.predict(sentences)
    return merge(raw_sentence,pred)[:-1]

if __name__ == '__main__':
    print(prediction('ताजमहल भारत के आगरा शहर में स्थित एक विश्व धरोहर मक़बरा है। इसका निर्माण मुग़ल सम्राट शाहजहाँ ने अपनी पत्नी मुमताज़ महल की याद में करवाया था।'))
    