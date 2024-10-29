n = int(input())
count = 0
end_value = 666

while True:
    if '666' in str(end_value):
        count += 1
        if count == n:
            break
    end_value += 1
    
print(end_value)