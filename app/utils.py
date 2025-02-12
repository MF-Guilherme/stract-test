from app.services import get_insights_by_account_name
import pandas as pd


def export_platform_report(plataforma):

    insights = get_insights_by_account_name(plataforma)

    data = []
    for account in insights:
        account_name = account['account_name']
        for insight in account['insights']:
            insight['account_name'] = account_name
            data.append(insight)

    df = pd.DataFrame(data)

    if 'id' in df.columns:
        df = df.drop(columns=['id'])

    columns = ['account_name'] + [col for col in df.columns if col != 'account_name']
    df = df[columns]

    # Função para substituir ponto por vírgula em colunas numéricas
    def replace_dot_with_comma(series):
        if pd.api.types.is_numeric_dtype(series):
            return series.astype(float).map(lambda x: f"{x:.3f}".replace('.', ','))
        return series

    # Aplicar a função a todas as colunas do DataFrame
    df = df.apply(replace_dot_with_comma)

    csv_filename = f'{plataforma}_report.csv'
    df.to_csv(csv_filename, sep=';', index=False)

    return csv_filename
