from matplotlib import pyplot as plt

def draw_a_plot(x_bst, x_avl, y, operation):
    # operation: choose one from ["deleting", "creating", "searching"]
    plt.plot(x_bst, y, marker='o', label="BST")
    plt.suptitle("BST & AVL - time complexity of "+operation.upper())
    plt.plot(x_avl, y, marker='o', label="AVL")
    plt.legend(prop={'size':9})
    plt.ylabel("Measured time (s)")
    plt.xlabel("Number of elements")
    plt.savefig(operation+'.png')
    plt.clf()