#写出数据库中连续三个相同的Num的值

# +----+-----+
# | Id | Num |
# +----+-----+
# | 1  |  1  |
# | 2  |  1  |
# | 3  |  1  |
# | 4  |  2  |
# | 5  |  1  |
# | 6  |  2  |
# | 7  |  2  |
# +----+-----+

# +-----------------+
# | ConsecutiveNums |
# +-----------------+
# | 1               |
# +-----------------+
"""select distinct l1.Num as ConsecutiveNums
from Logs l1,Logs l2,Logs l3
where
    l1.Id = l2.Id-1 and
    l2.Id = l3.Id-1 and
    l1.Num = l2.Num and
    l2.Num = l3.Num
"""