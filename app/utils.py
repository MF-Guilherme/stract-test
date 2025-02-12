from app.services import get_insights_by_account_name
import pandas as pd


def replace_dot_with_comma(series):
    if pd.api.types.is_numeric_dtype(series):
        return series.astype(float).map(lambda x: f"{x:.3f}".replace('.', ','))
    return series


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

    df = df.apply(replace_dot_with_comma)

    df.columns = df.columns.str.title()

    csv_filename = f'{plataforma}_report.csv'
    df.to_csv(csv_filename, sep=';', index=False)

    return csv_filename


def export_collapsed_platform_report(plataforma):
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

    numeric_cols = df.select_dtypes(include='number').columns
    df_collapsed = df.groupby('account_name').agg({**{col: 'sum' for col in numeric_cols}, **{
        col: 'first' for col in df.columns if col not in numeric_cols and col != 'account_name'}}).reset_index()

    for col in df_collapsed.columns:
        if col not in numeric_cols and col != 'account_name':
            df_collapsed[col] = ''

    df_collapsed = df_collapsed.apply(replace_dot_with_comma)

    df_collapsed.columns = df_collapsed.columns.str.title()

    csv_filename = f'{plataforma}_resumo_report.csv'
    df_collapsed.to_csv(csv_filename, sep=';', index=False)

    return csv_filename
