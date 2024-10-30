# gandi_flask_app_template

## About

A simple web application template to deploy on Gandi.

## Usage

Clone the project:

```bash
git clone https://github.com/ajrlewis/gandi_flask_app_template.git
cd gandi_flask_app_template
```

Install the requirements:

```bash
python3.9 -m venv venv
source venv/bin/activate
pip install --upgrade pip
pip install -r requirements.txt
```

Create the database:

```bash
source venv/bin/activate
flask db init
flask db migrate -m "init"
flask db upgrade
```

Add a user to the database:

```sql
INSERT INTO user (name, api_key) VALUES ('John Doe', 'api-key');
```

Locally host the website:

```bash
source venv/bin/activate
python3.9 wsgi.py
```

make sure to configure the environmental variables:

| Name | Description |
|--------------------|

## License

This package is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.
