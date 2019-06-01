from lexicographic import Lexicographic

class Attendance:
    def __init__(self, nstudents):
        self.students = Lexicographic(nstudents)
        
    def __call__(self, klist):
        for k in klist:
            yield self.students[k]
            
def DrDhruv(A, B):
    return list(Attendance(A)(B))
            
if __name__ == '__main__':
    A = int(input("Number of students (1 <= A <= 10\u2079): "))
    B = input("Enter , seprated K integers 1 <= K <= 1000 and K <= A: ")
    print (DrDhruv(A, map(int, B.split(','))))
    
    
