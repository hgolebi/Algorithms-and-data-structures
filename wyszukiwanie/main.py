# import algorytm_KR as KR
# import algorytm_KMP as KMP
# import algorytm_naiwny as N
from read_file import get_string
from time_measure import get_time
from drawing_plots import draw_a_plot

whole_txt = get_string("pan-tadeusz.txt")
naive_times = []
KR_times = []
KMP_times = []
checkpoints = [i for i in range(1, 11, 1)]

for i in checkpoints:

    pattern_list = whole_txt.split(maxsplit=i)
    pattern_list.pop()
    naive_times.append(get_time(whole_txt, pattern_list, "N", 1))
    KR_times.append(get_time(whole_txt, pattern_list, "KR", 1))
    KMP_times.append(get_time(whole_txt, pattern_list, "KMP", 1))
    print("iteration: "+str(i))


draw_a_plot(checkpoints, naive_times, KMP_times, KR_times)

# timen = get_time(whole_txt, ["Z radoscia zwaza dziecka zywosc i urode"], "N", 1)
# timekmp = get_time(whole_txt, ["Z radoscia zwaza dziecka zywosc i urode"], "KMP", 1)
# timekr = get_time(whole_txt, ["Z radoscia zwaza dziecka zywosc i urode"], "KR", 1)
# print("KR: "+str(timekr)+" KMP: "+str(timekmp)+" nainwy: "+str(timen))

