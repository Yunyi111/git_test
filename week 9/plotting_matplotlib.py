import matplotlib.pyplot as p

my_list=[2, 5.5, 6, 8.9] # x-values by default: 0, 1, 2, 3
my_list_xvalues=[2, 4, 6, 8] # define x-values
my_list_xvalues2=[1, 3, 5, 7]

# Trend plotting
#p.plot(my_list, linewidth=5)
#p.title("Square Numbers", fontsize=24)
#p.xlabel("Value", fontsize=14)
#p.ylabel("Square of values", fontsize=14)


# scatter plotting
p.scatter(my_list_xvalues, my_list, 100, c="red")
p.scatter(my_list_xvalues2, my_list, 100, c="blue")
p.title("Square Numbers", fontsize=24)
p.xlabel("Value", fontsize=14)
p.ylabel("Square of values", fontsize=14)

p.show()