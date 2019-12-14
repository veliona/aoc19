def is_increasing_digits_sequence(number):
    sequence = list(map(int,str(number)))
    print(sequence)
    for n in sequence:
        i=0
        for i in range(len(n)):
            if n[i+1] > n[i]:
                print(n)


with open(f"data.txt") as f:
    content = f.readlines()
    numbers = [x.strip() for x in content][0].split("-")
    numbers = [int(x) for x in numbers]
    list_numbers = list(range(numbers[0], numbers[1]))
    for number in list_numbers:
        if is_increasing_digits_sequence(number):
            #TODO: Check if there is the same number
            
    print(number)


#function is_increasing_digits_Sequence(num) {

#  var arr_num = ('' + num).split('');

#  for (var i = 0; i < arr_num.length - 1; i++) {
#    if (parseInt(arr_num[i]) >= parseInt(arr_num[i + 1]))
#      return false;
#    }
#  return true;
#}







