import investpy

res = investpy.search_quotes(text='eimi', countries=['united kingdom'])
res = res[0]  # pick the first one
print(investpy.get_stock_historical_data(stock=res.symbol, name=res.name, country=res.country, stock_currency='USD',
                                         id_=res.id_, from_date='01/01/2021', to_date='13/04/2021'))
