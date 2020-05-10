int1 = int(input())
int2 = int(input())
int3 = int(input())
negative = [i for i in [int1, int2, int3] if i < 0]

if int1 == 0 or int2 == 0 or int3 == 0:
    print('zero')
elif len(negative) > 0 and len(negative) % 2 == 0:
    print('positive')
elif len(negative) > 0 and len(negative) % 2 != 0:
    print('negative')
else:
    print('positive')
