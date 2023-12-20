total=0
count=0
count1=0
def mean(num):
    total=sum(num)
    count=len(num)
    return (total/count)

def median(numbers):
    sorted_numbers = sorted(numbers)
    count1 = len(sorted_numbers)
    if count1 % 2 == 0:
        middle_index = count1 // 2
        return (sorted_numbers[middle_index - 1] + sorted_numbers[middle_index]) / 2
    else:
        middle_index = (count1 - 1) // 2
        return sorted_numbers[middle_index]

def mode1(lst):
    str1=''
    mode_list=[]
    freq_dict = {}
    for elem in lst:
        if elem in freq_dict:
            freq_dict[elem] += 1
        else:
            freq_dict[elem] = 1
    max_freq = max(freq_dict.values())
    for hm in freq_dict:
        if freq_dict[hm]==max_freq:
            mode_list.append(hm)
    for hm1 in mode_list:
        str1=str1+'  '+str(hm1)
    
    return str1    
