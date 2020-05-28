import roommate
print("Ranking of all pairings by user")
results = roommate.getresults()
for student in results:
    print (student[1])
    for i in range(2,7):
            print(i-1,": ",student[i])
