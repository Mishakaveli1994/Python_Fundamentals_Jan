employee_happiness = [int(x) for x in input().split(' ')]
factor = int(input())
employee_happiness = [x * factor for x in employee_happiness]
average = sum(x for x in employee_happiness) / len(employee_happiness)
happy_employees = len([x for x in employee_happiness if x > average ])

if happy_employees >= len(employee_happiness)/2:
    print(f'Score: {happy_employees}/{len(employee_happiness)}. Employees are happy!')
else:
    print(f'Score: {happy_employees}/{len(employee_happiness)}. Employees are not happy!')