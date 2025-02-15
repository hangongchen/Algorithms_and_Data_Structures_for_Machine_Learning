import csv

# Implement a stack and use this stack for question 1 and 2 
class Stack:
    def __init__(self):
        self.length=0
        self.content=[]
        #write code here
        pass
    # add other functions for Stack
    def in_(self,element):
        self.content.append(element)
        self.length+=1
    def out(self):
        if self.length>0:
            self.content.pop()
            self.length-=1
            return True
        else:
            return False
    def last_element(self):
        if self.length>0:
            return self.content[-1]
        else:
            return False


#QUESTION 1
# Given a string s containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid. 

# An input string is valid if:

# 1) Open brackets must be closed by the same type of brackets.
# 2) Open brackets must be closed in the correct order.
# 3) Every close bracket has a corresponding open bracket of the same type.

def isValidParentheses(s: str) -> bool:
    #write code here
    s = s.lstrip('\ufeff')
    stack=Stack()
    for char in s:
        if char=='('or char=='['or char=='{':
            stack.in_(char)
        elif (char==')'and stack.last_element()=='(')\
                or (char==']'and stack.last_element()=='[')\
                or (char=='}'and stack.last_element()=='{'):
            if stack.out()==False:
                return False
        else:
            return False
    if stack.length==0:
        return True
    else:
        return False

#QUESTION 2
#Write code to evaluate a postfix expression using stack and return the integer value 
#Use stack which is implemented above for this problem
#Input -> an postfix expression string ex: "3 4 /"
#Output -> integer value after evaluating the string ex: 1
#Integers are positive and negative
#Instructions:
#DO NOT USE EVAL function for evaluating the expression.
#The valid operators are '+', '-', '*', and '/'.
def evaluatePostfix(exp:str) -> int:
    #write code here
    exp = exp.lstrip('\ufeff')
    stack=Stack()
    list=[]
    num = ''
    exp+=' '
    for element in exp:
        if element.isspace()==False:
            num+=element
        else:
            list.append(num)
            num = ''

    for element in list:
        if element.isdigit() or (element[0]=='-' and len(element)>1):
            stack.in_(int(element))
        elif element=='+':
            result=stack.content[-2]+stack.content[-1]
            stack.out()
            stack.out()
            stack.in_(result)
        elif element=='-':
            result=stack.content[-2]-stack.content[-1]
            stack.out()
            stack.out()
            stack.in_(result)
        elif element=='*':
            result=stack.content[-2]*stack.content[-1]
            stack.out()
            stack.out()
            stack.in_(result)
        elif element=='/':
            result=int(stack.content[-2]/stack.content[-1])
            stack.out()
            stack.out()
            stack.in_(result)
    return stack.content[0]



#DO NOT MODIFY BELOW CODE
if __name__ == "__main__":

    # QUESTION 1: Read Test Cases
    testcasesforquestion1 = []
    try:
        with open('question1.csv', 'r') as file:
            testCases = csv.reader(file)
            for row in testCases:
                testcasesforquestion1.append(row)
    except FileNotFoundError:
        print("File Not Found: question1.csv")

    # Running Test Cases for Question 1
    print("QUESTION 1 TEST CASES")
    for i, (inputValue, expectedOutput) in enumerate(testcasesforquestion1, start=1):
        actualOutput = isValidParentheses(inputValue)
        expectedBool = expectedOutput.lower() == 'true'  # Convert string to boolean
        if expectedBool == actualOutput:
            print(f"Test Case {i} : PASSED")
        else:
            print(f"Test Case {i}: Failed (Expected : {expectedOutput}, Actual: {actualOutput})")

    #QUESTION 2
    testcasesforquestion2 = []
    try:
        with open('question2.csv','r') as file:
            testCases = csv.reader(file)
            for row in testCases:
                testcasesforquestion2.append(row)
    except FileNotFoundError:
        print("File Not Found: question2.csv") 
    
    print("QUESTION 2 TEST CASES")
    #Running Test Cases for Question 2
    for i , (inputValue,expectedOutput) in enumerate(testcasesforquestion2,start=1):
        actualOutput = evaluatePostfix(inputValue)
        if(int(expectedOutput) == actualOutput):
            print(f"Test Case {i} : PASSED") 
        else:
            print(f"Test Case {i}: Failed (Expected : {expectedOutput}, Actual: {actualOutput})")