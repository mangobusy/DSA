class ArrayQueue():    # build array queue
    def __init__(self):
        self.data = []
        self.size = 0
    def enqueue(self,ele):   # add element to right
        self.data.append(ele)
        self.size += 1
    def dequeue(self):    # del element from left
        if self.data != []:
            del self.data[0]
            self.size -= 1
        else:
            return 'the queue is none'
    def length(self):
        return self.size
    def traversal(self):      # print the queue out
        if self.data != []:
            for i in self.data:
                print(i,end='')
        else:
            return 'the queue is none'

class goToSeeDoctor():
    def __init__(self):
        self.a=ArrayQueue()
        self.play=True
    def Queue(self):
        patientNum=input('input the number of patient: ')
        self.a.enqueue(patientNum)
    def see_the_doctor(self):
        print('the patient '+self.a.data[0]+' go to see the doctor')
        self.a.dequeue()
    def check_the_queue(self):
        print('patients in the queue: ',end='')
        self.a.traversal()
    def Stop_queue(self):
        print('patients go to see the doctor in order',end='')
        for i in self.a.data:
            print(i,end='')
    def Closed(self):
        self.play=False


if __name__=='__main__':
    test = goToSeeDoctor()

    while test.play==True:
        n = int(input('\nPlease select: '))
        if n==1:
            test.Queue()
        if n==2:
            test.see_the_doctor()
        if n==3:
            test.check_the_queue()
        if n==4:
            test.Stop_queue()
        if n==5:
            test.Closed()


