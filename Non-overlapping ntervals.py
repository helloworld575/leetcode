# leetcode 435. Non-overlapping Intervals
# Definition for an interval.
# class Interval:
#     def __init__(self, s=0, e=0):
#         self.start = s
#         self.end = e

class Solution:
    def eraseOverlapIntervals(self, intervals):
        """
        :type intervals: List[Interval]
        :rtype: int
        """
        # 有至少一种情况没思考到
        # if not intervals:
        #     return 0
        # sorted_intervals = sorted(intervals,key=lambda x:x.end-x.start)
        # ans = 0
        # ans_list = [sorted_intervals[0]]
        # for i in range(1,len(sorted_intervals)):
        #     flag = True
        #     for j in range(len(ans_list)):
        #         if (sorted_intervals[i].start<ans_list[j].start and sorted_intervals[i].end>ans_list[j].start) or (sorted_intervals[i].start<ans_list[j].end and sorted_intervals[i].end>ans_list[j].end) or (sorted_intervals[i].start==ans_list[j].start and sorted_intervals[i].end==ans_list[j].end):
        #             flag = False
        #             break
        #     if flag:
        #         ans_list.append(sorted_intervals[i])
        #     else:
        #         ans+=1
        # return ans

        # 正确答案如下，但为什么仅按结束时间排序可行呢？
        if len(intervals) == 0:
            return 0

        remove_count = 0

        sorted_intervals = sorted(intervals, key=lambda x: x.end)
        last = sorted_intervals[0]

        for interval in sorted_intervals[1:]:

            if interval.start < last.end:
                remove_count += 1
            else:
                last = interval

        return remove_count
