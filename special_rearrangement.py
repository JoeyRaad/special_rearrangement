
def special_rearrangement(nums):

    #create lists for both to store numbers in it
    even, odd=[], []
    
    for i in nums:
        #if modulus by 2 then even otherwise number is odd
        if i%2 == 0:
            #add index i to even list 
            even.append(i)
        else:
            odd.append(i)

        #sort both to relative sequence
        even.sort(), odd.sort()
    return even + odd


nums =[3, 1, 4, 2, 7, 5, 6]
print(special_rearrangement(nums))