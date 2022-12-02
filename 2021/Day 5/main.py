from pull2021 import AocInteraction
import matplotlib.pyplot as plt
import csv
import numpy as np
import pandas as pd
import seaborn as sns
from scipy.sparse import csr_matrix, coo_array, coo_matrix


def part_1(advent_of_code):
    row = []
    col = []
    data = []
    with open('input.txt', 'r') as input_file:
        entries = []
        for line in input_file:
            s = line.replace(" -> ", ",")
            coords = list(map(int, s.strip().split(",")))
            if coords[0] == coords[2]:
                x = coords[0]
                for y in range(min(coords[1],coords[3]), max(coords[1],coords[3])+1):
                    row.append(x)
                    col.append(y)
                    data.append(1)
            elif coords[1] == coords[3]:
                y = coords[1]
                for x in range(min(coords[0],coords[2]), max(coords[0],coords[2])+1):
                    row.append(x)
                    col.append(y)
                    data.append(1)
            # else:
            #     xstep = 1
            #     ystep = 1
            #     if coords[0] > coords[2]:
            #         xstep = -1
            #     if coords[1] > coords[3]:
            #         ystep = -1
            #     x_range = iter(range(coords[0], coords[2]+1, xstep))
            #     y_range = iter(range(coords[1], coords[3]+1, ystep))
            #     for x in range(0, abs(coords[0]-coords[2])):
            #             row.append(next(x_range))
            #             col.append(next(y_range))
            #             data.append(1)

        csr = coo_array((np.array(data), (np.array(row), np.array(col))), shape=(max(row)+1, max(col)+1)).tocsr()
        nnz_inds = csr.nonzero()
        keep = np.where(csr.data != 1)[0]
        n_keep = len(keep)
        b = csr_matrix((np.ones(n_keep), (nnz_inds[0][keep], nnz_inds[1][keep])), shape=csr.shape)

        b.count_nonzero()
        print(b.todense())

        advent_of_code.answer(1, b.count_nonzero())


def part_2(advent_of_code):
    row = []
    col = []
    data = []
    with open('input.txt', 'r') as input_file:
        entries = []
        for line in input_file:
            s = line.replace(" -> ", ",")
            coords = list(map(int, s.strip().split(",")))
            if coords[0] == coords[2]:
                x = coords[0]
                for y in range(min(coords[1], coords[3]), max(coords[1], coords[3]) + 1):
                    row.append(x)
                    col.append(y)
                    data.append(1)
            elif coords[1] == coords[3]:
                y = coords[1]
                for x in range(min(coords[0], coords[2]), max(coords[0], coords[2]) + 1):
                    row.append(x)
                    col.append(y)
                    data.append(1)
            else:
                xstep = 1
                ystep = 1
                if coords[0] > coords[2]:
                    xstep = -1
                if coords[1] > coords[3]:
                    ystep = -1
                x_range = range(coords[0], coords[2] + xstep, xstep)
                y_range = range(coords[1], coords[3] + ystep, ystep)
                for x in range(0, len(x_range)):
                    row.append(x_range[x])
                    col.append(y_range[x])
                    data.append(1)

        coo = coo_matrix((np.array(data), (np.array(row), np.array(col))), shape=(max(row) + 1, max(col) + 1))
        csr = coo.tocsr()
        nnz_inds = csr.nonzero()
        keep = np.where(csr.data != 1)[0]
        n_keep = len(keep)
        b = csr_matrix((np.ones(n_keep), (nnz_inds[0][keep], nnz_inds[1][keep])), shape=csr.shape).tocoo()

        df = pd.DataFrame({'x': coo.row,
                           'y': coo.col,
                           'value': coo.data})
        dfOverlap = pd.DataFrame({'x': b.row,
                           'y': b.col,
                           'value': b.data})

        # plot
        pl = sns.scatterplot(data=df, x="x", y="y", s=0.5, alpha=0.5)
        pl.scatter(data=dfOverlap, x="x", y="y", label="overlap", s=0.25, alpha=0.75)
        plt.gcf().set_dpi(300)
        pl.invert_yaxis()
        pl.xaxis.tick_top()
        pl.xaxis.set_label_position("top")
        plt.show()


        print(b.todense())
        advent_of_code.answer(2, b.count_nonzero())


if __name__ == "__main__":
    aoc_interaction = AocInteraction()
    part_1(aoc_interaction)
    part_2(aoc_interaction)
