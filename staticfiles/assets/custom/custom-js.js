function formatNumber(number) {
	var newNumber = number.toLocaleString('en-IN', {
		minimumFractionDigits: 2,
		maximumFractionDigits: 2,
		style: 'decimal',
		useGrouping: true,
	});
	return newNumber;
}