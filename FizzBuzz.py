#the_multiples-FizzBuzz
for n in range(1,1000):
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