import csv
import io
import base64
import matplotlib

matplotlib.use("Agg")
import matplotlib.pyplot as plt
from django.shortcuts import render


def index(request):
    return render(request, "ventes/index.html")


def resultats(request):
    if request.method == "POST" and request.FILES.get("fichier_csv"):
        fichier = request.FILES["fichier_csv"]
        contenu = fichier.read().decode("utf-8")
        reader = csv.DictReader(io.StringIO(contenu))

        rows = []
        ca_total = 0
        meilleur_id = None
        meilleur_ca_net = 0

        for ligne in reader:
            prix = float(ligne["Prix"])
            quantite = int(ligne["Quantite"])
            remise = float(ligne["Remise"])

            ca_brut = round(prix * quantite, 2)
            ca_net = round(ca_brut * (1 - remise / 100), 2)
            tva = round(ca_net * 0.20, 2)

            ca_total = round(ca_total + ca_net, 2)

            if ca_net > meilleur_ca_net:
                meilleur_ca_net = ca_net
                meilleur_id = ligne["ID"]

            rows.append(
                {
                    "ID": ligne["ID"],
                    "Prix": prix,
                    "Quantite": quantite,
                    "Remise": remise,
                    "CA_Brut": ca_brut,
                    "CA_Net": ca_net,
                    "TVA": tva,
                }
            )

        # Générer le graphique
        ids = [r["ID"] for r in rows]
        ca_bruts = [r["CA_Brut"] for r in rows]
        ca_nets = [r["CA_Net"] for r in rows]
        tvas = [r["TVA"] for r in rows]

        fig, axes = plt.subplots(1, 2, figsize=(13, 5))
        fig.suptitle("Analyse des Ventes", fontsize=14, fontweight="bold")

        x = list(range(len(ids)))
        largeur = 0.35

        for i in range(len(x)):
            axes[0].bar(
                x[i] - largeur / 2,
                ca_bruts[i],
                width=largeur,
                color="#4C72B0",
                label="CA Brut" if i == 0 else "",
            )
            axes[0].bar(
                x[i] + largeur / 2,
                ca_nets[i],
                width=largeur,
                color="#55A868",
                label="CA Net" if i == 0 else "",
            )

        axes[0].set_title("CA Brut vs CA Net par Produit")
        axes[0].set_xlabel("ID Produit")
        axes[0].set_ylabel("Montant (DT)")
        axes[0].set_xticks(x)
        axes[0].set_xticklabels(ids)
        axes[0].legend()

        axes[1].bar(ids, tvas, color="#C44E52")
        axes[1].set_title("Montant TVA par Produit")
        axes[1].set_xlabel("ID Produit")
        axes[1].set_ylabel("TVA (DT)")

        plt.tight_layout()

        buffer = io.BytesIO()
        plt.savefig(buffer, format="png", dpi=150)
        buffer.seek(0)
        graphique = base64.b64encode(buffer.read()).decode("utf-8")
        plt.close()

        return render(
            request,
            "ventes/resultats.html",
            {
                "rows": rows,
                "ca_total": ca_total,
                "meilleur_id": meilleur_id,
                "meilleur_ca_net": meilleur_ca_net,
                "graphique": graphique,
            },
        )

    return render(request, "ventes/index.html")