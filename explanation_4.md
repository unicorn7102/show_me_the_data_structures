In the worst-case senario, where the user is not in the group, we have to loop over all users in the group / subgroups. The time complexity would be $O(n)$. 

As we are calling the function recursively to search for the user in subgroups of the given group. The size of call stack depends on how many depths we have to go into. Again, in the worst-case senario, the space complexity would be $O(n)$.

