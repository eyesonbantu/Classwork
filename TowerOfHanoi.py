def TowerOfHanoi(n, source,destination, auxilliary_rod):

    if n == 1 :
        print("Move disk 1 from source",source,"to destination", destination)
        return
    TowerOfHanoi(n -1,source,auxilliary_rod,destination)
    print("Move disk",n,"from source",source,"to destination", destination)
    TowerOfHanoi(n-1,auxilliary_rod,destination,source)

n = 5
TowerOfHanoi(n, 'A','B','C')




