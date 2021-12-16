
import dlib


def minCost(arr):


	assignment = dlib.max_cost_assignment(arr)

	print(dlib.assignment_cost(arr, assignment))

arr = dlib.matrix([[3, 5], [10, 1]])

minCost(arr)
