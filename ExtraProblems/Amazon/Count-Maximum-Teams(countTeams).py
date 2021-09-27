"""
Amazon is hosting a team hackathon
1. Each team will have exactly teamSize developers.
2. A developer's skill level is dneoted by skill[i]
3. The difference betweeen the maximum and minimum skill levels, within a team cannot exceed a threshold, maxDiff


skill = [3,4,1,6,5], teamSize = 3, maxDiff = 2

At most 2 teams can be formed [3,3,1] and [4,6,5]. The differenc ebetewen the maximum and minimum skill levels is 2 in each case, which does no exceed the threshold valu eof 2.

Complete the function countMaximumTeams
"""

from math import comb
def numberOfTeams(num,skills,minAssociates,minLevel,maxLevel):
    count = 0
    for i in range(len(skills)):
        if minLevel <= skills[i] <= maxLevel:
            count += 1
    sum = 0
    while minAssociates <= count:
        sum = sum + comb(count,minAssociates)
        minAssociates += 1
    return sum
num = 6
skills = [12, 4, 6, 13, 5, 10]
minAssociates = 3
minLevel = 4
maxLevel = 10
print(numberOfTeams(num,skills,minAssociates,minLevel,maxLevel))

# brutal force
def countTeams(num: int, skills: List[int], minAssociates: int, minLevel: int,
               maxLevel: int) -> int:
    # WRITE YOUR BRILLIANT CODE HERE
    qualified = []
    possible_teams = [[]]
    for a in skills:
        if minLevel <= a <= maxLevel:
            qualified.append(a)
    num_teams = 0
    while qualified:
        person = qualified.pop()
        new_teams = []
        for team in possible_teams:
            print(team)
            print(person)
            new_team = [person] + team
            print(new_team)
            if len(new_team) >= minAssociates:
                num_teams += 1
            new_teams.append(new_team)
        possible_teams += new_teams
        print(possible_teams)

    return num_teams
	
if __name__ == "__main__":
    num = 6
    skills = [12, 4, 6, 13, 5, 10]
    minAssociates = 3
    minLevel = 4
    maxLevel = 10
    result = countTeams(num, skills, minAssociates, minLevel, maxLevel)
    print(result)