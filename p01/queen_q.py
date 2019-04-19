"""
你需要将8个皇后放在棋盘上,条件是任何一个
皇后都不能威胁其他皇后,即任何两个皇后都不能吃掉对方
"""

def conflict(state, nextX):
    """检查冲突"""
    nextY = len(state)
    for i in range(nextY):
        if abs(state[i] - nextX) in (0, nextY - i):
            return True
    return False

def queens(num=8, state=()):
    """如果只剩下最后一个皇后没有放好,就遍历所有可能的位置,并返回那些不会引发冲突的位置"""
    for pos in range(num):
        if not conflict(state, pos):
            if len(state) == num - 1:
                yield (pos,)
            else:
                for result in queens(num, state + (pos,)):
                    yield (pos,) + result

def prettyprint(solution):
    def line(pos, length=len(solution)):
        return '. ' * (pos) + 'X ' + '. ' * (length - pos - 1)

    for pos in solution:
        print(line(pos))

prettyprint(list(queens(5))[0])
print(list(queens(5)))