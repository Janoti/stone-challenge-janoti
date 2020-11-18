# Stone Challenge

## Para rodar a aplicação localmente em containers Docker:

    * Instale o Docker: ```apt install docker```

    * Clone o repositorio da app

    * Dentro do diretório, rode:

   ``` $make local ```
 
    -- Abra seu navegador e digite: http://127.0.0.1:5000/users
    
## Para rodar localmente no cluster Kubernetes:

   ``` $make k8s ```

## Rotas do app

     -- http://127.0.0.1:5000/users #retorna a lista de usuários

     -- http://127.0.0.1:5000/users/cpf #retorna o usuário pesquisando pelo cpf


## Acesso pelo GCP - Google

    * Retorna a lista de usuários

    -- http://34.67.24.110/users

    * Retorna o usuário pesquisando pelo cpf

    -- http://34.67.24.110/users/<cpf>
 
    * Para inserir um novo usuário, substitua os dados do usuário na estrutura abaixo:

       ``` curl --location --request POST 'http://34.67.24.110/users' \--header 'Content-Type: application/json' \--data-raw '{
         "nome": "InsiraSeuNome",
         "sobrenome": "InsiraSeu Sobrenome",
         "cpf": 122312321321,
         "email": "ninguemusa@yahoo.com.br",
         "data_nasc": "19/01/1989"}' ```

## Monitoramento 

* Principais gráficos de monitoramento do Cluster Kubernetes em Grafana com GKE CLuster Monitoring Plugin
``` http://34.71.211.208:3000/d/Z1HlU5FMa/gke-cluster-monitoring?orgId=1&from=1605647426677&to=1605651026679&var-datasource=Google%20Cloud%20Monitoring&var-project= ```

``` Login: stone ```
``` Senha : stone ```     

* Principais gráficos de Monitoramento das VMs

``` http://34.71.211.208:3000/d/4ZIrp9DMa/gce-vm-instance-monitoring?orgId=1&from=1605652821670&to=1605656421670&var-datasource=Google%20Cloud%20Monitoring&var-project= ```
     
## TERRAFORM 

-- Para gerar toda a infra no GKE, executar dentro da pasta terraform-gke

    -- terraform init
    -- terraform apply
    -- Após o término do Terraform criar a infra, execute:
    -- make build # vai pegar as credenciais do gke para o gcloud e rodar kubectl apply no deployment.yaml, criando o serviço e o deploy no gke. A imagem Docker está registrada em gcr.io/stone-challenge-janoti/challenge-stone
    
    
    

## Acesso pelo PAAS Heroku: 

* Retorna a lista de usuários

    ``` https://stone-challenge-janoti.herokuapp.com/users ```

* Retorna o usuário pesquisando pelo cpf

   ``` https://stone-challenge-janoti.herokuapp.com/users/ ```

* Para inserir um novo usuário, substitua os dados do usuário na estrutura abaixo:

   ``` curl --location --request POST 'https://stone-challenge-janoti.herokuapp.com/users' \--header 'Content-Type: application/json' \--data-raw '{
     "nocme": "InsiraSeuNome",
     "sobrenome": "InsiraSeu Sobrenome",
     "cpf": 122312321321,
     "email": "ninguemusa@yahoo.com.br",
     "data_nasc": "19/01/1989"}' ```
                
