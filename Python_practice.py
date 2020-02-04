print("hello")

# list of names
my_list = ["Grant", "Jane", "Jorge", "Sue", "Thomaz"]


poop = [1,5,9]

def call_average(numbers):
    sum_num = 0
    for t in numbers:
        sum_num = sum_num + t           

    avg = sum_num / len(numbers)
    return avg

print("The average is", call_average(poop))

# How many votes did you get?
my_votes = int(input("How many votes did you get in the election? "))
#  Total votes in the election
total_votes = int(input("What is the total votes in the election? "))
# Calculate the percentage of votes you received.
percentage_votes = (my_votes / total_votes) * 100
print("I received " + str(percentage_votes)+"% of the total votes.")