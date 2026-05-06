from scripts import update_data
from scripts import future_matches
from scripts import process_data
from scripts import pregame_model

def run_pipeline():
    
    # extraçao passado
    update_data.update_data()
    print("=" * 50)
    
    # extraçao futuro
    future_matches.main()
    print("=" * 50)
    
    # processamento
    process_data.main()
    print("=" * 50)
    
    # treino e previsao
    pregame_model.main()
    
if __name__ == "__main__":
    run_pipeline()