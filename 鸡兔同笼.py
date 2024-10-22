iHeads = int(input("请输入有多少个头："))
iFeet = int(input("请输入有多少个脚："))
a = iFeet - 2 *  iHeads
iRabbits = a/2
iChicken = iHeads - iRabbits
print("Numbner of chicken = %d,"% iChicken,"Number  of rebits = %d" %iRabbits)
print(iFeet == iChicken*2+iRabbits*4)