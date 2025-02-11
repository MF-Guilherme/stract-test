from app.services import search_accounts_from_platform, search_insights_for_account


def fields_by_platform(platform):
    fields_ga4 = 'adName,impressions,clicks,status,region,cost'
    fields_tiktok = 'ad_name,impressions,clicks,status,country,cost,cost_per_click'
    fields_meta_ads = 'ad_name,impressions,clicks,effective_status,country,spend,cpc,ctr,ctr_unique,global_objective'
    
    # Caso seja necessário adicionar outra plataforma, basta adicionar um novo elif
    if platform == 'ga4':
        return fields_ga4
    elif platform == 'tiktok_insights':
        return fields_tiktok
    else:
        return fields_meta_ads
    
def get_all_fields_to_platform_report(plataforma):
    # - pegar todas as accounts da plataforma (api/accounts?platform=...)
    accounts = search_accounts_from_platform(plataforma)
    # - para cada account da plataforma
    # - pegar o id, name e token (o name da account precisa ser apresentado no csv)
    # - pegar todos os insights da account passando plataforma, id da account, token e fields (api/insights?platform=...)
        ## atenção porque os fields variam de acordo com a plataforma ##
    for account in accounts:
        account_id = account['id']
        account_name = account['name']
        token = account['token']

        insights = search_insights_for_account(plataforma, account_id, token)

        #TODO retornar os campos necessários para o relatório
        pass