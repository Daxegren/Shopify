D = []
def add(**k): D.append(k)
import importlib
_src = {}
for _n in range(1, 10):
    for _p in importlib.import_module(f"vag1_0{_n}").D:
        _src[_p["id"]] = _p
def F(i): return _src[i]["fakta"]
def O(i): return _src[i]["orig_titel"]
def N(i): return _src[i]["nr"]

i = "10461917741322"
add(nr=N(i), id=i, orig_titel=O(i), fakta=F(i),
 titel="Gymnastikmatta Tunturi Fitnessmat Pro, 140 cm, blå",
 seo_title="Gymnastikmatta Tunturi Fitnessmat Pro",
 meta="Tunturi Fitness Mat Pro är en blå gymnastikmatta i gummi, 140 x 60 cm och 1,5 cm tjock, för magövningar och yogaövningar hemma eller på gymmet.",
 intro="Tunturi Fitness Mat Pro är en blå gymnastikmatta i gummi som mäter 140 x 60 x 1,5 cm, för användning hemma eller på gymmet.",
 passar=["Magövningar och yogaövningar","Träning på gymgolvet eller hemma","Dig som vill ha en egen matta att ta med"],
 spec=["Mått: 140 x 60 x 1,5 cm","Material: gummi","Färg: blå"],
 faq=[], marke=None,
 motivering="Fakta ur källan. Säljfraser och Tunturis märkestext utelämnas. Färgen blå står som uppgift i källan och i originaltiteln och behålls.",
 att_bekrafta=["Butiken har två varianter, \"14TUSFU125\" och \"blue\" (SKU 14TUSFU126). Bara den andra heter blå, så den första kan vara en annan färg. Om så är fallet ska \"blå\" tas bort ur titel, SEO och metabeskrivning.","Källan upprepar måttet och materialet (\"starkt gummi\" och \"hållbart gummimaterial\").","Produkttypen i butiken är \"Yogamattor\"."])

i = "10470888898826"
add(nr=N(i), id=i, orig_titel=O(i), fakta=F(i),
 titel="Luftnålar Tunturi med envägsventil, 2 st, krompläterade",
 seo_title="Luftnålar Tunturi med envägsventil, 2 st",
 meta="Tunturi luftnålar för att pumpa olika typer av bollar. Krompläterade nålbaser av metall med kontrollventil. Levereras som set om 2 st i blister.",
 intro="Tunturi luftnålar är avsedda för att pumpa olika typer av bollar. De har krompläterade nålbaser med kontrollventil och säljs i set om två.",
 passar=["Dig som vill pumpa olika typer av bollar","Dig som vill ha nålar med kontrollventil"],
 spec=["Antal: 2 st i blister","Material: metall","Färg: krompläterad","Utrustade med kontrollventil"],
 faq=[], marke=None,
 motivering="Fakta ur källan. Uppgiften att nålarna passar alla bollpumpar är borttagen ur meta, specifikation och vanliga frågor eftersom den är ett absolut passformslöfte. \"Starkt material\", \"säkerställer att endast luft kommer in\" och donationen till Fitkids Foundation utelämnas. Vikten 90 g utelämnas eftersom det inte framgår om den gäller en nål eller paketet.",
 att_bekrafta=["Tillverkaren anger att nålarna \"passar alla bollpumpar\". Bekräfta (olika ventiltyper och gängning) innan det tas med.","Det framgår inte om vikten 90 g gäller en nål eller hela paketet.","Nålens längd och diameter saknas.","\"Envägsventil\" i titeln är en översättning av \"one way valve\"; texten kallar den kontrollventil."])

i = "10462845829386"
add(nr=N(i), id=i, orig_titel=O(i), fakta=F(i),
 titel="Hantel Toorx i neopren, säljs styckvis",
 seo_title="Hantel Toorx i neopren, säljs styckvis",
 meta=None,
 intro="Hantel från Toorx i neopren. Hantlarna säljs styckvis.",
 passar=[], spec=[], faq=[], marke=None,
 motivering="Källan är tunn (titel och en rad om att hantlar säljs styckvis). Butiken har tre varianter (MN-1, MN-2, MN-3) som kan vara olika vikter. Vikten 2 kg och färgen grön är därför borttagna ur titel, SEO och text tills de bekräftats. Metabeskrivning utelämnad.",
 att_bekrafta=["Originaltiteln säger \"grön, 2 kg\", men det finns tre varianter (MN-1, MN-2, MN-3). Bekräfta vilken variant som är 2 kg och grön, och om de andra är andra vikter eller färger. Lägg därefter tillbaka vikt och färg i titeln.","Datablad behövs: material/överdrag, diameter, längd och grepp saknas.","\"Neopren\" kommer bara från titeln.","Säljs styckvis: bekräfta att priset gäller en hantel."])

i = "10472214921482"
add(nr=N(i), id=i, orig_titel=O(i), fakta=F(i),
 titel="Träningsboll Tunturi Gymball 90 cm",
 seo_title="Träningsboll Tunturi Gymball 90 cm",
 meta="Tunturi Gymball är en träningsboll i vinyl med diameter 90 cm och vikt 1475 g. Den är lämplig för kroppslängd över 190 cm enligt tillverkaren.",
 intro="Tunturi Gymball 90 cm är en träningsboll i vinyl med diameter 90 cm. Den är lämplig för kroppslängd över 190 cm.",
 passar=["Dig som är längre än 190 cm","Dig som vill ha en träningsboll i vinyl"],
 spec=["Diameter: 90 cm","Material: vinyl","Vikt: 1475 g","Lämplig för kroppslängd över 190 cm","Första användningen: fyll bollen med maximal mängd luft; det kan ta 1 eller 2 dagar innan den når rätt storlek"],
 faq=[("Hur gör jag första gången?","Fyll bollen med maximal mängd luft. Det kan ta 1 eller 2 dagar för bollen att nå rätt storlek.")], marke=None,
 motivering="Fakta ur källan. Färgen röd är borttagen ur titel, SEO och meta eftersom butiken har en variant som heter \"black\". Effektlöften, \"Beställ nu!\", belastningsuppgiften (avviker mellan bollar i serien), det oklara måttet 200 cm, \"uppblåsbar\" och Tunturis märkestext utelämnas.",
 att_bekrafta=["Originaltiteln säger \"röd\", men butiken har två varianter med samma SKU (14TUSFU285): \"Default Title\" och \"black\". Bekräfta färg eller färger och lägg därefter tillbaka färgen.","Maximal belastningskapacitet 120 kg i källan; blå Gymball 90 cm anger 220 kg. Utelämnad tills rätt värde är bekräftat.","\"Mått: 90 cm; Mått: 200 cm\" i källan är oklart. Utelämnat.","Källan nämner inte pump."])

i = "10472277803274"
add(nr=N(i), id=i, orig_titel=O(i), fakta=F(i),
 titel="Gymnastikboll Tunturi Gymball 75 cm",
 seo_title="Gymnastikboll Tunturi Gymball 75 cm",
 meta="Tunturi Gymball är en gymnastikboll med diameter 75 cm och vikt 1,2 kg. Den är lämplig för yoga och stretchövningar och passar längder 179–190 cm.",
 intro="Tunturi Gymball är en gymnastikboll med diameter 75 cm. Den är lämplig för yoga och stretchövningar. Storleken 75 cm passar längder 179–190 cm.",
 passar=["Yoga och stretchövningar","Dig som är 179–190 cm lång (storlek 75 cm)"],
 spec=["Diameter: 75 cm","Produktvikt: 1,2 kg","Bärförmåga: 220 kg"],
 faq=[("Vilken storlek ska jag välja?","Enligt tillverkaren passar 55 cm längder 155–165 cm, 65 cm längder 166–178 cm, 75 cm längder 179–190 cm och 90 cm längder över 190 cm.")], marke=None,
 motivering="Fakta ur källan. \"Anti-Burst\" (säkerhetslöfte och engelskt typord) och färgen är borttagna ur titeln: titeln säger mint men källan säger grönaktig. Bärförmågan 220 kg står entydigt i källan och behålls i specifikationen. Säljfraser, skrivbordsanvändning, \"garanterar\", mottot och företagshistoriken utelämnas. Storlekstabellen står bara i vanliga frågor.",
 att_bekrafta=["Originaltiteln säger \"Anti-Burst\" och \"Mint\". Källan förklarar inte Anti-Burst och anger färgen \"grönaktig\". Bekräfta båda innan de tas med.","Bärförmågan 220 kg: bekräfta mot datablad.","Produkten har status DRAFT i butiken.","Storlekarna 55, 65 och 90 cm finns i texten men inte som varianter."])

i = "10472279965962"
add(nr=N(i), id=i, orig_titel=O(i), fakta=F(i),
 titel="Gymnastikboll Tunturi Gymball 65 cm, röd",
 seo_title="Gymnastikboll Tunturi Gymball 65 cm",
 meta="Tunturi Gymnastikboll med diameter 65 cm och vikt 1,1 kg. Röd, lämplig för yoga och stretching och för längd 166–178 cm enligt tillverkaren.",
 intro="Tunturi Gymball är en röd gymnastikboll med diameter 65 cm. Den är lämplig för yoga och stretching och för längd 166–178 cm.",
 passar=["Dig som är 166–178 cm lång (storlek 65 cm)","Dig som vill ha en gymnastikboll för yoga och stretching"],
 spec=["Diameter: 65 cm","Produktvikt: 1,1 kg","Bärförmåga: 220 kg","Färg: röd","Lämplig för längd: 166–178 cm"],
 faq=[("Vilken längd passar 65 cm?","Enligt tillverkaren är storleken 65 cm lämplig för längd 166–178 cm.")], marke=None,
 motivering="Fakta ur källan. \"Anti-Burst\" är borttaget ur titel, SEO och meta (säkerhetslöfte och engelskt typord). Användning som sittplats vid skrivbord är borttagen eftersom källan bara säger \"kanske\". Bärförmågan 220 kg står entydigt i källan och behålls i specifikationen. Interna formuleringar (\"enligt källans storleksguide\") är bytta. Säljfraser och \"garanterar\" utelämnas.",
 att_bekrafta=["Originaltiteln säger \"Anti-Burst\". Källan förklarar inte egenskapen. Bekräfta innan den tas med.","Bärförmågan 220 kg: bekräfta mot datablad.","Produkten har status utkast (DRAFT) i butiken.","Källans länk antyder \"including pump\", men texten säger inget om pump. Pump nämns inte.","Raden \"Tillverkare .\" är tom."])

i = "10475373560074"
add(nr=N(i), id=i, orig_titel=O(i), fakta=F(i),
 titel="Handledsskydd Tunturi, bomull, vit",
 seo_title="Handledsskydd Tunturi, bomull, vit",
 meta="Tunturi handledsskydd i vit bomull med kardborrefäste och elastisk tumögla. Säljs per par. Mått 39,5 x 8,0 x 0,3 cm och vikt 38 g.",
 intro="Tunturi Wrist Wraps är handledsskydd i vit bomull med kardborrefäste som kan dras åt, och en elastisk tumögla. De säljs per par.",
 passar=["Dig som lyfter vikter och vill använda handledsskydd","Bänkpress, boot camp och andra viktbärande övningar"],
 spec=["Mått (L x B x H): 39,5 x 8,0 x 0,3 cm","Vikt: 38 g","Säljs per par","Fäste: kardborre, kan dras åt","Elastisk tumögla","Färg: vit","Material: bomull"],
 faq=[], marke=None,
 motivering="Fakta ur källan. Funktionslöften (stöd, skydd), \"utmärkta träningskompisar\", \"stadiga\", \"starkt\" material och Tunturis märkestext utelämnas. Färgen vit står som uppgift i källan och i originaltiteln.",
 att_bekrafta=["Butiken har två varianter (14TUSCF101 och 14TUSCF102) utan namn eller skillnad i källan. Om den andra är en annan färg eller storlek ska \"vit\" tas bort ur titel, SEO, metabeskrivning och specifikation.","Källan säger att materialet är \"Bomull\" men även \"starkt och elastiskt material\". Texten använder bomull.","Titelns \"Wrist Wraps\" är översatt till \"Handledsskydd\"."])

i = "10472277606666"
add(nr=N(i), id=i, orig_titel=O(i), fakta=F(i),
 titel="Minicykel Tunturi Mini Bike Foldable Easy",
 seo_title="Minicykel Tunturi Mini Bike, hopfällbar",
 meta="Tunturi Mini Bike Foldable Easy är en hopfällbar minicykel för hemmabruk med display för tid, rotationer och ungefärliga kalorier. Mått 35 x 50 x 39 cm.",
 intro="Tunturi Mini Bike är en hopfällbar minicykel och kompakt mobilitetstränare för hemmabruk. Den används sittande på en stol eller soffa och har en display.",
 passar=["Dig som vill träna sittande på en stol eller soffa","Dig som vill ha en kompakt, hopfällbar träningscykel för hemmabruk","Dig som vill följa tid, rotationer och ungefärliga kalorier på displayen"],
 spec=["Vikt: 2320 g","Mått: 35 x 50 x 39 cm","Hopfällbar","Display: visar antal rotationer, tid, ungefärliga förbrända kalorier och rotationer per minut"],
 faq=[("Kan jag använda minicykeln sittande?","Ja, den är lätt att använda när du sitter på en stol eller soffa.")], marke=None,
 motivering="Fakta ur källan. Leveranstiden för beställningsvaror är borttagen ur specifikationen (hör till standardblocket). \"Hopfällbar\" är borttaget ur titeln eftersom den dubblerade modellnamnet. \"Utmärkt verktyg för rehabilitering\" utelämnas (hälsopåstående).",
 att_bekrafta=["Motstånd/inställningar och maxvikt för användare saknas i källan.","Produkten är en beställningsvara (upp till 1 vecka längre leverans). Kontrollera att standardblocket täcker det.","\"Foldable Easy\" behålls som modellnamn.","Källan säger inget om batteri till displayen."])

i = "10650166853898"
add(nr=N(i), id=i, orig_titel=O(i), fakta=F(i),
 titel="Trampolin Hammer Cross Jump, 98 cm, vikbara ben",
 seo_title="Trampolin Hammer Cross Jump 98 cm",
 meta="Hammer Cross Jump är en fitnesstrampolin med hopparea på 98 cm i diameter och vikbara ben. Produktvikt 13 kg, maximal användarvikt 130 kg.",
 intro="Hammer Cross Jump är en fitnesstrampolin med en hopparea på 98 cm i diameter. Benen är vikbara, så trampolinen kan placeras utom synhåll när den inte används.",
 passar=["Dig som vill träna på trampolin","Dig som vill kunna fälla ihop benen och ställa undan trampolinen","Användare upp till 130 kg"],
 spec=["Hoppareans diameter: 98 cm","Mått: 120 x 130 x 140 cm","Produktvikt: 13 kg","Maximal användarvikt: 130 kg","Minsta takhöjd: 220 cm","Vikbara ben"],
 faq=[("Hur hög takhöjd behövs?","Minsta takhöjd är 220 cm.")], marke=None,
 motivering="Fakta ur källan. \"Hemma\" är borttaget ur användningsfallet eftersom källan inte nämner det. Viktnedgång, kaloriförbränning, kroppsformande löften, \"snabbt sätt\" och landet i parentes utelämnas.",
 att_bekrafta=["Butikens produkttyp är \"Utomhusträning\", men källan anger minsta takhöjd 220 cm, vilket tyder på inomhusbruk. Bekräfta.","Raden \"Minsta höjd på trampolinen: 220 cm\" är en dubblett av takhöjden och orimlig som trampolinhöjd. Utelämnad.","Om måttet 120 x 130 x 140 cm gäller uppfälld eller hopfälld framgår inte.","Inga uppgifter om studs/fjädrar, ram eller material."])
