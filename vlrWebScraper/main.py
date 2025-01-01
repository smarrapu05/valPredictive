import requests
from bs4 import BeautifulSoup
import pandas as pd

def findFirstDigit(arr):
    for k in range(0, len(arr)):
        if arr[k].isdigit():
            return k
    #print('notfound')
    return 0


def findFirstNonDigit(arr):
    for k in range(0, len(arr)):
        if not arr[k].isdigit() and arr[k] != '.':
            return k
    #print('notfound')
    return len(arr)


def removePreceding(arr):
    ind = 0
    for x in arr[:]:
        if not x.strip():
            arr.remove(x)
        else:
            ind = arr.index(x)
            break
    # print(ind)
    return ind


def getLineNumber(soup, element):
    htmlString = str(soup)
    return htmlString.find(element)

# arr = '45$'
# print(arr[len(arr)-1])
# print(findFirstNonDigit('45$'))

with open('links.txt') as file:
    links = [line.rstrip() for line in file]
finalTable = []
for link in links:
    r = requests.get(link)
    soup = BeautifulSoup(r.content, "html.parser")
    scoreWin = soup.find('span', {'class': 'match-header-vs-score-winner'})
    scoreLost = soup.find('span', {'class': 'match-header-vs-score-loser'})
    #print(str(scoreWin).splitlines()[0])
    #print(str(scoreLost))
    winnerLine = getLineNumber(soup, str(scoreWin).splitlines()[0])
    loserLine = getLineNumber(soup, str(scoreLost).splitlines()[0])
    if winnerLine < loserLine:
        winIndex = 2
    else:
        winIndex = 3
    for i in [2, 3]:
        table = soup.find_all('table', {'class': 'wf-table-inset mod-overview'})[i]
        rows = []
        for j, row in enumerate(table.find_all('tr')):
            if j != 0:
                rows.append([el.text.strip() for el in row.find_all('span', {'class': 'stats-sq'})])
        cleanData = [0] * 10

        for r in rows:
            # print(r)
            ind = removePreceding(r)
            r = r[ind:len(r) - 1]
            if len(r) > 10:
                r.pop(0)
            # print(r)
            cdi = 0
            for y in range(0, len(r)):
                if r[y] == '':
                    cleanData[cdi] = -1
                    cdi += 1
                elif y not in [4, 10]:
                    btr = r[y][findFirstDigit(r[y]):]
                    # print(str(cdi) + 'cdi')

                    # print(str(findFirstNonDigit(r[y])) + ':)')
                    # print(btr)

                    # if(btr == '7'):
                    #     print(btr[0:1])
                    if btr[0:findFirstNonDigit(btr)] != '':
                        #print(findFirstNonDigit(btr))
                        #print(btr[0:findFirstNonDigit(btr)])
                        cleanData[cdi] += int(btr[0:findFirstNonDigit(btr)])
                    else:
                        cleanData[cdi] = -1
                    cdi += 1
        if (i == winIndex):
            cleanData[9] = 1
        else:
            cleanData[9] = 0
        #print(cleanData)
        finalTable.append(cleanData)

df = pd.DataFrame(finalTable, columns=['ACS', 'KpR', 'DpR', 'ApR', 'KAST', 'ADR', 'HS', 'FK', 'FD', 'W/L'])
df.to_csv('data.csv', index=False)
