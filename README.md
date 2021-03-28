# PromBBQ w/iGrill V2

## iGrill.py Source

https://github.com/bendikwa/igrill/blob/master/igrill.py

## Running on Raspberry PI

1. Build the Docker image

```bash
docker build -t prombbq -f Dockerfile .
```

2. Run the new docker image.

```bash
docker run --net host -e PROMBBQ_PUSHSERVER=<pushgateway-url> -e PROMBBQ_BASIC_AUTH_USER=<basic-auth-user> -e PROMBBQ_BASIC_AUTH_PASSSWORD=<basicauth-pw> --restart always prombbq
```
