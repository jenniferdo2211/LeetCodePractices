import heapq

class Solution1WithHeap:
    def minMeetingRooms(self, intervals: List[List[int]]) -> int:
        if not intervals:
            return 0
        
        if len(intervals) == 1:
            return 1
        
        START_INDEX = 0
        END_INDEX = 1
        
        intervals.sort(key=lambda x: x[START_INDEX])
        
        count = 1
        endingsHeap = [intervals[0][END_INDEX]]        
        
        for meeting in intervals[1:]:
            if endingsHeap[0] <= meeting[START_INDEX]:
                heapq.heappop(endingsHeap)
            
            heapq.heappush(endingsHeap, meeting[END_INDEX])
        
        return len(endingsHeap)

class Solution2WithArray:
    def minMeetingRooms(self, intervals: List[List[int]]) -> int:
        if not intervals:
            return 0
        
        if len(intervals) == 1:
            return 1
        
        START_INDEX = 0
        END_INDEX = 1
        starts = [meeting[START_INDEX] for meeting in intervals]
        ends = [meeting[END_INDEX] for meeting in intervals]
        starts.sort()
        ends.sort()
        
        end_index = 0
        count = 0
        
        for start in starts:
            if start < ends[end_index]:
                count += 1
                continue
            
            if start >= ends[end_index]:
                end_index += 1
                
        return count    