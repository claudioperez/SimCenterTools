import matplotlib.pyplot as plt
import itertools
import numpy as np

def plot_confusion_matrix(cm, classes,
                          normalize=False,
                          title=None,
                          cmap=plt.cm.Blues,
                          ax=None,
                          xlabel='True label',
                          ylabel='Predicted label',
                          prec=2,rotation=0
):
    
    if not ax:
        fig, ax = plt.subplots()
    else:
        fig = ax.figure

    ax.matshow(cm, interpolation='nearest', cmap=cmap)
    if title:
        ax.set_title(title)

#     fig.colorbar()
#     tick_marks = np.arange(len(classes))
#     ax.set_xticklabels(tick_marks, classes, rotation=0)
#     ax.set_yticklabels(tick_marks, classes)
#     ax.set_xticklabels(classes, rotation=0)
#     ax.set_yticklabels(classes)


    thresh = cm.max() / 2.
    for i, j in itertools.product(range(cm.shape[0]), range(cm.shape[1])):
        ax.text(j, i, round(cm[i, j],prec),
                 horizontalalignment="center",
                 color="white" if cm[i, j] > thresh else "black")

    fig.tight_layout()
#     ax.set_ylabel(ylabel, fontsize=12)
#     ax.set_xlabel(xlabel, fontsize=12)
    ax.grid(b=None)
    ax.set_xlabel("Prediction")
    return ax
#     ax.set_xticklabel()
#     ax.set_yticks(fontsize=10)
#     ax.set_setp(ax.get_xticklabels(), rotation=rotation, ha="right", rotation_mode="anchor")
