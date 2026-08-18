# 🧠 LeetCode Pattern Practice Track

A structured collection of canonical LeetCode problems organized by fundamental algorithmic and data structure patterns (based on the NeetCode 150 / Blind 75 curriculum).

---

## 🗺️ Curriculum & Topic Breakdown

| Pattern / Category | Problem | Difficulty | Key Technique / Concepts |
|---|---|---|---|
| **01. Arrays & Hashing** | [001_two_sum.py](file:///e:/repositories/python_gym/technical/exercises/leetcode/01_arrays_and_hashing/001_two_sum.py) | `Easy` | Hash Map complement lookup $O(n)$ |
| | [217_contains_duplicate.py](file:///e:/repositories/python_gym/technical/exercises/leetcode/01_arrays_and_hashing/217_contains_duplicate.py) | `Easy` | Hash Set uniqueness check $O(n)$ |
| | [242_valid_anagram.py](file:///e:/repositories/python_gym/technical/exercises/leetcode/01_arrays_and_hashing/242_valid_anagram.py) | `Easy` | Frequency counter comparison $O(n)$ |
| | [049_group_anagrams.py](file:///e:/repositories/python_gym/technical/exercises/leetcode/01_arrays_and_hashing/049_group_anagrams.py) | `Medium` | Character count tuple hash keys $O(N \cdot K)$ |
| **02. Two Pointers** | [125_valid_palindrome.py](file:///e:/repositories/python_gym/technical/exercises/leetcode/02_two_pointers/125_valid_palindrome.py) | `Easy` | Converging pointer scan $O(n)$ |
| | [011_container_with_most_water.py](file:///e:/repositories/python_gym/technical/exercises/leetcode/02_two_pointers/011_container_with_most_water.py) | `Medium` | Greedy inward pointer shrink $O(n)$ |
| | [015_3sum.py](file:///e:/repositories/python_gym/technical/exercises/leetcode/02_two_pointers/015_3sum.py) | `Medium` | Sort + 2-pointer scan + duplicate skip $O(n^2)$ |
| **03. Sliding Window** | [121_best_time_to_buy_and_sell_stock.py](file:///e:/repositories/python_gym/technical/exercises/leetcode/03_sliding_window/121_best_time_to_buy_and_sell_stock.py) | `Easy` | Running minimum tracker $O(n)$ |
| | [003_longest_substring_without_repeating_characters.py](file:///e:/repositories/python_gym/technical/exercises/leetcode/03_sliding_window/003_longest_substring_without_repeating_characters.py) | `Medium` | Dynamic window with last-seen index map $O(n)$ |
| **04. Stack** | [020_valid_parentheses.py](file:///e:/repositories/python_gym/technical/exercises/leetcode/04_stack/020_valid_parentheses.py) | `Easy` | LIFO matching with bracket dictionary $O(n)$ |
| | [155_min_stack.py](file:///e:/repositories/python_gym/technical/exercises/leetcode/04_stack/155_min_stack.py) | `Medium` | Parallel prefix min tracking $O(1)$ ops |
| **05. Binary Search** | [704_binary_search.py](file:///e:/repositories/python_gym/technical/exercises/leetcode/05_binary_search/704_binary_search.py) | `Easy` | Classic iterative bisect $O(\log n)$ |
| | [033_search_in_rotated_sorted_array.py](file:///e:/repositories/python_gym/technical/exercises/leetcode/05_binary_search/033_search_in_rotated_sorted_array.py) | `Medium` | Pivot & sorted-half classification $O(\log n)$ |
| **06. Linked Lists** | [206_reverse_linked_list.py](file:///e:/repositories/python_gym/technical/exercises/leetcode/06_linked_lists/206_reverse_linked_list.py) | `Easy` | In-place iterative pointer reversal $O(n)$ |
| | [021_merge_two_sorted_lists.py](file:///e:/repositories/python_gym/technical/exercises/leetcode/06_linked_lists/021_merge_two_sorted_lists.py) | `Easy` | Dummy head merge splice $O(n+m)$ |
| | [141_linked_list_cycle.py](file:///e:/repositories/python_gym/technical/exercises/leetcode/06_linked_lists/141_linked_list_cycle.py) | `Easy` | Floyd's fast & slow pointer cycle check $O(n)$ |
| **07. Trees** | [226_invert_binary_tree.py](file:///e:/repositories/python_gym/technical/exercises/leetcode/07_trees/226_invert_binary_tree.py) | `Easy` | Post-order recursive swap $O(n)$ |
| | [104_maximum_depth_of_binary_tree.py](file:///e:/repositories/python_gym/technical/exercises/leetcode/07_trees/104_maximum_depth_of_binary_tree.py) | `Easy` | Recursive DFS height calculation $O(n)$ |
| | [100_same_tree.py](file:///e:/repositories/python_gym/technical/exercises/leetcode/07_trees/100_same_tree.py) | `Easy` | Simultaneous recursive structural match $O(n)$ |
| **08. Heaps & Priority Queues** | [703_kth_largest_element_in_a_stream.py](file:///e:/repositories/python_gym/technical/exercises/leetcode/08_heaps/703_kth_largest_element_in_a_stream.py) | `Easy` | Min-heap of size $k$ $O(\log k)$ |
| | [215_kth_largest_element_in_an_array.py](file:///e:/repositories/python_gym/technical/exercises/leetcode/08_heaps/215_kth_largest_element_in_an_array.py) | `Medium` | $k$-element min-heap extraction $O(n \log k)$ |
| **09. Backtracking** | [078_subsets.py](file:///e:/repositories/python_gym/technical/exercises/leetcode/09_backtracking/078_subsets.py) | `Medium` | Power set generation $O(n \cdot 2^n)$ |
| | [046_permutations.py](file:///e:/repositories/python_gym/technical/exercises/leetcode/09_backtracking/046_permutations.py) | `Medium` | Visited state permutation tree $O(n \cdot n!)$ |
| **10. Dynamic Programming** | [070_climbing_stairs.py](file:///e:/repositories/python_gym/technical/exercises/leetcode/10_dynamic_programming/070_climbing_stairs.py) | `Easy` | Fibonacci state recurrence $O(n)$ time, $O(1)$ space |
| | [198_house_robber.py](file:///e:/repositories/python_gym/technical/exercises/leetcode/10_dynamic_programming/198_house_robber.py) | `Medium` | Non-adjacent max loot optimization $O(n)$ |
| | [322_coin_change.py](file:///e:/repositories/python_gym/technical/exercises/leetcode/10_dynamic_programming/322_coin_change.py) | `Medium` | Bottom-up unbounded knapsack DP $O(A \cdot C)$ |

---

## 🏃 How to Run & Test

You can run each problem file directly:
```bash
python technical/exercises/leetcode/01_arrays_and_hashing/001_two_sum.py
```

Or run all LeetCode tests together using `pytest`:
```bash
pytest technical/exercises/leetcode
```
