import numpy as np
import random
import matplotlib.pyplot as plt
import wx
##初始化,N为种群规模，n为染色体长度
def init(N,n):
    C = []
    for i in range(N):
        c = []
        for j in range(n):
            a = np.random.randint(0,2)
            c.append(a)
        C.append(c)
    return C


##评估函数
# x(i)取值为1表示被选中，取值为0表示未被选中
# w(i)表示各个分量的重量，v（i）表示各个分量的价值，w表示最大承受重量
def fitness(C,N,n,W,V,w):
    S = []##用于存储被选中的下标
    F = []## 用于存放当前该个体的最大价值
    for i in range(N):
        s = []
        h = 0  # 重量
        f = 0  # 价值
        for j in range(n):
            if C[i][j]==1:
                if h+W[j]<=w:
                    h=h+W[j]
                    f = f+V[j]
                    s.append(j)
        S.append(s)
        F.append(f)
    return S,F

##适应值函数,B位返回的种族的基因下标，y为返回的最大值
def best_x(F,S,N):
    y = 0
    x = 0
    B = [0]*N
    for i in range(N):
        if y<F[i]:
            x = i
        y = F[x]
        B = S[x]
    return B,y

## 计算比率
def rate(x):
    p = [0] * len(x)
    s = 0
    for i in x:
        s += i
    for i in range(len(x)):
        p[i] = x[i] / s
    return p

## 选择
def chose(p, X, m, n):
    X1 = X
    r = np.random.rand(m)
    for i in range(m):
        k = 0
        for j in range(n):
            k = k + p[j]
            if r[i] <= k:
                X1[i] = X[j]
                break
    return X1

##交配
def match(X, m, n, p):
    r = np.random.rand(m)
    k = [0] * m
    for i in range(m):
        if r[i] < p:
            k[i] = 1
    u = v = 0
    k[0] = k[0] = 0
    for i in range(m):
        if k[i]:
            if k[u] == 0:
                u = i
            elif k[v] == 0:
                v = i
        if k[u] and k[v]:
            # print(u,v)
            q = np.random.randint(n - 1)
            # print(q)
            for i in range(q + 1, n):
                X[u][i], X[v][i] = X[v][i], X[u][i]
            k[u] = 0
            k[v] = 0
    return X

##变异
def vari(X, m, n, p):
    for i in range(m):
        for j in range(n):
            q = np.random.rand()
            if q < p:
                X[i][j] = np.random.randint(0,2)

    return X

m = 8##规模
N = 800  ##迭代次数
Pc = 0.8 ##交配概率
Pm = 0.05##变异概率
V =[408,921,1329,11,998,1009,104,839,943,299,374,673,703,954,1657,425,950,1375,430,541,971,332,483,815,654,706,1360,956,992,1948,228,435,663,575,687,1262,470,609,1079,696,907,1603,273,961,1234,281,461,742,54,957,1011,149,258,407,28,90,118,245,949,1194,246,298,544,205,546,751,33,712,745,335,956,1291,163,918,1081,79,671,750,972,991,1963,217,962,1179,380,846,1226,158,671,829,39,701,740,258,577,835,5,682,687,300,364,664,105,946,1051,68,675,743,450,465,915,686,697,1383,355,367,722,106,131,237,296,868,1164,621,807,1428,283,428,711,230,573,803,359,772,1131,270,642,912,134,507,641,21,242,263,236,705,941,469,785,1254,196,349,545,405,985,1390,865,988,1853,355,405,760,460,939,1399,142,408,550,291,436,727,644,922,1566,432,890,1322,352,885,1237,139,269,408,10,137,147,593,601,1194,724,764,1488,672,900,1572,892,981,1873,597,641,1238,810,996,1806,459,816,1275,416,872,1288,310,945,1255,283,674,957,180,697,877,112,629,741,559,869,1428,79,802,881,164,192,356,323,340,663,333,464,797,472,496,968,234,914,1148,285,691,976,401,513,914,599,755,1354,391,928,1319,244,502,746,541,837,1378,208,970,1178,107,449,556,705,887,1592,468,802,1270,444,683,1127,222,958,1180,18,24,42,153,540,693,54,633,687,853,903,1756,399,452,851,108,161,269,328,431,759]
W =[508,1021,1321,111,1098,1196,204,939,1107,399,474,719,803,1054,1781,525,1050,1362,530,641,903,432,583,894,754,806,1241,1056,1092,1545,328,535,579,675,787,1037,570,709,1171,796,1007,1251,373,1061,1101,381,561,774,154,1057,1198,249,358,446,128,190,288,345,1049,1053,346,398,622,305,646,930,133,812,892,435,1056,1406,263,1018,1192,179,771,802,1072,1091,1418,317,1062,1092,480,946,1064,258,771,846,139,801,888,358,677,679,105,782,862,400,464,747,205,1046,1133,168,775,839,550,565,727,786,797,1098,455,467,623,206,231,232,396,968,1064,721,907,1406,383,528,636,330,673,719,459,872,1316,370,742,846,234,607,737,121,342,372,336,805,1090,569,885,1245,296,449,729,505,1085,1364,965,1088,1510,455,505,758,560,1039,1363,242,508,642,391,536,855,744,1022,1231,532,990,992,452,985,1021,239,369,450,110,237,264,693,701,1176,824,864,1288,772,1000,1062,992,1081,1395,697,741,899,910,1096,1919,559,916,1296,516,972,1077,410,1045,1302,383,774,809,280,797,927,212,729,923,659,969,1065,179,902,1010,264,292,441,423,440,450,433,564,826,572,596,1057,334,1014,1148,385,791,1019,501,613,625,699,855,1289,491,1028,1381,344,602,609,641,937,1311,308,1070,1215,207,549,592,805,987,1133,568,902,952,544,783,1111,322,1058,1106,118,124,206,253,640,756,154,733,879,953,1003,1510,499,552,883,208,261,437,428,531,728]
n = len(W)##染色体长度
w = 1000

C = init(m, n)
S,F  = fitness(C,m,n,W,V,w)
B ,y = best_x(F,S,m)
Y =[y]
for i in range(N):
    p = rate(F)
    C = chose(p, C, m, n)
    C = match(C, m, n, Pc)
    C = vari(C, m, n, Pm)
    S, F = fitness(C, m, n, W, V, w)
    B1, y1 = best_x(F, S, m)
    if y1 > y:
        y = y1
    Y.append(y)
##print("最大值为：",y)



##app=wx.App()
class MyFrame(wx.Frame):
    def __init__(self,parent,id):
        wx.Frame.__init__(self,parent,id,'homework',size=(400,300))
        panel=wx.Panel(self)
        self.title=wx.StaticText(panel,label="请选择算法")
        
        self.bt1=wx.Button(panel,label='遗传算法')
        self.bt1.Bind(wx.EVT_BUTTON,self.OnclickSubmit)
        self.bt2=wx.Button(panel,label='动态规划')
        self.bt2.Bind(wx.EVT_BUTTON,self.OnclickSubmit)
        self.bt3=wx.Button(panel,label='折线图')
        self.bt3.Bind(wx.EVT_BUTTON,self.OnclickSubmit2)
        
        hsizer_button=wx.BoxSizer(wx.HORIZONTAL)
        hsizer_button.Add(self.bt1,proportion=0,flag=wx.ALIGN_CENTER,border=5)
        hsizer_button.Add(self.bt2,proportion=0,flag=wx.ALIGN_CENTER,border=5)
        hsizer_button.Add(self.bt3,proportion=0,flag=wx.ALIGN_CENTER,border=5)
        
        vsizer=wx.BoxSizer(wx.VERTICAL)
        vsizer.Add(self.title,proportion=0,flag=wx.BOTTOM|wx.TOP|wx.ALIGN_CENTER,border=25)
        vsizer.Add(hsizer_button,proportion=0,flag=wx.ALIGN_CENTER,border=15)
        panel.SetSizer(vsizer)

    def OnclickSubmit(self,event):
        message='最大值为'+str(y)
        wx.MessageBox(message)

    def OnclickSubmit2(self,event):
        #plt.xlabel('h')
        #plt.ylabel('f')
        #plt.scatter(h[i],f[i])
        plt.plot(Y)
        plt.show()
        
if __name__=='__main__':
    app=wx.App()
    frame=MyFrame(parent=None,id=-1)
    frame.Show()
    app.MainLoop
    
##plt.plot(Y)
##plt.show()
