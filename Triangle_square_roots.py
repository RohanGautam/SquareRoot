import matplotlib.pyplot as plt
from matplotlib import style
style.use('fivethirtyeight')
sides=[] #list which stores the sides of all the triangles


def issquare(n):#function to check if a number is a perfect square
    square=n**0.5
    return int(square)==square


def get_component_squares(n):#function to get all the sides of the triangles recursively
    part1=n-1 if n<100 else n>>1 #look for numbers from the middle if the number is large,else look from the end 
    while part1>=0:
        if issquare(part1):break
        part1-=1
        
    sides.append(part1)
    part2=n-part1
    if issquare(part2):
        sides.append(part2)
    else:
        get_component_squares(part2)


def pythagoras(a,b): #function to implement the pythagoras theorem
    return (a**2+b**2)**0.5

def show_squareroot_visually(L):#gets appropriate coordinates and plots them using matplotlib
    List=[]
    plt.axes()
    #The initial triangle:
    C=(0,0)
    B=(L[0],0)
    A=(L[0],L[1])
    
    List.append(plt.Polygon([A,B,C], fill=None, edgecolor='b',linewidth=2.0))#appending the polygon object
    def distance(x,y):
        return ((x[0]+y[0])**2 + (x[1]+y[1])**2)**0.5
    
    def plot_triangles(L):
        for polygon in L:
            plt.gca().add_patch(polygon)
        
        plt.axis('scaled')
        plt.title('Square root of {}'.format(n))
        plt.show()
            
    for i in range(1,len(L)-1):
        X=L[i+1]#length of next side
        Len=distance(A,C)
        R1=(A[0]+((X*(C[1]-A[1]))/Len),A[1]+((X*(A[0]-C[0]))/Len))
        points=[R1,A,C]
        List.append(plt.Polygon(points, fill=None, edgecolor='b',linewidth=2.0))
        B=A
        A=R1
    plot_triangles(List)



n=input('Enter a number:')
get_component_squares(n) 
sides=[x**0.5 for x in sides][::-1]

print 'square root:',reduce(pythagoras,sides) # Even the result is calculated using the pythagoras theorem 
show_squareroot_visually(sides)














