def divisors(number):
    divisors_sum = 0
    for i in range(1, int(number / 2 + 1)):
        if number % i == 0:
            divisors_sum += i
    if divisors_sum == number:
        print('We have a perfect number!')
    else:
        print("It's not so perfect.")

number = int(input())
divisors(number)

