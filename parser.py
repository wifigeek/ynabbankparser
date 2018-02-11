import argparse
import csv 


def csvparse(input, output, credit):
	out = open(output, 'w+')

	with open(input) as csvfile:
		reader = csv.DictReader(csvfile)
		fieldnames = ['Date', 'Payee', 'Category', 'Memo', 'Outflow', 'Inflow']

		writer = csv.DictWriter(out, fieldnames=fieldnames)
		writer.writeheader()

		for row in reader:
			if credit:
				## handle CSV format for halifax/lloyds credit cards
				writer.writerow({'Date': row['Date entered'], 'Payee': row['Description'], 'Category': '', 'Memo': '', 'Outflow': row['Amount'], 'Inflow': '' })
			else:
				## handle CSV format for lloyds/halifax current accounts
				writer.writerow({'Date': row['Transaction Date'], 'Payee': '', 'Category': '', 'Memo': row['Transaction Description'], 'Outflow': row['Debit Amount'], 'Inflow': row['Credit Amount'] })

def main():
	parser = argparse.ArgumentParser()
	parser.add_argument('--output', required=True, dest='output', help="CSV Output Location")
	parser.add_argument('--input', required=True, dest='input', help="CSV Input Location")
	parser.add_argument('--cc', required=False, dest='credit', action="store_true", help="Credit Card Transactions")
	args = parser.parse_args()
	csvparse(input=args.input,output=args.output,credit=args.credit)


if __name__ == "__main__":
	main()