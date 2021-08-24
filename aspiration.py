from urllib.request import urlopen
import re
import html
import pickle
from collections import defaultdict

pattern1 = r"<td class=\"at\">.+?</td>\s+<td>.+?</td>\s+<td>.+?</td>"
pattern2 = r'<td class="at">.+?<a.+?>(.+?)</a>.+?<td>(.+?)</td>'
index_lemmas = defaultdict(int)

for i in range(1, 75):
    pageCode = urlopen(
        "http://corpus.quran.com/lemmas.jsp?page=%d&sort=2" % i).read().decode(
        'utf-8')
    index = re.findall(pattern1, pageCode)
    for ind in index:
        strr = re.search(pattern2, ind, re.DOTALL)
        index_lemmas[html.unescape(strr.group(1))] = int(strr.group(2))

with open('data/index_lemmas.pik', 'wb') as w:
    pickle.dump(index_lemmas, w)
