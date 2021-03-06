for number in range(1,101):
    if number % 5 == 0 and number % 3 == 0:
        print "FizzBuzz"
    elif number % 3 == 0:
        print "Fizz"
    elif number % 5 == 0:
        print "Buzz"
    else:
        print number
        
        
# IN JAVA
# var fizzBuzz = function () {
# var i, output;
# for (i = 1; i < 101; i += 1) {
#   output = '';
#   if (!(i % 3)) { output += 'Fizz'; }
#   if (!(i % 5)) { output += 'Buzz'; }
#   console.log(output || i);//empty string is false, so we short-circuit
# }
# };


# IN MATLAB
# function fizzBuzz() 
#  for i = (1:100)
#       if mod(i,15) == 0
#          fprintf('FizzBuzz ')
#       elseif mod(i,3) == 0
#          fprintf('Fizz ')
#       elseif mod(i,5) == 0
#          fprintf('Buzz ')
#       else
#          fprintf('%i ',i)) 
#       end
#   end
#   fprintf('\n');   
# end