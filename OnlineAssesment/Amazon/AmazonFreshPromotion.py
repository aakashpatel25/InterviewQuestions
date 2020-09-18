"""
https://leetcode.com/discuss/interview-question/762546/

Approach:
My Initial approach was wrong where in I ran for loop and for each increment I compared the current counter coupon_code to the next len(coupon_code) elements. If matched increment counter. This approach would fail when a code was matched. Because once the code has been matched i is supposed to move up by len(coupon_code) to avoide duplicate matching.

Enhenced Approach:
Use while loop and increment the i by len(coupon_code) each time there is a match to avoid duplicate matching.

Time Complexity: O(N*K) - When there is no match and for each iteration of i it would keep redoing the match till last element of the size K coupon code.

Space Complexity: O(1) - We are not stroing anything in intermediate steps so constant.
"""

def compare(lst1, lst2):
    if len(lst1) != len(lst2):
        return False
    for ele1, ele2 in zip(lst1, lst2):
        if ele1 != "anything" and ele1!=ele2:
            return False
    return True


def has_won_promotion(coupon_code, shopping_cart):
    i, counter = 0, 0

    while i < len(shopping_cart) and i+len(coupon_code[counter]) < len(shopping_cart):
        if compare(coupon_code[counter], shopping_cart[i:i+len(coupon_code[counter])]):
            i+=len(coupon_code[counter])
            counter+=1
            if counter == len(coupon_code):
                return 1
        else:
            i+=1
    return 0



res1 = has_won_promotion([["apple", "apple"], ["banana", "anything", "banana"]],
        ["orange", "apple", "apple", "banana", "orange", "banana"])
res2 = has_won_promotion([["apple", "apple"], ["banana", "anything", "banana"]],
        ["orange", "banana", "orange", "banana", "apple", "apple"])
res3 = has_won_promotion([["apple", "apple"], ["banana", "anything", "banana"]],
        ["banana", "apple" ,"banana", "orange", "banana", "apple", "apple"])
res4 = has_won_promotion([['apple', 'apple'], ['banana', 'anything', 'banana']],
        ['banana', 'orange', 'banana', 'apple', 'apple'])
res5 = has_won_promotion([['apple', 'apple'], ['banana', 'anything', 'banana']],
        ['apple', 'banana', 'apple', 'banana', 'orange', 'banana'])
res6 = has_won_promotion([['apple', 'banana','apple', 'banana', 'coconut']],
        ['apple', 'banana', 'apple', 'banana', 'apple', 'banana'])
res7 = has_won_promotion([['apple', 'orange'], ['orange', 'banana', 'orange']],
        ['apple', 'orange', 'banana', 'orange', 'orange', 'banana', 'orange', 'grape'])
res8 = has_won_promotion([['anything']],
        ['apple', 'apple', 'apple', 'banana'])
res9 = has_won_promotion([['apple', 'orange'], ['orange', 'banana', 'orange']],
        ['apple', 'orange', 'banana', 'orange', 'orange', 'banana', 'grape', 'grape'])


assert res1 == 1
assert res2 == 0
assert res3 == 0
assert res4 == 0
assert res5 == 0
assert res6 == 0
assert res7 == 1
assert res8 == 1
assert res9 == 0