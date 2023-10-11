class Solution:
    def fullBloomFlowers(self, flowers: List[List[int]], people: List[int]) -> List[int]:
        start_list, end_list = [], []
        for start, end in flowers:
            start_list.append(start)
            end_list.append(end)

        start_list.sort()
        end_list.sort()
        print(start_list,end_list)

        def binary_search(low, high, arr, person, flag):
            best_idx = -1
            while low < high:
                mid =(low + high) // 2
                midval = arr[mid]
                #best_val = midval
                #print(person, arr[mid],low, high)
                if flag == "right":
                    if person >= midval:
                    
                        low = mid + 1
                    elif person < midval:
                        high = mid
                else:
                 
                    if person > midval:
                    
                        low = mid + 1
                    elif person <= midval:
                        high = mid
                
            
            return low

        res = []
        for person in people:
            start_idx = binary_search(0, len(start_list),start_list,person, "right")

            end_idx = binary_search(0, len(end_list),end_list,person,"left")
            #print(start_idx, end_idx)
            #print(abs(start_idx- end_idx))
            res.append(abs(start_idx-end_idx))


        return res



        
                    


        