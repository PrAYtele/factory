def a(nums1,nums2):
    array = []
    count1 = 0
    flag = 0
    count2 = 0
    i = 0
    while len(array)<((len(nums1)+len(nums2))):
        array.append(min(nums1[count1],nums2[count2]))
        if nums1[count1]>nums2[count2] and count2 <len(nums2):
            count2 += 1
        elif nums1[count1] <= nums2[count2] and count1<len(nums1):
            count1 += 1
        if count1 == len(nums1) or count2 == len(nums2):

        if len(nums1) != len(nums2) or (len(array) == (len(nums1)+len(nums2)-1)):
            if count1 == len(nums1)  and flag ==0:
                j = i
                while j<(len(nums1)+len(nums2)):
                    array.append(nums2[count2])
                    j+=1
                    flag=1
                    count2+=1
            if count2 == len(nums2)  and flag == 0:
                j = i
                while j<(len(nums1)+len(nums2)):
                    array.append(nums1[count1])
                    j+=1
                    flag = 1
        i+=1
    print(array)
    half = (len(nums1)+len(nums2))//2
    result = (array[half]+array[~half])/2
    return result
print(a([1,2],[3,4]))
