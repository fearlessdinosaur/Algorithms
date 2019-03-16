def Bubble(x):
    print (x)
    for i in range(0,len(x)):
        y = []
        #checks if changes have stopped
        if( y == x):
            break
        y = x
        #bubble sort loop
        for j in range(1,len(x)):
            if(x[j-1] > x[j]):
                temp = x[j]
                x[j] = x[j-1]
                x[j-1] = temp
                print(x)
