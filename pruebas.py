import math
import sys

class pruebas:
    a = 8
    b = 33.54
    c = 'o'


    # res2 = pow(a, -1, int(b))
    # print(res2)

    try:
       c = 'o'
    except IndexError:
        print("Error on line {}".format(sys.exc_info()[-1].tb_lineno))
    suSeno2 = math.tan(b)
    res2 = pow(23, -1, int(3))
    wfwe = 10 % 97
    print('Su valor de Seno es:', res2)