## notes format commit fetché

dans une balise 
```html 
<script type="application/json" data-target="react-app.embeddedData">
```

un objet 
```json
{"payload":{"commitGroups":[
```

dans commitGroups on a une liste de JSON au format 
```json
[{
    "title"   : "date (ex : Jun 20, 2026)",
    "commits" : [{* json représentatn un commit *voir plus bas* *},{autre json d'un commit}] 
}]

```

### format d'un commit
```json
{
"oid":"0b627eebd76ed5100dfaebccfcfba4a371177c89",
"url":"/Calliixte/proj-sdd/commit/0b627eebd76ed5100dfaebccfcfba4a371177c89",
"authoredDate":"2026-06-20T20:04:15.000+02:00",
"committedDate":"2026-06-20T20:04:15.000+02:00",
"shortMessage":"lint : better source show in readme",
"shortMessageMarkdown":null,
"shortMessageMarkdownLink":"\u003ca data-pjax=\"true\" title=\"lint : better source show in readme\" class=\"color-fg-default\" href=\"/Calliixte/proj-sdd/commit/0b627eebd76ed5100dfaebccfcfba4a371177c89\"\u003elint : better source show in readme\u003c/a\u003e",
"bodyMessageHtml":"",
"authors":
    [
        {"login":"Calliixte","displayName":"A. Baco","avatarUrl":"https://avatars.githubusercontent.com/u/190593977?v=4","path":"/Calliixte","profileName":null,"isGitHub":false}
    ],
"committerAttribution":false,
"committer":
    {
        "login":"Calliixte","displayName":"A. Baco","avatarUrl":"https://avatars.githubusercontent.com/u/190593977?v=4","path":"/Calliixte","profileName":null,"isGitHub":false
    },
    "pusher":null,
    "pushedDate":null
},
```
#### champs
> c'est du pur guess
- oid : identifiant unique du commit
- url : url pour retrouver le commit, c'est la prévisualisation
- authored/commited date : date de commit                         ```/!\ important pour mes graphes```
- short message : le message de commit                            ```/!\ important pour mes graphes```
- shortMessageMarkdown : ?
 - shortMessageMarkdownLink encore plus : ??
 - bodyMessageHtml ?
 - authors : liste des auteurs important plusieurs posssible       ```/!\ important pour mes graphes```
 - commiterAttribution : ?
 - committer : trouver la difference avec author franchement jsp
 - pusher : ig utilisé pour les merge
 - pushedDate : idem