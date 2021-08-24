import re
from collections import defaultdict
from transliteration import normalize_text_latin
from PyQt5 import QtWidgets
import pickle


def save_index_data_quran_buckwalter(data, to_txt: bool = True):
    """
    Save the index of quran generated to pik file
        and generate a text view of data if needed
    mapping the data of  to index data of quran
    :param data: data from 'quranic-corpus-morphology'
    :param to_txt: save data to txt for viewing
    :return: None
    """
    # import pickle

    with open('data/index_quran_buckwalter.pik', 'wb') as w:
        pickle.dump(data, w)

    if to_txt:
        with open('data/index_quran_buckwalter.txt', 'w') as w:
            w.write('souratNum:versetNum:wordPosition : WORDTashkilLatin | '
                    'WORDNoTashkilLatin | LEME | ROOT \n\n')
            for key in sorted(data.keys()):
                QtWidgets.QApplication.processEvents()
                w.write(key + " : " + data[key][0] + ' | ' + data[key][1])
                if data[key][2] != '':
                    w.write(" | " + data[key][2])
                    if data[key][3] != '':
                        w.write(" | " + data[key][3] + '\n')
                    else:
                        w.write('\n')
                else:
                    w.write('\n')


def load_data_index_quran_buckwalter():
    data = {}
    try:
        with open('data/index_quran_buckwalter.pik', 'rb') as r:
            data = pickle.load(r)
    except FileNotFoundError:
        pass
    return data


def load_sourats_names():
    with open('data/sourats.txt', 'r', encoding="utf-8") as file:
        data = file.read().splitlines()

    return data


def generate_index_quran_buckwalter(start, end, frame):
    """
    Generate Quran index of application
    :param start: start from num of sourat [1 .. 114]
    :param end: end from num of sourat [1 .. 114] and end >= start
    :param frame: the visible window
    :return: None
    """
    index_quran_buckwalter = defaultdict(list)
    sourats_names = load_sourats_names()
    with open('data/quranic-corpus-morphology-0.4.txt', 'r') as file:
        line = file.readline()
        while line != '' and not line.startswith("(" + str(start)):
            QtWidgets.QApplication.processEvents()
            line = file.readline()
        """
        reg pattern expression:
        for each line, extract a group of:
        1- num of sourat
        2- num of verset
        3- position of word in verset
        4- a part of word in verset
        5- word
        8- lemme of word if exist
        11- root of word if exist
        """
        pattern = r'\((.+?):(.+?):(.+?):(.+?)\)\t(|.+?)\t' \
                  r'(.+?(LEM:(.+?)\|((ROOT:(.+?)\|)|.+))|.+)'
        while line.strip() != '' and not line.startswith('(' + str(end + 1)):
            QtWidgets.QApplication.processEvents()
            index = re.search(pattern, line)
            frame.label.setText(
                'Generate ' + sourats_names[int(index.group(1)) - 1] + '...')
            """
            the format of key : n1:n2:n3 :
            n1 : number of 3 digits of sourat number ex : Elbaqara 002
            n2 : number of 3 digits of sourat verset
            n3 : number of 3 digits of word position in verset
            """
            key = "{0:0>3}".format(int(index.group(1))) + ':' + \
                  "{0:0>3}".format(int(index.group(2))) + ':' + \
                  "{0:0>3}".format(int(index.group(3)))
            if key in index_quran_buckwalter.keys():
                index_quran_buckwalter[key][0] += index.group(5)
                index_quran_buckwalter[key][1] += normalize_text_latin(
                    index.group(5))
            else:
                index_quran_buckwalter[key] = [
                    index.group(5),
                    normalize_text_latin(index.group(5)), '', '']
            if index.group(8) is not None:
                index_quran_buckwalter[key][2] = index.group(8)
            if index.group(11) is not None:
                index_quran_buckwalter[key][3] = index.group(11)
            line = file.readline()

    frame.label.setText("Save Quran index...")
    save_index_data_quran_buckwalter(index_quran_buckwalter)


def save_data_index_ahkaam_encoding(data):
    with open('data/index_ahkaam_encoding.pik', 'wb') as w:
        pickle.dump(data, w)


def load_data_index_ahkaam_encoding():
    data = {}
    try:
        with open('data/index_ahkaam_encoding.pik', 'rb') as r:
            data = pickle.load(r)
    except FileNotFoundError:
        pass
    return data


def generate_index_ahkaam_encoding(start, end, frame):
    """
    Generate Quran's Ahkam index of application
    :param start: start from num of sourat [1 .. 114]
    :param end: end from num of sourat [1 .. 114] and end >= start
    :param frame: the visible window
    :return: None
    """

    sourats_names = load_sourats_names()
    start = int(start)
    end = int(end)
    index_quran_ahkaam_encoding = defaultdict(list)
    with open('data/ahkaam_encoding.txt', 'r') as file:
        ahkaams = file.read()
    """
    Ahkaam regex expression:
    n1(n2:n3)
    n1: ahkaam encoding
    n2: sourat num
    n3: verset num of sourat    
    """
    pattern = r'(.+?)\((.+?):(.+?)\)'
    index = re.findall(pattern, ahkaams)
    for encode, num_sourat, num_verset in index:
        QtWidgets.QApplication.processEvents()
        frame.label.setText(
            'Generate ' + sourats_names[int(num_sourat) - 1] + '...')
        if num_sourat != '1' and num_verset == '1':
            encode = encode[12:]
        if int(num_sourat) in range(start, end + 1):
            index_quran_ahkaam_encoding[
                "{0:0>3}".format(int(num_sourat))].append(encode)
    frame.label.setText("Save Ahkaam idnex...")
    save_data_index_ahkaam_encoding(index_quran_ahkaam_encoding)
