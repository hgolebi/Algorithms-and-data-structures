from matplotlib import pyplot as plt

def draw_a_plot(x, N, KMP, KR):
    plt.suptitle("Searching - time complexity")
    plt.plot(x, N, marker='o', label="N")
    plt.plot(x, KMP, marker='o', label="KMP")
    plt.plot(x, KR, marker='o', label="KR")
    plt.legend(prop={'size':10})
    plt.ylabel("Measured time (s)")
    plt.xlabel("Number of executions")
    plt.savefig('searching_plot.png')
    plt.clf()
