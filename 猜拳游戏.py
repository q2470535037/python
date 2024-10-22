import random # 导入随机数模块
print('*******石头、剪刀、布********\n'
      '1.石头\n'
      '2.剪刀\n'
      '3.布\n')
Computer = random.choice(('石头','剪刀','布')) # 计算机随机出拳
Player = input('请出拳：') # 玩家出拳
Player = int(Player)
if Computer == '石头': # 计算机出拳为"石头"
    if Player == 1: # 玩家出拳为"石头"
        print('\n对手：石头\n'
              '你出：石头\n'
              '结果：平局')
    elif Player == 2: # 玩家出拳为"剪刀"
        print('\n对手：石头\n'
              '你出：剪刀\n'
              '结果：对手赢')
    elif Player == 3: # 玩家出拳为"布"
        print('\n对手：石头\n'
              '你出：布\n'
              '结果：你赢了')
    else:
        print('输入有误')
elif Computer == '剪刀': #计算机出拳为"剪刀"
    if Player == 1: # 玩家出拳为"石头"
        print('\n对手：剪刀\n'
              '你出：石头\n'
              '结果：你赢了')
    elif Player == 2: # 玩家出拳为"剪刀"
        print('\n对手：剪刀\n'
              '你出：剪刀\n'
              '结果：平局')
    elif Player == 3: # 玩家出拳为"布"
        print('\n对手：剪刀\n'
              '你出：布\n'
              '结果：对手赢')
    else:
        print('输入有误')
elif Computer == '布': #计算机出拳为"布"
    if Player == 1: # 玩家出拳为"石头"
        print('\n对手：布\n'
              '你出：石头\n'
              '结果：对手赢')
    elif Player == 2: # 玩家出拳为"剪刀"
        print('\n对手：布\n'
              '你出：剪刀\n'
              '结果：你赢了')
    elif Player == 3: # 玩家出拳为"布"
        print('\n对手：布\n'
              '你出：布\n'
              '结果：布')
    else:
        print('输入有误')
else:
    print('对手认输，你赢了')