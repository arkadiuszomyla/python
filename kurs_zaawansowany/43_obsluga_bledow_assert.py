import datetime

netto = 100
brutto = 120
#netto must be less or equal to brutto
assert netto <= brutto  #przerwie program z błędem jeżeli to nie prawda


orderDate = datetime.date(2023, 2, 24)
deliveryDate = datetime.date(2024, 2, 30)
#order date should be earlier than the delivery date
assert orderDate <= deliveryDate, 'Order date cannot be later than delivery date'