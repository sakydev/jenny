import jenny, chrome, os, subprocess

def howmuch(daily):
	weekly = daily * 7
	monthly = daily * 30
	quarterly = monthly * 3
	halfYear = monthly * 6
	yearly = monthly * 12

	print(f'Weekly: {weekly}')
	print(f'Monthly: {monthly}')
	print(f'Quarterly: {quarterly}')
	print(f'Half Year: {halfYear}')
	print(f'1 Year: {yearly}')
	print(f'5 Years: {fiveYears}')
	print(f'10 Years: {tenYears}')