def calculer_montant_ttc(prix_ht):
    if prix_ht > 200:
        prix_ht = prix_ht * 0.85  # Appliquer une réduction de 15%

    montant_ttc = prix_ht * 1.20

    return montant_ttc

if __name__ == "__main__":
    
    prix_ht = float(input("Entrez le prix total HT: "))
    montant_ttc = calculer_montant_ttc(prix_ht)
    print(f"Le montant TTC est: {montant_ttc:.2f} dh")
