Hi. This has been fun.

I started out day 25 by guessing numbers because I was tired.

My actual solution:
 - Make a dictionary of every node (component)'s connections
 - Pick a random starting node
 - Run Dijkstra's algorithm to find the distance from each node to the starting node,
   as well as the possible paths from the starting node to that node
 - Pick some ending node that is far away from the starting node
 - Examine every path from the starting node to the ending node
 - Find a pattern

Yeah, that's pretty much it.
I found three connections such that every path from the starting node to the ending node used exactly one of them
Then I altered the code to break those connections,
then ran Dijkstra's again on the starting point (just because I had already written it,
and it would tell me how many nodes were not connected to the starting node.)
