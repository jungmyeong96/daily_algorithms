
target = int(input())

idx = 1
route = 6
layer = 1

if (target == 1):
    print(layer)
else:
    layer += 1
    while route * idx < target - 1:
        idx += layer
        layer += 1
    print (layer)