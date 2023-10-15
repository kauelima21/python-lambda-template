# aws-python-sls-template
My personal template for aws lambda development with python and localstack.

## What do you need?

- [serverless framework](https://www.serverless.com/framework/) (version 3.15 or higher)
- [docker](https://docs.docker.com/)

## How to use
Clone this repository and run ```npm i``` or ```npm install```

Now you'll need to run the localstack container with the following commands:

```docker compose build```

```docker compose up```

then you're able to deploy on the localhost:

```serverless deploy --stage local```

## Using it

This template already has a CRUD example that you can use as a model to create yours.

The template is also created based on the DDD (Domain-driven design) principle.
