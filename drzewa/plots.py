from matplotlib import pyplot as plt

def draw_a_plot(x, y_bst, y_avl, operation):
    # operation: choose one from ["deleting", "creating", "searching"]
    plt.plot(x, y_bst, marker='o', label="BST")
    plt.suptitle("BST & AVL - time complexity of "+operation.upper())
    plt.plot(x, y_avl, marker='o', label="AVL")
    plt.legend(prop={'size':9})
    plt.ylabel("Measured time (s)")
    plt.xlabel("Number of elements")
    plt.savefig(operation+'.png')
    plt.clf()