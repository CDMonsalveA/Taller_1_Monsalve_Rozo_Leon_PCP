from math import exp
class SingleMachine:
    def __init__(self, n = 1 , p = [], d = [], r = [], start=0):
        """n: number of jobs
        #M: number of machines
        #J: number of jobs
        #p: processing time
        #d: due date
        #r: release date
        #start: start time
        #S: start time for job j
        #C: completion time for job j
        #L: lateness for job j
        #T: tardiness for job j
        #E: earliness for job j
        """
        self.n = n
        self.J = list(range(n))
        self.p = p
        self.d = d
        self.r = r
        self.S = [0]*self.n
        self.C = [0]*self.n
        self.L = [0]*self.n
        self.T = [0]*self.n
        self.E = [0]*self.n
    def process(self):
        for j in range(self.n):
            self.S[j] = max(self.r[j], self.C[j-1])
            self.C[j] = self.S[j] + self.p[j]
            self.L[j] = self.C[j] - self.d[j]
            self.T[j] = max(0, self.L[j])
            self.E[j] = max(0, -self.L[j])
            print(self.J[j],": ",self.r[j], self.C[j-1],"->", self.S[j],"-", self.C[j])
    def FCFS(self):
        self.J = sorted(self.J)
        self.process()
        return self.J
    def LCFS(self):
        self.J = sorted(self.J, reverse=True)
        self.process()
        return self.J
    FIFO = FCFS
    LIFO = LCFS
    def SPT(self):
        if self.r == [] or len(set(self.r)) == 1:
            self.J = [self.J for _, self.J in sorted(zip(self.p, self.J))]
            self.d = [self.d for _, self.d in sorted(zip(self.p, self.d))]
            self.p = sorted(self.p)
            self.process()
            return self.J
        else:
            #Sort the jobs by release date and processing time
            self.J = [x for _, x in sorted(zip(zip(self.r, self.p), self.J))]
            self.d = [x for _, x in sorted(zip(zip(self.r, self.p), self.d))]
            self.p = [x for _, x in sorted(zip(zip(self.r, self.p), self.p))]
            self.r = sorted(self.r)
        self.process()
        return self.J
    def LPT(self):
        if self.r == [] or len(set(self.r)) == 1:
            self.J = [self.J for _, self.J in sorted(zip(self.p, self.J))]
            self.d = [self.d for _, self.d in sorted(zip(self.p, self.d))]
            self.p = sorted(self.p)
            self.process()
            return self.J
        else:
            #Sort the jobs by release date and processing time
            self.J = [x for _, x in sorted(zip(zip(self.r, [-k for k in self.p]), self.J))]
            self.d = [x for _, x in sorted(zip(zip(self.r, [-k for k in self.p]), self.d))]
            self.p = [x for _, x in sorted(zip(zip(self.r, [-k for k in self.p]), self.p))]
            self.r = sorted(self.r)
        self.process()
        return self.J
    def EDD(self):
        if self.r == [] or len(set(self.r))==1:
            self.J = [self.J for _, self.J in sorted(zip(self.d, self.J))]
            self.p = [self.p for _, self.p in sorted(zip(self.d, self.p))]
            self.d = sorted(self.d)
        else:
            self.J = [x for _, x in sorted(zip(zip(self.r,self.d), self.J))]
            self.p = [x for _, x in sorted(zip(zip(self.r,self.d), self.p))]
            self.d = [x for _, x in sorted(zip(zip(self.r,self.d), self.d))]
            self.r = sorted(self.r)
        self.process()
        return self.J
    def LDD(self):
        if self.r == [] or len(set(self.r))==1:
            self.J = [self.J for _, self.J in sorted(zip(self.d, self.J), reverse=True)]
            self.p = [self.p for _, self.p in sorted(zip(self.d, self.p), reverse=True)]
            self.d = sorted(self.d, reverse=True)
        else:
            self.J = [x for _, x in sorted(zip(zip(self.r,[-k for k in self.d]), self.J))]
            self.p = [x for _, x in sorted(zip(zip(self.r,[-k for k in self.d]), self.p))]
            self.d = [x for _, x in sorted(zip(zip(self.r,[-k for k in self.d]), self.d))]
            self.r = sorted(self.r)
        self.process()
        return self.J
    def CR(self, check_time=False):
        if check_time == False:
            SyntaxError("check_time is not defined, Start time is used instead")
            check_time = self.start
        t = check_time
        CR = [0]*self.n
        for j in self.J:
            CR[j] = (self.d[j]-t)/self.p[j]
        self.J = [self.J for _, self.J in sorted(zip(CR, self.J))]
        self.p = [self.p for _, self.p in sorted(zip(CR, self.p))]
        self.d = [self.d for _, self.d in sorted(zip(CR, self.d))]
        self.process()
        return self.J
    CriticalRatio = CR
    def MinimumSlack(self, check_time=False):
        if check_time == False:
            SyntaxError("check_time is not defined, Start time is used instead")
            check_time = self.start
        t = check_time
        MS = [0]*self.n
        for j in self.J:
            MS[j] = max(0,self.d[j]-t-self.p[j])
        self.J = [self.J for _, self.J in sorted(zip(MS, self.J))]
        self.p = [self.p for _, self.p in sorted(zip(MS, self.p))]
        self.d = [self.d for _, self.d in sorted(zip(MS, self.d))]
        self.process()
        return self.J
    MinSlack = MinimumSlack
    def MaximumSlack(self, check_time=False):
        if check_time == False:
            SyntaxError("check_time is not defined, Start time is used instead")
            check_time = self.start
        t = check_time
        MS = [0]*self.n
        for j in self.J:
            MS[j] = max(0,self.d[j]-t-self.p[j])
        self.J = [self.J for _, self.J in sorted(zip(MS, self.J), reverse=True)]
        self.p = [self.p for _, self.p in sorted(zip(MS, self.p), reverse=True)]
        self.d = [self.d for _, self.d in sorted(zip(MS, self.d), reverse=True)]
        self.process()
        return self.J
    MaxSlack = MaximumSlack
    def ATC(self, check_time=False, K =False):
        if check_time == False:
            SyntaxError("check_time is not defined, Start time is used instead")
            check_time = self.start
        if K == False:
            SyntaxError("K is not defined, K = 1 is used instead")
            K = 1
        t = check_time
        ATC = [0]*self.n
        P = sum(self.p)/self.n
        for j in self.J:
            ATC[j] = (1/self.n)/(self.p[j])*exp(-max(self.d[j]-t-self.p[j], 0)/(K*P))
        self.J = [self.J for _, self.J in sorted(zip(ATC, self.J), reverse=True)]
        self.p = [self.p for _, self.p in sorted(zip(ATC, self.p), reverse=True)]
        self.d = [self.d for _, self.d in sorted(zip(ATC, self.d), reverse=True)]
        self.process()
        return self.J
    def CommonDueDate(self):
        if len(set(self.d)) != 1:
            SyntaxError("Not All jobs have the same due date")
        #Step 0: Rank the jobs in SPT order
        self.SPT()
        #Step 1: Create two sets A and B
        A = []
        B = []
        #Step 2: Compute Cmax = \sum_{j=1}^{n} p_j, i = n, R = Cmax-d
        n = self.n
        Cmax = sum(self.p)
        i = n
        R = Cmax - self.d[0]
        L = self.d[0]
        #Step 3: If R > L, then add job i to set A and go to step 4
        while i > 0:
            if R >= L:
                A.append(i)
                i -= 1
                R = R-self.p[i]
            else:
                B.append(i)
                i -= 1
                L = L-self.p[i] 
        Order = B + list(reversed(A))
        Lab = [0]*n
        for j in range(n):
            Lab[j] = self.J[Order[j]-1]
        self.J = Lab
        self.process()
        return self.J
    def DiferentDueDates(self, groups: int,  P1: float = 1, P2: float = 1, P3: float = 1):
        if len(set(self.d)) == 1:
            SyntaxError("All jobs have the same due date, Common Due Date is recomended instead")
        #Step 1: Rank the jobs in SPT order
        self.SPT()
        #Step 2: Set N[0] = 0, N[j] = sum_{k=1}^j n_k, j = 1,2,...,n
        n = list(range(self.n))
        N = [0]*self.n
        N[0] = 0
        for j in range(1,n):
            sum(n[:j])