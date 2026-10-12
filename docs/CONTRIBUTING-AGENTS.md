# Contribuer aux intégrations agent

Ce projet utilise les fichiers `SKILL.md` comme source de vérité portable. Les intégrations Codex, Claude Code, Cursor et VS Code sont des couches d’entrée courtes générées à partir de cette bibliothèque.

## Ajouter ou modifier un skill

1. Créer ou modifier le dossier `skills/<skill-name>/`.
2. Conserver un fichier `SKILL.md` avec un frontmatter valide :

```yaml
---
name: godot-example
description: Ce que fait ce skill. Use when <situations qui doivent le déclencher>.
---
```

   Le `name` doit correspondre au nom du dossier et la `description` doit contenir une clause `Use when` (ou `Keywords:`).

3. Documenter le modèle mental, les décisions d’architecture, les exemples et les anti-patterns.
4. Utiliser les APIs Godot 4.7+ et du GDScript typé lorsque du code est fourni.
5. Ne jamais inclure de chemins locaux, secrets ou configuration propre à un utilisateur.

## Mettre à jour les intégrations

Après toute modification du skill maître ou de ses métadonnées :

```powershell
python scripts\generate_agent_rules.py --target all
python scripts\validate_agent_support.py
```

Les fichiers générés sont :

- `.cursor/rules/godot-game-dev-studio.mdc`
- `.claude/skills/godot-game-dev-studio/SKILL.md`
- `.github/copilot-instructions.md`

Ne pas enrichir manuellement ces fichiers avec une logique qui devrait vivre dans `skills/`.

## Ajouter un script GDScript

- préférer des fonctions statiquement typées ;
- éviter les APIs Godot 3 obsolètes ;
- documenter les dépendances et le contexte d’exécution ;
- vérifier qu’il compile avec Godot 4.7 (`python scripts/check_gdscript.py --godot <godot>`) ;
- ne pas réutiliser un `class_name` déjà déclaré dans le même skill, ni masquer une classe native Godot ;
- pour un skill `godot-*`, recopier le script dans son miroir `skills/godot-master/scripts/` ;
- ne pas présenter un exemple comme production-ready s’il n’a pas été validé.

## MCP

MCP est optionnel. Une contribution doit rester utilisable sans MCP avec les skills et la CLI Godot. Les configurations MCP et secrets restent locales ; consulter `docs/mcp/` pour la documentation par outil.

## Vérifications avant contribution

```powershell
python update_skills_index.py
python update_skills_index.py --validate
python scripts\generate_agent_rules.py --target all
python scripts\validate_agent_support.py
python scripts\check_gdscript.py --godot <chemin-vers-godot-4.7>
Get-Content .codex-plugin\plugin.json | ConvertFrom-Json | Out-Null
```

La CI GitHub exécute automatiquement ces contrôles sur les pushs vers `main` et les pull requests. Si la génération modifie les fichiers d’intégration, il faut régénérer les fichiers et les inclure dans la contribution.

Vérifier également que le diff ne contient que les fichiers liés à la contribution et qu’aucun artefact comme `__pycache__` n’est ajouté.

La validation automatique inspecte les fichiers texte du paquet pour détecter les chemins personnels, vérifie que chaque dossier de skill contient un `SKILL.md` dont le `name` correspond au dossier, que `skills_index.json` liste tous les skills sans doublon, que les miroirs de `skills/godot-master/scripts/` sont identiques à leurs originaux et que tous les liens Markdown relatifs aboutissent. La CI compile aussi chaque script `.gd` avec Godot 4.7 ; les extraits qui dépendent d’un contexte absent de la bibliothèque (autoload, addon, asset du jeu) sont listés dans `scripts/gdscript_known_failures.txt`.

## Pull request

La description doit préciser :

- le problème ou le besoin couvert ;
- les skills concernés ;
- les changements de comportement attendus ;
- les commandes de validation exécutées ;
- les limites ou points restant à tester.
