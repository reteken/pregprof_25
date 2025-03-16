import requests
from matplotlib import pyplot as plt
from numpy import dot
from numpy.linalg import norm
from mpl_toolkits import mplot3d
import numpy as np
import matplotlib.pyplot as plt


def getDifferentTitles(titles):
    while len(titles) < 16:
        response = requests.get("https://olimp.miet.ru/ppo_it/api")
        response_json = response.json()
        if response_json["message"]["data"] not in titles:
            titles.append(response_json["message"]["data"])

    return titles


import numpy as np
from numpy.linalg import norm


def cosineF(A, B):
    return np.dot(A, B) / (norm(A) * norm(B))


def findfirstTitleIdx(titles):
    for i, title in enumerate(titles):
        if (
            np.sum(getGran(title, "u")) == 255 * 64
            and np.sum(getGran(title, "l")) == 255 * 64
        ):
            return i


def getGran(a, type):
    if type == "r":  # right
        return a[:, 64 - 1]
    elif type == "l":  # left
        return a[:, 0]
    elif type == "u":  # up
        return a[0, :]
    elif type == "d":  # down
        return a[64 - 1, :]
    return None


def getIndexMaxLikly(resultMap, typeMain, mainArr, titles, typeNeed):
    mainGran = getGran(mainArr, typeMain)

    resCos = []
    for i in range(16):
        gr = getGran(titles[i], typeNeed)

        if checkIfHave(resultMap, i):
            continue

        if np.sum(gr) == 255 * 64:
            continue

        resCos.append(cosineF(mainGran, gr))

    resCos = np.array(resCos)
    idMax = np.argmax(resCos)

    return idMax


def checkIfHave(resultMap, idx):
    res = list(resultMap)
    for element in res:
        if idx in element:
            return True

    return False


def joinMap(titles, maxTitles=16):
    resultMap = np.full((4, 4), -1)

    firstTitleIdx = findfirstTitleIdx(titles)  # левый верхний
    resultMap[0][0] = firstTitleIdx

    # Первые 4 элемента
    currectArray = titles[firstTitleIdx]
    for i in range(1, 4):
        currectId = getIndexMaxLikly(resultMap, "r", currectArray, titles, "l")
        resultMap[0][i] = currectId
        currectArray = titles[currectId]

    currectId = getIndexMaxLikly(resultMap, "d", titles[firstTitleIdx], titles, "u")
    resultMap[1][0] = currectId

    currectArray = titles[firstTitleIdx]
    for i in range(1, 4):
        currectId = getIndexMaxLikly(resultMap, "r", currectArray, titles, "l")
        resultMap[1][i] = currectId
        currectArray = titles[currectId]

    currectId = getIndexMaxLikly(resultMap, "d", titles[firstTitleIdx], titles, "u")
    resultMap[2][0] = currectId

    currectArray = titles[firstTitleIdx]
    for i in range(1, 4):
        currectId = getIndexMaxLikly(resultMap, "r", currectArray, titles, "l")
        resultMap[2][i] = currectId
        currectArray = titles[currectId]

    currectId = getIndexMaxLikly(resultMap, "d", titles[firstTitleIdx], titles, "u")
    resultMap[3][0] = currectId

    currectArray = titles[firstTitleIdx]
    for i in range(1, 4):
        currectId = getIndexMaxLikly(resultMap, "r", currectArray, titles, "l")
        resultMap[3][i] = currectId
        currectArray = titles[currectId]

    print(titles[0], resultMap)

    new_array = np.zeros((256, 256))

    for i1 in range(4):
        for i2 in range(4):
            for i3 in range(64):
                for i4 in range(64):
                    new_array[i1 * i3][i2 * i4] = titles[resultMap[i1][i2]][i3][i4]

    return new_array


titles = []

titles = getDifferentTitles(titles)

new_array = joinMap(np.array(titles))


print(len(titles))

new_array = joinMap(np.array(titles))

nike = plt.figure(figsize=(20, 20))

x, y = [], []

for i in range(64):
    x.append(i)
    y.append(i)


plt.subplot(4, 4, 1)

for i in range(16):
    ax = plt.axes(projection="3d")

    ax.subplot(4, 4, i + 1)

    xgrid, ygrid = np.meshgrid(x, y)
    plt.scatter(
        xgrid,
        ygrid,
        new_array[i],
        c="g",
        s=5,
    )

plt.savefig("test.png")

plt.show()


for i in range(len(titles)):
    maxi = max(titles[i])
    for i in range(len(titles)):
        if titles[i] == maxi:
            titles[i] = 1
        else:
            titles[i] = 0

print(titles)
