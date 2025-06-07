# Run 5 times, once for each iron block
if blacksmith.purity(FORWARD) <= 3:
    blacksmith.deny()
else:
    blacksmith.accept()