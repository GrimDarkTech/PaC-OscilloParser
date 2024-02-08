

#mathematical_expectation - мат. ожидание
#square_deviation - сред. квадрат. откл.

def Cut(values:list,mathematical_expectation:float,square_deviation:float) -> list:
    indexs = []
    for i in range (0, len(values)):
        if values[i] > mathematical_expectation + square_deviation or values[i] < mathematical_expectation - square_deviation:
            indexs.append(i)
    for i in range (0, len(indexs)):
        if indexs[1]-indexs[0] > 5:
            indexs.pop(0)
    cutVelues = []
    for i in range (indexs[0], indexs[len(indexs)-1]):
        cutVelues.append(values[i])
    return cutVelues