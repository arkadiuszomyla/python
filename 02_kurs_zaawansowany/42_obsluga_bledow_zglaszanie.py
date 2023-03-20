def processInvoice(netto, brutto):
    if netto >= brutto:
        raise Exception('Netto should be lower or equal to brutto')
        # raise ValueError('Netto should be lower or equal to brutto')
    else:
        print('Processing invoice: netto = {}, brutto = {}'.format(netto, brutto))


def endOfMouth():
    netto = 1230
    brutto = 1000

    try:
        processInvoice(netto, brutto)
    except ValueError as e:
        print('The value on invoice are incorrent: {}'.format(e))
        raise ValueError('Error when processing invoices') from e
    except Exception as e:
        print('Error proccesing invoice: {}'.format(e))
        raise Exception('General error when processing invoices') from e


endOfMouth()