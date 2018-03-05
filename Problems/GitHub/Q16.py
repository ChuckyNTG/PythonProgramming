def Q16(num_list):
    odds = [int(num)**2 for num in num_list.split(',') if int(num)%2==1]
    print ','.join([str(num) for num in odds])


Q16(raw_input())
