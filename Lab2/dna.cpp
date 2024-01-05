#include <iostream>
using namespace std;

int main()
{
  string dna;
  cin >> dna;

  int count = 1;
  int max = 1;
  for (int i = 0; dna[i] != '\0'; i++)
  {

    if (dna[i] == dna[i - 1])
    {
      count++;
    }
    else
    {
      count = 1;
    }

    if (count > max)
    {
      max = count;
    }
  }

  cout << max << endl;
  return 0;
}