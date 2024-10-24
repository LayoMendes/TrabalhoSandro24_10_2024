def obter_dados_usuario():
    nome = input("Qual é o seu nome? ")
    idade = input("Quantos anos você tem? ")
    habilidades = input("Quais são suas habilidades? ")
    nivel_academico = input("Qual o seu nível acadêmico? ")
    diferencial = input("Qual o seu diferencial? ")
    idiomas = input("Quais idiomas você sabe falar? ")
    img = input("Coloque aqui um link da web de sua imagem: ")
    whatsapp = input("Coloque aqui um link do contato de seu whatsapp: ")



    linguagens = []
    linguagem = input("Qual linguagem de programação você domina? ")
    linguagens.append(linguagem)
    
    while True:
        outra = input("Há mais alguma outra linguagem que você domina? Sim/Não ").strip().lower()
        if outra == "sim":
            linguagem = input("qual? ")
            linguagens.append(linguagem)
        elif outra == "não":
            break
        else:
            print("por favor, responda só sim ou não:")
    
    dados = {
        "nome": nome,
        "idade": idade,
        "habilidades": habilidades,
        "nivel_academico": nivel_academico,
        "diferencial": diferencial,
        "idiomas": idiomas,
        "linguagens": ", ".join(linguagens),
        "img": img,
        "whatsapp": whatsapp,
    }
    
    return dados

def gerar_html(dados):
    html_content = f"""
   <html>
    <head>
        <link rel="icon" href="https://cdn-icons-png.flaticon.com/512/226/226777.png" sizes="32x32">
        <title>Trabalho do Sandro 8pts</title>



        <style>
             body {{
                font-family: Verdana, Geneva, Tahoma, sans-serif;
                background:  linear-gradient(to right, rgb(43, 42, 42), rgba(0,0,0,0));
                margin: 0;
               
                line-height: 1.6;
            }}
 
            p {{
                margin: 5px 0;
            }}
            .quadradao {{
                max-width: 800px;
                margin: auto;
                background: #fff;
                padding: 40px;
                box-shadow: 0 0 30px rgba(0, 0, 0, 1.9);
                border-radius: 20px;
                margin-top: 12%;
                
            }}
             img {{
                max-width: 490px;
                height: 480px;
                float: right;
                border-radius: 20px;
                margin-top: -58%;
                box-shadow: 0 0 20px rgba(0, 0, 0, 0.4);
                border: 7px solid white; 
            }}
            .nome-douser{{
                background: linear-gradient(to left, #8baec4, #143963);
                border-radius: 20px;
                color: white;
                padding-left: 17px;    
                box-shadow: 0 0 20px rgba(0, 0, 0, 0.4);

            }}
            footer {{
                background-color: #333;
                color: #fff;
                padding: 20px;
                text-align: center;
                margin-top: 20%;
            }}
            .contato {{
                border-radius: 20px;
                background-color: rgb(255, 255, 255);
                padding: 10px; 
                width: 490px;
                transition: transform 0.3s ease; 
                border: 2px solid #ffffff;
                font-family: 'Verdana', sans-serif;
                text-align: center;
                text-decoration: none;
                color: #000000;
                margin: auto; 
                display: block; 
                margin-top: 40px;
                box-shadow: 0 0 20px rgba(0, 0, 0, 0.4);
                
            }}
            
            .contato:hover {{
                transform: scale(1.2);
                box-shadow: 7px 7px 10px rgba(0, 0, 0, 0.6); 
                font-family: 'Verdana', sans-serif; 
            }}
          
        </style>




    </head>

    <body>
        <div class='quadradao'>
            <h1 class="nome-douser">{dados['nome']}</h1>
            <p>|Idade: <br>{dados['idade']}</p>
            <p>|Habilidades: <br>{dados['habilidades']}</p>
            <p>|Nível Acadêmico:<br> {dados['nivel_academico']}</p>
            <p>|Diferencial:<br> {dados['diferencial']}</p>
            <p>|Idiomas: <br>{dados['idiomas']}</p>
            <p>|Linguagens de Programação:<br> {dados['linguagens']}</p>
            <img src='{dados['img']}' alt='foto de perfil' />
        </div>
             <a href="{dados['whatsapp']}" class="contato"><h3>CONTATO</h3></a>
        <footer>
        <p>&copy; 2024 - Todos os direitos reservados</p>
        <p>Entre em contato pelo e-mail: layohenrique33@gmail.com</p>       
        </footer>
    
    </body>

    </html>
    """

    with open("curriculo.html", "w") as file:
        file.write(html_content)

dados_usuario = obter_dados_usuario()
gerar_html(dados_usuario)
