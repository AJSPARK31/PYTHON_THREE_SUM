#!/usr/bin/env python
# coding: utf-8

# In[26]:


# 15. 3Sum
# Given an integer array nums, return all the triplets [nums[i], nums[j], nums[k]] such that i != j, i != k, and j != k, and nums[i] + nums[j] + nums[k] == 0.

# Notice that the solution set must not contain duplicate triplets.

 

# Example 1:

# Input: nums = [-1,0,1,2,-1,-4]
l=[]
# Output: [[-1,-1,2],[-1,0,1]]
# Explanation: 
# nums[0] + nums[1] + nums[2] = (-1) + 0 + 1 = 0.
# nums[1] + nums[2] + nums[4] = 0 + 1 + (-1) = 0.
# nums[0] + nums[3] + nums[4] = (-1) + 2 + (-1) = 0.
# The distinct triplets are [-1,0,1] and [-1,-1,2].
# Notice that the order of the output and the order of the triplets does not matter.
nums = [-3,1,-5,-1,0,-1,3,-4,1,2,-1,-1,-4,-4]
l=[]
for i in range(len(nums)):
    for j in range(i+1,len(nums)):
        for k in range(j+1,len(nums)):
            if nums[i]+nums[j]+nums[k]==0:
                l.append([nums[i],nums[j],nums[k]])

res = list(set(tuple(sorted(sub)) for sub in l))
result_list=[]
for i in res:
    x=list(i)
    result_list.append(x)

    
print(result_list)


# In[28]:


nums=[-3,1,-5,-1,0,-1,3,-4,1,2,-1,-1,-4,-4]
l=[]
nums_sorted=sorted(nums)
for i in range(len(nums_sorted)-2):
    if i>0 and nums_sorted[i]==nums_sorted[i-1]:
        continue
    j,k=i+1,len(nums_sorted)-1
    while j<k:
        total=nums_sorted[i]+nums_sorted[j]+nums_sorted[k]
        if total<0:
            j+=1
        elif total>0:
            k-=1
        else:
            l.append([nums_sorted[i],nums_sorted[j],nums_sorted[k]])
            while j < k and nums[j] == nums[j+1]:
                    j += 1
            while j < k and nums[k] == nums[k-1]:
                    k -= 1
            j += 1
            k -= 1

print(result)


# In[31]:





# In[ ]:




