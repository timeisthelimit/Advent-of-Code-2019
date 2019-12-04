count=0

for value in range(245182, 790572):
        value_as_str = (str(value).zfill(6))
        if value_as_str[0] <= value_as_str[1] and value_as_str[1] <= value_as_str[2] and value_as_str[2] <= value_as_str[3] and value_as_str[3] <= value_as_str[4] and value_as_str[4] <= value_as_str[5]:
            if value_as_str[0] == value_as_str[1] or value_as_str[1] == value_as_str[2] or value_as_str[2] == value_as_str[3] or value_as_str[3] == value_as_str[4] or value_as_str[4] == value_as_str[5]:
                print(value_as_str)
                count+=1

print(count)
