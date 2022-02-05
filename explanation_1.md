I used python dictionary for caching because the underlying data structure is a hash map and the set and get operations take constant time.

I used a linked list to keep track of the order of the key-value pairs being added or visited. Each time we add a new item we append the key to the end of the linked list so it has lowest priority of being removed from cache if the cache capacity is exceeded in the next step. Similarly, each time we visit/get a existing item we move the key to the end of the linked list so that it has lowest priority of being removed next.

Time complexity: the set() function takes $O(1)$ time because both adding an item to a dictionary and removing the head node from a linked list take constant time. For the get() function, if the target key is not present in cache, it takes constant time to return $-1$; however, if the target key is present, we need to search for the key in the linked list and move it to the tail which takes $O(n)$ in the worst case scenario.

Space complexity: apart from the dictionary of length n for storing the key-value pairs, additional space is required for a linked list of length n to track the activities.