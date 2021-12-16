from matplotlib import pyplot as plt

def draw_a_plot(x, y_2_ary, y_3_ary, y_4_ary, y_binary=None, operation="creating"):
    # operation: choose one from ["deleting root", "creating"]
    plt.suptitle("Heaps - time complexity of " + operation.upper())
    plt.plot(x, y_2_ary, marker='o', label="2-ary")
    plt.plot(x, y_3_ary, marker='o', label="3-ary")
    plt.plot(x, y_4_ary, marker='o', label="4-ary")
    if y_binary:
        plt.plot(x, y_binary, marker='o', label="binary")
    plt.legend(prop={'size':10})
    plt.ylabel("Measured time (s)")
    plt.xlabel("Number of executions")
    plt.savefig(operation+'.png')
    plt.clf()
