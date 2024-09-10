def intToStr(i):
    digits = '0123456789'

    if i == 0:
        return "0"
    
    results = ""
    while i>0 :
        results = digits[i%10] + results
        i= i//10
    return results

print(intToStr(764))

#Time complexity of O(log(n))