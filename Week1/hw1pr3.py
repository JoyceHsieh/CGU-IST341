#CodingBat.com

#Warmup-1>sleep_in
def sleep_in(weekday, vacation):
    '''
    The parameter weekday is True if it is a weekday, 
    and the parameter vacation is True if we are on vacation. 
    We sleep in if it is not a weekday or we're on vacation. 
    Return True if we sleep in.
    '''
    if not weekday or vacation:
        return True
    else:
        return False

#Warmup-1 > monkey_trouble
def monkey_trouble(a_smile, b_smile):
    '''
    We have two monkeys, a and b, and the parameters a_smile and b_smile indicate 
    if each is smiling. We are in trouble if they are both smiling or if neither of them is smiling. 
    Return True if we are in trouble.

    '''
    if a_smile and b_smile:
        return True
    elif not a_smile and not b_smile:
        return True
    else:
        return False

#Warmup-1 > sum_double
def sum_double(a, b):
    '''Given two int values, return their sum. 
    Unless the two values are the same, then return double their sum.
    '''

    if a!=b:
        return a+b
    else:
        return (a+b)*2

#Warmup-1 > diff21
def diff21(n):
    '''Given an int n, return the absolute difference between n and 21, 
    except return double the absolute difference if n is over 21.
    '''
    if n<21:
        return 21-n
    elif n>21:
        return (n-21)*2
    else:
        return 0
    
#Warmup-1 > parrot_trouble
def parrot_trouble(talking, hour):
    '''We have a loud talking parrot. 
    The "hour" parameter is the current hour time in the range 0..23. 
    We are in trouble if the parrot is talking and the hour is before 7 or after 20. 
    Return True if we are in trouble.
    '''
    if talking and hour<7:
        return True
    elif talking and hour>20:
        return True
    else:
        return False

#Warmup-1 > makes10
def makes10(a, b):
    '''Given 2 ints, a and b, return True if one if them is 10 
    or if their sum is 10.
    '''
    if a==10 or b==10:
        return True
    elif a+b==10:
        return True
    else:
        return False

#Warmup-1 > near_hundred
def near_hundred(n):
    '''Given an int n, return True if it is within 10 of 100 or 200. 
    Note: abs(num) computes the absolute value of a number.
    '''
    if abs(n-100)<=10 or abs(n-200)<=10:
        return True
    else:
        return False

#Warmup-1 > pos_neg
def pos_neg(a, b, negative):
    '''Given 2 int values, return True if one is negative and one is positive. 
    Except if the parameter "negative" is True, then return True only if both are negative.
    '''
    if negative:
        return (a<0 and b<0)
    else:
        return((a<0 and b>0) or (a>0 and b<0))

#Warmup-1 > not_string
def not_string(str):
    '''Given a string, return a new string where "not " has been added to the front. 
    However, if the string already begins with "not", return the string unchanged.
    '''
    if len(str)>=3 and str[:3]=="not":
        return str
    else:
        return "not " +str

#Warmup-1 > missing_char
def missing_char(str, n):
    '''Given a non-empty string and an int n, 
    return a new string where the char at index n has been removed. 
    The value of n will be a valid index of a char in the original string (i.e. n will be in the range 0..len(str)-1 inclusive).
    '''
    if len(str)>=n:
        return str[:n]+str[n+1:]
        
    front=str[:n]
    back=str[n-1:]
    return front+back

#Warmup-1 > front_back
def front_back(str):
    '''Given a string, return a new string where the first 
    and last chars have been exchanged.
    '''
    n=len(str)
    if n<=1:
        return str
    else:
        mid=str[1:n-1]
        return str[-1]+mid+str[0]

#Warmup-1 > front3
def front3(str):
    '''Given a string, we'll say that the front is the first 3 chars of the string. 
    If the string length is less than 3, the front is whatever is there. Return a new string which is 3 copies of the front.
    '''
    return str[0:3]*3

#Warmup-2 > string_times
def string_times(str, n):
    '''Given a string and a non-negative int n, 
    return a larger string that is n copies of the original string.
    '''
    return str*n

#Warmup-2 > front_times
def front_times(str, n):
    '''Given a string and a non-negative int n, 
    we'll say that the front of the string is the first 3 chars, 
    or whatever is there if the string is less than length 3. Return n copies of the front;
    '''
    return str[0:3]*n

#Warmup-2 > string_bits
def string_bits(str):
    '''Given a string, return a new string made of every other char starting with the first, 
    so "Hello" yields "Hlo".
    '''
    return str[0::2]

#Warmup-2 > string_splosion
def string_splosion(str):
    '''Given a non-empty string like "Code" return a string like "CCoCodCode".
    '''
    result=""
    n=len(str)
    for i in range(0,n):
        result=result+str[:i+1]
    return result


#Warmup-2 > last2
def last2(str):
    '''Given a string, return the count of the number of times 
    that a substring length 2 appears in the string 
    and also as the last 2 chars of the string, so "hixxxhi" yields 1 
    (we won't count the end substring).
    '''
    n=len(str)
    count=0
    last=str[-2:]
    for i in range(n-2):
        if str[i:i+2]==last:
            count=count+1
    return count

#Warmup-2 > array_count9
def array_count9(nums):
    '''Given an array of ints, return the number of 9's in the array.
    '''
    n=len(nums)
    count=0
    for i in range(n):
        if nums[i]==9:
            count=count+1
    return count

#Warmup-2 > array_front9
def array_front9(nums):
    '''Given an array of ints, 
    return True if one of the first 4 elements in the array is a 9. 
    The array length may be less than 4.
    '''
    n=len(nums)
    if n>4:
        n=4
    for i in range(n):
        if nums[i]==9:
            return True
    else:
        return False

#Warmup-2 > array123
def array123(nums):
    '''Given an array of ints, 
    return True if the sequence of numbers 1, 2, 3 appears in the array somewhere.
    '''
    n=len(nums)
    for i in range(n-2):
        if nums[i]==1 and nums[i+1]==2 and nums[i+2]==3:
            return True
    else:
        return False

#Warmup-2 > string_match
def string_match(a, b):
    '''Given 2 strings, a and b, 
    return the number of the positions where they contain the same length 2 substring. 
    So "xxcaazz" and "xxbaaz" yields 3, since the "xx", "aa", and "az" substrings appear in the same place in both strings.
    '''
    match=min(len(a),len(b))
    count=0
    
    for i in range(match-1):
        a_sub=a[i:i+2]
        b_sub=b[i:i+2]
        if a_sub==b_sub:
            count=count+1
    return count

#String-1 > hello_name
def hello_name(name):
    '''Given a string name, e.g. "Bob", 
    return a greeting of the form "Hello Bob!".
    '''
    h="Hello "
    return h+name+"!"

#String-1 > make_abba
def make_abba(a, b):
    '''Given two strings, a and b, return the result of putting them together in the order abba, e.g. 
    "Hi" and "Bye" returns "HiByeByeHi".
    '''
    return a+b+b+a

#String-1 > make_tags
def make_tags(tag, word):
    '''The web is built with HTML strings like "<i>Yay</i>" which draws Yay as italic text. 
    In this example, the "i" tag makes <i> and </i> which surround the word "Yay". 
    Given tag and word strings, create the HTML string with tags around the word, e.g. "<i>Yay</i>".
    '''
    HTML="<"+tag+">"+word+"</"+tag+">"
    return HTML

#String-1 > make_out_word
def make_out_word(out, word):
    '''Given an "out" string length 4, such as "<<>>", and a word, 
    return a new string where the word is in the middle of the out string, e.g. "<<word>>".
    '''
    return out[0:2]+word+out[2:]

#String-1 > extra_end
def extra_end(str):
    '''Given a string, return a new string made of 3 copies of the last 2 chars of the original string. 
    The string length will be at least 2.
    '''
    return str[-2:]*3

#String-1 > first_two
def first_two(str):
    '''Given a string, return the string made of its first two chars, 
    so the String "Hello" yields "He". If the string is shorter than length 2, 
    return whatever there is, so "X" yields "X", and the empty string "" yields the empty string "".
    '''
    return str[:2]

#String-1 > first_half
def first_half(str):
    '''Given a string of even length, return the first half. 
    So the string "WooHoo" yields "Woo".
    '''
    n=len(str)
    return str[:n/2]

#String-1 > without_end
def without_end(str):
    '''Given a string, return a version without the first and last char, so "Hello" yields "ell". 
    The string length will be at least 2.
    '''
    n=len(str)
    return str[1:n-1]

#String-1 > combo_string
def combo_string(a, b):
    '''Given 2 strings, a and b, return a string of the form short+long+short, 
    with the shorter string on the outside and the longer string on the inside. 
    The strings will not be the same length, but they may be empty (length 0).
    '''
    na=len(a)
    nb=len(b)
    if na>nb:
        return b+a+b
    else:
        return a+b+a

#String-1 > non_start
def non_start(a, b):
    '''Given 2 strings, return their concatenation, except omit the first char of each. 
    The strings will be at least length 1.
    '''
    return a[1:]+b[1:]

#String-1 > left2
def left2(str):
    '''Given a string, return a "rotated left 2" version where the first 2 chars are moved to the end. 
    The string length will be at least 2.
    '''
    return str[2:]+str[0:2]

#List-1 > first_last6
def first_last6(nums):
    '''Given an array of ints, return True if 6 appears as either the first or last element in the array. 
    The array will be length 1 or more.
    '''
    if nums[0]==6 or nums[-1]==6:
        return True
    else:
        return False

#List-1 > same_first_last
def same_first_last(nums):
    '''Given an array of ints, return True if the array is length 1 or more, 
    and the first element and the last element are equal.
    '''
    if len(nums)>0:
        if nums[0]==nums[-1]:
            return True
    return False

#List-1 > make_pi
def make_pi():
    '''Return an int array length 3 containing the first 3 digits of pi, {3, 1, 4}.
    '''
    list=[3,1,4]
    return list

#List-1 > common_end
def common_end(a, b):
    '''Given 2 arrays of ints, a and b, return True if they have the same first element or they have the same last element. 
    Both arrays will be length 1 or more.
    '''
    if a[0]==b[0] or a[-1]==b[-1]:
        return True
    else:
        return False

#List-1 > sum3
def sum3(nums):
    '''Given an array of ints length 3, return the sum of all the elements.
    '''
    sum=0
    for i in nums:
        sum+=i
    return sum

#List-1 > rotate_left3
def rotate_left3(nums):
    '''Given an array of ints length 3, 
    return an array with the elements "rotated left" so {1, 2, 3} yields {2, 3, 1}.
    '''
    a=[nums[0]]
    b=nums[1:]
    return b+a

#List-1 > reverse3
def reverse3(nums):
    '''Given an array of ints length 3, return a new array with the elements in reverse order, 
    so {1, 2, 3} becomes {3, 2, 1}.
    '''
    nums.reverse()
    return nums

#List-1 > max_end3
def max_end3(nums):
    '''Given an array of ints length 3, figure out which is larger, the first or last element in the array, 
    and set all the other elements to be that value. 
    Return the changed array.
    '''
    if nums[0]>nums[-1]:
        return [nums[0]]*3
    else:
        return [nums[-1]]*3

#List-1 > sum2
def sum2(nums):
    '''Given an array of ints, return the sum of the first 2 elements in the array. 
    If the array length is less than 2, just sum up the elements that exist, 
    returning 0 if the array is length 0.
    '''
    if len(nums)>=2:
        return nums[0]+nums[1]
    elif len(nums)==1:
        return nums[0]
    else:
        return 0

#List-1 > middle_way
def middle_way(a, b):
    '''Given 2 int arrays, a and b, each length 3, 
    return a new array length 2 containing their middle elements.
    '''
    if len(a)==3 and len(b)==3:
        return [a[1],b[1]]

#List-1 > make_ends
def make_ends(nums):
    '''Given an array of ints, return a new array length 2 containing the first and last elements from the original array. 
    The original array will be length 1 or more.
    '''
    if len(nums)>=1:
        return [nums[0],nums[-1]]

#List-1 > has23
def has23(nums):
    '''Given an int array length 2, return True if it contains a 2 or a 3.
    '''
    if len(nums)==2:
        for i in nums:
            if i==2 or i==3:
                return True
        return False

#Logic-1 > cigar_party
def cigar_party(cigars, is_weekend):
    '''When squirrels get together for a party, 
    they like to have cigars. A squirrel party is successful when the number of cigars is between 40 and 60, inclusive. 
    Unless it is the weekend, in which case there is no upper bound on the number of cigars. Return 
    True if the party with the given values is successful, or False otherwise.
    '''
    if is_weekend==False:
        if cigars>=40 and cigars<=60:
            return True
        else:
            return False
    else:
        if cigars>=40:
            return True
        else:
            return False

#Logic-1 > date_fashion
def date_fashion(you, date):
    '''You and your date are trying to get a table at a restaurant. 
    The parameter "you" is the stylishness of your clothes, in the range 0..10, 
    and "date" is the stylishness of your date's clothes. 
    The result getting the table is encoded as an int value with 0=no, 1=maybe, 2=yes. 
    If either of you is very stylish, 8 or more, then the result is 2 (yes). 
    With the exception that if either of you has style of 2 or less, then the result is 0 (no). 
    Otherwise the result is 1 (maybe).
    '''
    if you<=2 or date<=2:
        return 0
    elif you>=8 or date>=8:
        return 2
    else:
        return 1

#Logic-1 > squirrel_play
def squirrel_play(temp, is_summer):
    '''The squirrels in Palo Alto spend most of the day playing. 
    In particular, they play if the temperature is between 60 and 90 (inclusive). 
    Unless it is summer, then the upper limit is 100 instead of 90. 
    Given an int temperature and a boolean is_summer, 
    return True if the squirrels play and False otherwise.
    '''
    if is_summer==True:
        if temp>=60 and temp<=100:
            return True
        else:
            return False
    else:
        if temp>=60 and temp<=90:
            return True
        else:
            return False 

#Logic-1 > caught_speeding
def caught_speeding(speed, is_birthday):
    '''You are driving a little too fast, and a police officer stops you. 
      Write code to compute the result, encoded as an int value: 0=no ticket, 
      1=small ticket, 2=big ticket. If speed is 60 or less, the result is 0. 
      If speed is between 61 and 80 inclusive, the result is 1. If speed is 81 or more, 
      the result is 2. Unless it is your birthday -- on that day, your speed can be 5 higher in all cases.
      '''

    if is_birthday==False:
        if speed<=60:
            return 0
        elif speed<=80:
            return 1
        else:
            return 2
    else:
        if speed<=65:
            return 0
        elif speed<=85:
            return 1
        else:
            return 2

#Logic-1 > sorta_sum
def sorta_sum(a, b):
    '''Given 2 ints, a and b, return their sum. 
    However, sums in the range 10..19 inclusive, are forbidden, 
    so in that case just return 20.
    '''
    sum=a+b
    if sum>=10 and sum<=20:
        return 20
    else:
        return sum

#Logic-1 > alarm_clock
def alarm_clock(day, vacation):
    '''Given a day of the week encoded 
    as 0=Sun, 1=Mon, 2=Tue, ...6=Sat, and a boolean indicating 
    if we are on vacation, return a string of the form "7:00" 
    indicating when the alarm clock should ring. Weekdays, 
    the alarm should be "7:00" and on the weekend it should be "10:00". 
    Unless we are on vacation -- then on weekdays it should be "10:00" 
    and weekends it should be "off".
    '''
    if vacation==False:
        if day>0 and day<6:
            return '7:00'
        else:
            return '10:00'
    else:
        if day>0 and day<6:
            return '10:00'
        else:
            return 'off'

#Logic-1 > love6
def love6(a, b):
    '''The number 6 is a truly great number. 
    Given two int values, a and b, return True if either one is 6. 
    Or if their sum or difference is 6. Note: the function abs(num) computes the absolute value of a number.
    '''
    if a==6 or b==6:
        return True
    elif a+b==6:
        return True
    elif abs(a-b)==6:
        return True
    else:
        return False

#Logic-1 > in1to10
def in1to10(n, outside_mode):
    '''Given a number n, return True if n is in the range 1..10, inclusive. 
    Unless outside_mode is True, in which case return True if the number is less or equal to 1, 
    or greater or equal to 10.
    '''
    if outside_mode==False:
        if n in range(1,11):
            return True
        else:
            return False
    else:
        if n<=1 or n>=10:
            return True
        else:
            return False

#Logic-1 > near_ten
def near_ten(num):
    '''Given a non-negative number "num", 
    return True if num is within 2 of a multiple of 10. 
    Note: (a % b) is the remainder of dividing a by b, so (7 % 5) is 2. 
    '''
    x=str(num)
    y=int(x[-1])
    if y<=2 or y>=8:
        return True
    else:
        return False

#Logic-2 > make_bricks
def make_bricks(small, big, goal):
    '''We want to make a row of bricks that is goal inches long. 
    We have a number of small bricks (1 inch each) and big bricks (5 inches each). 
    Return True if it is possible to make the goal by choosing from the given bricks. 
    This is a little harder than it looks and can be done without any loops. 
    '''
    if goal> big*5+small:
        return False
    elif goal%5>small:
        return False
    else:
        return True

#Logic-2 > lone_sum
def lone_sum(a, b, c):
    '''Given 3 int values, a b c, return their sum. 
    However, if one of the values is the same as another of the values, 
    it does not count towards the sum.
    '''
    sum=0
    if a!=b and a!=c:
        sum+=a
    if b!=a and b!=c:
        sum+=b
    if c!=a and c!=b:
        sum+=c
    return sum

#Logic-2 > lucky_sum
def lucky_sum(a, b, c):
    '''Given 3 int values, a b c, return their sum. 
    However, if one of the values is 13 then it does not count towards the sum and values to its right do not count. 
    So for example, if b is 13, then both b and c do not count.
    '''
    sum=0
    if a!=13:
        sum+=a
        if b!=13:
            sum+=b
            if c!=13:
                sum+=c
                return sum
            else:
                return sum
        else:
            return a
    else:
        return 0

#Logic-2 > no_teen_sum
def no_teen_sum(a, b, c):
    '''Given 3 int values, a b c, return their sum. 
    However, if any of the values is a teen -- in the range 13..19 
    inclusive -- then that value counts as 0, except 15 and 16 do not count as a teens. 
    Write a separate helper "def fix_teen(n):"that takes in an int value and returns that value fixed for the teen rule. 
    In this way, you avoid repeating the teen code 3 times (i.e. "decomposition"). Define the helper below and at the same indent level as the main no_teen_sum().
    '''
    sum=0
    if a<13 or a>19:
        sum+=a
    elif a==15 or a==16:
        sum+=a
    if b<13 or b>19:
        sum+=b
    elif b==15 or b==16:
        sum+=b
    if c<13 or c>19:
        sum+=c
    elif c==15 or c==16:
        sum+=c
    return sum

#Logic-2 > round_sum
def round_sum(a, b, c):
    '''For this problem, we'll round an int value up to the next multiple of 10 if its rightmost digit is 5 or more, 
    so 15 rounds up to 20. Alternately, round down to the previous multiple of 10 if its rightmost digit is less than 5, so 12 rounds down to 10. 
    Given 3 ints, a b c, return the sum of their rounded values. To avoid code repetition, write a separate helper "def round10(num):" and call it 3 times. 
    Write the helper entirely below and at the same indent level as round_sum().
    
    # def round_sum(a, b, c):
    #   return round10(a) + round10(b) + round10(c)
  
    # def round10(num):
    #   mod = num % 10
    #   num -= mod
    #   if mod >= 5: num += 10
    #   return number
    
    '''
    sa=str(a)
    ia=int(sa[-1])
    sb=str(b)
    ib=int(sb[-1])
    sc=str(c)
    ic=int(sc[-1])
    sum=0
    if ia>=5:
        sum=sum+a+10-ia
    else:
        sum=sum+a-ia
    if ib>=5:
        sum=sum+b+10-ib
    else:
        sum=sum+b-ib
    if ic>=5:
        sum=sum+c+10-ic
    else:
        sum=sum+c-ic
    return sum

#Logic-2 > close_far
def close_far(a, b, c):
    '''Given three ints, a b c, return True if one of b or c is "close" (differing from a by at most 1), 
    while the other is "far", differing from both other values by 2 or more. 
    Note: abs(num) computes the absolute value of a number.
    '''
    if abs(b-c)<=1:
        return False
    elif abs(b-a)<=1 and abs(c-a)>=2:
        return True
    elif abs(c-a)<=1 and abs(b-a)>=2:
        return True
    else:
        return False

#Logic-2 > make_chocolate
def make_chocolate(small, big, goal):
    '''We want make a package of goal kilos of chocolate. 
    We have small bars (1 kilo each) and big bars (5 kilos each). 
    Return the number of small bars to use, assuming we always use big bars before small bars. 
    Return -1 if it can't be done.
    '''
    sum=small+big*5
    if goal> big*5+small:
        return -1
    elif goal%5>small:
        return -1
    else:
        if goal>big*5:
            return goal-big*5
        elif goal%5==0:
            return 0
        elif goal<5:
            return small
        elif goal<big*5:
            return goal-5
        else:
            return small

#String-2 > double_char
def double_char(str):
    '''Given a string, return a string where for every char in the original, there are two chars.
    '''
    n=len(str)
    x=''
    for i in str[:]:
        x=x+(i*2)
    return x

#String-2 > count_hi
def count_hi(str):
    '''Return the number of times that the string "hi" appears anywhere in the given string.
    '''
    n=len(str)
    sum=0
    for i in range(n-1):
        if str[i:i+2]=='hi':
            sum+=1
    return sum

#String-2 > cat_dog
def cat_dog(str):
    '''Return True if the string "cat" and "dog" appear the same number of times in the given string.
    '''
    cat=0
    dog=0
    n=len(str)
    for i in range(n):
        if str[i:i+3]=='cat':
            cat+=1
        elif str[i:i+3]=='dog':
            dog+=1
    if cat==dog:
        return True
    else:
        return False

#String-2 > count_code
def count_code(str):
    '''Return the number of times that the string "code" appears anywhere in the given string, 
    except we'll accept any letter for the 'd', so "cope" and "cooe" count.
    '''
    n=len(str)
    sum=0
    for i in range(0,n-3):
        if str[i:i+2]=='co' and str[i+3]=='e':
            sum+=1
    
    return sum

#String-2 > end_other
def end_other(a, b):
    '''Given two strings, return True if either of the strings appears at the very end of the other string, 
    ignoring upper/lower case differences (in other words, the computation should not be "case sensitive"). 
    Note: s.lower() returns the lowercase version of a string.
    #def end_other(a, b):
        #a = a.lower()
        #b = b.lower()
        #return (b.endswith(a) or a.endswith(b))
    '''
    la=a.lower()
    lb=b.lower()
    if len(a)>len(b):
        for i in range(len(a)):
            if lb[:]==la[-(len(b)):]:
                return True
    elif len(b)>len(a):
        for i in range(len(b)):
            if la[:]==lb[-(len(a)):]:
                return True
    elif a==b:
        return True
    return False

#String-2 > xyz_there
def xyz_there(str):
    '''Return True if the given string contains 
    an appearance of "xyz" where the xyz is not directly preceeded by 
    a period (.). So "xxyz" counts but "x.xyz" does not.
    '''
    n=len(str)
    for i in range(n):
        if str[i:i+3]=='xyz' and str[i-1:i]!=".":
            return True
    return False

#List-2 > count_evens
def count_evens(nums):
    '''Return the number of even ints in the given array. 
    Note: the % "mod" operator computes the remainder, e.g. 5 % 2 is 1.
    '''
    sum=0
    for i in nums:
        if i%2==0:
            sum+=1
    return sum

#List-2 > big_diff
def big_diff(nums):
    '''Given an array length 1 or more of ints, 
    return the difference between the largest and smallest values in the array. 
    Note: the built-in min(v1, v2) and max(v1, v2) functions return the smaller or larger of two values.
    '''
    x=max(nums)
    y=min(nums)
    return x-y

#List-2 > centered_average
def centered_average(nums):
    '''Return the "centered" average of an array of ints, 
    which we'll say is the mean average of the values, 
    except ignoring the largest and smallest values in the array. 
    If there are multiple copies of the smallest value, 
    ignore just one copy, and likewise for the largest value. 
    Use int division to produce the final average. You may assume that the array is length 3 or more.
    '''
    nums.remove(max(nums))
    nums.remove(min(nums))
    sum=0
    n=len(nums)
    for i in nums:
        sum+=i
    return sum/n

#List-2 > sum13
def sum13(nums):
    '''Return the sum of the numbers in the array, 
    returning 0 for an empty array. 
    Except the number 13 is very unlucky, 
    so it does not count and numbers that come immediately after a 13 also do not count.
    '''
    nums.append(0)
    n=len(nums)
    sum=0
    for i in range(n):
        if nums[i]==13 or nums[i-1]==13:
            sum+=0
        else:
            sum+=nums[i]
    return sum

#List-2 > sum67
def sum67(nums):
    '''Return the sum of the numbers in the array, 
    except ignore sections of numbers starting with a 6 and extending to the next 7 
    (every 6 will be followed by at least one 7). Return 0 for no numbers.
    '''
  
  
    #[1, 2, 2, 6, 99, 99, 7]
    # T
    
    
    count=True
    sum=0
    
    for i in range(0, len(nums)):
        
        if nums[i]==6:
            count=False
        elif count==False and nums[i]==7:
            count =True
        elif count==True:
            sum=sum+nums[i]
    
    return sum

#List-2 > has22
def has22(nums):
    '''Given an array of ints, return True if the array contains a 2 next to a 2 somewhere.
    '''
    nums.append(0)
    n=len(nums)
    for i in range(n-1):
        if nums[i]==2:
            if nums[i+1]==2 or nums[i-1]==2:
                return True
    return False
