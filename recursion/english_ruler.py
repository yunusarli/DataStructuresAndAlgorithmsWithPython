"""
Drawing an english ruler
---- 0 (start point)
-
--
-
---
-
--
-
----1

"""



def draw_line(thick,label=""):
    stick = "-"*thick
    if label:
        stick += label
    print(stick)

def draw_interval(central_length):
    
    if central_length > 0:
        draw_interval(central_length-1)
        draw_line(central_length)
        draw_interval(central_length-1)

def draw_ruler(length,num_inch):
    draw_line(length,label="0")

    for i in range(1,num_inch+1):
        draw_interval(int(length)-1)
        draw_line(int(length),label=str(i))

draw_ruler(10,1)