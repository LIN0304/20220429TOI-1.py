n=int(input())
box=list(map(int, input().split()))
total=sum(box)
total_average=int(total/n)
loss=max(box)-total_average
box_max=box.index(max(box))
box_min=box.index(min(box))
box[box_max]=max(box)-loss
box[box_min]=min(box)+loss





box_=' '.join(str(i) for i in box)


print(box_)