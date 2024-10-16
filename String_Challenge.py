String Challenge

Have the function StringChallenge (str) take the str parameter being passed and determine the largest number of unique characters that exists between a pair of matching letters anywhere in the string. For example: if str is "ahyjakh" then there are only two pairs of matching letters, the two a's and the two h's. Between the pair of a's there are 3 unique characters: h, y, and j. Between the h's there are 4 unique characters: y, j, a, and k. So for this example your program should return 4.

Another example: if str is "ghececgkaem" then your program should return 5 because the most unique characters exists within the farthest pair of e characters. The input string may not contain any character pairs, and in that case your program should just return 0. The input will only consist of lowercase alphabetic characters.

Examples

Input: "mmmerme"

Output: 3

Input:

"abccdefghi"

Output: 0

My Solution:- 

def StringChallenge(strParam):
    char_indices = {}
    max_unique_chars = 0

    for i, char in enumerate(strParam):
        if char in char_indices:
            start_idx = char_indices[char]
            substring = strParam[start_idx + 1 : i]
            unique_chars = set(substring)
            max_unique_chars = max(max_unique_chars, len(unique_chars))
        else:
            char_indices[char] = i
            
    return max_unique_chars
# keep this function call here 
print(StringChallenge(input()))