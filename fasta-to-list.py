file_name = '/home/parric/Desktop/>sp|Q9Y653|AGRG1_HUMAN Adhesion G-protein coupled.txt'
with open(file_name) as fasta_data:
    contents = fasta_data.readlines()
    contents = list(map(lambda s: s.strip(), contents))
    contents = ['>sp|Q9Y653|AGRG1_HUMAN Adhesion G-protein coupled receptor G1 OS=Homo sapiens OX=9606 GN=ADGRG1 PE=1 SV=2', 'MTPQSLLQTTLFLLSLLFLVQGAHGRGHREDFRFCSQRNQTHRSSLHYKPTPDLRISIEN', 'SEEALTVHAPFPAAHPASRSFPDPRGLYHFCLYWNRHAGRLHLLYGKRDFLLSDKASSLL','>sp|Q9Y653|AGRG1_HUMAN Adhesion G-protein coupled receptor G1 OS=Homo sapiens OX=9606 GN=ADGRG1 PE=1 SV=2','RHAGRLHLLYGKRDFLLSDKASSLL']
    header_list= []
    seq_list = []
    seq = ''
    header_bool = True
    header_counter = 0

    for i in contents:
        if contents:
            if '>' in i and header_counter == 0:
                header_list.append(i)
                header_counter += 1
            elif '>' in i and header_counter > 0:
                header_list.append(i)
                seq_list.append(seq)
                seq = ''
                header_counter += 1
            elif '>' not in i and i != contents[-1] :
                seq += i
            elif '>' not in i and i == contents[-1]:
                seq += i
                seq_list.append(seq)
        else:
            print('contents is a empty list.')


    print(contents)
    print(header_list)
    print(seq_list)
    print(seq)
