def solution(T):
    # Convert the string temperature to a float
    temperature = float(T)
    
    # Determine the temperature state
    if temperature < 35.0:
        # Temperature below 35.0 degrees C indicates hypothermia
        return "hypothermia"
    elif 35.0 <= temperature <= 37.5:
        # Temperature between 35.0 and 37.5 degrees C indicates normal body temperature
        return "normal"
    elif 37.6 <= temperature <= 40.0:
        # Temperature between 37.6 and 40.0 degrees C indicates fever
        return "fever"
    else:  # temperature > 40.0
        # Temperature above 40.0 degrees C indicates hyperpyrexia
        return "hyperpyrexia"

# Test cases
print(solution("34.5"))  # Expected output: "hypothermia"
print(solution("36.5"))  # Expected output: "normal"
print(solution("38.0"))  # Expected output: "fever"
print(solution("40.5"))  # Expected output: "hyperpyrexia"
