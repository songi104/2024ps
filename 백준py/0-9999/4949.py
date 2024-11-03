# while True:
#     line = input()
#     if line == ".":
#         break

#     stack1 = []
#     stack2 = []
#     for s in line:
#         if s in ["(",")"]:
#             stack1.append(s)
#         elif s in ["[", "]"]:
#             stack2.append(s)

#     cnt1 = 0
#     while stack1:
#         p = stack1.pop()
#         if p == ")":
#             cnt1 += 1
#         else:
#             cnt1 -= 1
        
#         if cnt1<0: break
    
#     cnt2 = 0
#     while stack2:
#         p = stack2.pop()
#         if p == "]":
#             cnt2 += 1
#         else:
#             cnt2 -= 1
#         if cnt2<0: break

#     if (cnt1 == 0 and cnt2==0): print("yes")
#     else: print("no")


while True:
    line = input()
    if line == ".":
        break

    stack = []
    for s in line:
        if s == "[" or s=="(":
            stack.append(s)
        elif s == ")":
            if len(stack) != 0 and stack[-1] == "(":
                stack.pop()
            else:
                stack.append(s)
        elif s == "]":
            if len(stack) != 0 and stack[-1] == "[":
                stack.pop()
            else:
                stack.append(s)
    
    if len(stack) == 0:
        print("yes")
    else:
        print("no")