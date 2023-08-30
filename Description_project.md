# Projekt Python:
Dostupnosť základných potravín širokej verejnosti
(Vybrané otázky)
V predchádzajúcom projekte sme prostredníctvom dotazov SQL zodpovedali na požadované výskumné otázky. Niektoré som sa rozhodla širšie spracovať v programe Python.

Zdroj dát: Projekt SQL – Dostupnosť základných potravín širokej verejnosti. 


# Grafické znázornenie otázky č. 4 - Percentuálny medziročný nárast HDP, miezd a cien v ČR za obdobie 2008-2018

Existuje rok, ve kterém byl meziroční nárůst cen potravin výrazně vyšší než růst mezd (větší než 10 %)? 
Z datasetu prostredníctvom select dotazu sme získali údaje, pre porovnanie medziročnej zmeny (nárast alebo pokles) miezd a cien potravín. 
V nadväznosti na ďalšie spracovanie sme do grafu pridali aj medziročný nárast HDP.
Počas celého sledovaného obdobia nebol rast cien výrazne vyšší (viac ako 10 %), ako rast miezd. Najvýraznejší nárast môžeme pozorovať v roku 2017, kde priemerné ceny potravín vzrástli o 9,98% a priemerná výška miezd iba o 6,4%. 
V sledovanom období nezaznamenávame ani výraznejší rast HDP (nad 10%). Z časového hľadiska je medziročný nárast HDP plynulejší, podobne reagujú aj mzdy. Najvýraznejšie sa medziročné zmeny prejavujú u cien potravín.


# Grafické znázornenie otázky č. 5 - Má výška HDP vliv na změny ve mzdách a cenách potravin? 
Neboli, pokud HDP vzroste výrazněji v jednom roce, projeví se to na cenách potravin či mzdách ve stejném nebo následujícím roce výraznějším růstem?

Pre posúdenie vzájomného vzťahu medzi HDP, mzdami a cenami urobíme korelačnú analýzu. Korelácia nám zmeria silu a smer lineárneho vzťahu medzi dvoma premennými. 
Dataset používame opäť z Projektu SQL, kde sme si pomocou SQL dotazu pripravili dáta. Následne ich v Pythone (spracované v GoogleColab) jednotlivo vizualizujeme. 
Postupne si pripravíme kódy pre koreláciu dát a zobrazíme prostredníctvom Heatmap. Pre výpočet korelačného koeficientu použijeme vzorec Pearsonovho korelačného koeficientu.

Korelačný koeficient medzi HDP a priemernými mzdami je zaokrúhlene 0,92. 
Korelačný koeficient medzi HDP a priemernými cenami je zaokrúhlene 0,89. 
Korelačný koeficient medzi priemernými mzdami a priemernými cenami je zaokrúhlene 0,92.

Celkovo dáta ukazujú silnú pozitívnu koreláciu medzi priemernými mzdami, cenami a HDP. To naznačuje, že keď ekonomika rastie (meraná HDP), mzdy i ceny majú tendenciu rásť. 
Posúdiť vplyv z časového hľadiska je náročnejšie. Korelácia nám poukazuje len na súčasný vzťah medzi premennými za poskytnuté roky.
Ekonomickým zmenám často trvá, než sa presadia systémom a ovplyvnia rôzne odvetvia. Napr. Zvýšenie HDP môže viesť k zvýšeniu ekonomickej aktivity a dopytu, čo môže viesť k zvýšeniu miezd, pretože zamestnávatelia súťažia o kvalifikovanú pracovnú silu. 
Podobne zvýšená ekonomická aktivita a dopyt môžu vyvolať rast cien potravín. Tieto mechanizmy zvyčajne fungujú s rôznym časovým oneskorením a ich účinky nemusia byť okamžité.

Aj keď v našom datasete existuje silná korelácia medzi HDP, mzdami a cenami potravín, nemôžeme dôjsť k záveru, že zmeny v HDP priamo spôsobujú zmeny miezd a cien potravín. 
Vzťah medzi týmito premennými je zložitejší a ovplyvnený rôznymi ekonomickými faktormi. 
