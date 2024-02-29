'''
pip install solana
pip install pandas
'''

import requests
import pandas as pd

def get_solana_token_balances(address):
    url = 'https://api.mainnet-beta.solana.com/'
    headers = {'Content-Type': 'application/json'}
    payload = {
        'jsonrpc': "2.0",
        'id': 1,
        'method': 'getTokenAccountsByOwner',
        'params': [
            address,
            {
                'programId': 'TokenkegQfeZyiNwAJbNbGKPFXCWuBvf9Ss623VQ5DA'
            },
            {
                'encoding': 'jsonParsed'
            }
        ]
    }

    response = requests.post(url, json=payload, headers=headers)
    response_data = response.json()

    mint_addresses = []
    amounts = []

    if 'result' in response_data and 'value' in response_data['result']:
        for item in response_data['result']['value']:
            mint_address = item['account']['data']['parsed']['info']['mint']
            balance = item['account']['data']['parsed']['info']['tokenAmount']['uiAmount']
            mint_addresses.append(mint_address)
            amounts.append(balance)

    #Create DataFrame with mint adresses
    df = pd.DataFrame({'Mint Adresse': mint_addresses, 'Amount': amounts})

    #Convert DataFrame to JSON (orient='records')
    json_output = df.to_json(orient='records')

    return json_output, df

# Example usage
solana_address = "FhyMkVNUTvjFVN88qAXmp6jqYxpDEwJmQpMrQAmj2HtD"
json_data, dataframe = get_solana_token_balances(solana_address)
print(json_data)
print("#"*80)
print(dataframe)
