#the_multiples-FizzBuzz
def fizzbuzz(r):
    for n in range(1,r):
        if(n%3==0 and n%5==0):
            print(str(n)+"= FizzBuzz")
        else:
            if(n%3==0):
                print(str(n)+"= Fizz")
            else:
                if(n%5==0):
                    print(str(n)+"= Buzz")
                else:
                    print(n)