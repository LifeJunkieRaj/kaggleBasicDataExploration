
# def test_loop (num_list):
#     # nums_tuple = (0, 99, -2)
#     for num in num_list:
#         print(num)
#         my_min = min(num, 123, 3, 58, 9324)
#         my_max = max(num, 321, 30, 85, 9, 3, 42)
#         if num < 200:
#             print(my_min)
#         elif num > 200:
#             print(my_max)
        
# print(test_loop((1, 50, 500, 5000)))

candidate_max_leaf_nodes = [5, 25, 50, 100, 250, 500]
scores = {leaf_size: max(leaf_size, 123, 3, 58) for leaf_size in candidate_max_leaf_nodes}

best_tree_size = min(scores, key=scores.get) # <== We get the min value from scores, then "key=scores.get" stores that min value (I think???)
print(scores)
print("----")
print(best_tree_size)

