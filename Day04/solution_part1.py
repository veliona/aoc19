def is_increasing_digits_sequence(number):
    for number in numbers:
        sequence = list(map(int,str(number)))
        print(sequence)
        for sequence in number:
            x = 0
            results = 0
            for value in sequence:
                y = value
                if (y > x and y=x):
                    results +=
    print(results)
        #value = 0
        #for sequence in :
        #    value += seq_value












#function is_increasing_digits_Sequence(num) {

#  var arr_num = ('' + num).split('');

#  for (var i = 0; i < arr_num.length - 1; i++) {
#    if (parseInt(arr_num[i]) >= parseInt(arr_num[i + 1]))
#      return false;
#    }
#  return true;
#}





with open(f"data.txt") as f:
    content = f.readlines()
    numbers = [x.strip() for x in content][0].split("-")
    numbers = [int(x) for x in numbers]
    list_numbers = list(range(numbers[0], numbers[1]))
    print(is_increasing_digits_sequence(list_numbers[0]))
    #for number in list_numbers:
    #    if

