my_list = [
  [1, 3, 6, 11],
  [4, 2, 4],
  [9, 17, 16, 0],
]

outer = 0

while outer < len(my_list):
    inner = 0 
    while inner  < len(my_list[outer]):
        num = my_list[outer][inner]
        if num % 2 == 0:
            print(num)
        inner += 1
    outer += 1