# Create a virtual environment

```sh
## Create virtual environment
python -m venv .venv

## Enable the virtual environment
source .venv/bin/activate
```

# Install python libraries

```sh
pip install -r requirements.txt
```

# Run the application

```sh
python main.py
```

# Mock Data

```json
[
	{
		"name": "Colby Harding",
		"phone": "1-355-757-1364",
		"email": "metus.eu@google.couk",
		"address": "P.O. Box 752, 9560 Ornare, Av."
	},
	{
		"name": "Gil Farley",
		"phone": "1-854-828-1649",
		"email": "odio.vel@outlook.com",
		"address": "124-7704 Ornare Avenue"
	},
	{
		"name": "Keaton Hood",
		"phone": "1-679-242-3564",
		"email": "nibh.donec.est@protonmail.com",
		"address": "942-5680 Nec St."
	},
	{
		"name": "Anne Shaffer",
		"phone": "(973) 848-5178",
		"email": "arcu.imperdiet@yahoo.couk",
		"address": "Ap #687-9405 Ut St."
	},
	{
		"name": "James Elliott",
		"phone": "(537) 225-3071",
		"email": "mauris.id@google.net",
		"address": "3595 A, Rd."
	}
```

# API Calls

- You can use the postman collection saved in the root directory

## Fetch and transform data

```sh
curl --location --request POST 'http://127.0.0.1:5000/fetch-data'
```

- I have used a simple transformation to convert all text in dictionary values to lowercase
- The mock data is in the `mock_data.json` file

### Response

```json
{
    "data": {
        "transformation_id": 1
    },
    "error": false,
    "message": "Data fetched and transformed"
}
```

## Fetch Transformed Data

```sh
curl --location 'http://127.0.0.1:5000/get-processed-data/<transformation_id>'
```
- Add `transformation_id` from the `POST` API above.

```json
{
    "data": [
        {
            "address": "p.o. box 752, 9560 ornare, av.",
            "email": "metus.eu@google.couk",
            "name": "colby harding",
            "phone": "1-355-757-1364"
        },
        {
            "address": "124-7704 ornare avenue",
            "email": "odio.vel@outlook.com",
            "name": "gil farley",
            "phone": "1-854-828-1649"
        },
        {
            "address": "942-5680 nec st.",
            "email": "nibh.donec.est@protonmail.com",
            "name": "keaton hood",
            "phone": "1-679-242-3564"
        },
        {
            "address": "ap #687-9405 ut st.",
            "email": "arcu.imperdiet@yahoo.couk",
            "name": "anne shaffer",
            "phone": "(973) 848-5178"
        },
        {
            "address": "3595 a, rd.",
            "email": "mauris.id@google.net",
            "name": "james elliott",
            "phone": "(537) 225-3071"
        }
    ],
    "error": false,
    "message": ""
}
```
