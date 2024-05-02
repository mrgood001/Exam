print("x y z w")
for x in range(2):
    for y in range(2):
        for z in range(2):
            for w in range(2):
                f = (x<=y) or (not(w) == z) and (x<=y) == (w and not(z))
                if f ==0:
                    print(x,y,z,w, int(f))
#xzy
#  yzx
#xwzy