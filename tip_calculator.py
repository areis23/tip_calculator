from optparse import OptionParser

parser = OptionParser()

parser.add_option("-m", "--meal", dest="meal", help="Starting cost of the meal")
parser.add_option("-t", "--tax", dest="tax", help="Sales tax rate")
parser.add_option("-p", "--tip", dest="tip", help="Tip rate", default = ".15")

(options, args) = parser.parse_args()

if not (options.meal and options.tax):
	parser.error("You need to supply arguments for both the cost of the meal and the tax rate")

meal = (float(options.meal))
tax = (float(options.tax))
tip = (float(options.tip))


tax_value = meal * tax
meal_with_tax = meal + tax_value
tip_value = meal_with_tax * tip
total = meal_with_tax + tip_value
print "The meal costs ${0:.2f}".format(meal);
print "The tax is ${0:.2f}".format(tax_value);
print "The tip should be ${0:.2f}".format(tip_value);
print "The total is ${0:.2f}".format(total);

