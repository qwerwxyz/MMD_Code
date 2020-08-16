import math
class Nist:
    def __init__(self, ref, candi, N):
        self.ref = ref
        self.candi = candi
        self.N = N
        self.co_occur = None
        self.candi_set = None
        self.ref_set = None
        self.beta = 0.5
        self.ref_list = []
        self.candi_list = []
        self.ref_list_n = []
        self.candi_list_n = []

    def cal_information(self):
        '''calculate information'''
        info = 0.
        for words in self.co_occur:
            Wn_1 = words[:-1]
            Wn = words
            count_Wn = self.find_word_in_list(Wn, 'Wn')
            if len(words) == 1:
                count_Wn_1 = len(self.ref_list)
            else:
                count_Wn_1 = self.find_word_in_list(Wn_1, 'Wn-1')
            info += math.log2(float(count_Wn_1 / count_Wn))
        return info

    def find_word_in_list(self, key_word, flag):
        count = 0
        for word in self.ref_list_n:
            if flag == 'Wn-1':
                if word[:-1] == key_word:
                    count += 1
            else:
                if word == key_word:
                    count += 1
        return count

    def cal_one_nist(self, info):
        sys_output = len(self.candi_list_n)
        print(self.candi_list_n)
        temp = float(info/sys_output)
        return temp

    def find_cooccur_word(self, i):
        '''find co-occur word'''
        self.ref_list_n = []
        self.candi_list_n = []
        for j in range(len(self.ref_list) - i + 1):
            str = ''
            for item in self.ref_list[j: j + i]:
                str = str + '&' + item
            self.ref_list_n.append(str)
        for j in range(len(self.candi_list) - i + 1):
            str = ''
            for item in self.candi_list[j: j + i]:
                str = str + '&' + item
            self.candi_list_n.append(str)
        ref_set = set(self.ref_list_n)
        candi_set = set(self.candi_list_n)
        self.co_occur = list(set(ref_set) & set(candi_set))
        for i in range(len(self.co_occur)):
            self.co_occur[i] = self.co_occur[i].split('&')[1:]
        for i in range(len(self.candi_list_n)):
            self.candi_list_n[i] = self.candi_list_n[i].split('&')[1:]
        for i in range(len(self.ref_list_n)):
            self.ref_list_n[i] = self.ref_list_n[i].split('&')[1:]

    def token(self):
        self.ref_list = self.ref
        self.candi_list = self.candi

    def calculate(self):
        self.token()
        temp = 0.
        for i in range(1, min(self.N + 1, len(self.candi) + 1, len(self.ref_list) + 1)):
            self.find_cooccur_word(i)
            info = self.cal_information()
            temp += self.cal_one_nist(info)
        nist = temp * math.exp(self.beta * math.pow(math.log2(min(len(self.candi_list)/len(self.ref_list),1)),2))
        print('---------', nist)
        return nist

def main(ref, candi):

    test = Nist(ref, candi, 5)
    nist = test.calculate()
    return nist
