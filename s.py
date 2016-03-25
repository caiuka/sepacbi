from sepacbi import IdHolder, Payment
payer = IdHolder(name='Ethics S.r.l.', cf='02519740415', cuc='1408170V')
payment = Payment(debtor=payer, account='IT22O0101003403100000006001')
payment.add_transaction(creditor=IdHolder(name='Zanotti David'), account='IT21V020082430900004042591', amount=100.00, rmtinfo='Acconto compenso')
payment.add_transaction(creditor=IdHolder(name='Ostigh Paolo'), account='IT32S0305155181000020460770', amount=100.00, rmtinfo='Acconto compenso')
print payment.xml_text()
