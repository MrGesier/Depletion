# Depletion
Tools that calculate time to ruin a pool
# Simulation de dépôts basés sur la croissance d'utilisateurs et distribution tronquée

Ce projet simule l'évolution du nombre de clients ainsi que leurs dépôts quotidiens, en utilisant :
- Une fonction de croissance logistique pour modéliser l'adoption des utilisateurs.
- Une distribution normale tronquée pour générer les dépôts (montants investis).
- Un tracé graphique de l'évolution des dépôts (journaliers et cumulés) sur la période.

## Description des principales étapes

1. **Paramétrage de la simulation**  
   - `initial_clients`: nombre initial de clients.
   - `target_clients`: nombre cible de clients à atteindre.
   - `adoption_duration_days`: durée (en jours) sur laquelle se fait l’adoption des utilisateurs.
   - `slope`: taux de croissance dans la fonction logistique.
   - Les dépôts sont ensuite générés à l’aide d’une distribution normale tronquée (définie par `mu`, `sigma`, `lower`, `upper`).

2. **Fonction de croissance logistique**  
   - `logistic_growth(t, start, end, growth_rate, duration)`: calcule le nombre de clients à chaque jour `t`.

3. **Calcul des nouveaux clients quotidiens**  
   - `daily_new_clients = np.diff(clients_over_time, prepend=clients_over_time[0])` : dérivée discrète du nombre de clients sur la période.

4. **Génération des dépôts quotidiens**  
   - Utilisation d’une **distribution normale tronquée** (`truncnorm`) pour générer une valeur moyenne de dépôt (`base_deposits`).
   - Les dépôts quotidiens sont ensuite pondérés par le ratio du nombre de nouveaux clients par rapport au maximum de nouveaux clients quotidiens.

5. **Visualisations**  
   - **Histogramme** de la distribution des dépôts journaliers.
   - **Courbes** des dépôts journaliers et de leur cumul au cours du temps.

## Prérequis

- Python 3.7 ou supérieur (recommandé).
- Les dépendances listées dans `requirements.txt`.

## Installation

1. Cloner ou télécharger ce dépôt.
2. Se placer dans le répertoire du projet.
3. Installer les dépendances avec :
   ```bash
   pip install -r requirements.txt
