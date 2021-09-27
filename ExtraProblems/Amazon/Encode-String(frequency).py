# https://leetcode.com/discuss/interview-question/1010329/goldman-sachs-online-encode-string

"""
Consider a string consisting of lowercase English alphabetic letters (i.e., [a-z]) only. We use the following rules to encode all of its characters into string s:
· a is encoded as 1, b is encoded as 2, c is encoded as 3, ..., and i is encoded as 9.
· j is encoded as 10#, k is encoded as 11#, i is encoded as 12#, ..., and z is encoded as 26#.
· If there are two or more consecutive occurrences of any character, then the character count is written within parentheses (i.e., (c) , where c is an integer denoting the count of consecutive occurrences being encoded) immediately following the character. For example, consider the following string encodings:
o String "abzx" is encoded as s = "1226#24#".
o String "aabccc" is encoded as s = "1(2)23(3)".
o String "bajj" is encoded as s = "2110#(2)".
o String "wwxyzwww" is encoded as s = "23#(2)24#25#26#23#(3)°.
Complete the frequency function in the editor below. It has one parameter: a string, s, that was encoded using the rules above and consists of digits (i.e., decimal integers from 0 to 9), # symbols, and parentheses. It must return an array of 26 integ
· The element at index 0 denotes the frequency of character a in the original string.
· The element at index 1 denotes the frequency of character b in the original string.
· The element at index 2 denotes the frequency of character c in the original string.
· The element at index 25 denotes the frequency of character z in the original string. Input Format
Locked stub code in the editor reads encoded string s from stdin and passes it to the function.
Constraints
· String s consists of decimal integers from 0 to 9, #s, and O's only.
· 1 length of s 105
· It is guaranteed that string s is a valid encoded string.
· 2 c 104, where c is a parenthetical count of consecutive occurrences of an encoded character.
Output Format
The function must return an array of 26 integers denoting the respective frequencies of each character (i.e., a through z) in the decoded string. This is printed to stdout by locked stub code in the editor.
Sample Input 0
1226#24#
Sample Output 0
1 1 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 1 0 1
"""
def decode(array):
    result=[0]*26
    i=len(array)-1
 
    #print (i)
    #print (result)
    while i>=0:
        print (i)
        if array[i]=="#":
            number=int(array[i-2:i])
            result[number-1]+=1
            i-=3
        elif array[i]==")":
            count=int(array[i-1])
            if array[i-3]=="#":
                number=int(array[i-5:i-3])
                i-=6
            else:
                number=int(array[i-3:i-2])
                i-=4
            result[number-1]+=count
        else:
            number=int(array[i])
            result[number-1]+=1
            i-=1
    #print (result)
    return result

array="1226#24#"
print (decode(array))
array="1"
print (decode(array))
array="1(2)23(3)"
print (decode(array))
array="2110#(2)"
print (decode(array))
array="23#(2)24#25#26#23#(3)"
print (decode(array))

# reverse decode

def decode(a):
    out=''
    n=len(a)
    i=0
    while i<n:
        c=1
        while i<n-1 and a[i]==a[i+1]:
            c+=1
            i+=1
        i+=1
        
        if (ord(a[i-1])-96) < 10:
            if c>1:
                out+=str(ord(a[i-1])-96)+'('+str(c)+')'
            else:
                out+=str(ord(a[i-1])-96)
        else:
            if c>1:
                out+=str(ord(a[i-1])-96)+'#'+'('+str(c)+')'
            else:
                out+=str(ord(a[i-1])-96)+'#'
    return out

array="abzx"
print(decode(array))
array="aabcc"
print(decode(array))
array="bajj"
print(decode(array))
array="wwxyzwww"
print(decode(array))
