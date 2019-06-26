# hotdog
*(Nalaina tamin'ny série TV Silicon Valley)*

Reconnaissance de nouriture (identification d'un image s'il s'agit d'un hot-dog ou pas) avec keras.

![hotdog 97.15%](/capture/hotdog.jpg)

![not hotdog 56.69%](/capture/nothotdog.png)

Mampiasa datasets misy sary roa karazany:
  - Ao anaty répertoire hotdogs misy an'ireo sarina hotdog maro (417)
  - Ao amin'ny répertoire nothodogs kosa misy sary sakafo hafa, na zavatra hafa tsy mifandray amin'ny hotdog (10459)  

# Fampiasana azy:
Télechargena ny dataset izay ilaina amin'ny alalan'ireto script python ireto :
 - **down_image_from_google.py** ; Mila ovana ny tableau searc_queries arakarakin'ny sary tadiavina (hotdog na pizza, na izy roa miaraka)
 - **down_image_from_other_engine.py** ; Maka liste urls (lien sary) amin'ny moteur de recherche duckduckgo, bing, google. Misy variable query misy ny sary ho tadiavina (ex: query='pizza')
 - **Fomba fakana ny liste urls sary eo amin'ny recherche google image :**

     Eo amin'ny navigateur, mandeha any amin'ny site google eo amin'ny fanaovana recherche sary. 

     Scrolleo hatrany amin'ny farany ny resultat ny recherche eo. 

     Sokafy ny console (click droit - examiner l'élément na F12). Copieo ao ireto script javascript ireto :
 
        var script = document.createElement('script');
        script.src = "https://ajax.googleapis.com/ajax/libs/jquery/2.2.0/jquery.min.js";
        document.getElementsByTagName('head')[0].appendChild(script);
                
        avy eo
        
        var urls = $('.rg_di .rg_meta').map(function() { return JSON.parse($(this).text()).ou; });
           
        ary
        
        var textToSave = urls.toArray().join('\n');
        var hiddenElement = document.createElement('a');
        hiddenElement.href = 'data:attachment/text,' + encodeURI(textToSave);
        hiddenElement.target = '_blank';
        hiddenElement.download = 'urls.txt';
        hiddenElement.click();
        
         misy fichier urls.txt azo avy eo ka afaka ampiasaina amin'ny script eto ambany.

 - **get_datasets.py** ; Télécharge ny sary izay mifanaraka amin'ny urls azo teto ambony

Nanampy be dia be koa ny dataset [ukbench](https://archive.org/details/ukbench). Izy ity dia misy sary maro izay tsy misy hifandraisany amin'ny sakafo

Rehefa azo ny dataset rehetra ka efa tadifitra ao amin'ny répertoire-ny avy dia afaka alefa ny entrainement

```
python train.py
```

Efa misy modèle efa vita entrainement ao anaty dossier models, ka raha hanao test dia toy izao

```
python test.py -t test.jpeg
```

# dependences

- opencv
- keras
- numpy
- matplotlib

Telechargement sary :

- google_images_download
- BeautifulSoup
- requests

**Mazotoa manandrana**






