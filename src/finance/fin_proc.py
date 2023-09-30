def get_fin_data(df, school_name=None, year=None, report_type=None, REGON=None):
    df = df[df['NazwaJednostki'].str.contains(school_name)]
    df = df[df['Rok'] == year]
    df = df[df['TypSprawozdania'] == report_type]
    df = df[df['REGON'] == REGON]
    return df