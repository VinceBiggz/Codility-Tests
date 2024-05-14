def solution(A):
    # Initialize the sum of positive integers
    positive_sum = 0
    
    # Counter for the number of positive integers found
    count = 0
    
    # Iterate through the array
    for number in A:
        # Check if the number is positive
        if number > 0:
            # Add the positive number to the sum
            positive_sum += number
            # Increment the count of positive numbers found
            count += 1
            
            # If we've found three positive integers, break out of the loop
            if count == 3:
                break
    
    # Return the sum of the first three positive integers
    return positive_sum

# Test cases
print(solution([4, -2, 0, 5, -2, 1, 6]))  # Expected output: 10
print(solution([3, -2, 0]))              # Expected output: 3
print(solution([-9, -4, -2, -6]))        # Expected output: 0
