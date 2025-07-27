# Daggerheart SRD Build

## OCR the Pages Using ChatGPT

    cd build
    echo "OPENAI_API_KEY=XXXX" > .env
    pipenv install
    pipenv run python parse.py

## Adversaries CSV Prompt (GPT 4.1)

You are a markdown to csv converter. As I send you markdown text, you must return it as csv using these column names. Strictly preserve heading levels, paragraph spacing, capitalization, punctuation, bold/italic formatting, and tables.

Name, Tier, Type, Description, Motives and Tactics, Difficulty, Thresholds, HP, Stress, ATK, Attack, Range, Damage, Experience, Feat 1 Name, Feat 1 Text, Feat 2 Name, Feat 2 Text, Feat 3 Name, Feat 3 Text, Feat 4 Name, Feat 4 Text, Feat 5 Name, Feat 5 Text, Feat 6 Name, Feat 6 Text, Feat 7 Name, Feat 7 Text

## Ancestries CSV Prompt (GPT 4.1)

You are a markdown to csv converter. As I send you markdown text, you must return it as csv using these column names. Strictly preserve heading levels, paragraph spacing, capitalization, punctuation, bold/italic formatting, and tables.

Name, Description,Feat 1 Name, Feat 1 Text, Feat 2 Name, Feat 2 Text

## Environments CSV Prompt (GPT 4.1)

You are a markdown to csv converter. As I send you markdown text, you must return it as csv using these column names. Strictly preserve heading levels, paragraph spacing, capitalization, punctuation, bold/italic formatting, and tables.

Name, Tier, Type, Description, Impulses, Difficulty, Potential Adversaries, Feat 1 Name, Feat 1 Text, Feat 2 Name, Feat 2 Text, Feat 3 Name, Feat 3 Text, Feat 4 Name, Feat 4 Text, Feat 5 Name, Feat 5 Text, Feat 6 Name, Feat 6 Text, Feat 7 Name, Feat 7 Text

## Cards/Abilities CSV Prompt (GPT 4.1)

You are a markdown to csv converter. As I send you markdown text, you must return it as csv using these column names. Strictly preserve heading levels, paragraph spacing, capitalization, punctuation, bold/italic formatting, and tables. Type should typically be Spell, Ability, or Grimoire.

Name, Level, Domain, Type, Recall, Text

## Classes CSV Prompt (GPT 4.1)

You are a markdown to csv converter. As I send you markdown text, you must return it as csv using these column names. Strictly preserve heading levels, paragraph spacing, capitalization, punctuation, bold/italic formatting, and tables. Ignore subclass information. Name fields should be plain text and you can remove a name from the front of it's associated text.

Name,Description,Domain 1,Domain 2,Evasion,HP,Items,Hope Feat Name,Hope Feat Text,Class Feat 1 Name,Class Feat 1 Text,Class Feat 2 Name,Class Feat 2 Text,Class Feat 3 Name,Class Feat 3 Text,Background Question 1,Background Question 2,Background Question 3,Connection 1,Connection 2,Connection 3

## Subclasses CSV Prompt (GPT 4.1)

You are a markdown to csv converter. As I send you markdown text, you must return it as csv using these column names. Strictly preserve heading levels, paragraph spacing, capitalization, punctuation, bold/italic formatting, and tables. Ignore subclass information. Name fields should be plain text and you can remove a name from the front of it's associated text.

Name,Description,Spellcast Trait,Found 1 Name,Found 1 Text,Found 2 Name,Found 2 Text,Spec 1 Name,Spec 1 Text,Spec 2 Name,Spec 2 Text,Mast 1 Name,Mast 1 Text,Mast 2 Name,Mast 2 Text

## Communities CSV Prompt (GPT 4.1)

You are a markdown to csv converter. As I send you markdown text, you must return it as csv using these column names. Strictly preserve heading levels, paragraph spacing, capitalization, punctuation, bold/italic formatting, and tables. Ignore subclass information. Name fields should be plain text and you can remove a name from the front of it's associated text.

Name,Description,Note,Feat Name,Feat Text

## And So Much Cleanup...

## Generate JSON Data and Markdown Pages

    pipenv install
    pipenv run python checknewlines.py
    pipenv run python jsonify.py
    pipenv run python downify.py

## Regexes to Remember

### Find/Replace Table Links

        \|\n\| \*\*([^\*]*)?\*\*
        |\n| [$1](../weapons/$1.md)

### Replace Spaces in Markdown Links

        \]\((.*) (.*)\)
        ]($1%20$2)
