"""
1.九宫格
1至9九个数字，横竖都有3个格，思考怎么使每行、每列和对角线上的三数之和都等于15

"""
import itertools

all_rows = list(itertools.permutations(range(1, 10), r=3))

for i in range(len(all_rows)):
    row1_1 = all_rows[i][0]
    row1_2 = all_rows[i][1]
    row1_3 = all_rows[i][2]

    row1 = all_rows[i]
    if sum(row1) == 15:
        for j in range(len(all_rows)):
            row2_1 = all_rows[j][0]
            row2_2 = all_rows[j][1]
            row2_3 = all_rows[j][2]

            row2 = all_rows[j]
            if sum(row2) == 15:
                for t in range(len(all_rows)):
                    row3_1 = all_rows[t][0]
                    row3_2 = all_rows[t][1]
                    row3_3 = all_rows[t][2]
                    row3 = all_rows[t]
                    if sum(row3) == 15:
                        if len(set(row1) & set(row2)) == 0 and len(set(row2) & set(row3)) == 0 and len(
                            set(row1) & set(row3)) == 0:
                            if row1_1+row2_1+row3_1==15 and row1_2+row2_2+row3_2==15 and row1_3+row2_3+row3_3==15:
                                if row1_1+row2_2+row3_3==15 and row1_3+row2_2+row3_1==15:
                                    print(row1)
                                    print(row2)
                                    print(row3)
                                    print('=================')