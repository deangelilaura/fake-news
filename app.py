punteggi_parole = {
    "shock": -2,
    "incredibile": -2,
    "esclusivo": -1.5,
    "clickbait": -2,
    "scandalo": -1.5,
    "allarmante": -1.5,
    "segreto": -1.5,
    "virale": -1,
    "sensazionale": -1.5,
    "truffa": -2,

    "studio": 2,
    "ricerca": 2,
    "ufficiale": 1.5,
    "verificato": 2,
    "fonte": 1.5,
    "scientifico": 2,
    "approvato": 1.5,
    "autorizzato": 1.5,
    "esperto": 2,
    "analisi": 1.5,
}

def titolo(titolo):
    title_lower = titolo.lower()
    parole = title_lower.split()
    
    calcolo_punteggio = sum(punteggi_parole.get(parola, 0) for parola in parole)
    
    if calcolo_punteggio < -2:
        classificazione = "Fake News"
    elif -2 <= calcolo_punteggio <= 2:
        classificazione = "Notizia Dubbia"
    else:
        classificazione = "Notizia Affidabile"
    
    return {"titolo": titolo, "punteggio": calcolo_punteggio, "classificazione": classificazione}

def main():
    print("Inserisci i titoli delle notizie (uno per riga). Digita 'STOP' per terminare:")
    titoli = []
    while True:
        titolo_usato = input("> ")
        if titolo_usato.upper() == "STOP":
            break
        titoli.append(titolo_usato)

    print("\nRisultati:")
    for risultati in [titolo(titolo_usato) for titolo_usato in titoli]:
        print(f"Titolo: {risultati['titolo']}")
        print(f"  Classificazione: {risultati['classificazione']}")
        print(f"  Punteggio: {risultati['punteggio']:.2f}")
        print("-" * 40)

if __name__ == "__main__":
    main()