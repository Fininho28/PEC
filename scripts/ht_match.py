import requests
import pandas as pd
from pathlib import Path

def get_half_time_result(api_key):
    url = "https://api.football-data.org/v4/competitions/PPL/matches?status=IN_PLAY,PAUSED"
    
    headers = {
        "X-Auth-Token": api_key
    }
    
    print("A obter o resultado ao intervalo de um jogo ao vivo da Primeira Liga através da API football-data.org.")
    
    response = requests.get(url,headers=headers)
    
    if response.status_code != 200:
        print(f"Erro ao ligar à API: {response.status_code}")
        print(response.text)
        return None
    
    data = response.json()
    matches = data.get("matches", [])
    
    if not matches:
        print("Não há nenhum jogo da Primeira Liga a decorrer neste momento.")
        return None
    
    # ajustar os nomes que a API retorna para os mesmos do csv
    team_names={
        "FC Famalicão": "Famalicao",
        "FC Arouca": "Arouca",
        "FC Alverca": "Alverca",
        "AVS": "AVS",
        "Moreirense FC": "Moreirense",
        "CD Nacional": "Nacional",
        "Sporting Clube de Braga": "Sp Braga",
        "Sporting Clube de Portugal": "Sp Lisbon",
        "GD Estoril Praia": "Estoril",
        "Casa Pia AC": "Casa Pia",
        "CF Estrela da Amadora": "Estrela",
        "Gil Vicente FC": "Gil Vicente",
        "Sport Lisboa e Benfica": "Benfica",
        "FC Porto": "Porto",
        "CD Santa Clara": "Santa Clara",
        "Vitória SC": "Guimaraes",
        "CD Tondela": "Tondela",
        "Rio Ave FC": "Rio Ave"
    }
    
    # criar lista de dicionarios com jogos a decorrer
    live_matches = []
    
    for match in matches:
        api_home = match['homeTeam']['name']
        api_away = match['awayTeam']['name']
        
        home_team = team_names.get(api_home, api_home) # ajustar o nome da equipa
        away_team = team_names.get(api_away, api_away)
        
        ht_home = match['score']['halfTime']['home']
        ht_away = match['score']['halfTime']['away']
        
        # garantir que ha resultado ao intervalo, e nao extrair jogos que ainda nao chegaram ao intervalo
        if ht_home is not None and ht_away is not None:
            live_matches.append({
                "HomeTeam": home_team,
                "AwayTeam": away_team,
                "HTHG": ht_home,
                "HTAG": ht_away
            })

            print(f"Intervalo Detetado: {home_team} {ht_home} - {ht_away} {away_team}")
        else:
            print(f"Jogo a decorrer, mas ainda não chegou ao intervalo: {home_team} vs {away_team}")
            
    # caso ainda nenhum jogo tenha chegado ao intervalo, retornar None
    if not live_matches:
            return None

    df = pd.DataFrame(live_matches)
        
    print("Resultado obtido com sucesso.")
    return df
    
if __name__ == "__main__":
    df = get_half_time_result("406db38d29bc42b0b72d3f826ecd9866")
    
    if df is not None:
        df.to_csv(Path("data/processed/half_time_result.csv"), index=False)
    