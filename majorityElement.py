def majorityElement(nums):
        # Dictionary to store the count of each element in 'nums'
        dic = {}
        
        # Iterate over the elements in 'nums'
        for num in nums:
            # Check if the element is already in the dictionary
            if num in dic.keys():
                # If yes, increment the count
                dic[num] += 1
            else:
                # If not, add the element to the dictionary with count 1
                dic[num] = 1

        # Initialize variables to find the element with the maximum count
        max_k = 0
        count = None
        
        # Iterate over the keys in the dictionary
        for key in dic.keys():
            # Check if the count of the current element is greater than the current max count
            if dic[key] > max_k:
                # If yes, update the max count and the majority element
                max_k = dic[key]
                count = key

        # Return the majority element found
        return count

        # for key in dic.keys():
        #         # Check if the count of the current element is equal to the maximum count in the dictionary
        #         if dic[key] == max(list(dic.values())):
        #             # If yes, return the element as it is the majority element
        #             return key

# Example usage
nums_list = [1, 2, 2, 3, 2, 4, 2, 2, 5]

result = majorityElement(nums_list)

if result is not None:
    print(f'The majority element is: {result}')
else:
    print('No majority element found in the list.')
