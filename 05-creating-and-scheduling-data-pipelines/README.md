
# Model
![alt text](https://cdn.discordapp.com/attachments/953573962519031848/1043924709768691772/Diagram.png)
# Airflow Screenshots

![alt text](https://cdn.discordapp.com/attachments/953573962519031848/1043923659045212221/Screenshot_2565-11-20_at_22.53.52.png)
![alt text](https://cdn.discordapp.com/attachments/953573962519031848/1043923659405938698/Screenshot_2565-11-20_at_22.57.12.png)
![alt text](https://cdn.discordapp.com/attachments/953573962519031848/1043923659716304996/Screenshot_2565-11-20_at_22.58.58.png)
# Creating and Scheduling Data Pipelines

On Linux, we need to make sure that we configure these:

```sh
mkdir -p ./dags ./logs ./plugins
echo -e "AIRFLOW_UID=$(id -u)" > .env
```
