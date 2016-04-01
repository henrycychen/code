def first_last6(nums):
    if nums[0] == 6 or nums[len(nums)-1] == 6:
        print True
    else:
        print False
first_last6([1, 2, 6])
first_last6([6, 1, 2, 3])
first_last6([13, 6, 1, 2, 3])

def same_first_last(nums):
    if len(nums) > 1 and nums[0] == nums[len(nums)-1]:
        print True
    else:
        print False
same_first_last([1, 2, 3])
same_first_last([1, 2, 3, 1])
same_first_last([1, 2, 1])

#Return an int array length 3 containing the first 3 digits of pi, {3, 1, 4}.
def make_pi():
    pi = [3,1,4]
    print pi
make_pi()

#Given 2 arrays of ints, a and b, return True if they have the same first element or they have the same last element.
#Both arrays will be length 1 or more.

def common_end(a, b):
    if a[0] == b[0]:
        print True
    elif a[2] == (b[len(b)-1]):
        print True
    else:
        print False

common_end([1, 2, 3], [7, 3])
common_end([1, 2, 3], [7, 3, 2])
common_end([1, 2, 3], [1, 3])

#Given an array of ints length 3, return the sum of all the elements.
def sum3(nums):
    x = nums[0] + nums[1] + nums[2]
    print x
sum3([1, 2, 3])
sum3([5, 11, 2])
sum3([7, 0, 0])

#Given an array of ints length 3, return an array with the elements "rotated left" so {1, 2, 3} yields {2, 3, 1}.
def rotate_left3(nums):
    print nums[1], nums[2], nums[0]

rotate_left3([1, 2, 3])
rotate_left3([5, 11, 9])
rotate_left3([7, 0, 0])

#Given a string and a non-negative int n, return a larger string that is n copies of the original string.


def string_times(str,n):
    result = ""
    for i in range(n):
         result += str
    print result

string_times('Hi', 2)
string_times('Hi', 3)
string_times('Hi', 1)


#Given a string and a non-negative int n, we'll say that the front of the string is the first 3 chars, or whatever is '
#there if the string is less than length 3. Return n copies of the front;

def front_times(str,n):
    result = ""
    for i in range(n):
        result = result + str[0:3]
    print result
front_times('Chocolate', 2)
front_times('Chocolate', 3)
front_times('Abc', 3)

#Given a string, return a new string made of every other char starting with the first, so "Hello" yields "Hlo".
def string_bits(str):
    print str[::2]
string_bits('Hello')
string_bits('Hi')
string_bits('Heeololeo')

def string_bits(str):
  result = ""
  # Many ways to do this. This uses the standard loop of i on every char,
  # and inside the loop skips the odd index values.
  for i in range(len(str)):
    if i % 2 == 0:
      result = result + str[i]
  print result

string_bits('Hello')
string_bits('Hi')
string_bits('Heeololeo')

#Given a non-empty string like "Code" return a string like "CCoCodCode".
def string_splosion(str):
    result = ""
    for i in range(len(str)):
        result = result + str[:i+1]
        print result

string_splosion('Code')
string_splosion('abc')
string_splosion('ab')

#Given a string, return the count of the number of times that a substring length 2 appears in the string and also as
#the last 2 chars of the string, so "hixxxhi" yields 1 (we won't count the end substring).
def last2(str):

last2('hixxhi') → 1
last2('xaxxaxaxx') → 1
last2('axxxaaxx') → 2