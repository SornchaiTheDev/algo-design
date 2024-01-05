#include <iostream>
using namespace std;

int gcd(int a, int b)
{
  if (b == 0)
    return a;

  return gcd(b, a % b);
}

int main()
{
  int a, b;
  cin >> a >> b;

  for (int start = a; start <= b; start++)
  {
    int tmp = start;
    int sum = 0;
    while (tmp > 0)
    {
      int result = tmp % 10;
      sum += result;
      tmp /= 10;
    }
    if (gcd(start, sum) != 1)
    {
      cout << start << " ";
    }
  }
}