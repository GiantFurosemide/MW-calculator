class cal_MV():
    def __init__(self):
        self.data_list = []
        self.weight_dict = {
            'A': 89.000,
            'R': 174.000,
            'N': 132.000,
            'D': 133.000,
            'C': 121.000,
            'Q': 146.000,
            'E': 147.000,
            'G': 75.000,
            'H': 155.000,
            'I': 131.000,
            'L': 131.000,
            'K': 146.000,
            'M': 149.000,
            'F': 165.000,
            'P': 115.000,
            'S': 105.000,
            'T': 119.000,
            'W': 204.000,
            'Y': 181.000,
            'V': 117.000
        }
        self.amino_list = ['A', 'R', 'N', 'D', 'C', 'Q', 'E', 'G', 'H', 'I', 'L',
                           'K', 'M', 'F', 'P', 'S', 'T', 'W', 'Y', 'V']

    def cal_MV(self):
        MV_list = []
        for j in self.data_list:
            MV_Sum = 0
            for i in self.amino_list:
                num = j.count(i)
                MV = num * self.weight_dict[i]
                MV_Sum += MV
            MV_list.append(str(MV_Sum/1000)+' KDa')
        print(MV_list)


'''
a = cal_MV()
a.data_list = [' A', ' MTPQSLLQTTLFLLSLLFLVQGA']
a.cal_MV()
'''

