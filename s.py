from sepacbi import IdHolder, Payment
payer = IdHolder(name='Easy Life s.r.l.', cf='02405500204', cuc='1397200L')
payment = Payment(debtor=payer, account='IT04T0101003403100000006006')
payment.add_transaction(creditor=IdHolder(name='Lisa Lagni'), account='IT08W0200811802000102833784', amount=50.12, rmtinfo='Rimborso Spese')
print payment.xml_text()

#32
#63
