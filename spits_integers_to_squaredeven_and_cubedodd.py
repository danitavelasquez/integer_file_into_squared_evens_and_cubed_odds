# defines the function, also reads a file
def integer():
    integers = open("integers.txt", "r")
    # creates list
    even = []
    odd = []
    # splits linea
    for line in integers:
        numbers = line.split()

        for n in numbers:
            n = int(n)
            # checks if even then squares it
            if n % 2 == 0:
                even.append(n ** 2)
            # checks if odd then cubes it
            else:
                odd.append(n ** 3)

        # writes a file containing all the doubled even integers
        double_even = open("double.txt", "w")
        for num in even:
            double_even.write(str(num) + "\n")
        double_even.close()
        # writes a file containing all the cubed odd integers
        triple_odd = open("triple.txt", "w")
        for num in odd:
            triple_odd.write(str(num) + "\n")
        triple_odd.close()

    integers.close()
integer()