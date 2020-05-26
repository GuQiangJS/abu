import abupy


def test_QAAdvAPI():
    symbol = abupy.ABuMarket.code_to_symbol('sz300002')
    df = abupy.MarketBu.ABuDataFeed.QAAdvAPI(symbol).kline()
    print(df.head())
