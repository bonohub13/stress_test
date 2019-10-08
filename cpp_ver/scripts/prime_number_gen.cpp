#include <iostream>
#include <vector>
#include <chrono>
#include "cmath"

using namespace std;
using namespace std::chrono;

class PrimeNumberGenerator
{
	vector<long int> prime_num_list = {2};
	long int init_prime = 2;
	int counter = 0;
	int max_len;
	public:
		PrimeNumberGenerator(int maxLength)
		{
			if (maxLength == 0)
			{
				max_len = pow(10, 4);
			}
			else
			{
				max_len = pow(10, maxLength);
			}
		}

		auto prime_num_gen()
		{
			while (prime_num_list.size() < max_len)
			{
				++init_prime;
				int checker = 0;
				for (long int prime : prime_num_list)
				{
					double judge = init_prime%prime;
					if (judge != 0)
					{
						++checker;
					}
				}
				if (checker == prime_num_list.size())
				{
					prime_num_list.resize(prime_num_list.size()+1);
					prime_num_list.at(prime_num_list.size()-1) = init_prime;
				}
			}
		}

		auto data()
		{
			return this -> prime_num_list;
		}
};

int main()
{
	int size;
	cout << "enter level of stress[default is 4(for default enter 0)]:";
	cin >> size;
	PrimeNumberGenerator prime_num(size);
	time_t start, stop;
	time(&start);
	prime_num.prime_num_gen();
	time(&stop);
	
	auto runtime = stop - start;

	cout << "runtime: " << runtime << endl;
}
