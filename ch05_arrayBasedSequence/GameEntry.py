class GameEntry:
    """
    存储游戏条目对象的姓名和分数
    """
    def __init__(self,name,score):
        self._name = name
        self._score = score

    def get_name(self):
        return self._name

    def get_score(self):
        return self._score

    def __str__(self):
        return '({0},{1})'.format(self._name,self._score)