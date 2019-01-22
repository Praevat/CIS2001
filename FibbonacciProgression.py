import Lab2ProgressionClass

fiboprog = Lab2ProgressionClass.FibonacciProgression()

#Fiboprog.print_progression(10)

leading_digits_amount = {} # creates dictionary

for count in range (500):
    fib_sequencer = next(fiboprog)
    leading_digits_amount[str(fiboprog)[0]] = 0 # adds to dictionary the generated fibbonacci number and converts to string

for keys, value in leading_digits_amount.items():
    print(keys, ":", value) # prints first number of keyed value as well as the entire number


