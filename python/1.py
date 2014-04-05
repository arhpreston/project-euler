
## We wish to find the sum of all numbers that divide 3 or 5
## in the following data set
nums = range(1, 1000)


### Method 1
num3 = [i%3==0 for i in nums]
num5 = [i%5==0 for i in nums]

def myOr( a, b ):
    return a or b

def myTimes( a, b ):
    return a * b

nums3or5 = map( myOr, num3, num5 )
n = map( myTimes, nums, nums3or5 )

print 'Answer 1:', sum(n)


### Method 2

def makeDivBy( m ):
    return lambda x: x%m == 0

my3 = makeDivBy( 3 )
my5 = makeDivBy( 5 )

n = filter( lambda x: my3(x) or my5(x), nums )
print 'Answer 2:', sum(n)



### Method 3
n = filter( lambda x: not (x%3 and x%5), nums )
print 'Answer 3:', sum(n)
