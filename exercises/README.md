# 🏋️ Technical Exercises & Interview Preparation

Welcome to the **Exercises** section of Python Gym! This directory contains curated problem-solving exercises, algorithmic challenges, and technical interview preparation tracks from **LeetCode** and **HackerRank**.

---

## 🗂️ Tracks & Directories

```
technical/exercises/
├── utils/                             # Shared data structure helpers (ListNode, TreeNode, builder utils)
├── leetcode/                          # LeetCode pattern-based tracks (NeetCode 150 / Blind 75)
│   ├── 01_arrays_and_hashing/
│   ├── 02_two_pointers/
│   ├── 03_sliding_window/
│   ├── 04_stack/
│   ├── 05_binary_search/
│   ├── 06_linked_lists/
│   ├── 07_trees/
│   ├── 08_heaps/
│   ├── 09_backtracking/
│   ├── 10_dynamic_programming/
│   └── README.md
├── hackerrank/                        # HackerRank tracks & Interview Preparation Kit
│   ├── 01_warmup/
│   ├── 02_strings/
│   ├── 03_sorting/
│   ├── 04_greedy_algorithms/
│   ├── 05_dictionaries_and_hashmaps/
│   └── README.md
└── README.md                          # This directory guide
```

---

## 🎯 Track Overviews

### 🧠 [LeetCode Track (`technical/exercises/leetcode/`)](file:///e:/repositories/python_gym/technical/exercises/leetcode/README.md)
Organized by algorithmic patterns to build transferable intuition:
- **Arrays & Hashing**: Two Sum, Contains Duplicate, Valid Anagram, Group Anagrams
- **Two Pointers**: Valid Palindrome, Container With Most Water, 3Sum
- **Sliding Window**: Best Time to Buy and Sell Stock, Longest Substring Without Repeating Characters
- **Stack**: Valid Parentheses, Min Stack
- **Binary Search**: Binary Search, Search in Rotated Sorted Array
- **Linked Lists**: Reverse Linked List, Merge Two Sorted Lists, Linked List Cycle
- **Trees**: Invert Binary Tree, Maximum Depth of Binary Tree, Same Tree
- **Heaps / Priority Queues**: Kth Largest Element in a Stream, Kth Largest Element in an Array
- **Backtracking**: Subsets, Permutations
- **Dynamic Programming**: Climbing Stairs, House Robber, Coin Change

### 🏆 [HackerRank Track (`technical/exercises/hackerrank/`)](file:///e:/repositories/python_gym/technical/exercises/hackerrank/README.md)
Organized by difficulty and topic tracks:
- **Warmup**: Simple Array Sum, Compare the Triplets, Plus Minus, Staircase, Mini-Max Sum, Birthday Cake Candles, Time Conversion
- **Strings**: CamelCase, Strong Password, Mars Exploration
- **Sorting**: Bubble Sort (Count Swaps), Mark and Toys
- **Greedy Algorithms**: Minimum Absolute Difference, Luck Balance
- **Dictionaries & Hashmaps**: Ransom Note, Two Strings

---

## 🧪 Testing & Execution

### Run Single Problem
Every file is fully self-contained and runnable directly:
```bash
python technical/exercises/leetcode/01_arrays_and_hashing/001_two_sum.py
python technical/exercises/hackerrank/01_warmup/simple_array_sum.py
```

### Run Full Test Suite with Pytest
Run all exercises across all platforms with a single command:
```bash
# Run all tests
pytest technical/exercises/

# Run only LeetCode tests
pytest technical/exercises/leetcode

# Run only HackerRank tests
pytest technical/exercises/hackerrank
```
