"""
Arabic Buckwalter dictionnary
key: value => latin_letter: arabic_letter
"""
buckWalterArabic = {"'": "ء", "|": "آ", ">": "أ", "&": "ؤ", "<": "إ", "}": "ئ",
                    "A": "ا", "b": "ب", "p": "ة", "t": "ت",
                    "v": "ث", "j": "ج", "H": "ح", "x": "خ", "d": "د", "*": "ذ",
                    "r": "ر", "z": "ز", "s": "س", "$": "ش",
                    "S": "ص", "D": "ض", "T": "ط", "Z": "ظ", "E": "ع", "g": "غ",
                    "_": "ـ", "f": "ف", "q": "ق", "k": "ك",
                    "l": "ل", "m": "م", "n": "ن", "h": "ه", "w": "و", "Y": "ى",
                    "y": "ي", "F": "ً", "N": "ٌ", "K": "ٍ",
                    "~": "ّ", "o": "ْ", "u": "ُ", "a": "َ", "i": "ِ", "`": "ٰ",
                    "{": "ٱ", "^": "ٓ", "#": "ٔ", ":": "ۜ",
                    "@": "۟", '"': "۠", "[": "ۢ", ";": "ۣ", ",": "ۥ", ".": "ۦ",
                    "!": "ۨ", "-": "۪", "+": "۫", "%": "۬",
                    "]": "ۭ"}

"""
Latin Buckwalter dictionnary
key: value => arabic_letter: latin_letter
"""
buckWalterLatin = {"ء": "'", "آ": "|", "أ": ">", "ؤ": "&", "إ": "<", "ئ": "}",
                   "ا": "A", "ب": "b", "ة": "p", "ت": "t",
                   "ث": "v", "ج": "j", "ح": "H", "خ": "x", "د": "d", "ذ": "*",
                   "ر": "r", "ز": "z", "س": "s", "ش": "$",
                   "ص": "S", "ض": "D", "ط": "T", "ظ": "Z", "ع": "E", "غ": "g",
                   "ـ": "_", "ف": "f", "ق": "q", "ك": "k",
                   "ل": "l", "م": "m", "ن": "n", "ه": "h", "و": "w", "ى": "Y",
                   "ي": "y", "ً": "F", "ٌ": "N", "ٍ": "K",
                   "ّ": "~", "ْ": "o", "ُ": "u", "َ": "a", "ِ": "i", "ٰ": "`",
                   "ٱ": "{", "ٓ": "^", "ٔ": "#", "ۜ": ":",
                   "۟": "@", "۠": '"', "ۢ": "[", "ۣ": ";", "ۥ": ",", "ۦ": ".",
                   "ۨ": "!", "۪": "-", "۫": "+", "۬": "%",
                   "ۭ": "]"}

# list of letters without diacritics
buckWalterSansTashkil = ["'", "|", ">", "&", "<", "}", "A", "b", "p", "t", "v",
                         "j", "H", "x", "d", "*", "r",
                         "z", "s", "$", "S", "D", "T", "Z", "E", "g", "_", "f",
                         "q", "k", "l", "m", "n", "h",
                         "w", "Y", "y", "{"]

# unicode letters for using the URL of a referral site in the testing phase
buckWalterUnicode = {"'": 'C1', '|': 'C2', '>': 'C3', '&': 'C4', '<': 'C5',
                     '}': 'C6', 'A': 'C7', 'b': 'C8', 'p': 'C9',
                     't': 'CA', 'v': 'CB', 'j': 'CC', 'H': 'CD', 'x': 'CE',
                     'd': 'CF', '*': 'D0', 'r': 'D1', 'z': 'D2',
                     's': 'D3', '$': 'D4', 'S': 'D5', 'D': 'D6', 'T': 'D8',
                     'Z': 'D9', 'E': 'DA', 'g': 'DB', '_': 'DC',
                     'f': 'DD', 'q': 'DE', 'k': 'DF', 'l': 'E1', 'm': 'E3',
                     'n': 'E4', 'h': 'E5', 'w': 'E6', 'Y': 'EC',
                     'y': 'ED', 'F': 'F0', 'N': 'F1', 'K': 'F2', 'a': 'F3',
                     'u': 'F5', 'i': 'F6', '~': 'F8', 'o': 'FA',
                     'P': '81', 'J': '8D', 'V': ' ', 'G': '90'}


def translit_to_arab(text_latin):
    """
    transliterate Latin text into Arabic used buckwalter dictionnary
    :param text_latin: text in latin letters
    :return: text arabic
    """
    list_text_latin = text_latin.strip().split()
    text_arab = ""
    for word in list_text_latin:
        text_arab = text_arab + ''.join(
            [buckWalterArabic[letter] for letter in word]) + ' '
    return text_arab[:-1]


def translit_to_latin(text_arab):
    """
    transliterate arabic text into latin used buckwalter dictionnary
    :param text_arab: text in arab letters
    :return: text latin
    """
    list_text_arab = text_arab.strip().split()
    text_latin = ""
    for word in list_text_arab:
        text_latin = text_latin + ''.join(
            [buckWalterLatin[letter] for letter in word]) + ' '
    return text_latin[:-1]


# enlever les diacritiques dans le cas où le texte en contient
def normalize_text_latin(text_latin):
    """
    remove diacritics if the text contains them
    :param text_latin: text in latin letter
    :return: latin text without diacritics letters
    """
    text_without_tashkil = ' '.join(
        [''.join([letter for letter in word if letter in buckWalterSansTashkil])
         for word in text_latin.split()])
    text = ""
    for letter in text_without_tashkil:
        # if you find "Alif + Maddah" or
        # "Alif + HamzatWasl" then you have to put "Alif"
        if letter in ["|", "{"]:
            letter = "A"
        text += letter

    return text


def normalize_text_arab(text_arab):
    """
    remove diacritics if the text contains them
    :param text_arab: text in arabic letters
    :return: arabic text without diacritics letters
    """
    return translit_to_arab(normalize_text_latin(translit_to_latin(text_arab)))


def is_arabic(text: str):
    """
    Detect text if arabic
    :param text: text string
    :return: boolean value
    """
    for word in text.strip().split():
        for letter in word:
            if letter not in buckWalterLatin.keys():
                return False
    return True


def is_latin(text: str):
    """
    Detect text if latin
    :param text: text string
    :return: boolean value
    """
    for word in text.strip().split():
        for letter in word:
            if letter not in buckWalterArabic.keys():
                return False
    return True


def unicode_text_latin(text_latin):
    """
    Transform latin text to unicode text
    :param text_latin:
    :return: unicode text
    """
    text = normalize_text_latin(text_latin)
    return ''.join(['%' + buckWalterUnicode[letter] for letter in text if
                    letter in buckWalterUnicode.keys()])
