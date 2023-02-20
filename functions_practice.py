# Define the hello function
def hello():
    print("Hello, greetings user!")

# Define the pack function
def pack(item1,item2,item3):
  return [item1,item2,item3]

# Define the eat_lunch function
def eat_lunch(my_lst):
  if len(my_lst) == 0:
    print("My lunchbox is empty!")
  else:
    for i in range(len(my_lst)):
      if i == 0:
        print(f"First I eat {my_lst[0]}")
      else:
        print(f"Next I eat {my_lst[i]}")

# Test
hello()
print(pack("item1","item2","item3"))
print(pack(1,2,3))
eat_lunch([])
eat_lunch(["sandwich"])
eat_lunch(["apple","banana","sandwich","cookie"])