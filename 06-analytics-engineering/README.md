
![Graph](https://cdn.discordapp.com/attachments/953573962519031848/1046383336936964116/picc.png)

# Analytics Engineering

  

`~/.dbt/profiles.yml`

  

```yml

greenery:

outputs:

  

dev:

type: postgres

threads: 1

host: localhost

port: 5432

user: postgres

pass: postgres

dbname: greenery

schema: public

  

prod:

type: postgres

threads: 1

host: localhost

port: 5432

user: postgres

pass: postgres

dbname: greenery

schema: prod

  

target: dev

```