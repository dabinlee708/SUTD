data="""A certain king had a beautiful garden, and in the garden stood a tree which bore golden apples. These apples were always counted, and about the time when they began to grow ripe it was found that every night one of them was gone. The king became very angry at this, and ordered the gardener to keep watch all night under the tree. The gardener set his eldest son to watch; but about twelve o'clock he fell asleep, and in the morning another of the apples was missing. Then the second son was ordered to watch; and at midnight he too fell asleep, and in the morning another apple was gone. Then the third son offered to keep watch; but the gardener at first would not let him, for fear some harm should come to him: however, at last he consented, and the young man laid himself under the tree to watch. As the clock struck twelve he heard a rustling noise in the air, and a bird came flying that was of pure gold; and as it was snapping at one of the apples with its beak, the gardener's son jumped up and shot an arrow at it. But the arrow did the bird no harm; only it dropped a golden feather from its tail, and then flew away. The golden feather was brought to the king in the morning, and all the council was called together. Everyone agreed that it was worth more than all the wealth of the kingdom: but the king said, 'One feather is of no use to me, I must have the whole bird.
"""
data=data.lower()
dataList={}
for a in data:
	if a in dataList.keys():
		dataList[a]+=1
	else:
		dataList[a]=1
# print dataList
dataList=sorted(dataList.items(), key=lambda x: (-x[1], x[0]))
for a in dataList:
	print a