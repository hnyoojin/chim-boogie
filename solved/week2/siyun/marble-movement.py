n, m, t, k = map(int, input().split())
# a는 활성화된 인덱스를 표시하기 위함
r, c, d, v, a = [], [], [], [], []
for _ in range(m):
    ri, ci, di, vi = input().split()
    r.append(int(ri)-1)
    c.append(int(ci)-1)
    d.append(di)
    v.append(int(vi))
    a.append(True)

# Please write your code here.
# 방향
dir = {"L" : (0,-1), "U" : (-1,0), "R" : (0,1), "D" : (1,0)}

class Marbles :

    def __init__(self):
        # 이동하는 구슬의 위치 딕셔너리. key는 위치, value는 구슬 인덱스
        self.marbles={}
        # 0초에서 구슬의 위치 초기화
        for i in range (m):
            self.marbles[(r[i],c[i])]=[i]

    def move(self,i):
        if a[i]==True: 
            #이전 위치는 위치 딕셔너리에서 지우기
            before_pos = (r[i],c[i])
            if len(self.marbles[before_pos])>1:
                self.marbles[before_pos].remove(i)
            else: del self.marbles[before_pos]
            # 각 구슬들의 속도만큼 한칸씩 이동하며 벽에 부딪히는지 검사
            for block in range (v[i]):
                now_d=d[i]
                dy=r[i]+dir[now_d][0]
                dx=c[i]+dir[now_d][1]
                # 벽에 부딪혔을 때는 방향 바꿔서 이동
                if dy<0 or dy>=n or dx<0 or dx>=n :
                    now_d = d[i] = self.change_dir(d[i])
                    dy=r[i]+dir[now_d][0]
                    dx=c[i]+dir[now_d][1]
                r[i]=dy
                c[i]=dx

            # 이동한 곳으로 위치 딕셔너리 업데이트
            now_pos=(r[i],c[i])
            if (now_pos) in self.marbles:
                self.marbles[now_pos].append(i)
            else: self.marbles[now_pos]=[i]

    # 방향 전환
    def change_dir(self,original_d):
        direction_map = {
            "L": "R",
            "R": "L",
            "U": "D",
            "D": "U"
        }
        return direction_map.get(original_d)

    # 같은 위치에 k이상의 구슬이 있을 경우 삭제
    def remove_same_locate(self):
        for key in list(self.marbles.keys()):
            if len(self.marbles[key]) > k:
                # 속도, 인덱스 순으로 정렬하여 k개만 남기고 삭제
                value = self.marbles[key]
                value.sort(key=lambda x : (v[x],x))
                
                for i in range(len(value)-k):
                    a[value[i]] = False
                
                self.marbles[key]=value[-k:]

def move_marbles():
    marbles=Marbles()
    for time in range(t):
        for i in range (m):
            marbles.move(i)
        marbles.remove_same_locate()
    

move_marbles()

active_count = sum(1 for i in a if i)
print(active_count) 
