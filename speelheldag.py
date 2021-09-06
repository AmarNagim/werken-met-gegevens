# berekening feestlunch
# info: Dat kost een toegangsticket per persoon van 7,45 euro voor de hele dag. Jullie willen ook met zijn 
# allen voor 45 minuten in de VIP-VR-GameSeat. De VIP-VR GameSeat kost per persoon 37 eurocent per 5 minuten. 
# Jij trakteert dus betaal je alles. Laat Python dat uitrekenen. Hoe duur wordt jouw speelhal-dag?

dagticket_pp = 7.45
vip_per_5_min = 0.37
aantal_mensen = 4

prijs_dagtickets = dagticket_pp*aantal_mensen
prijs_vip_pp = vip_per_5_min*9
prijs_vip = prijs_vip_pp*4

prijs_totaal = round(prijs_dagtickets+prijs_vip, 2)

print(f'De totaalprijs word: €{prijs_totaal},-')




