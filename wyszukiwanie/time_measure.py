import gc
import time
import algorytm_naiwny
import algorytm_KMP
import algorytm_KR

def get_time(txt, pattern_list, algorithm, rep):
    '''

    argument algorithm wyznacza, ktorego algorytmu uzyc do pomiaru:
    'N' = algorytm naiwny
    'KMP' = algorytm Knutha-Morrisa-Pratta
    'KR' = algorytm Karpa-Rabina

    '''
    times = 0

    # algorytm naiwny
    if algorithm == 'N':
        for i in range(rep):
            gc_old = gc.isenabled()
            gc.disable()
            start = time.process_time()
            for elem in pattern_list:
                algorytm_naiwny.find(elem, txt)
            stop = time.process_time()
            gc.enable()
            times += stop - start

    # algorytm KMP
    elif algorithm == 'KMP':
        for i in range(rep):
            gc_old = gc.isenabled()
            gc.disable()
            start = time.process_time()
            for elem in pattern_list:
                algorytm_KMP.KMP_find(elem, txt)
            stop = time.process_time()
            gc.enable()
            times += stop - start

    # algorytm KR
    elif algorithm == 'KR':
        for i in range(rep):
            gc_old = gc.isenabled()
            gc.disable()
            start = time.process_time()
            for elem in pattern_list:
                algorytm_KR.find(elem, txt)
            stop = time.process_time()
            gc.enable()
            times += stop - start
    else:
        raise ValueError

    return times/rep