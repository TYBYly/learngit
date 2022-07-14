import math
import Random
import threading

computation_budget = 1000
time_budget = 1


class MNode(object):
    def __init__(self, team_loc, turn):
        self.team_loc = team_loc  # 该节点代表的行棋方所在的方位
        self.turn = turn  # 该节点代表的行棋方式先手还是后手

        self.parents = []
        self.children = []

        self.vis = 0
        self.val = 0.0
        self.cnt = 0
        self.UCB = 0.0
        self.board = None

        self.update_path = []

    def get_ucb(self, vis_all):
        self.val = self.vis / self.cnt
        self.UCB = self.val + 2.0 * math.sqrt(2.0 * math.log(vis_all) / self.vis)

    def recall(self): #  恢复价值损失值
        self.val += loss_v

    def is_win(self, board): # 返回当前节点是否是赢家，返回值：True / False
        pass

    def is_end(self):
        pass

    def is_leaf(self): # 判断当前节点是否为叶节点
        pass

    def select(self): # PPMCTS 四个阶段中第一阶段：选择最值节点
        pass

    def expand(self):  # PPMCTS 第二阶段：扩展选中的最值节点
        pass

    def simulate(self):  # PPMCTS 第三阶段： 对扩展所有的节点jin
        board = self.board
        team_loc = self.team_loc
        while is_terminal(team_loc, board) is False:
            next_move = ran_simulate(board, turn, team_loc)
            board = move(next_move[0], next_move[1], board)
            team_loc = -team_loc
        return is_win(board)

    def update(self, res):
        node = self
        while is_root(node) is False:
            t = threading.current_thread()
            t.acquire()
            node.recall()
            node.cnt += res
            node.vis += 1
            t.release()
            t.acquire()
            node = node.parents[update_path[t]]
            node.recall()
            t.release()
            res = ~res
            node = node.parent




class ProNode(object):
    def __init__(self, dice):
        self.dice = dice
        self.p = 1 / 6
        self.parent = None
        self.children = []

    def reset_p(self, dice):  # 追踪父节点进行判断
        if not self.parent.parent and self.dice == dice:
            self.p = 1
        else:
            self.p = 0

    def set_tree(self, parent, children):
        self.parent = parent
        self.children = children

    def recall(self):
        self.p *= loss_p


def best_choice(node):
    t = []
    for i in node.children:
        t.append(node.children[i].val)
    return node.children[t.index(max(t))].board


class PPMCTS:  # PPMCTS树的数据结构
    def __init__(self):
        self.root = MNode()

    def PPMCTS(self):
        for i in range(computation_budget):
            self.root.select()
            self.root.expand()
            res = self.root.simulate()
            self.root.update(res)
        new_board = best_choice(node)
        return new_board
