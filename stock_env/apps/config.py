## stockstats technical indicator column names
TECHNICAL_INDICATORS_LIST = [
    "macd",
    "boll_ub",
    "boll_lb",
    "rsi_30",
    "cci_30",
    "dx_30",
    "close_30_sma",
    "close_60_sma"
]

# TECHNICAL_INDICATORS_LIST = [
#     "rsi_20",
#     "close_30_trix",
#     "close_30_mvar",
#     "close_30_ema",
#     "dma",
#     "wr_30",
#     "atr"
# ]

########################################################
############## Stock Ticker Setup starts ##############

Dow_TICKER = [
    "AAPL",
    "MSFT",
    "JPM",
    "V",
    "RTX",
    "PG",
    "GS",
    "NKE",
    "DIS",
    "AXP",
    "HD",
    "INTC",
    "WMT",
    "IBM",
    "MRK",
    "UNH",
    "KO",
    "CAT",
    "TRV",
    "JNJ",
    "CVX",
    "MCD",
    "VZ",
    "CSCO",
    "XOM",
    "BA",
    "MMM",
    "PFE",
    "WBA",
    "DD",
]

HighTech_TICKER = [
    'AAPL',
    'NVDA',
    'GOOG',
    'AMZN',
    'AMD',
    'QCOM',
    'INTC',
    'MSFT',
    'BIDU'
 ]

HSI_TICKER = [
    "0011.HK",
    "0005.HK",
    "0012.HK",
    "0006.HK",
    "0003.HK",
    "0016.HK",
    "0019.HK",
    "0002.HK",
    "0001.HK",
    "0267.HK",
    "0101.HK",
    "0941.HK",
    "0762.HK",
    "0066.HK",
    "0883.HK",
    "2388.HK",
    "0017.HK",
    "0083.HK",
    "0939.HK",
    "0388.HK",
    "0386.HK",
    "3988.HK",
    "2628.HK",
    "1398.HK",
    "2318.HK",
    "3328.HK",
    "0688.HK",
    "0857.HK",
    "1088.HK",
    "0700.HK",
    "0836.HK",
    "1109.HK",
    "1044.HK",
    "1299.HK",
    "0151.HK",
    "1928.HK",
    "0027.HK",
    "2319.HK",
    "0823.HK",
    "1113.HK",
    "1038.HK",
    "2018.HK",
    "0175.HK",
    "0288.HK",
    "1997.HK",
    "2007.HK",
    "2382.HK",
    "1093.HK"
]

SP_TICKER = [
    "HOLX",
    "SIVB",
    "NWS",
    "EMR",
    "IRM",
    "AMT",
    "RCL",
    "HLT",
    "VMC",
    "GPS",
    "TEL",
    "APA",
    "COO",
    "EIX",
    "BMY",
    "LHX",
    "HSY",
    "NWL",
    "TPR",
    "JCI",
    "ROP",
    "SYK",
    "PGR",
    "AON",
    "MSI",
    "DHR",
    "ABBV",
    "AVB",
    "LLY",
    "HPE",
    "CHRW",
    "SYF",
    "CI",
    "FFIV",
    "ZBH"
]

CSI_TICKER = [
    "600000.SS",
    "600004.SS",
    "600009.SS",
    "600010.SS",
    "600011.SS",
    "600015.SS",
    "600016.SS",
    "600018.SS",
    "600019.SS",
    "600025.SS",
    "600027.SS",
    "600028.SS",
    "600029.SS",
    "600030.SS",
    "600031.SS",
    "600036.SS",
    "600038.SS",
    "600048.SS",
    "600050.SS",
    "600061.SS",
    "600066.SS",
    "600085.SS",
    "600089.SS",
    "600104.SS",
    "600109.SS",
    "600111.SS",
    "600115.SS",
    "600118.SS",
    "600170.SS",
    "600176.SS",
    "600177.SS",
    "600183.SS",
    "600188.SS",
    "600196.SS",
    "600208.SS",
    "600219.SS",
    "600221.SS",
    "600233.SS",
    "600271.SS",
    "600276.SS",
    "600297.SS",
    "600299.SS",
    "600309.SS",
    "600332.SS",
    "600340.SS",
    "600346.SS",
    "600352.SS",
    "600362.SS",
    "600369.SS",
    "600372.SS",
    "600383.SS",
    "600390.SS",
    "600398.SS",
    "600406.SS",
    "600436.SS",
    "600438.SS",
    "600482.SS",
    "600487.SS",
    "600489.SS",
    "600498.SS",
    "600516.SS",
    "600519.SS",
    "600522.SS",
    "600547.SS",
    "600570.SS",
    "600583.SS",
    "600585.SS",
    "600588.SS",
    "600606.SS",
    "600637.SS",
    "600655.SS",
    "600660.SS",
    "600674.SS",
    "600690.SS",
    "600703.SS",
    "600705.SS",
    "600741.SS",
    "600745.SS",
    "600760.SS",
    "600795.SS",
    "600809.SS",
    "600837.SS",
    "600848.SS",
    "600867.SS",
    "600886.SS",
    "600887.SS",
    "600893.SS",
    "600900.SS",
    "600919.SS",
    "600926.SS",
    "600928.SS",
    "600958.SS",
    "600968.SS",
    "600977.SS",
    "600989.SS",
    "600998.SS",
    "600999.SS",
    "601006.SS",
    "601009.SS",
    "601012.SS",
    "601018.SS",
    "601021.SS",
    "601066.SS",
    "601077.SS",
    "601088.SS",
    "601100.SS",
    "601108.SS",
    "601111.SS",
    "601117.SS",
    "601138.SS",
    "601155.SS",
    "601162.SS",
    "601166.SS",
    "601169.SS",
    "601186.SS",
    "601198.SS",
    "601211.SS",
    "601212.SS",
    "601216.SS",
    "601225.SS",
    "601229.SS",
    "601231.SS",
    "601236.SS",
    "601238.SS",
    "601288.SS",
    "601298.SS",
    "601318.SS",
    "601319.SS",
    "601328.SS",
    "601336.SS",
    "601360.SS",
    "601377.SS",
    "601390.SS",
    "601398.SS",
    "601555.SS",
    "601577.SS",
    "601600.SS",
    "601601.SS",
    "601607.SS",
    "601618.SS",
    "601628.SS",
    "601633.SS",
    "601658.SS",
    "601668.SS",
    "601669.SS",
    "601688.SS",
    "601698.SS",
    "601727.SS",
    "601766.SS",
    "601788.SS",
    "601800.SS",
    "601808.SS",
    "601816.SS",
    "601818.SS",
    "601828.SS",
    "601838.SS",
    "601857.SS",
    "601877.SS",
    "601878.SS",
    "601881.SS",
    "601888.SS",
    "601898.SS",
    "601899.SS",
    "601901.SS",
    "601916.SS",
    "601919.SS",
    "601933.SS",
    "601939.SS",
    "601985.SS",
    "601988.SS",
    "601989.SS",
    "601992.SS",
    "601997.SS",
    "601998.SS",
    "603019.SS",
    "603156.SS",
    "603160.SS",
    "603259.SS",
    "603260.SS",
    "603288.SS",
    "603369.SS",
    "603501.SS",
    "603658.SS",
    "603799.SS",
    "603833.SS",
    "603899.SS",
    "603986.SS",
    "603993.SS",
    "000001.SZ",
    "000002.SZ",
    "000063.SZ",
    "000066.SZ",
    "000069.SZ",
    "000100.SZ",
    "000157.SZ",
    "000166.SZ",
    "000333.SZ",
    "000338.SZ",
    "000425.SZ",
    "000538.SZ"
]

MDAX_TICKER = [
    "1COV.DE",
    "AIR.DE",
    "AOX.DE",
    "ARL.DE",
    "BNR.DE",
    "BOSS.DE",
    "DEQ.DE",
    "DUE.DE",
    "DWNI.DE",
    "EVD.DE",
    "EVK.DE",
    "FIE.DE",
    "FPE3.DE",
    "FRA.DE",
    "G1A.DE",
    "GBF.DE",
    "GXI.DE",
    "HLE.DE",
    "HNR1.DE",
    "HOT.DE",
    "JUN3.DE",
    "KGX.DE",
    "KRN.DE",
    "LEG.DE",
    "LEO.DE",
    "LXS.DE",
    "MTX.DE",
    "NDA.DE",
    "NOEJ.DE",
    "PBB.DE",
    "RAA.DE",
    "RHM.DE",
    "RRTL.DE",
    "SAX.DE",
    "SDF.DE",
    "SHA.DE",
    "SNH.DE",
    "SY1.DE",
    "SZG.DE",
    "SZU.DE"
]

