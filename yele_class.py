# declaring the class
class Arithmetic():
    #creating an empty list to store values from user
    number_list = []
   def values(number_list):

        #looping and adding each value to the list
        for i in range(0, 5):
            print("enter digit ", i + 1)
            values = int(input())
            number_list.append(values)
        return number_list

    def arith_activities(number_list):
        #where sum and product are the accumulators
        n = 5
        sum = 0
        product = 1
        #iterating and performing activities
        for value in number_list:
            sum = sum + value
            product = product * value
            average = sum/n
        print(f'the sum is {sum}')
        print(f'the product is {product}')
        print(f'the average is {average}')
    #calling the values function and pasing it into the arithmetic functions
    arith_activities(values(number_list))