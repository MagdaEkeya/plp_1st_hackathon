int sum(int a, int b) {
  return a + b;
}
int multiply(int a, int b) {
  return a * b;
}
void main() { 
int number1 = 10;
  int number2 = 5;
 // Sum function
  int resultSum = sum(number1, number2);
  print("The sum of $number1 and $number2 is $resultSum.");
 // Multiply function
  int resultMultiply = multiply(number1, number2);
  print("The product of $number1 and $number2 is $resultMultiply.");
}
