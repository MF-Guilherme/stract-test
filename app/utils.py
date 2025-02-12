from app.services import get_insights_by_account_name
import pandas as pd


def export_platform_report(plataforma):

    insights = get_insights_by_account_name(plataforma)

    data = []
    for account in insights:
        platform_name = account['platform']
        account_name = account['account_name']
        for insight in account['insights']:
            insight['platform'] = platform_name
            insight['account_name'] = account_name
            data.append(insight)

    df = pd.DataFrame(data)

    if 'id' in df.columns:
        df = df.drop(columns=['id'])

    columns = ['platform'] + [col for col in df.columns if col != 'platform']
    df = df[columns]

    def replace_dot_with_comma(series):
        if pd.api.types.is_numeric_dtype(series):
            return series.astype(float).map(lambda x: f"{x:.3f}".replace('.', ','))
        return series

    df = df.apply(replace_dot_with_comma)

    df.columns = df.columns.str.title()
    
    csv_filename = f'{plataforma}_report.csv'
    df.to_csv(csv_filename, sep=';', index=False)

    return csv_filename
