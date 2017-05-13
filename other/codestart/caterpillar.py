totalLeaves = 10
totalCaterpillars = 3
jumpNumbers = [2,4,5]
leafStates = [False] * totalLeaves

SOLUTION 1 - O(2n+1), w(n)
for jumper in jumpNumbers:
    for i in xrange(jumper - 1, totalLeaves, jumper):
        leafStates[i] = True

print totalLeaves - sum(leafStates)
print leafStates.count(False)

#SOLUTION 2 - O(6n+1), w(n)
# for i in xrange(jumpNumbers[0] - 1, totalLeaves):
#     for jumper in jumpNumbers:
#         if (i - 1) % jumper == 0:
#             leafStates[i] = True
#             break
#
# print totalLeaves - sum(leafStates)
# print leafStates.count(False)
