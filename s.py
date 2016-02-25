from sepacbi import IdHolder, Payment
payer = IdHolder(name='Sample Business S.P.A.', cf='12312312311', cuc='0123456A')
payment = Payment(debtor=payer, account='IT 39P 06040 15400 000000138416')
payment.add_transaction(creditor=IdHolder(name='John Smith'), account='IT83D 07601 01000 000010741106', amount=50.12, rmtinfo='Expense reimbursement')
print payment.xml_text()