# creates class
class IntegerProcessor:
    def __init__(self):
        # input and output file names
        self.input_file = "integers.txt"
        self.even_file = "double.txt"
        self.odd_file = "triple.txt"

    # process the numbers and opens file
    def process_numbers(self):
        integers = open(self.input_file, "r")
        # creates list
        even = []
        odd = []

        # splits lines
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

        integers.close()

        # writes a file containing all the doubled even integers
        double_even = open(self.even_file, "w")
        for num in even:
            double_even.write(str(num) + "\n")
        double_even.close()
        # writes a file containing all the cubed odd integers
        triple_odd = open(self.odd_file, "w")
        for num in odd:
            triple_odd.write(str(num) + "\n")
        triple_odd.close()


# creates object and runs
processor = IntegerProcessor()
processor.process_numbers()