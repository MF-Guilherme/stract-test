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