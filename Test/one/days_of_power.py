import unittest
from unittest import TestCase


def get_days_of_power(R1, D1, R2, D2, R3, D3, K):

	"""A function that computes days of power given 
	loan parameters(rate(R1,R2,R3,days(D1,D2,D3)) and 
	deposit(K)"""

	days_of_power = 0 
	account_balance = 0 + K 
	counter = 0 
	account_daily_rate = 0
	isDeviceAble =False
	loans =[(R1,D1),(R2,D2),(R3,D3)]
	
	while True:	
		for rate, days in loans:
			if(days==counter):
				#calculate the daily rate
				account_daily_rate += rate

		if(account_daily_rate==0):
			#no active loans available
			days_of_power = 0

		elif(account_daily_rate>account_balance):
			
			break
		else:
			#reduce account balance, provide day of power and enable the device
			account_balance -= account_daily_rate
			days_of_power +=1
			isDeviceAble =True

		counter +=1
	print(f'Account Balance | Daily Rate | Days of Power | Device Status |\n-------------------------\n{account_balance}|{account_daily_rate}|{days_of_power}|{isDeviceAble}\n-------------------------')
	return days_of_power
	


class Test(TestCase):


	def test_get_days_of_power(self):

		days_of_power = get_days_of_power(R1=1000, D1=3, R2=500, D2=10, R3=1500, D3=7, K=21000)
 
		self.assertEqual(days_of_power, 10)

		days_of_power =	get_days_of_power(R1=500, D1=3, R2=500, D2=10, R3=500, D3=7, K=21000)

		self.assertEqual(days_of_power, 17)

		days_of_power = get_days_of_power(R1=1300, D1=0, R2=500, D2=0, R3=1500, D3=7, K=10000)

		self.assertEqual(days_of_power, 5)

		days_of_power = get_days_of_power(R1=10000, D1=3, R2=500, D2=10, R3=1500, D3=7, K=11000)

		self.assertEqual(days_of_power, 1)

		days_of_power = get_days_of_power(R1=10000, D1=3, R2=500, D2=10, R3=1500, D3=7, K=0)

		self.assertEqual(days_of_power, 0)
 
if __name__ == "__main__":
    unittest.main()

