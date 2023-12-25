#include <iostream>
#include <algorithm>
using namespace std;

int main()
{
  int runeAmount, runeThreshold;
  cin >> runeAmount >> runeThreshold;

  int runes[runeAmount];
  for (int i = 0; i < runeAmount; i++)
  {
    cin >> runes[i];
  }

  sort(runes, runes + runeAmount, greater<int>());

  int left = 0, right = runeAmount - 1, count = 0, diff = 0;

  while (count < runeThreshold)
  {
    diff += runes[left] - runes[right];
    left++;
    right--;
    count++;
  }
  
  cout << diff;
}