from chalice import Chalice

app = Chalice(app_name='consumers')

# Dados fictícios 
users = {
    "users": [
        {"name": "user1", "phone": "11999999991"},
        {"name": "user2", "phone": "11999999992"},
        {"name": "user3", "phone": "11999999993"},
    ]
}

companies = {
    "companies": [
        {"name": "company1", "phone": "11999999991"},
        {"name": "company2", "phone": "11999999992"},
        {"name": "company3", "phone": "11999999993"},
    ]
}

# Rotas - User
# Retornando usuários
@app.route('/consumers/users', methods = ['GET'])
def get_users():
    requests_params = app.current_request.json_body
    
    response = {
        "statusCode": 200,
        "body": users
    }
    
    return response

# Adicionando usuário
@app.route('/consumers/users', methods = ['POST'])
def add_user():
    requests_params = app.current_request.json_body
    
    response = {
        "statusCode": 200,
        "body": f"Usuário '{requests_params}' cadastrado com sucesso!"
    }
    
    return response

# Alterando dados do usuário
@app.route('/consumers/users', methods = ['PUT'])
def update_user():
    requests_params = app.current_request.json_body
    
    response = {
        "statusCode": 200,
        "body": f"Dados do usuário '{requests_params}' atualizados com sucesso!"
    }
    
    return response

# Deletando usuário
@app.route('/consumers/users', methods = ['DELETE'])
def delete_user():
    requests_params = app.current_request.json_body
    
    response = {
        "statusCode": 200,
        "body": f"Usuário '{requests_params}' deletado com sucesso!"
    }
    
    return response

# Rotas - Companies
# Retornando empresas
@app.route('/consumers/companies', methods = ['GET'])
def get_companies():
    requests_params = app.current_request.json_body
    
    response = {
        "statusCode": 200,
        "body": companies
    }
    
    return response

# Adicionando empresa
@app.route('/consumers/companies', methods = ['POST'])
def add_company():
    requests_params = app.current_request.json_body
    
    response = {
        "statusCode": 200,
        "body": f"Empresa '{requests_params}' cadastrada com sucesso!"
    }
    
    return response

# Alterando dados do usuário
@app.route('/consumers/companies', methods = ['PUT'])
def update_company():
    requests_params = app.current_request.json_body
    
    response = {
        "statusCode": 200,
        "body": f"Dados da empresa '{requests_params}' atualizados com sucesso!"
    }
    
    return response

# Deletando usuário
@app.route('/consumers/companies', methods = ['DELETE'])
def delete_company():
    requests_params = app.current_request.json_body
    
    response = {
        "statusCode": 200,
        "body": f"Empresa '{requests_params}' deletada com sucesso!"
    }
    
    return response